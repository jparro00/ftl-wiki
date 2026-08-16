#!/usr/bin/env python3
"""MOCK ONLY — Federation Space sector page with the review notes applied.

Not part of the pipeline. It imports tools/build-sector.py, reuses its data loading
and its row rendering, and replaces the parts the review notes change, so every
number on the mock still comes from sectors/data/federation-space.sector.json.

Output: sectors/sector-federation-space-mock.html (+ the review layer appended).

Once a shape is agreed, the changes move where SECTOR-PAGE.md §8 says they belong:
words → sector-copy/, layout → sector-page-render.html, structure → build-sector.py.
"""

import html
import importlib.util
import io
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SLUG = "federation-space"
OUT = HERE / f"sector-{SLUG}-mock.html"
REVIEW_LAYER = REPO / "tools" / "review-layer.html"

spec = importlib.util.spec_from_file_location("bs", REPO / "tools" / "build-sector.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

data = json.loads((REPO / "sectors" / "data" / f"{SLUG}.sector.json").read_text(encoding="utf-8"))
copy = json.loads((REPO / "tools" / "sector-copy" / f"{SLUG}.json").read_text(encoding="utf-8"))

E = html.escape
MARKERS = data["rollup"]["markers"]
DISTRESS = set(MARKERS["distress"]["events"])
STORE_MARKED = set(MARKERS["store"])


# ---------------------------------------------------------------- note 13: distress tag
# A row that shows a distress marker on the map says so, wherever it is rendered.
# Derived from <distressBeacon/>, so it is a fact about the event, not about the line.

_tags_html = B.tags_html


def tags_html(record):
    out = _tags_html(record)
    extra = []
    if record.get("id") in DISTRESS:
        extra.append('<span class="tg distress">Distress signal</span>')
    if record.get("id") in STORE_MARKED:
        extra.append('<span class="tg store">Store marker</span>')
    if not extra:
        return out
    if out:
        return out[: -len("</div>")] + "".join(extra) + "</div>"
    return f'<div class="tags">{"".join(extra)}</div>'


B.tags_html = tags_html


# ---------------------------------------------------------------- note 15: block odds
# Each line rolls its own count between min and max inclusive (raw/wiki/sectors.md).
# Read as a uniform roll, the k-th optional block lands whenever the roll reaches k,
# so its chance is (max - k + 1) / (max - min + 1).

def block_odds(low, high):
    span = high - low + 1
    return [round((high - k + 1) / span * 100) for k in range(low + 1, high + 1)]


def blocks(low, high):
    out = [f'<i class="blk" title="always placed, if the map has room"></i>' for _ in range(low)]
    for pct in block_odds(low, high):
        out.append(f'<i class="blk maybe" title="{pct}% chance"></i>')
    return "".join(out) or '<i class="blk maybe"></i>'


# ---------------------------------------------------------------- note 14: AE adds inline

def delta_html(entry):
    """The Advanced Edition twin of this list, at the bottom of the line it belongs to."""
    override = entry.get("override")
    if not override or not (override["added"] or override["removed"]):
        return ""
    inner = [f'<div class="head">Advanced Edition adds &mdash; {E(override["list"])}</div>']
    if override["added"]:
        inner.append(f'<div class="pool">{"".join(B.event_html(e) for e in override["added"])}</div>')
    if override["removed"]:
        inner.append(f'<p class="note">Not in the AE list: {E(", ".join(override["removed"]))}</p>')
    inner.append('<p class="note">Whether the engine uses this list instead is not stated by any file here.</p>')
    return f'<div class="delta">{"".join(inner)}</div>'


def budget_html():
    rows = []
    for entry in B.placement_order(data):
        place = entry["placement"]
        classes = ""
        if entry["section"] in ("hostile", "boarders"):
            classes += " hostile"
        if entry["max"] == 0:
            classes += " zero"
        if place["at_risk"]:
            classes += " risk"
        count = str(entry["min"]) if entry["min"] == entry["max"] else f'{entry["min"]}–{entry["max"]}'
        marks = ""
        if place["nebula_first"]:
            marks += '<span class="mark first">placed first</span>'
        if place["at_risk"]:
            marks += '<span class="mark risk">may be cut</span>'
        head = (
            f'<div class="rank">{place["position"] + 1}</div>'
            f'<div class="name">{E(entry["name"])}{marks}</div>'
            f'<div class="cnt">{count}</div>'
            f'<div class="track">{blocks(entry["min"], entry["max"])}</div>'
        )
        body = ""
        if entry["events"]:
            body += f'<div class="pool">{"".join(B.event_html(r) for r in entry["events"])}</div>'
        note = (copy.get("section_notes") or {}).get(entry["name"])
        if note:
            body += f'<p class="note">{B.inline(note, TITLES, SLUG, "section_notes")}</p>'
        body += delta_html(entry)
        if body:
            rows.append(
                f'<details class="bwrap"><summary class="brow expandable{classes}">{head}</summary>'
                f'<div class="bpool">{body}</div></details>'
            )
        else:
            rows.append(f'<div class="brow{classes}">{head}</div>')

    gen = data["generation"]
    span = gen.get("fallback_beacons") or {}
    low, high = span.get("min", 0), span.get("max", 0)
    head = (
        '<div class="rank">+</div>'
        f'<div class="name">{E(gen["fallback_list"])}<span class="mark fill">fill-in</span></div>'
        f'<div class="cnt">{low if low == high else f"{low}–{high}"}</div>'
        # No roll governs this line — it takes whatever the table leaves — so its blocks
        # carry a range, not a per-block chance.
        f'<div class="track">'
        + "".join(f'<i class="blk maybe" title="filled only if the table leaves room"></i>'
                  for _ in range(high))
        + "</div>"
    )
    events = gen.get("fallback_events") or []
    if high and events:
        pool = "".join(B.event_html(r) for r in events)
        rows.append(
            f'<details class="bwrap"><summary class="brow expandable fill">{head}</summary>'
            f'<div class="bpool"><div class="pool">{pool}</div></div></details>'
        )
    else:
        rows.append(f'<div class="brow fill">{head}</div>')
    return f'<div class="budget">{"".join(rows)}</div>'


# ---------------------------------------------------------------- note 15: the legend

def legend_html():
    """A faded block is 'at least this many', not 'this exact count'.

    The line rolls one number between min and max and every outcome is equally likely,
    so the k-th optional block lights whenever the roll reaches k — which is the chance
    of at least k, and what block_odds computes.
    """
    widest = max(data["entries"], key=lambda e: e["max"] - e["min"])
    low, high = widest["min"], widest["max"]
    each = round(100 / (high - low + 1))
    odds = block_odds(low, high)
    return (
        '<div class="legend">'
        '<div class="lgrow"><span class="lgkey"><i class="blk"></i><i class="blk hostile"></i></span>'
        '<span><b>Must be placed</b> — every solid block is filled, as long as the map still '
        'has a free beacon when the line comes up.</span></div>'
        '<div class="lgrow"><span class="lgkey"><i class="blk maybe"></i><i class="blk maybe hostile"></i></span>'
        '<span><b>May be placed</b> — the line rolls one count between its minimum and its '
        f'maximum and every outcome is equally likely. {E(widest["name"])} rolls {low}–{high}, '
        f'so each of those {high - low + 1} counts is {each}%. A faded block is the chance of '
        f'<b>at least</b> that many: {odds[0]}% for one, {odds[-1]}% for all {high}. '
        'Hover any block for its own figure.</span></div>'
        '<div class="lgrow"><span class="lgkey"><i class="blk hostile"></i><i class="blk maybe hostile"></i></span>'
        '<span>Beacons that always put you in a fight.</span></div>'
        "</div>"
    )


# ---------------------------------------------------------------- note 16 + 24: how a map is built

def generation_html():
    gen = data["generation"]
    nebula = next(e for e in data["entries"] if e["name"] == "NEBULA")
    storms = len(MARKERS["environment"]["storm"])
    return (
        '<p class="note">'
        f'The map is a 6×4 grid and each cell has an <b>80% chance</b> of holding a beacon, so a '
        f'sector has at most <b>{gen["grid_beacons"]}</b> of them. The lines above are then filled '
        'in that order, each rolling its own count, until the beacons run out — so a line near the '
        'bottom can get nothing. Whatever is still empty at the end is filled from the shared '
        f'<code>{E(gen["fallback_list"])}</code> list.</p>'
        '<p class="note">Clouds are drawn before any of it. A beacon under one is converted and '
        f'draws from <code>NEBULA</code> instead — and {storms} of that list\'s '
        f'{len(nebula["events"])} events are plasma storms, which halve your reactor on arrival. '
        'Which of them you land on is a draw from the list like any other, not a fixed slot.</p>'
    )


# ---------------------------------------------------------------- note 8 + 9 + 10: blue options

TOP_GATES = 4


def systems():
    """The ids that name a ship system, so a level on the gate means something.

    Read from the blueprints rather than listed by hand: `lvl` is a floor on a system's
    level, and every other kind of req — crew, augment, weapon list — has no level at all.
    """
    names = set()
    for path in ("blueprints.xml", "dlcBlueprints.xml"):
        src = (REPO / "raw" / "gamedata" / path).read_text(encoding="utf-8", errors="replace")
        names |= set(re.findall(r'<systemBlueprint name="([^"]+)"', src))
    return names


def gate_rows():
    """One row per option *and level* — Sensors 2 and Sensors 3 are different keys.

    rollup.gates counts an option once however many levels it asks for, so the split is
    rebuilt from the per-event gates, which carry `lvl`. Labels come from the rollup so a
    merged option (Teleporter) still reads the way it does everywhere else.

    A system gate with no `lvl` asks for the system at all, which is level 1 — it merges
    into the level-1 row and reads `1+`, since `lvl` is a floor. A non-system gate cannot
    carry a level, so it carries no chip.
    """
    sysnames = systems()
    label_of = {req: g["label"] for g in data["rollup"]["gates"] for req in g["reqs"]}
    counts = {}
    for entry in data["entries"]:
        for record in entry["events"]:
            for gate in record.get("gates") or []:
                is_system = gate["req"] in sysnames
                level = (gate.get("lvl") or "1") if is_system else None
                key = (label_of.get(gate["req"], gate["label"]), level)
                counts.setdefault(key, set()).add(record["id"])
    rows = [(label, lvl, len(ids)) for (label, lvl), ids in counts.items()]
    rows.sort(key=lambda r: (-r[2], r[0].lower(), r[1] or ""))
    return rows


def gates_html():
    rows = gate_rows()

    def row(label, lvl, hits):
        # The level is part of the option's name, not a chip beside it.
        name = f"{label} {lvl}+" if lvl else label
        return (f'<div class="grow"><span class="g">{E(name)}</span>'
                f'<span class="h">{hits}</span></div>')

    head = "".join(row(*r) for r in rows[:TOP_GATES])
    rest = "".join(row(*r) for r in rows[TOP_GATES:])
    options = len({r[0] for r in rows})
    hits = sum(len(g["events"]) for g in data["rollup"]["gates"])
    # The whole box is the toggle, not a link inside it.
    return (
        f'<details class="panel gp gtoggle"><summary><h3>Blue options in the pool'
        f'<span class="cnt">{options} options · {hits} hits</span></h3>'
        f'<div class="gates">{head}</div>'
        f'<div class="morehint">Show all {len(rows)}</div></summary>'
        f'<div class="gates rest">{rest}</div></details>'
    )


# ---------------------------------------------------------------- note 11 + 12: crew a store sells

def excluded_crew():
    """Species a store here cannot offer: crewBlueprints whose effective rarity is 0.

    Read from the blueprint files rather than named by hand — the sector declares no
    rarityList, so every species keeps its base value.
    """
    titles = {}
    text = (REPO / "raw" / "gamedata" / "text_blueprints.xml").read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r'<text name="(crew_\w+_title)">([^<]*)</text>', text):
        titles[m.group(1)] = m.group(2)
    sold = {c["id"] for c in data["crew_store_odds"]["crew"]}
    out = []
    for path in ("blueprints.xml", "dlcBlueprints.xml"):
        src = (REPO / "raw" / "gamedata" / path).read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r'<crewBlueprint name="([^"]+)">(.*?)</crewBlueprint>', src, re.S):
            name, body = m.group(1), m.group(2)
            rarity = re.search(r"<rarity>(\d+)</rarity>", body)
            title = re.search(r'<title id="([^"]+)"', body)
            if name in sold or not rarity or rarity.group(1) != "0" or not title:
                continue
            out.append(titles.get(title.group(1), name))
    return out


def crew_odds_html():
    """The baseline's row — species, per slot, in store — folded down the middle.

    Weight is dropped (it is 6 − rarity, and nothing is played off it) and the two
    percentages are whole numbers. Rarity 0 is a flag meaning "not in the pool", so
    those species stay in the table at 0% rather than in a line of their own.
    """
    odds = data["crew_store_odds"]
    rows = [(c["label"], round(c["share"]), round(c["in_store"]), False) for c in odds["crew"]]
    rows += [(label, 0, 0, True) for label in excluded_crew()]

    # The panel's title rides in the empty label cell of the first column's sub-header,
    # so the heading costs no line of its own.
    def head(title=""):
        return ('<div class="crow chead t2">'
                f'<span class="cl">{title}</span>'
                '<span class="cp" title="per slot">slot</span>'
                '<span class="cs" title="in at least one of the three slots">store</span></div>')

    def row(label, share, in_store, out):
        return (f'<div class="crow t2{" out" if out else ""}"><span class="cl">{E(label)}</span>'
                f'<span class="cp">{share}%</span><span class="cs">{in_store}%</span></div>')

    # Down, then across: the rank scan runs top-to-bottom as it always has, and the
    # species a store here cannot sell land together at the foot of the second column.
    half = -(-len(rows) // 2)
    groups = [g for g in (rows[:half], rows[half:]) if g]
    columns = "".join(
        f'<div class="tcol">{head("<h3>Crew in stores</h3>" if i == 0 else "")}'
        f'{"".join(row(*r) for r in group)}</div>'
        for i, group in enumerate(groups)
    )
    return f'<div class="panel gp crewpanel"><div class="two">{columns}</div></div>'


# ---------------------------------------------------------------- notes 18–21: markers

def markers_html():
    titles = {r["id"]: r for e in data["entries"] for r in e["events"]}
    pool = lambda ids: "".join(B.event_html(titles[i]) for i in ids if i in titles)
    return (
        "<section>"
        "<h2>Distress signals</h2>"
        f'<div class="pool">{pool(MARKERS["distress"]["events"])}</div>'
        '<p class="note"><i>Note: not every beacon from the <code>DISTRESS</code> pool '
        'broadcasts a distress signal, and some of these show up in the neutral pools too.</i></p>'
        "</section>"
        "<section>"
        "<h2>Stores</h2>"
        f'<div class="pool">{pool(sorted(MARKERS["store"]))}</div>'
        "</section>"
    )


# ---------------------------------------------------------------- assembly

TITLES = {}
for entry in data["entries"]:
    for record in entry["events"]:
        TITLES[record["id"]] = record["title"]
    for record in (entry.get("override") or {}).get("added") or []:
        TITLES[record["id"]] = record["title"]
if data.get("start_event"):
    TITLES[data["start_event"]["id"]] = data["start_event"]["title"]
for group in data["rollup"]["quest_targets"]:
    TITLES.setdefault(group["value"], group["value"])

# The game shows this sector as "Sector 1: Civilian Sector" (confirmed in game), while
# text_sectorname.xml names STANDARD_SPACE "Federation Space". The page leads with what
# the player sees.
LEDE = "The sector every run starts in — the game calls it **Sector 1: Civilian Sector**."

FACTS = [
    ("earliest sector", str(data.get("earliest_sector", data["min_sector"] + 1))),
    ("", "can repeat in a run"),
    ("music", " · ".join(data["tracks"])),
    ("", "built from Advanced Edition files"),
]

header = (
    f'<header><p class="eyebrow">Sector profile · {E(data["id"])}</p>'
    f'<h1>{E(data["title"])}</h1>'
    f'<p class="lede">{B.inline(LEDE, TITLES, SLUG, "lede")}</p>'
    '<div class="facts">'
    + "".join(
        f'<span class="fact">{E(label)} <b>{E(value)}</b></span>' if label
        else f'<span class="fact"><b>{E(value)}</b></span>'
        for label, value in FACTS
    )
    + "</div></header>"
)

glance = (
    "<section><h2>At a glance</h2>"
    f'<div class="glance">{gates_html()}{crew_odds_html()}</div></section>'
)

budget = (
    "<section>"
    '<h2>Beacon budget'
    f'<span class="meta">{data["metrics"]["beacons_min"]}–{data["metrics"]["beacons_max"]} slots '
    f'allocated · {data["metrics"]["distinct_events"]} events in pool</span></h2>'
    f"{budget_html()}"
    f"{legend_html()}"
    f"{generation_html()}"
    "</section>"
)

panels = [p for p in copy["panels"] if p["title"] != "Reading the map here"]
panels_out = B.panels_html(data, {"panels": panels}, TITLES, SLUG)

# A <details> only toggles from its <summary>, so an open blue-options box could not be
# closed by clicking its body. This closes it from anywhere in the box, while leaving
# text selection (and the review layer's commenting) alone.
TOGGLE_JS = """
<script>
document.querySelectorAll(".gtoggle").forEach(box => {
  box.addEventListener("click", event => {
    if (event.target.closest("summary")) return;
    if (String(window.getSelection())) return;
    box.open = !box.open;
  });
});
</script>
"""

content = "".join([
    header,
    glance,
    budget,
    markers_html(),
    B.chain_html(copy, TITLES, SLUG),
    panels_out,
    B.loader_html(),
    TOGGLE_JS,
])

# ---------------------------------------------------------------- mock-only styling
# Everything here would move to sector-page-render.html if the shape is kept.

EXTRA_CSS = """
<style id="mock-style">
  /* Blue options read in the card's blue, the colour they carry in game. */
  .grow .g { color: hsl(204, 100%, 50%); }
  /* The whole blue-options box is the toggle. */
  .gtoggle { cursor: pointer; }
  .gtoggle > summary { list-style: none; display: flex; flex-direction: column; gap: .55rem; }
  .gtoggle > summary::-webkit-details-marker { display: none; }
  .gtoggle:hover { border-color: var(--rail); }
  .gtoggle:hover .morehint { color: var(--cyan); }
  .morehint {
    font-family: var(--mono); font-size: .62rem; letter-spacing: .12em;
    text-transform: uppercase; color: var(--faint);
  }
  .morehint::after { content: " ›"; }
  .gtoggle[open] .morehint::after { content: " ‹"; }
  .gtoggle[open] .morehint { visibility: hidden; height: 0; }
  .gates.rest { padding-top: .3rem; border-top: 1px solid var(--sunk); }

  /* A species a store here cannot offer, kept in the table at 0%. */
  .crow.out .cl, .crow.out .cp, .crow.out .cs { color: var(--faint); }

  /* The crew list folded down the middle: two columns of four, each with its own
     sub-header so the labels sit over their own numbers. */
  .two { display: grid; grid-template-columns: 1fr 1fr; gap: .18rem 1.1rem; }
  .tcol { display: flex; flex-direction: column; gap: .18rem; }
  .crow.t2 { grid-template-columns: 1fr 2.9rem 2.9rem; gap: .3rem; }
  @media (max-width: 40rem) { .two { grid-template-columns: 1fr; } }

  /* The title sits on the sub-header line rather than above it. */
  .crow.chead .cl h3 {
    margin: 0; font-family: var(--mono); font-size: .66rem; letter-spacing: .15em;
    text-transform: uppercase; color: var(--dim); font-weight: 600; white-space: nowrap;
  }
  .crewpanel { justify-content: flex-start; }

  .tg.distress { color: var(--amber); }

  .never {
    display: flex; gap: .5rem; align-items: baseline; flex-wrap: wrap;
    border-top: 1px solid var(--sunk); padding-top: .45rem; margin-top: .1rem;
  }
  .never .nk {
    font-family: var(--mono); font-size: .58rem; letter-spacing: .1em;
    text-transform: uppercase; color: var(--faint);
  }
  .never .nv { font-size: .8rem; color: var(--dim); }

  .legend {
    display: flex; flex-direction: column; gap: .4rem;
    border: 1px solid var(--edge); border-radius: 2px; background: var(--sunk);
    padding: .6rem .75rem;
  }
  .lgrow { display: grid; grid-template-columns: 3rem 1fr; gap: .7rem; align-items: baseline;
           font-size: .82rem; color: var(--dim); }
  .lgrow .lgkey { display: flex; gap: 2px; padding-top: .3rem; }
  .lgrow b { color: var(--ink); font-weight: 600; }
  /* The budget paints red per row; the legend needs both colours side by side. */
  .blk.hostile { background: var(--red); }
  .blk.maybe.hostile { background: var(--barred); }

  h3.sub {
    margin: .5rem 0 0; font-family: var(--mono); font-size: .62rem; letter-spacing: .14em;
    text-transform: uppercase; color: var(--faint); font-weight: 600;
  }
  .bpool .delta { margin-top: .5rem; }
  .bpool .note { margin-top: .5rem; }
</style>
"""

template = (REPO / "tools" / "sector-page-render.html").read_text(encoding="utf-8")
page = template.replace(B.MARKER, content)
page = B.TITLE.sub(f"<title>{data['title']} — sector profile (mock)</title>", page, count=1)
page = page.replace("</style>\n\n<div class=\"wrap\">", "</style>\n" + EXTRA_CSS + "\n<div class=\"wrap\">", 1)
page += REVIEW_LAYER.read_text(encoding="utf-8")

# The renderer's card paths are relative to `sectors/`, and this file sits one level
# deeper — so a box would open onto nothing without the extra hop.
page = page.replace('"../cards/', '"../../cards/')

OUT.write_text(page, encoding="utf-8")
print(OUT)
