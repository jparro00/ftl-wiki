#!/usr/bin/env python3
"""Build an FTL sector profile page from its extracted data plus its copy file.

    python tools/build-sector.py engi-homeworlds
    python tools/build-sector.py --all

Two inputs, and the split between them is the whole design:

    sectors/data/<slug>.sector.json   every number and every event — generated, never edited
    tools/sector-copy/<slug>.json     the words — hand-written, holds no numbers

Every number on the page names a metric and is filled in from the data. Prose refers to
an event as {{EVENT_ID}} and the renderer resolves its title, so a page cannot name an
event this sector does not have. Both rules exist so that no fact on a sector page is
typed by a human.

See tools/SECTOR-PAGE.md for the spec this implements.
"""

import argparse
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
TEMPLATE = TOOLS / "sector-page-render.html"
VOCAB = TOOLS / "sector-vocab.json"
COPY_DIR = TOOLS / "sector-copy"
DATA_DIR = ROOT / "sectors" / "data"
SCHEMA = "ftl-sector-profile/1"

MARKER = "<!--SECTOR-CONTENT-->"
TITLE = re.compile(r"^<title>[^\n]*?</title>$", re.MULTILINE)

# Cards are built to cards/card-<slug>.html and sector pages to sectors/sector-<slug>.html,
# so one hop up and across reaches a card from a page opened off disk. Relative on purpose:
# a published artifact mints its URL at publish time, so no absolute link is knowable here.
CARD_HREF = "../cards/card-{slug}.html"
CARD_RUNTIME = "../cards/runtime/card.js"
CARD_CSS = "../cards/runtime/card.css"
CARD_DATA = "../cards/data/{slug}.js"
LOADER = TOOLS / "sector-cards.js"
TOGGLE = TOOLS / "sector-toggle.js"

# Five keys, and `stats` and `callout` are deliberately not among them: the tiles and the
# boxed note were cut from the page, so a copy file carrying either is stale rather than
# harmless, and failing the build is how it gets found (SECTOR-PAGE.md §5).
COPY_KEYS = {"slug", "lede", "section_notes", "panels", "chain"}
REQUIRED = {"slug", "lede", "panels"}

# The top of the blue-options block; the rest is behind the box itself.
TOP_GATES = 4


class CopyError(SystemExit):
    pass


def fail(slug, message):
    raise CopyError(f"{slug}: {message}")


# ---------------------------------------------------------------- inline markup

INLINE = re.compile(r"\*\*(.+?)\*\*|`(.+?)`|\{\{([A-Z0-9_]+)\}\}")


def inline(text, titles, slug, where):
    """Escape, then honour the three markup forms copy is allowed to use.

    {{EVENT_ID}} is checked against this sector's own pool: a page that mentions an
    event the sector cannot produce is a factual error, so it fails the build rather
    than rendering.
    """
    out, last = [], 0
    for m in INLINE.finditer(text):
        out.append(html.escape(text[last:m.start()]))
        bold, code, ref = m.groups()
        if bold is not None:
            out.append(f"<strong>{html.escape(bold)}</strong>")
        elif code is not None:
            out.append(f"<code>{html.escape(code)}</code>")
        else:
            if ref not in titles:
                fail(slug, f"{where}: {{{{{ref}}}}} is not an event this sector can produce")
            out.append(f'<span class="ref">{html.escape(titles[ref])}</span>')
        last = m.end()
    out.append(html.escape(text[last:]))
    return "".join(out)


# ---------------------------------------------------------------- validation

def check(copy, data, slug):
    unknown = set(copy) - COPY_KEYS
    if unknown:
        fail(slug, f"unknown key(s) in copy: {', '.join(sorted(unknown))}")
    missing = REQUIRED - set(copy)
    if missing:
        fail(slug, f"copy is missing: {', '.join(sorted(missing))}")
    if copy["slug"] != data["slug"]:
        fail(slug, f"copy slug {copy['slug']!r} does not match data slug {data['slug']!r}")

    if not 2 <= len(copy["panels"]) <= 4:
        fail(slug, f"panels: expected 2–4, found {len(copy['panels'])}")
    for panel in copy["panels"]:
        if set(panel) - {"title", "items"} or not {"title", "items"} <= set(panel):
            fail(slug, "panels: each panel needs exactly 'title' and 'items'")
        if not 2 <= len(panel["items"]) <= 6:
            fail(slug, f"panels: {panel['title']!r} needs 2–6 items, found {len(panel['items'])}")
        for item in panel["items"]:
            if set(item) - {"lead", "text"} or not {"lead", "text"} <= set(item):
                fail(slug, f"panels: {panel['title']!r} items need exactly 'lead' and 'text'")

    names = {e["name"] for e in data["entries"]}
    for name in copy.get("section_notes") or {}:
        if name not in names:
            fail(slug, f"section_notes: {name!r} is not an entry in this sector")

    chain = copy.get("chain")
    if chain is not None:
        if set(chain) - {"title", "steps"} or not {"title", "steps"} <= set(chain):
            fail(slug, "chain: needs exactly 'title' and 'steps'")
        for step in chain["steps"]:
            if set(step) - {"marker", "title", "detail", "ref"}:
                fail(slug, "chain: a step may only have 'marker', 'title', 'detail', 'ref'")
            if not {"marker", "title", "detail"} <= set(step):
                fail(slug, "chain: a step needs 'marker', 'title' and 'detail'")


# ---------------------------------------------------------------- rendering

def metric(data, expr):
    """A number the page shows: one metric key, or 'a..b' rendered as a range."""
    keys = expr.split("..")
    values = [data["metrics"][k] for k in keys]
    if len(values) == 1:
        return str(values[0])
    low, high = values[0], values[-1]
    if low == high:
        return str(low)
    return f"{low}{VOC['format']['range_join']}{high}"


def tag_chip(name):
    return f'<span class="tg {name}">{html.escape(VOC["tags"][name])}</span>'


def tags_html(record):
    tags = record.get("tags") or []
    picked = [t for t in VOC["tag_order"] if t in tags][: VOC["tag_limit"]]
    out = [tag_chip(t) for t in picked]
    if record.get("weight"):
        out.append(f'<span class="tg">{html.escape(VOC["format"]["weight"].format(n=record["weight"]))}</span>')
    # The marker tags say what the map draws on the beacon before you jump to it, which
    # is a different kind of fact from the rest and the one a row is read for. They sit
    # outside the tag limit so they cannot be squeezed off a busy row.
    out += [tag_chip(t) for t in VOC["marker_tags"] if t in tags]
    return f'<div class="tags">{"".join(out)}</div>' if out else ""


def rail_of(record):
    for tag in VOC["tag_order"]:
        if tag in (record.get("tags") or []) and tag in VOC["rail"]:
            return " " + VOC["rail"][tag]
    return ""


def event_html(record):
    """One beacon box.

    A box whose event has a card opens onto that card, rendered in place by
    tools/sector-cards.js — the panel starts empty and is filled the first time the
    box is opened. The corner link still goes to the standalone card page. An event
    with no card stays an inert box rather than promising something that is not there.
    """
    body = (
        f'<div class="t">{html.escape(record["title"])}</div>'
        f'<div class="id">{html.escape(record["id"])}</div>'
        f"{tags_html(record)}"
    )
    if record.get("card") and record.get("slug"):
        href = CARD_HREF.format(slug=record["slug"])
        link = (
            f'<a class="cardlink" href="{html.escape(href, quote=True)}"'
            f' title="{html.escape(VOC["cards"]["open"], quote=True)}">'
            f'{html.escape(VOC["cards"]["open_mark"])}</a>'
        )
        return (
            f'<details class="evbox{rail_of(record)}" data-card="{html.escape(record["slug"], quote=True)}">'
            f'<summary class="ev">{body}{link}</summary>'
            '<div class="cardpanel"></div>'
            "</details>"
        )
    return f'<div class="ev{rail_of(record)}">{body}</div>'


def block_odds(low, high):
    """The chance of each optional block, in order.

    The line rolls one count between min and max inclusive (raw/wiki/sectors.md) and
    every outcome is read as equally likely, so the k-th optional block lands whenever
    the roll reaches k — a chance of *at least* k, not of exactly k.
    """
    span = high - low + 1
    return [round((high - k + 1) / span * 100) for k in range(low + 1, high + 1)]


def blocks(low, high):
    title = html.escape(VOC["budget"]["block_always"], quote=True)
    out = [f'<i class="blk" title="{title}"></i>' for _ in range(low)]
    for pct in block_odds(low, high):
        chance = html.escape(VOC["budget"]["block_chance"].format(pct=pct), quote=True)
        out.append(f'<i class="blk maybe" title="{chance}"></i>')
    return "".join(out) or '<i class="blk maybe"></i>'


def placement_order(data):
    """Entries in the order the game fills them — nebula lists first, then file order."""
    return sorted(data["entries"], key=lambda e: e["placement"]["position"])


def delta_html(entry):
    """The Advanced Edition twin of this list, at the foot of the line it belongs to.

    A delta, never a merge: whether the engine substitutes the override list is not
    stated anywhere, so the page shows the difference and says so (SECTOR-PAGE.md §4.4).
    """
    override = entry.get("override")
    if not override or not (override["added"] or override["removed"]):
        return ""
    head = VOC["delta"]["head"].format(list=override["list"])
    inner = [f'<div class="head">{html.escape(head)}</div>']
    if override["added"]:
        inner.append(f'<div class="pool">{"".join(event_html(e) for e in override["added"])}</div>')
    if override["removed"]:
        dropped = ", ".join(override["removed"])
        inner.append(f'<p class="note">{html.escape(VOC["delta"]["removed"])} {html.escape(dropped)}</p>')
    inner.append(f'<p class="note">{html.escape(VOC["delta"]["unconfirmed"])}</p>')
    return f'<div class="delta">{"".join(inner)}</div>'


def budget_html(data, copy, titles, slug):
    rows = []
    for entry in placement_order(data):
        place = entry["placement"]
        classes = ""
        if entry["section"] in ("hostile", "boarders"):
            classes += " hostile"
        if entry["max"] == 0:
            classes += " zero"
        if place.get("always_short"):
            classes += " short"
        count = str(entry["min"]) if entry["min"] == entry["max"] else \
            f'{entry["min"]}{VOC["format"]["range_join"]}{entry["max"]}'
        marks = ""
        if place["nebula_first"]:
            marks += f'<span class="mark first">{html.escape(VOC["budget"]["nebula_mark"])}</span>'
        # `at_risk` is still computed and still in the profile JSON -- it is simply not
        # shown. The chip said "may be cut", which is a possibility rather than a
        # prediction, and it fired on most lines of most sectors; a warning that common
        # is read as decoration. The amber left border went with it: it encoded the same
        # predicate, and a colour with nothing naming it is worse than either.
        if place.get("always_short"):
            marks += f'<span class="mark short">{html.escape(VOC["budget"]["short_mark"])}</span>'
        head = (
            f'<div class="rank">{place["position"] + 1}</div>'
            f'<div class="name">{html.escape(entry["name"])}{marks}</div>'
            f'<div class="cnt">{count}</div>'
            f'<div class="track">{blocks(entry["min"], entry["max"])}</div>'
        )
        # A line is a list, and the list is the interesting part: the row opens onto the
        # events it can place, this line's own note, and the Advanced Edition twin of the
        # list where there is one. An entry that resolves to nothing stays a plain row.
        body = ""
        if entry["events"]:
            pool = "".join(event_html(record) for record in entry["events"])
            body += f'<div class="pool">{pool}</div>'
        note = (copy.get("section_notes") or {}).get(entry["name"])
        if note:
            body += f'<p class="note">{inline(note, titles, slug, "section_notes")}</p>'
        body += delta_html(entry)
        if body:
            rows.append(
                f'<details class="bwrap"><summary class="brow expandable{classes}">{head}</summary>'
                f'<div class="bpool">{body}</div></details>'
            )
        else:
            rows.append(f'<div class="brow{classes}">{head}</div>')
    rows.append(fallback_row(data))
    return f'<div class="budget">{"".join(rows)}</div>'


def fallback_row(data):
    """The fill-in line — last, because it is what happens after the table runs out.

    It is not in `sector_data.xml`: the engine reaches `NEUTRAL` by name once the table is
    exhausted. But it places real beacons, so a budget that stops at the table understates
    the map. Marked rather than numbered, since the file has no such line to count.
    """
    gen = data["generation"]
    span = gen.get("fallback_beacons")
    if not span:
        return ""
    low, high = span["min"], span["max"]
    classes = " fill" + (" zero" if high == 0 else "")
    count = str(low) if low == high else \
        f'{low}{VOC["format"]["range_join"]}{high}'
    # No roll governs this line — it takes whatever the table leaves — so its blocks
    # carry the reason rather than a per-block chance.
    fill = html.escape(VOC["budget"]["block_fill"], quote=True)
    track = "".join(f'<i class="blk maybe" title="{fill}"></i>' for _ in range(high))
    head = (
        f'<div class="rank">{html.escape(VOC["budget"]["fallback_rank"])}</div>'
        f'<div class="name">{html.escape(gen["fallback_list"])}'
        f'<span class="mark fill">{html.escape(VOC["budget"]["fallback_mark"])}</span></div>'
        f'<div class="cnt">{count}</div>'
        f'<div class="track">{track}</div>'
    )
    # A sector whose minima already cover the map can never reach the list, so there is
    # nothing to open — the same rule the table's own zero rows follow.
    events = gen.get("fallback_events") or []
    if high and events:
        pool = "".join(event_html(record) for record in events)
        return (
            f'<details class="bwrap"><summary class="brow expandable{classes}">{head}</summary>'
            f'<div class="bpool"><div class="pool">{pool}</div></div></details>'
        )
    return f'<div class="brow{classes}">{head}</div>'


def legend_html(data):
    """What a block means — solid, faded, and red — with the odds worked once.

    The worked example uses the widest line on this sector, because the arithmetic is
    only legible on a line with several optional blocks. A sector whose lines are all
    fixed has no example to give and gets the rule without one.
    """
    widest = max(data["entries"], key=lambda e: e["max"] - e["min"], default=None)
    low, high = (widest["min"], widest["max"]) if widest else (0, 0)
    odds = block_odds(low, high)
    if odds:
        # "80% for one" is only true where the line's minimum is 0 and the first faded
        # block is the first block; a line that already guarantees some says so instead.
        wording = VOC["legend"]["may" if low == 0 else "may_offset"]
        may = wording.format(
            name=widest["name"], low=low, high=high, counts=high - low + 1,
            each=round(100 / (high - low + 1)), first=odds[0], last=odds[-1])
    else:
        may = VOC["legend"]["may_plain"]

    def row(keys, text):
        # The budget paints red per row; the legend needs both colours side by side.
        blocks_html = "".join(f'<i class="blk{" " + k if k else ""}"></i>' for k in keys)
        return (f'<div class="lgrow"><span class="lgkey">{blocks_html}</span>'
                f'<span>{inline(text, {}, data["slug"], "legend")}</span></div>')

    return (
        '<div class="legend">'
        + row(["", "hostile"], VOC["legend"]["must"])
        + row(["maybe", "maybe hostile"], may)
        + row(["hostile", "maybe hostile"], VOC["legend"]["fight"])
        + "</div>"
    )


def generation_html(data):
    """How this table becomes a map, in two paragraphs — none of it in the game files.

    The cloud paragraph can only count the storms in the shared NEBULA list where the
    sector allocates that list itself; elsewhere it states the conversion rule alone.

    Two sectors need a third line, and only they get one: a table that cannot fit the
    map (Hidden Crystal Worlds) and a table that names the fill-in list as a numbered
    line too (both Slug nebulas, where the budget otherwise shows NEUTRAL twice with
    nothing to say why).
    """
    gen = data["generation"]
    notes = [VOC["generation"]["order"].format(
        grid=gen["grid_beacons"], list=gen["fallback_list"])]

    nebula = next((e for e in data["entries"] if e["name"] == "NEBULA"), None)
    storms = set((data["rollup"].get("markers") or {}).get("environment", {}).get("storm") or [])
    if nebula:
        in_list = storms & {r["id"] for r in nebula["events"]}
        notes.append(VOC["generation"]["clouds_storms"].format(
            storms=len(in_list), events=len(nebula["events"])))
    else:
        notes.append(VOC["generation"]["clouds"])

    if gen.get("cannot_meet_minimum"):
        notes.append(VOC["generation"]["cannot_meet_minimum"].format(
            min=gen["allocated_min"], grid=gen["grid_beacons"]))
    if any(e["name"] == gen["fallback_list"] for e in data["entries"]):
        notes.append(VOC["generation"]["fallback_also_allocated"].format(
            list=gen["fallback_list"]))
    return "".join(f'<p class="note">{inline(n, {}, data["slug"], "generation")}</p>'
                   for n in notes)


def markers_html(data):
    """The two things the map draws on a beacon before you jump to it.

    Membership is exact — <distressBeacon/> and <store/> on the event itself — and the
    same two facts ride every event row on the page as tags, so these sections are the
    whole set rather than the only place they are said.
    """
    markers = data["rollup"].get("markers") or {}
    distress = (markers.get("distress") or {}).get("events") or []
    store = markers.get("store") or []

    records = {}
    for entry in data["entries"]:
        for record in entry["events"]:
            records[record["id"]] = record

    def pool(ids):
        return "".join(event_html(records[i]) for i in ids if i in records)

    out = []
    if distress:
        out.append(
            f'<section><h2>{html.escape(VOC["headings"]["distress"])}</h2>'
            f'<div class="pool">{pool(distress)}</div>'
            f'<p class="note"><i>{inline(VOC["markers"]["distress_note"], {}, data["slug"], "markers")}'
            "</i></p></section>"
        )
    if store:
        out.append(
            f'<section><h2>{html.escape(VOC["headings"]["stores"])}</h2>'
            f'<div class="pool">{pool(sorted(store))}</div></section>'
        )
    return "".join(out)


def gate_rows(data):
    """One row per option *and* level, most-gated first.

    rollup.gates counts an option once however many levels it asks for; levels_detail
    splits it. A system gate with no level of its own is folded into level 1 by the
    extractor, because `lvl` is a floor and a system you merely have is at level 1; a
    non-system gate — crew, augment, weapon list — carries no level at all.
    """
    rows = []
    for gate in data["rollup"]["gates"]:
        for level in gate.get("levels_detail") or []:
            rows.append((gate["label"], level.get("lvl"), len(level["events"])))
    rows.sort(key=lambda r: (-r[2], r[0].lower(), r[1] or ""))
    return rows


def gates_html(data):
    """Every blue option the pool can offer, and how many of its events offer it.

    Derived whole from rollup.gates, which is why it carries no prose: the count is
    events-that-offer-it, and no file states how often any of them is placed. The top
    rows are visible and the rest are behind the box, which is its own toggle.
    """
    gates = data["rollup"]["gates"]
    if not gates:
        return ""
    rows = gate_rows(data)

    def row(label, lvl, hits):
        # The level is part of the option's name, not a chip beside it.
        name = VOC["gates"]["level_name"].format(label=label, lvl=lvl) if lvl else label
        return (f'<div class="grow"><span class="g">{html.escape(name)}</span>'
                f'<span class="h">{hits}</span></div>')

    head = "".join(row(*r) for r in rows[:TOP_GATES])
    rest = "".join(row(*r) for r in rows[TOP_GATES:])
    meta = VOC["gates"]["meta"].format(
        options=len(gates), hits=sum(len(g["events"]) for g in gates))
    more = (f'<div class="morehint">{html.escape(VOC["gates"]["more"].format(n=len(rows)))}</div>'
            if rest else "")
    return (
        f'<details class="panel gp gtoggle"><summary>'
        f'<h3>{html.escape(VOC["gates"]["title"])}'
        f'<span class="cnt">{html.escape(meta)}</span></h3>'
        f'<div class="gates">{head}</div>{more}</summary>'
        f'<div class="gates rest">{rest}</div></details>'
    )


def crew_odds_html(data):
    """What a store here can sell, and how likely each species is per slot.

    Every number is arithmetic on the engine's own rule — candidate list = crew with
    non-zero effective rarity, weight = 6 - rarity, one independent draw per slot —
    read out of the binary rather than inferred (SECTOR-PAGE.md §4.3c). Weight is not
    shown: it is 6 - rarity and nothing is played off it.

    Species a store here cannot sell stay in the table at 0% rather than in a line of
    their own: rarity 0 is a flag meaning "not in the pool", and the zero row says that
    where a player is already looking.
    """
    odds = data.get("crew_store_odds") or {}
    crew = odds.get("crew") or []
    if not crew:
        return ""
    rows = [(c["label"], round(c["share"]), round(c["in_store"]), False) for c in crew]
    rows += [(c["label"], 0, 0, True) for c in odds.get("excluded") or []]

    # The panel's title rides in the empty label cell of the first column's sub-header,
    # so the heading costs no line of its own.
    def head(title=""):
        slot = html.escape(VOC["crew_odds"]["head_slot_title"], quote=True)
        store = html.escape(VOC["crew_odds"]["head_store_title"], quote=True)
        return ('<div class="crow chead t2">'
                f'<span class="cl">{title}</span>'
                f'<span class="cp" title="{slot}">{html.escape(VOC["crew_odds"]["head_slot"])}</span>'
                f'<span class="cs" title="{store}">{html.escape(VOC["crew_odds"]["head_store"])}</span></div>')

    def row(label, share, in_store, out):
        return (f'<div class="crow t2{" out" if out else ""}">'
                f'<span class="cl">{html.escape(label)}</span>'
                f'<span class="cp">{share}%</span><span class="cs">{in_store}%</span></div>')

    # Down, then across: the rank scan runs top-to-bottom as it always has, and the
    # species a store here cannot sell land together at the foot of the second column.
    half = -(-len(rows) // 2)
    groups = [g for g in (rows[:half], rows[half:]) if g]
    title = f'<h3>{html.escape(VOC["crew_odds"]["title"])}</h3>'
    columns = "".join(
        f'<div class="tcol">{head(title if index == 0 else "")}'
        f'{"".join(row(*r) for r in group)}</div>'
        for index, group in enumerate(groups)
    )
    return f'<div class="panel gp crewpanel"><div class="two">{columns}</div></div>'


def glance_html(data):
    """The two generated blocks, above the budget. Omitted entirely when a sector has
    neither — the Last Stand gates nothing at all."""
    blocks = [b for b in (gates_html(data), crew_odds_html(data)) if b]
    if not blocks:
        return ""
    return (
        f'<section><h2>{html.escape(VOC["headings"]["glance"])}</h2>'
        f'<div class="glance">{"".join(blocks)}</div></section>'
    )


def panels_html(data, copy, titles, slug):
    out = []
    for panel in copy["panels"]:
        items = "".join(
            f'<li><span class="lead">{inline(i["lead"], titles, slug, "panels")}</span>'
            f'<span>{inline(i["text"], titles, slug, "panels")}</span></li>'
            for i in panel["items"]
        )
        out.append(
            f'<div class="panel"><h3>{inline(panel["title"], titles, slug, "panels")}</h3>'
            f"<ul>{items}</ul></div>"
        )
    return f'<div class="cols">{"".join(out)}</div>'


def chain_html(copy, titles, slug):
    chain = copy.get("chain")
    if not chain:
        return ""
    steps = []
    for index, step in enumerate(chain["steps"]):
        last = index == len(chain["steps"]) - 1
        line = "" if last else '<div class="line"></div>'
        ref = f'<div class="id">{html.escape(step["ref"])}</div>' if step.get("ref") else ""
        steps.append(
            f'<div class="step{" end" if last else ""}">'
            f'<div class="marker"><div class="dot">{html.escape(step["marker"])}</div>{line}</div>'
            f'<div class="body"><div class="t">{inline(step["title"], titles, slug, "chain")}</div>'
            f'<div class="d">{inline(step["detail"], titles, slug, "chain")}</div>{ref}</div></div>'
        )
    return (
        f'<section><h2>{html.escape(VOC["headings"]["chain"])}'
        f'<span class="meta">{inline(chain["title"], titles, slug, "chain")}</span></h2>'
        f'<div class="chain">{"".join(steps)}</div></section>'
    )


def loader_html():
    """The config block and the loader that turns a beacon box into its card.

    The paths and every word the loader can show are emitted here; the script itself
    holds no English and no path, the same split the rest of this pipeline uses.
    """
    config = {
        "runtime": CARD_RUNTIME,
        "css": CARD_CSS,
        "data": CARD_DATA,
        "strings": {
            "loading": VOC["cards"]["loading"],
            "failed": VOC["cards"]["failed"],
        },
    }
    payload = json.dumps(config, ensure_ascii=False, indent=2).replace("<", "\\u003c")
    return (
        '<script type="application/json" id="sector-card-loader">\n'
        f"{payload}\n</script>\n"
        f"<script>\n{LOADER.read_text(encoding='utf-8')}</script>"
    )


def toggle_html():
    """The blue-options box is its own toggle — see tools/sector-toggle.js.

    Inlined the way the card loader is, and for the same reason: the page must load
    nothing at runtime, because a published artifact runs under a CSP that blocks it.
    """
    return f"<script>\n{TOGGLE.read_text(encoding='utf-8')}</script>"


def header_html(data, copy, titles, slug):
    facts = [
        (VOC["facts"]["earliest"], str(data.get("earliest_sector", data["min_sector"] + 1))),
        ("", VOC["facts"]["unique"] if data["unique"] else VOC["facts"]["repeatable"]),
    ]
    if data.get("tracks"):
        facts.append((VOC["facts"]["tracks"], " · ".join(data["tracks"])))
    facts.append(("", VOC["facts"]["data"]))

    chips = "".join(
        f'<span class="fact">{html.escape(label)} <b>{html.escape(value)}</b></span>'
        if label else f'<span class="fact"><b>{html.escape(value)}</b></span>'
        for label, value in facts
    )
    eyebrow = f'{VOC["eyebrow"]} · {data["id"]}'
    return (
        f'<header><p class="eyebrow">{html.escape(eyebrow)}</p>'
        f'<h1>{html.escape(data["title"])}</h1>'
        f'<p class="lede">{inline(copy["lede"], titles, slug, "lede")}</p>'
        f'<div class="facts">{chips}</div></header>'
    )


def render(data, copy):
    slug = data["slug"]
    titles = {}
    for entry in data["entries"]:
        for record in entry["events"]:
            titles[record["id"]] = record["title"]
        for record in (entry.get("override") or {}).get("added") or []:
            titles[record["id"]] = record["title"]
    if data.get("start_event"):
        titles[data["start_event"]["id"]] = data["start_event"]["title"]
    for group in data["rollup"]["quest_targets"]:
        titles.setdefault(group["value"], group["value"])

    # The two numbers that survived the stat tiles ride in the budget heading, which is
    # where they mean something. Both are still metrics, so neither is typed by hand.
    meta = VOC["headings"]["budget_meta"].format(
        spread=metric(data, "beacons_min..beacons_max"),
        events=data["metrics"]["distinct_events"])
    budget = [
        f'<h2>{html.escape(VOC["headings"]["budget"])}'
        f'<span class="meta">{html.escape(meta)}</span></h2>',
        budget_html(data, copy, titles, slug),
        legend_html(data),
        generation_html(data),
    ]

    parts = [
        header_html(data, copy, titles, slug),
        glance_html(data),
        f"<section>{''.join(budget)}</section>",
        markers_html(data),
        chain_html(copy, titles, slug),
        panels_html(data, copy, titles, slug),
        loader_html(),
        toggle_html(),
    ]
    return "".join(parts)


def build(slug, out_path=None):
    data_path = DATA_DIR / f"{slug}.sector.json"
    copy_path = COPY_DIR / f"{slug}.json"
    if not data_path.exists():
        sys.exit(f"{data_path}: not found — run tools/extract-sector.py first")
    if not copy_path.exists():
        sys.exit(f"{copy_path}: not found — every page needs a copy file (see tools/SECTOR-PAGE.md §5)")

    data = json.loads(data_path.read_text(encoding="utf-8"))
    if data.get("schema") != SCHEMA:
        sys.exit(f"{data_path}: expected schema {SCHEMA!r}, found {data.get('schema')!r}")
    copy = json.loads(copy_path.read_text(encoding="utf-8"))

    check(copy, data, slug)

    template = TEMPLATE.read_text(encoding="utf-8")
    if MARKER not in template:
        sys.exit(f"{TEMPLATE}: no {MARKER} to fill")
    if not TITLE.search(template):
        sys.exit(f"{TEMPLATE}: no <title> element on a line of its own")

    html_out = template.replace(MARKER, render(data, copy))
    html_out = TITLE.sub(f"<title>{data['title']} — sector profile</title>", html_out, count=1)

    out = out_path or ROOT / "sectors" / f"sector-{slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_out, encoding="utf-8")
    return out


VOC = json.loads(VOCAB.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="sector slug, e.g. engi-homeworlds")
    ap.add_argument("--all", action="store_true", help="every sector that has a copy file")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output .html (single sector only)")
    args = ap.parse_args()

    if args.all:
        slugs = sorted(p.stem for p in COPY_DIR.glob("*.json")) if COPY_DIR.is_dir() else []
        if not slugs:
            sys.exit(f"{COPY_DIR}: no copy files")
    elif args.slug:
        slugs = [args.slug]
    else:
        ap.error("give a sector slug or --all")

    for slug in slugs:
        print(build(slug, args.out if len(slugs) == 1 else None))


if __name__ == "__main__":
    main()
