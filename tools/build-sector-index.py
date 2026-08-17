#!/usr/bin/env python3
"""Build `sectors/index.html`: the chooser you read at a jump.

    python tools/build-sector-index.py            # write sectors/index.html
    python tools/build-sector-index.py --verify    # check an already-built page

The sector map offers **two** destinations. This page lists all 19 sectors under the
designation the map colours them with, and lets two of them be pinned into a panel at
the top, side by side, with the numbers that decide a jump. Clicking a sector opens its
profile (`SECTOR-PAGE.md`).

Everything except the words comes from `sectors/data/*.sector.json` — the same profiles
the pages are built from — plus one thing those files do not carry: the civilian /
hostile / nebula designation. That **is** in the game data, in the `<sectorType>` draw
lists at the top of `sector_data.xml`, which is where the map gets it. The community
wiki's grouping (`raw/wiki/sectors.md`) is read too, but only as a cross-check and for
the one thing the draw lists cannot say — that a sector is pinned to one position.

Words live in `tools/sector-vocab.json` under `index`, like every other sector page.
"""

import argparse
import html
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "sectors" / "data"
OUT = ROOT / "sectors" / "index.html"
SHELL = ROOT / "tools" / "sector-page-render.html"
VOCAB = ROOT / "tools" / "sector-vocab.json"
RAW_SECTORS = ROOT / "raw" / "wiki" / "sectors.md"
WIKI_SECTORS = ROOT / "wiki" / "sectors"

VOC = json.loads(VOCAB.read_text(encoding="utf-8"))["index"]

# The community wiki heads its three groups with these -- used for the cross-check and
# for the section bodies, not for the designation itself, which comes from the draw
# lists below. The class order is display order on the page.
GROUP_HEADINGS = [
    ("civilian", "Civilian Sectors"),
    ("hostile", "Hostile Sectors"),
    ("nebula", "Nebula Sectors"),
]
CLASS_ORDER = ["civilian", "hostile", "nebula", "special"]

# One name disagrees between the two layers, for a reason worth keeping visible: the
# community wiki calls STANDARD_SPACE the "Civilian (Starting) Sector", while
# text_sectorname.xml — which is what the profiles use — calls it Federation Space.
HEADING_ALIASES = {"Civilian (Starting) Sector": "Federation Space"}


SECTOR_DATA_XML = ROOT / "raw" / "gamedata" / "sector_data.xml"

# The draw lists the map rolls against. OVERRIDE_HOSTILE is the Advanced Edition form
# of HOSTILE -- the same substitution resolved for event lists in
# `concept-sector-event-allocation` -- and it differs by exactly one sector.
TYPE_CLASS = {"CIVILIAN": "civilian", "HOSTILE": "hostile",
              "OVERRIDE_HOSTILE": "hostile", "NEBULA": "nebula"}


def load_types():
    """Sector id -> {class, ae_only}, from `sector_data.xml`'s `<sectorType>` lists.

    A sector in none of them is in no draw list at all and the map can never offer it:
    STANDARD_SPACE (filed under `UNKNOWN`), CRYSTAL_HOME and FINAL. That is a stronger
    statement than "the community wiki groups it separately", and it is the file's.

    Comments are stripped first. `UNKNOWN` carries four commented-out members, and
    `ZOLTAN_HOME` and `ROCK_HOME` are among them -- reading those would contradict
    their live entries in CIVILIAN and HOSTILE.
    """
    text = re.sub(r"<!--.*?-->", "", SECTOR_DATA_XML.read_text(encoding="utf-8"),
                  flags=re.S)
    vanilla, ae = {}, {}
    for match in re.finditer(r'<sectorType name="([A-Z_]+)">(.*?)</sectorType>',
                             text, re.S):
        name, body = match.groups()
        cls = TYPE_CLASS.get(name)
        if not cls:
            continue
        target = ae if name.startswith("OVERRIDE_") else vanilla
        for sector_id in re.findall(r"<sector>([A-Z_0-9]+)</sector>", body):
            target[sector_id] = cls
    # Union, like every other OVERRIDE_ read in this repo: what a running game can
    # offer, with the edition difference recorded rather than resolved away.
    out = {sid: {"class": cls, "ae_only": False} for sid, cls in vanilla.items()}
    for sid, cls in ae.items():
        if sid in out:
            continue
        out[sid] = {"class": cls, "ae_only": True}
    return out


def load_sectors():
    out = []
    for path in sorted(DATA.glob("*.sector.json")):
        out.append(json.loads(path.read_text(encoding="utf-8")))
    if not out:
        raise SystemExit("no sector profiles in %s -- run extract-sector.py --all" % DATA)
    return out


# A sector the map never offers as a choice says so in its own section. Read rather
# than listed: if the wording changes the note simply stops appearing, which is the
# right failure -- no claim is invented.
FIXED_SECTOR = re.compile(r"always (?:and only )?sector\s*'*(\d)", re.I)


def community_groups():
    """Display name -> (class, section text), off the community wiki's headings.

    Two heading shapes, and the difference between them is the structure: `==` opens
    a group, `===` names a sector inside the group last opened. The two specials are
    written as `==` sections of their own, which is exactly how the page says they are
    not part of the three-colour roll. Reading the structure keeps this derived rather
    than hand-listed, which matters because it is the one field on this page that no
    game file states.

    Every section's body is kept too — that is where a sector says it is fixed to one
    position ("always sector 8"), which the allocation table cannot express.
    """
    text = RAW_SECTORS.read_text(encoding="utf-8", errors="replace")
    groups = {heading: key for key, heading in GROUP_HEADINGS}

    headings = list(re.finditer(
        r"^(?:==\s*<span[^>]*>'''(?P<top>.+?)'''</span>\s*=="
        r"|===\s*<h2>(?P<sub>.+?)</h2>\s*===)\s*$", text, re.M))
    if not any(h.group("top") in groups for h in headings):
        raise SystemExit("no group headings in %s -- has the page been restructured?"
                         % RAW_SECTORS)

    classes, group = {}, None
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[match.end():end]
        top, sub = match.group("top"), match.group("sub")
        if top is not None:
            group = groups.get(top)
            if group is None:
                # A top-level section that is not a group: the two specials, and the
                # page's own technical sections, which no sector name will match.
                classes[HEADING_ALIASES.get(top.strip(), top.strip())] = (None, body)
        else:
            name = HEADING_ALIASES.get(sub.strip(), sub.strip())
            classes[name] = (group, body)
    return classes


def wiki_class(slug):
    """What our own sector page claims, for the cross-check. None if it says nothing."""
    path = WIKI_SECTORS / ("%s.md" % slug)
    if not path.exists():
        return None
    match = re.search(r"^sector_class:\s*(\w+)", path.read_text(encoding="utf-8"), re.M)
    return match.group(1) if match else None


def classify(sectors):
    """Attach a class to every sector, and report where the other layers disagree.

    The draw lists decide. The community wiki's grouping and our own `sector_class`
    frontmatter are read only to be checked against them — a disagreement is a note,
    never an override, because one of the three is a game file and the other two are
    interpretations of it.
    """
    by_id = load_types()
    by_name = community_groups()
    notes = []
    for sector in sectors:
        entry = by_id.get(sector["id"])
        sector["class"] = entry["class"] if entry else "special"
        sector["ae_only"] = bool(entry and entry["ae_only"])

        group, body = by_name.get(sector["display_name"], (None, ""))
        fixed = FIXED_SECTOR.search(body or "")
        sector["fixed_sector"] = int(fixed.group(1)) if fixed else None

        if group and group != sector["class"]:
            notes.append("%s: the draw lists say %r, the community wiki groups it as %r"
                         % (sector["slug"], sector["class"], group))
        ours = wiki_class(sector["slug"])
        if ours and ours != sector["class"]:
            notes.append("%s: wiki/sectors says %r, the draw lists say %r"
                         % (sector["slug"], ours, sector["class"]))
    return notes


def compare_rows(sector):
    """The handful of numbers that decide a jump, as (id, label, low, high)."""
    metrics, generation = sector["metrics"], sector["generation"]
    rows = []
    for key, label in VOC["compare"]:
        if key == "beacons":
            low, high = metrics["beacons_min"], metrics["beacons_max"]
        elif key == "fallback":
            span = generation.get("fallback_beacons") or {}
            low, high = span.get("min", 0), span.get("max", 0)
        elif key.endswith(":"):
            low, high = metrics.get(key + "min", 0), metrics.get(key + "max", 0)
        else:
            low = high = metrics.get(key, 0)
        rows.append({"key": key, "label": label, "low": low, "high": high})
    return rows


def record(sector):
    """Everything the page needs about one sector, in one place."""
    return {
        "slug": sector["slug"],
        "id": sector["id"],
        "name": sector["display_name"],
        "class": sector["class"],
        "earliest": sector["earliest_sector"],
        "fixed": sector.get("fixed_sector"),
        "ae_only": bool(sector.get("ae_only")),
        "unique": bool(sector["unique"]),
        # The two specials are never offered as a map colour; say so rather than
        # implying they can turn up at their earliest sector like the rest.
        "offered": sector["class"] != "special",
        "rows": compare_rows(sector),
    }


def tokens():
    """The palette, sliced out of the page shell so the two cannot drift."""
    shell = SHELL.read_text(encoding="utf-8")
    start = shell.index("/* TOKENS-START")
    start = shell.index("*/", start) + 2
    end = shell.index("/* TOKENS-END */")
    return shell[start:end].strip()


CSS = """
  * { box-sizing: border-box; }
  body {
    margin: 0; padding: 2.6rem 1.15rem 4.5rem;
    background: var(--void);
    background-image: radial-gradient(var(--hex) 1px, transparent 1.6px);
    background-size: 22px 22px;
    color: var(--ink); font-family: var(--sans); line-height: 1.5;
  }
  /* the width the sector profiles are read at -- the panel below spans it exactly,
     in every state, so the page does not resize itself as sectors are pinned. */
  .wrap { max-width: 58rem; margin: 0 auto; }
  h1 { font-size: 1.9rem; margin: 0 0 .2rem; letter-spacing: -.01em; }
  h2 {
    font-size: .82rem; letter-spacing: .12em; text-transform: uppercase;
    color: var(--ink); margin: 2.4rem 0 .2rem; display: flex; flex-wrap: wrap;
    align-items: baseline; gap: .6rem;
  }
  h2 .meta {
    font-family: var(--sans); font-size: .72rem; letter-spacing: 0;
    text-transform: none; color: var(--faint);
  }
  section > .note { color: var(--faint); font-size: .78rem; margin: .3rem 0 1rem; }

  /* the pinned pair — each box is the header of its own column of numbers, so the
     alignment is structural: box and figures are the same table column, not two
     layouts hoping to agree on a width. */
  .cmp-wrap { margin-top: .9rem; overflow-x: auto; }
  /* Always the full content width, whatever is pinned: the columns are percentages,
     so the panel neither grows as sectors arrive nor shrinks to fit two boxes. */
  .cmp { width: 100%; min-width: 34rem; border-collapse: collapse; table-layout: fixed; }
  .cmp th, .cmp td {
    padding: .34rem .5rem; font-size: .82rem; font-variant-numeric: tabular-nums;
  }
  .cmp thead th { padding: 0 0 .55rem .55rem; vertical-align: bottom; }
  .cmp thead th.lab { padding: 0; }
  .cmp tbody th, .cmp tbody td { border-top: 1px solid var(--edge); }
  .cmp tbody th { text-align: left; font-weight: 400; color: var(--dim); }
  /* Centred, not flushed right: the label and the figures then sit evenly across the
     row instead of leaving a gulf between the two. */
  .cmp tbody td { text-align: center; font-family: var(--mono); }
  .cmp tbody td.more { color: var(--cyan); }
  .cmp tbody td.blank { color: var(--faint); }
  /* The whole box is the link to the profile, not just the name. */
  .slot {
    position: relative; text-align: left; min-height: 5.2rem;
    display: flex; flex-direction: column; align-items: flex-start;
    border: 1px solid var(--edge); border-top: 2px solid var(--rail);
    border-radius: 3px; background: var(--panel); padding: .5rem .6rem .55rem;
    text-decoration: none; color: inherit;
  }
  a.slot:hover { border-color: var(--rail); background: var(--sunk); }
  a.slot:hover .name { color: var(--cyan); }
  .slot.civilian { border-top-color: var(--green); }
  .slot.hostile  { border-top-color: var(--red); }
  .slot.nebula   { border-top-color: #9B7BD4; }
  .slot.special  { border-top-color: var(--amber); }
  .slot .name {
    display: block; font-size: .92rem; font-weight: 600; padding-right: 1.2rem;
    line-height: 1.25; color: var(--ink);
  }
  .slot .chip { display: inline-block; margin-top: .32rem; }
  /* margin-top:auto takes up whatever slack the equal heights leave, so the sub line
     sits on the box's floor in every column rather than wherever its name ended. */
  .slot .sub {
    font-family: var(--mono); font-size: .66rem; color: var(--faint);
    margin-top: auto; padding-top: .4rem; line-height: 1.35;
  }
  .slot .drop {
    position: absolute; top: .32rem; right: .32rem;
    background: none; border: 1px solid var(--edge); color: var(--faint);
    font-family: var(--mono); font-size: .72rem; border-radius: 2px; cursor: pointer;
    line-height: 1; padding: .1rem .3rem;
  }
  .slot .drop:hover { color: var(--red); border-color: var(--red); }
  .slot.empty {
    border: 1px dashed var(--edge); background: transparent; color: var(--faint);
    display: flex; align-items: center; justify-content: center; text-align: center;
    font-size: .74rem; padding: .85rem .6rem;
  }

  /* the 19 */
  .grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(17rem, 1fr));
    gap: .55rem; margin-top: .9rem;
  }
  .card {
    display: block; position: relative; text-decoration: none; color: inherit;
    border: 1px solid var(--edge); border-left: 2px solid var(--rail); border-radius: 3px;
    background: var(--panel); padding: .62rem .75rem .68rem;
  }
  .card:hover { border-color: var(--rail); background: var(--sunk); }
  .card:hover .name { color: var(--cyan); }
  .card.civilian { border-left-color: var(--green); }
  .card.hostile  { border-left-color: var(--red); }
  .card.nebula   { border-left-color: #9B7BD4; }
  .card.special  { border-left-color: var(--amber); }
  .card .name { font-size: .95rem; font-weight: 600; padding-right: 1.6rem; }
  .card .sub {
    font-family: var(--mono); font-size: .68rem; color: var(--faint); margin-top: .2rem;
  }
  .card .nums {
    display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .45rem;
    font-family: var(--mono); font-size: .7rem; color: var(--dim);
  }
  .card .nums b { color: var(--ink); font-weight: 600; }
  .pin {
    position: absolute; top: .45rem; right: .45rem; width: 1.35rem; height: 1.35rem;
    border: 1px solid var(--edge); border-radius: 2px; background: var(--sunk);
    color: var(--faint); font-family: var(--mono); font-size: .8rem; line-height: 1;
    cursor: pointer; padding: 0;
  }
  .pin:hover { color: var(--cyan); border-color: var(--cyan); }
  .card.pinned { border-color: var(--cyan); }
  .card.pinned .pin { color: var(--cyan); border-color: var(--cyan); }
  .chip {
    font-size: .58rem; letter-spacing: .09em; text-transform: uppercase;
    padding: .06rem .3rem; border-radius: 2px; border: 1px solid currentColor;
    font-family: var(--sans);
  }
  .chip.civilian { color: var(--green); }
  .chip.hostile { color: var(--red); }
  .chip.nebula { color: #9B7BD4; }
  .chip.special { color: var(--amber); }
  .chip.unique { color: var(--faint); }
"""

SCRIPT = """
const SECTORS = %(data)s;
const WORDS = %(words)s;
const METRICS = %(metrics)s;   // the row labels, which the table shows pinned or not
const KEY = 'ftl-sector-picks';
const MAX_PINS = 2;      // what the map offers, and what a hand can pin
const MAX_SLOTS = 4;     // ...but a map column can hold four, and a URL may carry them

const ALL = Object.keys(SECTORS);

// One `?pick=` token to one sector, or to nothing. Four ways in, tried in this order,
// because a caller may hold any of them: the save watcher resolves names off the
// Hyperspace log, a hand-written link is likelier to carry a slug, and a game id is
// what `sector_data.xml` and the log itself use.
//
//   1. slug            rock-homeworlds
//   2. game id         ROCK_HOME
//   3. display name    Rock Homeworlds
//   4. unique prefix   rock-home        (of a slug or a name)
//   5. unique substring
//
// Case and the three word separators (`-`, `_`, space) are all normalised away, so
// `ROCK_HOME`, `rock home` and `Rock-Home` are one token. **A token that matches
// nothing, or more than one sector, resolves to nothing and is reported** -- naming a
// sector the caller did not mean is worse than naming none, and the same rule already
// governs the watcher's own name resolution.
function norm(s) { return String(s).toLowerCase().replace(/[\\s_-]+/g, '-'); }

function resolvePick(token) {
  const want = norm(token);
  if (!want) return null;
  const keys = s => [norm(SECTORS[s].slug), norm(SECTORS[s].id), norm(SECTORS[s].name)];
  let hit = ALL.filter(s => keys(s).indexOf(want) >= 0);
  if (hit.length !== 1) hit = ALL.filter(s => keys(s).some(k => k.indexOf(want) === 0));
  if (hit.length !== 1) hit = ALL.filter(s => keys(s).some(k => k.indexOf(want) >= 0));
  return hit.length === 1 ? hit[0] : null;
}

// The URL is the state. `?pick=` seeds the page and every pin writes it back, so the
// address bar always reproduces what is on screen and a filtered view is a link you
// can send. localStorage is the fallback for the *bare* URL only -- with a `pick` in
// hand, a remembered pin would silently rewrite what somebody deliberately linked to.
const params = new URLSearchParams(location.search);
const asked = (params.get('pick') || '').split(',').map(s => s.trim()).filter(Boolean);
const resolved = asked.map(resolvePick);
const dropped = asked.filter((t, i) => resolved[i] === null);
let picks = resolved.filter(Boolean).filter((s, i, a) => a.indexOf(s) === i)
                    .slice(0, MAX_SLOTS);

if (!asked.length) {
  try { picks = JSON.parse(localStorage.getItem(KEY) || '[]').filter(s => SECTORS[s]); }
  catch (e) { picks = []; }
}

// &column=1 means these are the next column of the map, not a verified list of what
// this sector connects to -- Hyperspace does not expose the adjacency. The page says so
// rather than letting the panel imply a promise the data cannot make. Pinning by hand
// clears it: the caveat is about an offer the map reported, and a hand-picked pair is
// no longer that offer.
let isColumn = picks.length > 0 && params.get('column') === '1';

function writeUrl() {
  const next = new URLSearchParams();
  if (picks.length) next.set('pick', picks.join(','));
  if (isColumn) next.set('column', '1');
  const qs = next.toString();
  history.replaceState(null, '', qs ? '?' + qs : location.pathname);
}

function chip(cls, text) {
  return '<span class="chip ' + cls + '">' + text + '</span>';
}

// One pinned sector, as the box that heads its column. The box carries the name, so
// the table below it has no name row -- it would say the same thing twice. The whole
// box is the link; the unpin button sits on top of it and cancels the navigation.
function slotBox(s, anyPinned) {
  if (!s) return '<div class="slot empty">' +
    (anyPinned ? WORDS.picks_one : WORDS.picks_empty) + '</div>';
  return '<a class="slot ' + s.cls + '" href="sector-' + s.slug + '.html" title="' +
    WORDS.open + '">' +
    '<button class="drop" data-drop="' + s.slug + '" title="' + WORDS.unpin + '">' +
    WORDS.unpin_mark + '</button>' +
    '<span class="name">' + s.name + '</span>' +
    chip(s.cls, WORDS.classes[s.cls].label) +
    '<span class="sub">' + s.sub + '</span></a>';
}

// Level the header boxes by measurement. CSS cannot do this from inside a table
// cell: a percentage height in a `<th>` has no basis to resolve against, so the box
// falls back to its own content -- or, given a floor, to the floor, and a name that
// wraps then spills out under the border. Measure the tallest, set them all to it.
// Re-run on resize, because the column width is what decides whether a name wraps.
function levelBoxes() {
  const boxes = Array.prototype.slice.call(
    document.querySelectorAll('#cmp thead .slot'));
  if (!boxes.length) return;
  boxes.forEach(b => { b.style.height = 'auto'; });
  const tallest = Math.max.apply(null,
    boxes.map(b => b.getBoundingClientRect().height));
  boxes.forEach(b => { b.style.height = tallest + 'px'; });
}

let levelPending = 0;
window.addEventListener('resize', () => {
  cancelAnimationFrame(levelPending);
  levelPending = requestAnimationFrame(levelBoxes);
});

function render() {
  // The panel is one table: the boxes are its header cells and the figures fall in
  // the same columns beneath them. Two columns normally; three or four only when
  // something handed us that many, which the sector map can.
  // Two things can want saying above the panel, and a dropped token always says so:
  // a `?pick=` that quietly matched nothing looks exactly like a page that ignored
  // the link, which is how a wrong sector name survives unnoticed.
  const lines = [];
  if (isColumn) lines.push(WORDS.picks_column);
  if (dropped.length)
    lines.push(WORDS.picks_dropped.replace('{list}', dropped.join(', ')));
  const caveat = document.getElementById('caveat');
  caveat.textContent = lines.join('  ');
  caveat.style.display = lines.length ? 'block' : 'none';

  // The table is always here, pinned or not: the questions it asks are the same ones
  // whatever is in the columns, and a panel that appears and disappears moves the
  // whole page under the reader.
  const panel = document.getElementById('cmp');
  const chosen = picks.map(s => SECTORS[s]).filter(Boolean);
  const count = Math.max(MAX_PINS, chosen.length);
  // Percentages, not fixed widths: the panel is the content width in every state, and
  // the label and the figures still come out evenly spaced across the row.
  const cols = '<colgroup><col style="width:28%%">' +
    ('<col class="pick" style="width:' + (72 / count).toFixed(2) + '%%">').repeat(count) +
    '</colgroup>';
  const head = '<thead><tr><th class="lab"></th>' +
    Array.from({length: count}, (_, i) =>
      '<th class="pick">' + slotBox(chosen[i], chosen.length > 0) + '</th>'
    ).join('') + '</tr></thead>';

  const span = r => r.low === r.high ? String(r.low) : r.low + '\\u2013' + r.high;
  const body = '<tbody>' + METRICS.map((label, i) => {
    const all = Array.from({length: count}, (_, c) => chosen[c] ? chosen[c].rows[i] : null);
    const real = all.filter(Boolean);
    const top = Math.max.apply(null, real.map(r => r.high));
    // The leading side is marked, never judged: more fights is not worse and more
    // stores is not better without knowing the run. Ties mark nothing, and one
    // sector on its own leads nothing -- there is no comparison to lead.
    const tied = real.filter(r => r.high === top).length > 1;
    const mark = real.length >= 2 && !tied;
    return '<tr><th>' + label + '</th>' + all.map(r =>
      r ? '<td' + (mark && r.high === top ? ' class="more"' : '') + '>' + span(r) + '</td>'
        : '<td class="blank">' + WORDS.blank + '</td>'
    ).join('') + '</tr>';
  }).join('') + '</tbody>';

  panel.innerHTML = '<table class="cmp">' + cols + head + body + '</table>';
  levelBoxes();

  document.querySelectorAll('.card').forEach(card => {
    const on = picks.indexOf(card.dataset.slug) >= 0;
    card.classList.toggle('pinned', on);
    const pin = card.querySelector('.pin');
    pin.textContent = on ? WORDS.unpin_mark : WORDS.pin_mark;
    pin.title = on ? WORDS.unpin : WORDS.pin;
  });
  writeUrl();
}

function toggle(slug) {
  const at = picks.indexOf(slug);
  if (at >= 0) picks.splice(at, 1);
  // A hand pin caps at two -- what the map offers and what a comparison is for. Four
  // slots exist only because the sector map can report a column of four; touching one
  // by hand collapses that back to a pair, keeping the newest.
  else if (picks.length < MAX_PINS) picks.push(slug);
  else picks = picks.slice(-(MAX_PINS - 1)).concat(slug);  // oldest falls out
  isColumn = false;
  // Only a hand action is remembered. Seeding from `?pick=` must not overwrite the
  // reader's own pins -- the watcher opens this page at every sector choice, and a
  // reported offer is not a preference.
  try { localStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) {}
  render();
}

document.addEventListener('click', ev => {
  const pin = ev.target.closest('.pin');
  if (pin) { ev.preventDefault(); toggle(pin.closest('.card').dataset.slug); return; }
  const drop = ev.target.closest('.drop');
  if (drop) { ev.preventDefault(); toggle(drop.dataset.drop); }
});

render();
"""


def card_html(rec):
    sub = " · ".join(rec["sub_parts"])
    nums = "".join(
        '<span><b>%s</b> %s</span>' % (html.escape(value), html.escape(label))
        for label, value in rec["nums"])
    return (
        '<a class="card %(cls)s" data-slug="%(slug)s" href="sector-%(slug)s.html" '
        'title="%(open)s">'
        '<button class="pin" title="%(pin)s">%(mark)s</button>'
        '<div class="name">%(name)s</div>'
        '<div class="sub">%(sub)s</div>'
        '<div class="nums">%(nums)s</div>'
        "</a>" % {
            "cls": rec["class"], "slug": html.escape(rec["slug"], quote=True),
            "name": html.escape(rec["name"]), "sub": html.escape(sub), "nums": nums,
            "open": html.escape(VOC["open"], quote=True),
            "pin": html.escape(VOC["pin"], quote=True),
            "mark": html.escape(VOC["pin_mark"]),
        })


def build():
    sectors = load_sectors()
    notes = classify(sectors)
    records = [record(s) for s in sectors]

    for rec in records:
        beacons = next(r for r in rec["rows"] if r["key"] == "beacons")
        stores = next(r for r in rec["rows"] if r["key"] == "section:store:")
        fights = next(r for r in rec["rows"] if r["key"] == "always_fight_events")
        if rec["fixed"]:
            first = VOC["fixed"].format(n=rec["fixed"])
        elif rec["offered"]:
            first = VOC["from"].format(n=rec["earliest"])
        else:
            first = VOC["hidden"]
        rec["sub_parts"] = [first]
        if rec["unique"] and not rec["fixed"]:
            rec["sub_parts"].append(VOC["unique"])
        # In no vanilla draw list: the map can only offer it under Advanced Edition.
        if rec["ae_only"]:
            rec["sub_parts"].append(VOC["ae_only"])
        rec["nums"] = [
            ("beacons", "%d–%d" % (beacons["low"], beacons["high"])),
            ("stores", "%d" % stores["low"] if stores["low"] == stores["high"]
             else "%d–%d" % (stores["low"], stores["high"])),
            ("open in a fight", "%d" % fights["high"]),
        ]

    body = []
    for cls in CLASS_ORDER:
        group = [r for r in records if r["class"] == cls]
        if not group:
            continue
        group.sort(key=lambda r: (r["earliest"], r["name"]))
        label = VOC["classes"][cls]["label"]
        hint = VOC["classes"][cls]["hint"]
        body.append(
            "<section><h2>%s<span class=\"meta\">%s</span></h2><div class=\"grid\">%s"
            "</div></section>"
            % (html.escape(label), html.escape(hint),
               "".join(card_html(r) for r in group)))

    # `id` rides along because `?pick=` resolves game ids too -- `ROCK_HOME` is what
    # sector_data.xml and the Hyperspace log call this sector, so it is what a caller
    # with a log line in hand has to offer.
    data = {r["slug"]: {"slug": r["slug"], "id": r["id"], "name": r["name"],
                        "cls": r["class"], "sub": " · ".join(r["sub_parts"]),
                        "rows": r["rows"]}
            for r in records}
    words = {k: VOC[k] for k in ("picks_empty", "picks_one", "picks_column",
                                 "picks_dropped", "pin", "unpin", "pin_mark",
                                 "unpin_mark", "open", "blank", "classes")}

    page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
%(tokens)s
%(css)s
</style></head>
<body><div class="wrap">
<header><h1>%(heading)s</h1></header>
<section>
  <p class="note" id="caveat" style="display:none"></p>
  <div class="cmp-wrap" id="cmp"></div>
</section>
%(body)s
<p class="note">%(source)s</p>
</div>
<script>
%(script)s
</script>
</body></html>
""" % {
        "title": html.escape(VOC["title"]),
        "tokens": tokens(),
        "css": CSS,
        "heading": html.escape(VOC["heading"]),
        "body": "".join(body),
        "source": html.escape(VOC["source"]),
        "script": SCRIPT % {
            "data": json.dumps(data, ensure_ascii=False),
            "words": json.dumps(words, ensure_ascii=False),
            "metrics": json.dumps([label for _, label in VOC["compare"]],
                                  ensure_ascii=False)},
    }
    OUT.write_text(page, encoding="utf-8", newline="\n")
    return records, notes


def verify(records=None):
    problems = []
    page = OUT.read_text(encoding="utf-8")
    records = records or [record(s) for s in (lambda ss: (classify(ss), ss)[1])(load_sectors())]

    if len(records) != 19:
        problems.append("%d sector profiles, expected 19" % len(records))
    for rec in records:
        if rec["class"] not in CLASS_ORDER:
            problems.append("%s has no designation" % rec["slug"])
        # A card that links nowhere is worse than a card that is missing.
        target = OUT.parent / ("sector-%s.html" % rec["slug"])
        if not target.exists():
            problems.append("%s links to a page that does not exist (%s)"
                            % (rec["slug"], target.name))
        if ('data-slug="%s"' % rec["slug"]) not in page:
            problems.append("%s is missing from the page" % rec["slug"])
    if "%(" in page or "%s" in page:
        problems.append("an unsubstituted format token survived into the page")
    if "--void" not in page:
        problems.append("the palette was not sliced out of the shell")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true",
                    help="check the built page without rebuilding it")
    args = ap.parse_args()

    records, notes = (None, [])
    if not args.verify:
        records, notes = build()
        counts = {}
        for rec in records:
            counts[rec["class"]] = counts.get(rec["class"], 0) + 1
        print("built    %s" % OUT)
        print("         %s" % ", ".join("%d %s" % (counts[c], c)
                                        for c in CLASS_ORDER if c in counts))

    problems = verify(records)
    if problems:
        for problem in problems:
            print("FAIL     %s" % problem)
        return 1
    print("verified 19 sectors, every link resolves, palette sliced from the shell")
    # Not a failure: our own layer is allowed to lag, but the disagreement is worth
    # seeing rather than being silently overridden by the community wiki's grouping.
    for note in notes:
        print("NOTE     %s" % note)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
