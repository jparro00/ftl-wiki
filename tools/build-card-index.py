#!/usr/bin/env python3
"""Build `cards/index.html`: the way in to all 386 event cards.

    python tools/build-card-index.py            # write cards/index.html
    python tools/build-card-index.py --verify   # check an already-built page

The cards have never had an index. There are 386 of them and the only ways to reach one
were a direct link and a beacon box on a sector profile, so an event nobody had thought
of was unreachable. This is the list: name, in-game id, its derived tags, and which
sector pools can place it — searchable, and every filter in the URL.

Everything is read, nothing is written by hand:

    cards/trees/*.tree.json        the 386 cards — slug, title, in-game id
    extract-sector.Trees.profile   the tags and blue options, derived from the tree
    sectors/data/*.sector.json     which sector pools can place the event

**The tags come from `extract-sector.py`, not from the sector profiles.** Same function
the sector pages tag their pool rows with, called here on every tree — so a tag reads
identically in both places, and the 118 cards below are tagged too. Reading the tags
back out of the profiles would have tagged only what a pool happens to list.

**118 of the 386 sit in no sector pool** and are listed as such rather than dropped.
They are reachable another way — a chain step, a fight outcome, the boss — and a list
that quietly held 268 would read as the whole set.

Words live in `tools/site-vocab.json` under `cards_index`. Tag labels are read from
`tools/sector-vocab.json`, so a tag reads the same here as on a sector page.
"""

import argparse
import html
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
TREES = ROOT / "cards" / "trees"
CARDS = ROOT / "cards"
SECTOR_DATA = ROOT / "sectors" / "data"
OUT = CARDS / "index.html"
SHELL = ROOT / "tools" / "sector-page-render.html"
SITE_VOCAB = ROOT / "tools" / "site-vocab.json"
SECTOR_VOCAB = ROOT / "tools" / "sector-vocab.json"

VOC = json.loads(SITE_VOCAB.read_text(encoding="utf-8"))["cards_index"]
_SEC = json.loads(SECTOR_VOCAB.read_text(encoding="utf-8"))
TAG_LABEL = _SEC["tags"]
TAG_ORDER = _SEC["tag_order"] + [t for t in _SEC["marker_tags"]]


def _load_sector_extractor():
    """Reuse `extract-sector.py`'s tag derivation; its module name is not importable.

    Same trick `extract-sector.py` itself uses to reach `extract-event.py`. What is
    borrowed is `Trees.profile()` — the one function that turns a tree into tags and
    blue options. A second implementation of it here would drift from the sector pages
    within a week, and the drift would be invisible: two plausible tag lists.
    """
    spec = importlib.util.spec_from_file_location(
        "ftl_extract_sector", TOOLS / "extract-sector.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tokens():
    """The palette, sliced out of the page shell — same block, same reason, as
    `build-sector-index.py` and `serve-site.py`: the pages must not drift in colour."""
    shell = SHELL.read_text(encoding="utf-8")
    start = shell.index("/* TOKENS-START")
    start = shell.index("*/", start) + 2
    end = shell.index("/* TOKENS-END */")
    return shell[start:end].strip()


def load_cards():
    """slug -> {slug, title, id}, one per built tree."""
    out = {}
    for path in sorted(TREES.glob("*.tree.json")):
        tree = json.loads(path.read_text(encoding="utf-8"))
        out[tree["slug"]] = {"slug": tree["slug"], "title": tree["title"],
                             "id": tree.get("id") or tree.get("name") or ""}
    if not out:
        raise SystemExit("no trees in %s -- run tools/extract-event.py" % TREES)
    return out


def load_pools():
    """Which sector pools can place each event.

    Returns (sectors, per_event): `sectors` is slug -> display name in earliest-first
    order; `per_event` is event slug -> [sector slug]. An event listed twice in one
    sector is one entry — the pools are lists of what can be placed, not of beacons,
    and counting a repeat would read as a frequency no file states.

    Only membership is taken from here. The tags come from the tree (see `profiles`),
    so a card outside every pool is tagged the same way as one inside twelve.
    """
    sectors, per_event, ordered = {}, {}, []
    for path in sorted(SECTOR_DATA.glob("*.sector.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        ordered.append((data["earliest_sector"], data["display_name"], data["slug"]))
        for entry in data["entries"]:
            for event in entry.get("events") or []:
                slug = event.get("slug")
                if not slug:
                    continue
                pools = per_event.setdefault(slug, [])
                if data["slug"] not in pools:
                    pools.append(data["slug"])
    for _, name, slug in sorted(ordered):
        sectors[slug] = name
    return sectors, per_event


def profiles():
    """event id -> the derived tag/gate profile, from `extract-sector.py`'s own code."""
    return _load_sector_extractor().Trees()


def record(card, pools, sector_names, trees):
    mine = pools.get(card["slug"], [])
    profile = trees.profile(card["id"]) if card["id"] else {"card": False}
    tags = [t for t in TAG_ORDER if t in (profile.get("tags") or [])]
    gates = sorted({g["label"] for g in profile.get("gates") or []})
    return {
        "slug": card["slug"],
        "title": card["title"],
        "id": card["id"],
        "sectors": mine,
        "sector_names": [sector_names[s] for s in mine],
        "tags": tags,
        "gates": gates,
    }


CSS = """
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 2.6rem 1.15rem 4.5rem;
    background: var(--void);
    background-image: radial-gradient(var(--hex) 1px, transparent 1.6px);
    background-size: 22px 22px;
    color: var(--ink); font-family: var(--sans); line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }
  /* the width the cards and the sector profiles are read at */
  .wrap { max-width: 58rem; margin: 0 auto; }
  .eyebrow {
    font-family: var(--mono); font-size: .66rem; letter-spacing: .19em;
    text-transform: uppercase; color: var(--cyan); margin: 0 0 .55rem;
  }
  h1 { font-size: 1.9rem; margin: 0 0 .3rem; letter-spacing: -.01em; }
  .lede { color: var(--dim); font-size: .92rem; max-width: 40rem; margin: 0 0 1.6rem; }

  /* The controls are sticky because the list is 386 rows long: a filter you have to
     scroll back up to change is a filter nobody changes twice. */
  .bar {
    position: sticky; top: 0; z-index: 20; display: flex; flex-wrap: wrap;
    gap: .5rem; align-items: center; padding: .7rem 0;
    background: var(--void); border-bottom: 1px solid var(--edge);
  }
  .bar input, .bar select {
    background: var(--sunk); color: var(--ink); border: 1px solid var(--edge);
    border-radius: 2px; padding: .4rem .55rem; font-family: var(--sans);
    font-size: .82rem; line-height: 1.2;
  }
  .bar input { flex: 1 1 15rem; min-width: 10rem; }
  .bar input:focus, .bar select:focus { outline: none; border-color: var(--cyan); }
  .bar .count {
    font-family: var(--mono); font-size: .72rem; color: var(--faint);
    margin-left: auto; white-space: nowrap;
  }
  .bar button {
    background: transparent; border: 1px solid var(--edge); border-radius: 2px;
    color: var(--faint); font-family: var(--sans); font-size: .76rem;
    padding: .4rem .55rem; cursor: pointer;
  }
  .bar button:hover { color: var(--cyan); border-color: var(--cyan); }
  .bar button[hidden] { display: none; }

  .list { margin-top: .3rem; }
  /* One grid per row rather than a table, so the id and the tags can drop below the
     name on a narrow window -- which a table cell cannot do.
     **Every column is a fixed width except the name.** Each row is its own grid, so an
     `auto` or `1fr` track is sized from that row's own content and the columns come out
     ragged down the page: the ids wandered left and right by a hundred pixels because
     the tag cell above them held one chip and the one below held six. */
  .row {
    display: grid; grid-template-columns: minmax(8rem, 1fr) 11.5rem 19rem 4.5rem;
    align-items: baseline; gap: .3rem .8rem;
    padding: .5rem .55rem; text-decoration: none; color: inherit;
    border-bottom: 1px solid var(--sunk);
  }
  .row:hover { background: var(--panel); }
  /* The same grid, so the labels sit over the columns they name. Without them the last
     cell is a bare integer and nothing on the page says what it counts. */
  .row.head {
    font-family: var(--mono); font-size: .62rem; letter-spacing: .1em;
    text-transform: uppercase; color: var(--faint);
    border-bottom: 1px solid var(--edge); padding-top: .8rem;
  }
  .row.head:hover { background: none; }
  .row.head .tg, .row.head .sc { text-align: right; display: block; }
  .row .nm { font-size: .88rem; font-weight: 500; }
  .row:hover .nm { color: var(--cyan); }
  .row .id {
    font-family: var(--mono); font-size: .68rem; color: var(--faint);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }
  .row .tg { display: flex; flex-wrap: wrap; gap: .25rem; justify-content: flex-end; }
  .row .sc {
    font-family: var(--mono); font-size: .7rem; color: var(--dim); text-align: right;
    white-space: nowrap;
  }
  .row .sc.none { color: var(--faint); }
  .row[hidden] { display: none; }
  .chip {
    font-size: .58rem; letter-spacing: .09em; text-transform: uppercase;
    padding: .06rem .3rem; border-radius: 2px; border: 1px solid currentColor;
    color: var(--faint); white-space: nowrap;
  }
  .chip.fight, .chip.boarders, .chip.crew-loss { color: var(--red); }
  .chip.may-fight { color: var(--amber); }
  .chip.crew, .chip.reward { color: var(--green); }
  .chip.store, .chip.store-marker, .chip.quest, .chip.distress { color: var(--cyan); }

  .empty { color: var(--faint); font-size: .85rem; padding: 2rem .55rem; }
  .empty[hidden] { display: none; }
  .note { color: var(--faint); font-size: .76rem; margin-top: 1.6rem; }
"""

SCRIPT = """
const WORDS = %(words)s;

// Every filter is in the URL, and the URL is the state -- so a filtered list is a link
// you can send, and reloading one reproduces it. Nothing is remembered anywhere else:
// a stored filter would silently hide events from the next reader of a shared link.
const params = new URLSearchParams(location.search);
const q = document.getElementById('q');
const sec = document.getElementById('sec');
const tag = document.getElementById('tag');
const count = document.getElementById('count');
const empty = document.getElementById('empty');
const clear = document.getElementById('clear');
// `.list .row`, not `.row`: the column-label row above the list is the same grid and
// therefore the same class, but it carries no data attributes -- selecting it counted it
// as a 387th event and threw on the first keystroke.
const rows = Array.prototype.slice.call(document.querySelectorAll('.list .row'));
const total = rows.length;

q.value = params.get('q') || '';
sec.value = params.get('sector') || '';
tag.value = params.get('tag') || '';

function apply(push) {
  const needle = q.value.trim().toLowerCase();
  const wantSec = sec.value;
  const wantTag = tag.value;
  let shown = 0;
  rows.forEach(row => {
    // `none` is the 118 events no sector pool lists. It is a real answer to "which
    // pool places this", not the absence of one, so it is a filter value like any other.
    const pools = row.dataset.sectors;
    const ok =
      (!needle || row.dataset.find.indexOf(needle) >= 0) &&
      (!wantSec || (wantSec === 'none' ? !pools : (' ' + pools + ' ').indexOf(' ' + wantSec + ' ') >= 0)) &&
      (!wantTag || (' ' + row.dataset.tags + ' ').indexOf(' ' + wantTag + ' ') >= 0);
    row.hidden = !ok;
    if (ok) shown++;
  });
  const filtered = needle || wantSec || wantTag;
  count.textContent = filtered
    ? WORDS.count.replace('{shown}', shown).replace('{total}', total)
    : WORDS.count_all.replace('{total}', total);
  empty.hidden = shown > 0;
  clear.hidden = !filtered;

  if (push !== false) {
    const next = new URLSearchParams();
    if (needle) next.set('q', q.value.trim());
    if (wantSec) next.set('sector', wantSec);
    if (wantTag) next.set('tag', wantTag);
    const qs = next.toString();
    history.replaceState(null, '', qs ? '?' + qs : location.pathname);
  }
}

q.addEventListener('input', () => apply());
sec.addEventListener('change', () => apply());
tag.addEventListener('change', () => apply());
clear.addEventListener('click', () => {
  q.value = ''; sec.value = ''; tag.value = ''; apply();
});

apply(false);
"""


def row_html(rec):
    tags = "".join('<span class="chip %s">%s</span>' % (t, html.escape(TAG_LABEL[t]))
                   for t in rec["tags"])
    if rec["sectors"]:
        pools = " · ".join(rec["sector_names"])
        cell = ('<span class="sc" title="%s">%d</span>'
                % (html.escape(pools, quote=True), len(rec["sectors"])))
    else:
        cell = ('<span class="sc none" title="%s">%s</span>'
                % (html.escape(VOC["no_pool_hint"], quote=True), "—"))
    # What a search matches: the name, the in-game id, the tag labels and the blue
    # options. All lowercased once here rather than 386 times per keystroke.
    find = " ".join([rec["title"], rec["id"]]
                    + [TAG_LABEL[t] for t in rec["tags"]]
                    + rec["gates"] + rec["sector_names"]).lower()
    return (
        '<a class="row" href="card-%(slug)s.html" data-slug="%(slug)s" '
        'data-sectors="%(sectors)s" data-tags="%(tags)s" data-find="%(find)s" '
        'title="%(open)s">'
        '<span class="nm">%(title)s</span>'
        '<span class="id">%(id)s</span>'
        '<span class="tg">%(chips)s</span>'
        '%(cell)s</a>' % {
            "slug": html.escape(rec["slug"], quote=True),
            "sectors": html.escape(" ".join(rec["sectors"]), quote=True),
            "tags": html.escape(" ".join(rec["tags"]), quote=True),
            "find": html.escape(find, quote=True),
            "open": html.escape(VOC["open"], quote=True),
            "title": html.escape(rec["title"]),
            "id": html.escape(rec["id"]),
            "chips": tags, "cell": cell,
        })


def build():
    cards = load_cards()
    sector_names, pools = load_pools()
    trees = profiles()
    records = [record(c, pools, sector_names, trees) for c in cards.values()]
    records.sort(key=lambda r: (r["title"].lower(), r["slug"]))

    unknown = sorted(set(pools) - set(cards))
    orphan = [r for r in records if not r["sectors"]]

    sec_options = "".join(
        '<option value="%s">%s</option>' % (html.escape(slug, quote=True),
                                            html.escape(name))
        for slug, name in sector_names.items())
    used_tags = sorted({t for r in records for t in r["tags"]},
                       key=lambda t: TAG_ORDER.index(t))
    tag_options = "".join(
        '<option value="%s">%s</option>' % (html.escape(t, quote=True),
                                            html.escape(TAG_LABEL[t]))
        for t in used_tags)

    page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
%(tokens)s
%(css)s
</style></head>
<body><div class="wrap">
<header>
  <p class="eyebrow">%(eyebrow)s</p>
  <h1>%(heading)s</h1>
  <p class="lede">%(lede)s</p>
</header>
<div class="bar">
  <input id="q" type="search" placeholder="%(search)s" aria-label="%(search_label)s">
  <select id="sec" aria-label="%(sector_label)s">
    <option value="">%(any_sector)s</option>
    %(sec_options)s
    <option value="none">%(no_pool)s</option>
  </select>
  <select id="tag" aria-label="%(tag_label)s">
    <option value="">%(any_tag)s</option>
    %(tag_options)s
  </select>
  <button id="clear" type="button" hidden>%(clear)s</button>
  <span class="count" id="count"></span>
</div>
<div class="row head" aria-hidden="true">
  <span class="nm">%(col_name)s</span><span class="id">%(col_id)s</span>
  <span class="tg">%(col_tags)s</span><span class="sc">%(col_pools)s</span>
</div>
<div class="list">%(rows)s</div>
<p class="empty" id="empty" hidden>%(none)s</p>
<p class="note">%(note)s</p>
</div>
<script>
%(script)s
</script>
</body></html>
""" % {
        "title": html.escape(VOC["title"]),
        "tokens": tokens(),
        "css": CSS,
        "eyebrow": html.escape(VOC["eyebrow"]),
        "heading": html.escape(VOC["heading"]),
        "lede": html.escape(VOC["lede"]),
        "search": html.escape(VOC["search"], quote=True),
        "search_label": html.escape(VOC["search_label"], quote=True),
        "sector_label": html.escape(VOC["sector_label"], quote=True),
        "tag_label": html.escape(VOC["tag_label"], quote=True),
        "any_sector": html.escape(VOC["any_sector"]),
        "any_tag": html.escape(VOC["any_tag"]),
        "no_pool": html.escape(VOC["no_pool"]),
        "sec_options": sec_options,
        "tag_options": tag_options,
        "clear": html.escape(VOC["clear"]),
        "col_name": html.escape(VOC["col_name"]),
        "col_id": html.escape(VOC["col_id"]),
        "col_tags": html.escape(VOC["col_tags"]),
        "col_pools": html.escape(VOC["sectors_col"]),
        "rows": "".join(row_html(r) for r in records),
        "none": html.escape(VOC["none"]),
        "note": html.escape(VOC["note"]),
        "script": SCRIPT % {"words": json.dumps(
            {k: VOC[k] for k in ("count", "count_all")}, ensure_ascii=False)},
    }
    OUT.write_text(page, encoding="utf-8", newline="\n")
    return records, orphan, unknown


def verify(records=None):
    problems = []
    if not OUT.exists():
        return ["%s does not exist -- build it" % OUT]
    page = OUT.read_text(encoding="utf-8")
    if records is None:
        cards = load_cards()
        sector_names, pools = load_pools()
        trees = profiles()
        records = [record(c, pools, sector_names, trees) for c in cards.values()]

    built = set(re.findall(r'data-slug="([a-z0-9-]+)"', page))
    for rec in records:
        if rec["slug"] not in built:
            problems.append("%s is missing from the page" % rec["slug"])
        # A row that links nowhere is worse than a row that is missing.
        if not (OUT.parent / ("card-%s.html" % rec["slug"])).exists():
            problems.append("%s links to a card that does not exist" % rec["slug"])
    for extra in sorted(built - {r["slug"] for r in records}):
        problems.append("%s is on the page but has no tree" % extra)
    if "%(" in page or re.search(r"%[sd]\b", page):
        problems.append("an unsubstituted format token survived into the page")
    if "--void" not in page:
        problems.append("the palette was not sliced out of the shell")
    for marker in ('id="q"', 'id="sec"', 'id="tag"', 'id="count"'):
        if marker not in page:
            problems.append("the filter bar is missing %s" % marker)
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true",
                    help="check the built page without rebuilding it")
    args = ap.parse_args()

    records = None
    if not args.verify:
        records, orphan, unknown = build()
        print("built    %s" % OUT)
        print("         %d cards, %d in no sector pool"
              % (len(records), len(orphan)))
        if unknown:
            # A pool naming an event with no tree is a card that was never built.
            print("         %d pool events have no card: %s"
                  % (len(unknown), ", ".join(unknown[:6])))

    problems = verify(records)
    if problems:
        print("\n%d problem(s):" % len(problems))
        for line in problems[:30]:
            print("  " + line)
        return 1
    print("verified ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
