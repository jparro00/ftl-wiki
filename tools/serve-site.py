#!/usr/bin/env python3
"""Serve the built pages as a local website.

    python tools/serve-site.py                 # http://127.0.0.1:8080
    python tools/serve-site.py --open          # ...and open a browser at it
    python tools/serve-site.py --check         # walk every route, print, exit non-zero
                                               # on a broken one. No server started.
    python tools/serve-site.py --routes        # print the route table and exit

`tools/LOCAL-SITE.md` is the normative spec. The short version:

The generated output is already a website's worth of pages — 19 sector profiles, 386
event cards, two indexes — but on disk they are `sectors/sector-<slug>.html` and
`cards/card-<slug>.html`, and the profiles and cards are **fragments** (no `<html>`,
no `<head>`) because the Artifact publisher supplies the document around them. This
server supplies that document instead, adds one nav bar, and gives every page a URL
worth typing:

    /                     home
    /sectors/             the chooser — all 19, two pinnable
    /sectors/<slug>       one sector profile
    /cards/               the event index — all 386, searchable
    /cards/<slug>         one event card

**It rewrites no link and edits no built file.** That is not restraint for its own
sake: the pages must keep working off `file://` and keep publishing as artifacts, so
their links stay relative and their content stays exactly what the build wrote. What
makes this work is that `/sectors/<slug>` has the same base path as
`sectors/sector-<slug>.html` on disk, so every relative link in a built page resolves
to a real route here. The old shapes redirect (301) to the clean ones, which upgrades
in-page links as they are followed instead of editing them.
"""

import argparse
import html
import http.server
import json
import mimetypes
import os
import pathlib
import re
import socketserver
import sys
import urllib.parse
import webbrowser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTOR_DIR = ROOT / "sectors"
CARD_DIR = ROOT / "cards"
TREES = CARD_DIR / "trees"
SHELL = ROOT / "tools" / "sector-page-render.html"
VOCAB = ROOT / "tools" / "site-vocab.json"

VOC = json.loads(VOCAB.read_text(encoding="utf-8"))
NAV = VOC["nav"]
HOME = VOC["home"]
SEEN = VOC["seen"]

SLUG = r"[a-z0-9-]+"


# --------------------------------------------------------------------------
# The palette
# --------------------------------------------------------------------------

def tokens():
    """The colour tokens, sliced out of the page shell.

    `build-sector-index.py` slices the same marked block out of the same file for the
    same reason: the chrome must not be able to drift from the pages it wraps. The
    slice is duplicated; the palette is not.
    """
    shell = SHELL.read_text(encoding="utf-8")
    start = shell.index("/* TOKENS-START")
    start = shell.index("*/", start) + 2
    end = shell.index("/* TOKENS-END */")
    return shell[start:end].strip()


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------

# Every selector is prefixed `sb-`. The pages this wraps define `.wrap`, `.card`,
# `.note`, `.chip` and `.name` in their own stylesheets, and a bare class name here
# would repaint them -- or be repainted by them, since their <style> comes later in
# the document than this one.
NAV_CSS = """
  /* --- site chrome (tools/serve-site.py) ------------------------------- */
  /* The bar is fixed rather than sticky: a sticky element inside the pages'
     padded body is inset horizontally and resolves its containing block against
     whatever ancestor the page happens to have. Fixed has neither problem. The
     !important is aimed at the pages' own `body { padding: ... }`, which differs
     between a card (2.4rem) and a profile (2.6rem) -- overriding it by weight
     rather than by matching each value keeps this independent of both. */
  body { padding-top: 3.5rem !important; }
  .sb-bar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 60;
    display: flex; align-items: center; gap: .9rem;
    height: 2.7rem; padding: 0 1rem;
    background: color-mix(in srgb, var(--void) 88%, transparent);
    backdrop-filter: blur(7px);
    border-bottom: 1px solid var(--edge);
    font-family: var(--sans); font-size: .78rem; line-height: 1;
  }
  .sb-brand {
    font-weight: 600; color: var(--ink); text-decoration: none;
    letter-spacing: -.005em; white-space: nowrap;
  }
  .sb-brand:hover { color: var(--cyan); }
  .sb-links { display: flex; gap: .1rem; }
  .sb-links a {
    color: var(--dim); text-decoration: none; padding: .34rem .5rem;
    border-radius: 2px; border: 1px solid transparent; white-space: nowrap;
  }
  .sb-links a:hover { color: var(--ink); border-color: var(--edge); }
  .sb-links a.sb-on { color: var(--cyan); border-color: var(--rail); }
  .sb-crumb {
    flex: 1 1 auto; min-width: 0; color: var(--faint);
    font-family: var(--mono); font-size: .68rem;
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .sb-crumb b { color: var(--dim); font-weight: 400; }
  .sb-crumb a { color: inherit; text-decoration: none; }
  .sb-crumb a:hover { color: var(--cyan); }
  .sb-act {
    background: transparent; border: 1px solid var(--edge); border-radius: 2px;
    color: var(--faint); font-family: var(--mono); font-size: .72rem;
    padding: .3rem .45rem; cursor: pointer; line-height: 1; text-decoration: none;
  }
  .sb-act:hover { color: var(--cyan); border-color: var(--cyan); }
  @media (max-width: 34rem) { .sb-crumb { display: none; } }
"""

# Runs in <head>, before the page paints, so a remembered theme does not arrive as a
# flash of the other one. No theme stored means no attribute set, which is the state
# the pages are designed for: prefers-color-scheme decides.
THEME_INIT = """
try {
  var t = localStorage.getItem('ftl-theme');
  if (t === 'dark' || t === 'light') document.documentElement.dataset.theme = t;
} catch (e) {}
"""

THEME_JS = """
document.addEventListener('click', function (ev) {
  var b = ev.target.closest('.sb-theme');
  if (!b) return;
  var el = document.documentElement;
  // No attribute means "follow the system", and the first click has to pick a side.
  // Pick the opposite of what is on screen, which is what the reader just asked for.
  var now = el.dataset.theme ||
    (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  var next = now === 'dark' ? 'light' : 'dark';
  el.dataset.theme = next;
  try { localStorage.setItem('ftl-theme', next); } catch (e) {}
});
"""


def nav_html(active, crumbs, source=None):
    """The bar. `active` is 'sectors', 'cards' or None; `crumbs` is a list of
    (label, href-or-None); `source` is true when this page has a built file behind it,
    which `?raw=1` on the same URL serves verbatim."""
    links = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' class="sb-on"' if active == key else "",
                                   html.escape(label))
        for key, label, href in (("sectors", NAV["sectors"], "/sectors/"),
                                 ("cards", NAV["cards"], "/cards/")))
    trail = "".join(
        (' <b>›</b> <a href="%s">%s</a>' % (href, html.escape(label)))
        if href else (" <b>›</b> " + html.escape(label))
        for label, href in crumbs)
    src = ('<a class="sb-act" href="%s" title="%s">%s</a>'
           % (source, html.escape(NAV["source_title"], quote=True),
              html.escape(NAV["source"]))) if source else ""
    return (
        '<nav class="sb-bar">'
        '<a class="sb-brand" href="/" title="%(bt)s">%(brand)s</a>'
        '<span class="sb-links">%(links)s</span>'
        '<span class="sb-crumb">%(trail)s</span>'
        '%(src)s'
        '<button class="sb-act sb-theme" title="%(theme)s">%(mark)s</button>'
        "</nav>" % {
            "bt": html.escape(NAV["brand_title"], quote=True),
            "brand": html.escape(NAV["brand"]),
            "links": links, "trail": trail, "src": src,
            "theme": html.escape(NAV["theme"], quote=True),
            "mark": html.escape(NAV["theme_mark"]),
        })


# --------------------------------------------------------------------------
# `?seen=` — the beacons this run has already visited
# --------------------------------------------------------------------------

# Injected into sector profiles only, and only as chrome: the built page is never
# touched, so it still opens off `file://` and still publishes as an artifact. The
# overlay reads `?seen=` and marks what the run has already been to. Nothing is
# derived here and nothing is guessed -- the URL is the whole input.
#
# The watcher owns the state (LOCAL-SITE.md 5c). It carries the set on the URL because
# an externally hosted site gives it no other channel, and 24 slugs is ~800 characters,
# which costs nothing measurable to pass or to parse.

SEEN_CSS = """
  /* --- ?seen= overlay (tools/serve-site.py) ----------------------------- */
  /* The chip rides inline in the box's own `.t` (the event name) and the count in the
     budget row's own `.name`, so both inherit the page's `.tg` / `.mark` styling and
     neither adds a grid child -- `.brow` is a five-column grid and a sixth cell would
     shift the pips and the count this must not touch. */
  .tg.sb-seen {
    color: var(--green);
    /* `.t` is `font-weight: 500`, which the chip would otherwise inherit and render
       heavier than the same chip does down in the tags row. */
    font-weight: 400;
    display: inline-block; vertical-align: middle; white-space: nowrap;
    margin-left: .4rem;
  }
  .mark.sb-seen-count { color: var(--green); }
  /* Cyan, which `.mark.first` ("placed first") also uses. They only ever meet on line
     one and read differently, and the colour was asked for -- but it is why the count
     chips carry their own class rather than reusing `.mark.first`. */
  .mark.sb-overlap-count { color: var(--cyan); }
  /* Seen means behind you, so the title recedes. Kept above `.evbox:hover .t`
     only by source order -- the page's stylesheet comes later in the document, so
     hover still wins, which is what we want. */
  .ev.sb-is-seen .t, .evbox.sb-is-seen .t { color: var(--dim); }
  .ev.sb-is-seen, .evbox.sb-is-seen { background: var(--sunk); }

  /* The strip under the bar: what landed, and what did not. */
  body.sb-has-seen { padding-top: 5.1rem !important; }
  .sb-seenbar {
    position: fixed; top: 2.7rem; left: 0; right: 0; z-index: 59;
    display: flex; gap: .8rem; align-items: baseline;
    padding: .3rem 1rem; border-bottom: 1px solid var(--edge);
    background: color-mix(in srgb, var(--sunk) 92%, transparent);
    backdrop-filter: blur(7px);
    font-family: var(--mono); font-size: .66rem; color: var(--dim);
  }
  .sb-seenbar .miss { color: var(--amber); }
"""

SEEN_JS = """
(function () {
  const WORDS = %(words)s;
  const raw = new URLSearchParams(location.search).get('seen');
  // No parameter, no markup. A sector page with no `?seen=` must be byte-for-byte
  // the page it was before this existed.
  if (raw === null) return;

  // Case and the three word separators are normalised away, so a token may be the
  // slug (`ancient-device`) or the in-game event id the Hyperspace log prints
  // (`ROCK_CRYSTAL_BEACON`, `rock_crystal_beacon`). Measured across all 386 cards:
  // no normalised event id equals a *different* event's slug, so one flat lookup
  // cannot mistake one event for another.
  const norm = s => String(s).toLowerCase().replace(/[\\s_-]+/g, '-');

  // A token may carry how many times the beacon was visited, two ways:
  //
  //   store-engi          once
  //   store-engi:3        three times
  //   store-engi,store-engi   also twice -- repeats accumulate
  //
  // The repeat form exists because it is what the watcher naturally produces: one
  // token per `Creating event:` line, appended in order, with no counting to do.
  // The `:n` form is for a hand-written or compacted URL. Every token is a visit
  // record, so both forms add: `store-engi:2,STORE_ENGI` is three visits.
  //
  // The bound on URL length does not change. A run visits at most 24 beacons, so
  // there are at most 24 tokens either way.
  const counts = new Map();       // normalised token -> visits
  const tokens = [], bad = [];
  raw.split(',').map(s => s.trim()).filter(Boolean).forEach(tok => {
    const at = tok.lastIndexOf(':');
    let name = tok, n = 1;
    if (at >= 0) {
      name = tok.slice(0, at);
      const digits = tok.slice(at + 1);
      // Slugs are [a-z0-9-] and ids are [A-Z0-9_], so a colon is never part of a name.
      // A count that is not a number is refused rather than read as one visit, which
      // would report a figure nobody asked for -- and it is reported as a *count*
      // problem, not as "not in this sector's pool", which would blame the wrong thing
      // about an event that is sitting right there in the list.
      if (!/^[0-9]+$/.test(digits)) { bad.push(tok); return; }
      n = Number(digits);
      // `:0` is not an error. It says the beacon was visited zero times, which is what
      // saying nothing says, so the token drops and nothing is marked or reported.
      if (n < 1) return;
    }
    const key = norm(name);
    if (!key) return;
    if (!counts.has(key)) { counts.set(key, 0); tokens.push(name); }
    counts.set(key, counts.get(key) + n);
  });
  const want = new Set(counts.keys());

  // Every beacon box on the page -- `details.evbox` where the event has a card, plain
  // `div.ev` where it does not. Both carry the event id in `.id`, so an event with no
  // card is still markable: the run visited it either way.
  const boxes = Array.prototype.slice.call(document.querySelectorAll('.evbox, .ev'))
    .filter(el => !el.matches('summary'));

  // `hit` is which *tokens* landed; `events` is how many distinct events they named.
  // The two differ, and the bar must report the second: an event reachable through a
  // budget line and a marker section has a box in each, so counting boxes reported
  // ten for five events and read as though half the sector had been visited.
  const hit = new Set(), events = new Set();
  // Every box's visit count, by the element itself -- the same event has a box in each
  // place it is listed, and each of those boxes shows the same count.
  const visitsOf = new Map();
  let visits = 0;
  boxes.forEach(el => {
    const idEl = el.querySelector('.id');
    const keys = [el.dataset.card, idEl && idEl.textContent]
      .filter(Boolean).map(norm);
    // **Deduplicated.** A box contributes its slug and its normalised id as lookup
    // keys, and for plenty of events those are the same string -- `store-engi` and
    // `STORE_ENGI` both normalise to `store-engi`. Summing over the raw key list
    // therefore counted that event's visits twice, and `store-engi:2` read as `Seen 4`.
    const matched = keys.filter((k, i) => want.has(k) && keys.indexOf(k) === i);
    if (!matched.length) return;
    matched.forEach(k => hit.add(k));
    // Summed over the distinct matching keys, because an event named both by slug and
    // by a *different* id string is two visit records, exactly as naming it twice by
    // slug would be.
    const n = matched.reduce((sum, k) => sum + counts.get(k), 0);
    const key = el.dataset.card || keys[0];
    if (!events.has(key)) { events.add(key); visits += n; }
    visitsOf.set(el, n);
    el.classList.add('sb-is-seen');
    // Inline in the event name, not down in the tags row: the name is the line a reader
    // scans, and every box has a `.t` whether or not it has any tags -- so there is no
    // container to create and no box that cannot take the chip.
    const chip = document.createElement('span');
    chip.className = 'tg sb-seen';
    // One visit is the ordinary case and says nothing extra; a repeat is the news.
    chip.textContent = n > 1 ? WORDS.chip_n.replace('{n}', n) : WORDS.chip;
    const title = el.querySelector('.t');
    (title || el).appendChild(chip);
  });

  // Per budget line: how many of the events *this line* can place are marked.
  // `.bpool > .pool` is deliberately direct-child only -- an AE delta block sits in
  // the same expansion with a `.pool` of its own, and counting it would inflate the
  // line by events the base list does not hold.
  //
  // Collected before anything is appended, because the line's own name is read out of
  // `.name` and `.name` is where the chips go -- read it after and the label picks up
  // the chip text of whatever was added first.
  const lines = [];
  document.querySelectorAll('details.bwrap').forEach(row => {
    const pool = row.querySelector(':scope > .bpool > .pool');
    const brow = row.querySelector(':scope > .brow');
    const name = brow && brow.querySelector('.name');
    if (!pool || !name) return;
    const own = Array.prototype.slice.call(pool.children);
    lines.push({
      name: name,
      total: own.length,
      // Text nodes only: `.name` already carries `placed first` / `fill-in` chips as
      // element children, and textContent would glue their words onto the list name.
      label: Array.prototype.filter.call(name.childNodes, n => n.nodeType === 3)
        .map(n => n.textContent).join('').trim(),
      // Each seen box in this line, as {key, visits}. The line's count is the sum of
      // the visits, not the number of events: a store visited twice is two beacons of
      // this line's allocation spent, which is the question the budget answers.
      hits: own.filter(el => el.classList.contains('sb-is-seen')).map(el => ({
        key: el.dataset.card || norm(el.querySelector('.id').textContent),
        visits: visitsOf.get(el) || 1,
      })),
    });
  });

  // Which lines each seen event lands on. An event in two lines is counted by both --
  // that is the intended reading, since the URL says which event was visited and not
  // which beacon, so there is nothing to attribute it with. The overlap chip makes
  // that visible instead of leaving the per-line counts summing past the total.
  const on = new Map();
  lines.forEach((line, i) => line.hits.forEach(h => {
    if (!on.has(h.key)) on.set(h.key, []);
    on.get(h.key).push(i);
  }));

  const sum = hs => hs.reduce((t, h) => t + h.visits, 0);

  lines.forEach((line, i) => {
    if (!line.hits.length) return;
    const chip = document.createElement('span');
    chip.className = 'mark sb-seen-count';
    chip.textContent = WORDS.row.replace('{n}', sum(line.hits));
    chip.title = WORDS.row_title
      .replace('{n}', sum(line.hits))
      .replace('{events}', line.hits.length)
      .replace('{total}', line.total);
    line.name.appendChild(chip);

    // Overlap is counted in visits too, so the two chips are in the same unit and the
    // arithmetic closes: the per-line counts exceed the run's real total by exactly
    // the overlaps.
    const shared = line.hits.filter(h => on.get(h.key).length > 1);
    if (!shared.length) return;
    // Lines are identified by index, never by label: two entries in one allocation
    // table can carry the same list name, and a label key would merge them.
    const others = [];
    shared.forEach(h => on.get(h.key).forEach(j => {
      if (j !== i && others.indexOf(lines[j].label) < 0) others.push(lines[j].label);
    }));
    const dup = document.createElement('span');
    dup.className = 'mark sb-overlap-count';
    dup.textContent = WORDS.overlap.replace('{n}', sum(shared));
    dup.title = WORDS.overlap_title
      .replace('{n}', sum(shared)).replace('{list}', others.join(', '));
    line.name.appendChild(dup);
  });

  // What did not land. A token can be a real event that simply is not in this
  // sector's pool, and the page cannot tell that from a typo -- it holds one
  // sector's events and nothing wider. So it says the true thing.
  // Two different failures, reported as two different things. A name the pool does not
  // hold and a count that is not a number are not the same mistake, and one message for
  // both would have said "not in this sector's pool" about `FREE_WEAPON:tow`, whose
  // event is in the pool twice over.
  const missed = tokens.filter(t => !hit.has(norm(t)));
  const esc = t => t.replace(/[<&]/g, c => (c === '<' ? '&lt;' : '&amp;'));
  const miss = (words, list) => list.length
    ? '<span class="miss">' + words.replace('{n}', list.length)
        .replace('{list}', list.map(esc).join(', ')) + '</span>'
    : '';
  const bar = document.createElement('div');
  bar.className = 'sb-seenbar';
  bar.innerHTML = '<span>' + (events.size
      ? WORDS.bar.replace('{n}', events.size).replace('{total}', tokens.length)
      : WORDS.bar_none) + '</span>' +
    // Only when a repeat exists: with one visit each, visits and events are the same
    // number and printing both says nothing twice.
    (visits > events.size
      ? '<span>' + WORDS.bar_visits.replace('{n}', visits) + '</span>' : '') +
    miss(WORDS.unmatched, missed) + miss(WORDS.badcount, bad);
  document.body.classList.add('sb-has-seen');
  const nav = document.querySelector('.sb-bar');
  if (nav) nav.parentNode.insertBefore(bar, nav.nextSibling);
  else document.body.insertBefore(bar, document.body.firstChild);
})();
""" % {"words": json.dumps(SEEN, ensure_ascii=False)}


# --------------------------------------------------------------------------
# Responses
# --------------------------------------------------------------------------

class Response:
    def __init__(self, status, body=b"", ctype="text/html; charset=utf-8", location=None):
        self.status = status
        self.body = body.encode("utf-8") if isinstance(body, str) else body
        self.ctype = ctype
        self.location = location

    def __repr__(self):
        return "<%d %s%s>" % (self.status, self.ctype.split(";")[0],
                              " -> " + self.location if self.location else "")


def redirect(to):
    return Response(301, "", location=to)


def text(body, status=200):
    return Response(status, body, "text/plain; charset=utf-8")


TITLE_RE = re.compile(r"<title>(.*?)</title>\s*", re.S | re.I)
BODY_OPEN = re.compile(r"<body\b[^>]*>", re.I)
COMMENT = re.compile(r"<!--.*?-->", re.S)


def find_title(raw):
    """The fragment's own `<title>`, ignoring any inside an HTML comment.

    Both shells open with a comment explaining that the build replaces "the `<title>`
    line" — so a plain search for `<title>` matches the comment and, with DOTALL, runs
    to the real closing tag. The whole banner then becomes the browser tab's name.
    Comments are blanked in a scratch copy of equal length, so the offsets a match
    reports still index the original text.
    """
    masked = COMMENT.sub(lambda m: " " * len(m.group(0)), raw)
    return TITLE_RE.search(masked)


def document(title, body, active=None, crumbs=(), head="", source=None, tail=""):
    """Wrap page content in the document the fragments do not carry.

    `tail` runs after the page's own markup and its own scripts, which is what an
    overlay reading the built DOM needs -- the beacon boxes have to exist first.
    """
    return Response(200, """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
%(tokens)s
%(nav_css)s
</style>
<script>%(theme_init)s</script>
%(head)s</head>
<body>
%(nav)s
%(body)s
<script>%(theme_js)s</script>
%(tail)s</body></html>
""" % {
        "title": html.escape(title),
        "tokens": tokens(),
        "nav_css": NAV_CSS,
        "theme_init": THEME_INIT,
        "head": head,
        "nav": nav_html(active, crumbs, source),
        "body": body,
        "theme_js": THEME_JS,
        "tail": tail,
    })


def fragment_page(path, active, crumbs, source, head="", tail=""):
    """A built fragment — a card or a sector profile — made into a page.

    The fragment opens with its own `<title>` and `<style>`; the title is lifted into
    the head we are building and the style is left exactly where it is. A `<style>`
    in the body is honoured by every browser, and moving it would put the page's
    stylesheet before this chrome's instead of after it, quietly changing which one
    wins wherever they happen to collide.
    """
    raw = path.read_text(encoding="utf-8")
    match = find_title(raw)
    title, body = path.stem, raw
    if match:
        title = html.unescape(match.group(1).strip())
        body = raw[:match.start()] + raw[match.end():]
    return document(title, body, active=active, crumbs=crumbs, source=source,
                    head=head, tail=tail)


def spliced_page(path, active, crumbs, source):
    """A built page that is already a document — the two indexes. Insert the chrome
    rather than wrapping: the page's own `<head>` is the one that must be extended."""
    raw = path.read_text(encoding="utf-8")
    head = ("<style>\n%s\n</style>\n<script>%s</script>\n"
            % (NAV_CSS, THEME_INIT))
    if "</head>" in raw:
        raw = raw.replace("</head>", head + "</head>", 1)
    bar = nav_html(active, crumbs, source)
    raw, count = BODY_OPEN.subn(lambda m: m.group(0) + "\n" + bar, raw, count=1)
    if not count:                      # no <body> to splice into: prepend and say so
        raw = head + bar + raw
    if "</body>" in raw:
        raw = raw.replace("</body>", "<script>%s</script>\n</body>" % THEME_JS, 1)
    else:
        raw += "<script>%s</script>" % THEME_JS
    return Response(200, raw)


# --------------------------------------------------------------------------
# What is on disk
# --------------------------------------------------------------------------

def sector_slugs():
    return sorted(p.name[len("sector-"):-len(".html")]
                  for p in SECTOR_DIR.glob("sector-*.html")
                  if not p.name.endswith("-review.html"))


def card_slugs():
    return sorted(p.name[len("card-"):-len(".html")]
                  for p in CARD_DIR.glob("card-*.html"))


def sector_title(slug):
    data = SECTOR_DIR / "data" / ("%s.sector.json" % slug)
    if data.exists():
        try:
            return json.loads(data.read_text(encoding="utf-8"))["display_name"]
        except (ValueError, KeyError):
            pass
    return slug.replace("-", " ")


def card_title(slug):
    """Read from the tree, which is where the title is maintained.

    One small file per request rather than 386 at startup, so a card rebuilt while
    the server is up shows its new title without a restart.
    """
    tree = TREES / ("%s.tree.json" % slug)
    if tree.exists():
        try:
            return json.loads(tree.read_text(encoding="utf-8"))["title"]
        except (ValueError, KeyError):
            pass
    return slug.replace("-", " ")


def sector_menu():
    """The 19, earliest first — the order the chooser groups them in."""
    out = []
    for path in sorted((SECTOR_DIR / "data").glob("*.sector.json")):
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        out.append((d["earliest_sector"], d["display_name"], d["slug"]))
    return [(name, slug) for _, name, slug in sorted(out)]


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

HOME_CSS = """
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 0 1.15rem 5rem;
    background: var(--void);
    background-image: radial-gradient(var(--hex) 1px, transparent 1.6px);
    background-size: 22px 22px;
    color: var(--ink); font-family: var(--sans); line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }
  .hm { max-width: 58rem; margin: 0 auto; padding-top: 3.6rem; }
  .hm .eyebrow {
    font-family: var(--mono); font-size: .66rem; letter-spacing: .19em;
    text-transform: uppercase; color: var(--cyan); margin: 0 0 .55rem;
  }
  .hm h1 { font-size: 2.2rem; margin: 0 0 .5rem; letter-spacing: -.015em; }
  .hm .lede { color: var(--dim); font-size: 1rem; max-width: 38rem; margin: 0 0 2.6rem; }
  .hm .doors { display: grid; grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr));
               gap: 1rem; }
  .hm .door {
    display: block; text-decoration: none; color: inherit;
    background: var(--panel); border: 1px solid var(--edge); border-radius: 3px;
    padding: 1.15rem 1.25rem 1.3rem;
  }
  .hm .door:hover { border-color: var(--cyan); }
  .hm .door .n {
    font-family: var(--mono); font-size: .68rem; letter-spacing: .1em;
    text-transform: uppercase; color: var(--cyan);
  }
  .hm .door h2 { font-size: 1.15rem; margin: .35rem 0 .45rem; font-weight: 600; }
  .hm .door p { margin: 0; color: var(--dim); font-size: .84rem; }
  .hm h3 {
    font-size: .8rem; letter-spacing: .12em; text-transform: uppercase;
    color: var(--ink); margin: 2.8rem 0 .7rem;
  }
  .hm .jump { display: flex; flex-wrap: wrap; gap: .4rem; }
  .hm .jump a {
    font-size: .78rem; color: var(--dim); text-decoration: none;
    border: 1px solid var(--edge); border-radius: 2px; padding: .28rem .55rem;
    background: var(--sunk);
  }
  .hm .jump a:hover { color: var(--cyan); border-color: var(--cyan); }
  .hm .note { color: var(--faint); font-size: .76rem; margin-top: 2.6rem; }
"""


def home_page():
    sectors, cards = sector_slugs(), card_slugs()
    doors = "".join(
        '<a class="door" href="%s"><div class="n">%s</div><h2>%s</h2><p>%s</p></a>' % (
            href, html.escape(count), html.escape(title), html.escape(blurb))
        for href, count, title, blurb in (
            ("/sectors/", HOME["sectors_count"].format(n=len(sectors)),
             HOME["sectors_title"], HOME["sectors_blurb"]),
            ("/cards/", HOME["cards_count"].format(n=len(cards)),
             HOME["cards_title"], HOME["cards_blurb"])))
    jump = "".join('<a href="/sectors/%s">%s</a>' % (slug, html.escape(name))
                   for name, slug in sector_menu())
    body = (
        '<div class="hm">'
        '<p class="eyebrow">%(eyebrow)s</p><h1>%(heading)s</h1>'
        '<p class="lede">%(lede)s</p>'
        '<div class="doors">%(doors)s</div>'
        '<h3>%(jh)s</h3><div class="jump">%(jump)s</div>'
        '<p class="note">%(note)s</p>'
        "</div>" % {
            "eyebrow": html.escape(HOME["eyebrow"]),
            "heading": html.escape(HOME["heading"]),
            "lede": html.escape(HOME["lede"]),
            "doors": doors,
            "jh": html.escape(HOME["jump_heading"]),
            "jump": jump,
            "note": html.escape(HOME["note"]),
        })
    return document(HOME["title"], body, head="<style>%s</style>" % HOME_CSS)


# --------------------------------------------------------------------------
# Routing
# --------------------------------------------------------------------------

def keep(query):
    return "?" + query if query else ""


def wants_raw(query):
    return "raw=1" in query.split("&")


def serve_raw(path):
    """The built file, byte for byte, as source rather than as a page.

    What the nav's `Built file` link opens. Without it that link pointed at the built
    file's own URL, which redirects to the clean one -- so it navigated back to the page
    the reader was already on. The point of the link is to see what the build wrote,
    chrome and all, so it is served as text/plain."""
    return Response(200, path.read_bytes(), "text/plain; charset=utf-8")


def static(root, rel):
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", rel or "") or ".." in rel:
        return text("bad path", 400)
    path = os.path.normpath(os.path.join(str(root), rel))
    if os.path.commonpath([path, str(root)]) != str(root) or not os.path.isfile(path):
        return text("not found", 404)
    ctype, _ = mimetypes.guess_type(path)
    with open(path, "rb") as fh:
        return Response(200, fh.read(), ctype or "application/octet-stream")


def resolve(path, query=""):
    """path -> Response. The whole route table, as one pure function, so `--check`
    exercises exactly what a browser gets and not a second implementation of it."""

    if path == "/":
        return home_page()

    # A directory index needs its trailing slash, or every relative link in the page
    # resolves one level too high: from `/sectors`, `sector-x.html` is `/sector-x.html`.
    if path in ("/sectors", "/cards"):
        return redirect(path + "/" + keep(query))

    if path == "/sectors/":
        page = SECTOR_DIR / "index.html"
        if not page.exists():
            return text("no sectors/index.html -- run tools/build-sector-index.py", 404)
        if wants_raw(query):
            return serve_raw(page)
        return spliced_page(page, "sectors", [], "?raw=1")

    if path == "/cards/":
        page = CARD_DIR / "index.html"
        if not page.exists():
            return text("no cards/index.html -- run tools/build-card-index.py", 404)
        if wants_raw(query):
            return serve_raw(page)
        return spliced_page(page, "cards", [], "?raw=1")

    # The built shapes, and the watcher's, upgraded to the canonical ones as they are
    # followed. This is what lets the pages keep their own relative links: a profile's
    # `../cards/card-x.html` lands here and leaves with `/cards/x`.
    for pattern, to in (
            (r"/sectors/index\.html", "/sectors/"),
            (r"/cards/index\.html", "/cards/"),
            (r"/sectors/sector-(%s)\.html" % SLUG, "/sectors/%s"),
            (r"/cards/card-(%s)\.html" % SLUG, "/cards/%s"),
            (r"/sector/(%s)" % SLUG, "/sectors/%s"),
            (r"/card/(%s)" % SLUG, "/cards/%s")):
        match = re.fullmatch(pattern, path)
        if match:
            target = to % match.group(1) if "%s" in to else to
            return redirect(target + keep(query))

    match = re.fullmatch(r"/sectors/(%s)" % SLUG, path)
    if match:
        slug = match.group(1)
        page = SECTOR_DIR / ("sector-%s.html" % slug)
        if page.exists():
            if wants_raw(query):
                return serve_raw(page)
            # The `?seen=` overlay is only ever attached here, and only when the
            # parameter is present, so a plain sector page is unchanged by its
            # existence. The style goes in the head; the script goes last, because it
            # reads beacon boxes the page's own markup has to have produced first.
            asked_seen = "seen" in urllib.parse.parse_qs(query)
            return fragment_page(
                page, "sectors",
                [(NAV["sectors"], "/sectors/"), (sector_title(slug), None)], "?raw=1",
                head="<style>%s</style>" % SEEN_CSS if asked_seen else "",
                tail="<script>%s</script>" % SEEN_JS if asked_seen else "")

    match = re.fullmatch(r"/cards/(%s)" % SLUG, path)
    if match:
        slug = match.group(1)
        page = CARD_DIR / ("card-%s.html" % slug)
        if page.exists():
            if wants_raw(query):
                return serve_raw(page)
            return fragment_page(page, "cards",
                                 [(NAV["cards"], "/cards/"), (card_title(slug), None)],
                                 "?raw=1")

    # Everything else under the two directories is a file the pages ask for by its own
    # relative path: the card runtime, a card payload, a sector profile's JSON.
    for prefix, root in (("/sectors/", SECTOR_DIR), ("/cards/", CARD_DIR)):
        if path.startswith(prefix):
            return static(root, path[len(prefix):])

    return text("not found", 404)


# --------------------------------------------------------------------------
# Check
# --------------------------------------------------------------------------

def routes():
    """Every URL this site claims to serve, in reading order."""
    out = [("/", "home"), ("/sectors", "redirect"), ("/sectors/", "chooser")]
    out += [("/sectors/%s" % s, "sector") for s in sector_slugs()]
    out += [("/cards", "redirect"), ("/cards/", "event index")]
    out += [("/cards/%s" % s, "card") for s in card_slugs()]
    out += [("/cards/runtime/card.js", "static"), ("/cards/runtime/card.css", "static")]
    return out


# A relative reference to a sibling file. The charset is deliberately narrow: these
# pages build hrefs in JavaScript too (`'sector-' + s.slug + '.html'`), and a pattern
# loose enough to admit a quote or a plus reports those as missing files. Only what
# could actually be a path on disk counts.
ASSET = re.compile(r'(?:src|href)="((?:\.\./)?[A-Za-z0-9][A-Za-z0-9._/-]*'
                   r'\.(?:js|css|html))"', re.I)


def check(verbose=False):
    """Walk every route, follow one redirect hop, and resolve every relative asset a
    page asks for. A link that 404s is the failure this catches; nothing else can,
    because the pages are built for `file://` and their links are all relative."""
    problems, seen = [], 0

    def get(path, query=""):
        """Returns the path the content actually came from, which is what a relative
        link in that content resolves against -- not the path asked for. Following a
        redirect and then resolving assets against the pre-redirect path is how a
        checker invents failures nobody can reproduce in a browser."""
        response = resolve(path, query)
        if response.status == 301:
            path, _, query = response.location.partition("?")
            response = resolve(path, query)
        return path, response

    for path, kind in routes():
        seen += 1
        final, response = get(path)
        if response.status != 200:
            problems.append("%-46s %s %d" % (path, kind, response.status))
            continue
        if verbose:
            print("  %-46s %s" % (path, kind))
        if not response.ctype.startswith("text/html"):
            continue
        # The assets the page itself asks for, resolved the way a browser resolves
        # them: relative to the directory of the URL it was served from.
        base = final.rsplit("/", 1)[0] + "/"
        for ref in sorted(set(ASSET.findall(response.body.decode("utf-8", "replace")))):
            target = os.path.normpath(os.path.join(base, ref)).replace("\\", "/")
            if get(target)[1].status != 200:
                problems.append("%-46s asks for %s -- missing" % (final, target))

    # `?raw=1` is the nav's `Built file` link. It shares no code with the wrapped path,
    # so nothing above would notice it breaking.
    raw_probes = ["/sectors/", "/cards/"]
    raw_probes += ["/sectors/%s" % s for s in sector_slugs()[:1]]
    raw_probes += ["/cards/%s" % s for s in card_slugs()[:1]]
    for path in raw_probes:
        response = resolve(path, "raw=1")
        seen += 1
        if response.status != 200 or not response.ctype.startswith("text/plain"):
            problems.append("%-46s raw=1 %s" % (path, response))

    # `?seen=` is attached by the server, not the build, so nothing above sees it. The
    # invariant worth holding is symmetric: present when asked for, and **absent when
    # not** -- a sector page with no `?seen=` must be the page it was before the
    # overlay existed.
    for slug in sector_slugs()[:1]:
        seen += 2
        with_seen = resolve("/sectors/%s" % slug, "seen=store-engi").body.decode()
        without = resolve("/sectors/%s" % slug).body.decode()
        if "sb-seenbar" not in with_seen or "sb-is-seen" not in with_seen:
            problems.append("%-46s ?seen= did not attach the overlay" % slug)
        if "sb-seen" in without:
            problems.append("%-46s overlay leaked onto a page with no ?seen=" % slug)

    print("routes    %d" % seen)
    print("sectors   %d" % len(sector_slugs()))
    print("cards     %d" % len(card_slugs()))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for line in problems[:40]:
            print("  " + line)
        if len(problems) > 40:
            print("  ... and %d more" % (len(problems) - 40))
        return 1
    print("\nok — every route serves and every asset it asks for resolves")
    return 0


# --------------------------------------------------------------------------
# Server
# --------------------------------------------------------------------------

def make_handler(quiet):
    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, fmt, *args):
            if not quiet:
                sys.stderr.write("  %s %s\n" % (self.command, self.path))

        def _respond(self, body=True):
            path, _, query = self.path.partition("?")
            try:
                response = resolve(path, query)
            except Exception as exc:                       # a broken build, not a crash
                response = text("%s: %s" % (type(exc).__name__, exc), 500)
            self.send_response(response.status)
            if response.location:
                self.send_header("Location", response.location)
            self.send_header("Content-Type", response.ctype)
            # Sent even on a HEAD, where it describes the body a GET would return. The
            # length must still be right or keep-alive desynchronises on HTTP/1.1.
            self.send_header("Content-Length", str(len(response.body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if body:
                self.wfile.write(response.body)

        def do_GET(self):
            self._respond()

        def do_HEAD(self):
            self._respond(body=False)

    return Handler


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--open", action="store_true", help="open a browser at the site")
    ap.add_argument("--check", action="store_true",
                    help="walk every route and every asset, then exit")
    ap.add_argument("--routes", action="store_true", help="print the route table, exit")
    ap.add_argument("--verbose", action="store_true", help="list routes while checking")
    ap.add_argument("--quiet", action="store_true", help="do not log requests")
    args = ap.parse_args()

    if args.routes:
        for path, kind in routes():
            print("%-46s %s" % (path, kind))
        return 0
    if args.check:
        return check(args.verbose)

    url = "http://%s:%d/" % (args.host, args.port)
    with Server((args.host, args.port), make_handler(args.quiet)) as srv:
        print("serving %s" % url)
        print("        %d sectors, %d cards" % (len(sector_slugs()), len(card_slugs())))
        if args.open:
            webbrowser.open(url)
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
