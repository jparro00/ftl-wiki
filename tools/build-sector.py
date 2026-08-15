#!/usr/bin/env python3
"""Build an FTL sector profile page from its extracted data plus its copy file.

    python tools/build-sector.py engi-homeworlds
    python tools/build-sector.py --all

Two inputs, and the split between them is the whole design:

    sectors/data/<slug>.sector.json   every number and every event — generated, never edited
    tools/sector-copy/<slug>.json     the words — hand-written, holds no numbers

A stat tile names a metric and supplies a label; the number comes from the data. Prose
refers to an event as {{EVENT_ID}} and the renderer resolves its title, so a page cannot
name an event this sector does not have. Both rules exist so that no fact on a sector
page is typed by a human.

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

COPY_KEYS = {"slug", "lede", "stats", "callout", "section_notes", "panels", "chain"}
REQUIRED = {"slug", "lede", "stats", "panels"}

SOURCE_FILES = ["sector_data.xml", "events*.xml", "newEvents.xml", "dlcEventsOverwrite.xml"]


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

    if not 3 <= len(copy["stats"]) <= 5:
        fail(slug, f"stats: expected 3–5 tiles, found {len(copy['stats'])}")
    for tile in copy["stats"]:
        if set(tile) - {"metric", "label"} or not {"metric", "label"} <= set(tile):
            fail(slug, "stats: each tile needs exactly 'metric' and 'label'")
        for key in tile["metric"].split(".."):
            if key not in data["metrics"]:
                fail(slug, f"stats: unknown metric {key!r}")

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
    """A stat tile's number: one metric key, or 'a..b' rendered as a range."""
    keys = expr.split("..")
    values = [data["metrics"][k] for k in keys]
    if len(values) == 1:
        return str(values[0])
    low, high = values[0], values[-1]
    if low == high:
        return str(low)
    return f"{low}{VOC['format']['range_join']}{high}"


def tags_html(record):
    picked = [t for t in VOC["tag_order"] if t in (record.get("tags") or [])]
    picked = picked[: VOC["tag_limit"]]
    out = [f'<span class="tg {t}">{html.escape(VOC["tags"][t])}</span>' for t in picked]
    if record.get("weight"):
        out.append(f'<span class="tg">{html.escape(VOC["format"]["weight"].format(n=record["weight"]))}</span>')
    return f'<div class="tags">{"".join(out)}</div>' if out else ""


def rail_of(record):
    for tag in VOC["tag_order"]:
        if tag in (record.get("tags") or []) and tag in VOC["rail"]:
            return " " + VOC["rail"][tag]
    return ""


def event_html(record):
    return (
        f'<div class="ev{rail_of(record)}">'
        f'<div class="t">{html.escape(record["title"])}</div>'
        f'<div class="id">{html.escape(record["id"])}</div>'
        f"{tags_html(record)}"
        "</div>"
    )


def blocks(low, high, extra_class=""):
    out = [f'<i class="blk{extra_class}"></i>' for _ in range(low)]
    out += [f'<i class="blk maybe{extra_class}"></i>' for _ in range(max(0, high - low))]
    return "".join(out) or '<i class="blk maybe"></i>'


def budget_html(data):
    rows = []
    for entry in data["entries"]:
        hostile = " hostile" if entry["section"] in ("hostile", "boarders") else ""
        zero = " zero" if entry["max"] == 0 else ""
        count = str(entry["min"]) if entry["min"] == entry["max"] else \
            f'{entry["min"]}{VOC["format"]["range_join"]}{entry["max"]}'
        rows.append(
            f'<div class="brow{hostile}{zero}">'
            f'<div class="name">{html.escape(entry["name"])}</div>'
            f'<div class="cnt">{count}</div>'
            f'<div class="track">{blocks(entry["min"], entry["max"])}</div>'
            "</div>"
        )
    return f'<div class="budget">{"".join(rows)}</div>'


def pool_sections(data, copy, titles, slug):
    out = []
    notes = copy.get("section_notes") or {}
    for entry in data["entries"]:
        section = VOC["sections"].get(entry["section"], {"label": entry["section"], "hint": ""})
        if entry["min"] != entry["max"]:
            count = VOC["format"]["beacons"].format(min=entry["min"], max=entry["max"])
        elif entry["min"] == 1:
            count = VOC["format"]["beacons_one"]
        else:
            count = VOC["format"]["beacons_fixed"].format(min=entry["min"])
        meta = VOC["format"]["meta_join"].join(
            [entry["name"], count] + ([section["hint"]] if section["hint"] else [])
        )
        body = [
            f"<h2>{html.escape(section['label'])}"
            f'<span class="meta">{html.escape(meta)}</span></h2>'
        ]
        if entry["events"]:
            body.append(f'<div class="pool">{"".join(event_html(e) for e in entry["events"])}</div>')
        if entry["max"] == 0:
            body.append(f'<p class="note">{html.escape(VOC["budget"]["zero"])}</p>')
        if entry["name"] in notes:
            body.append(f'<p class="note">{inline(notes[entry["name"]], titles, slug, "section_notes")}</p>')

        override = entry.get("override")
        if override and (override["added"] or override["removed"]):
            head = VOC["delta"]["head"].format(list=override["list"])
            inner = [f'<div class="head">{html.escape(head)}</div>']
            if override["added"]:
                inner.append(
                    f'<p class="note">{html.escape(VOC["delta"]["added"])}</p>'
                    f'<div class="pool">{"".join(event_html(e) for e in override["added"])}</div>'
                )
            if override["removed"]:
                dropped = ", ".join(override["removed"])
                inner.append(f'<p class="note">{html.escape(VOC["delta"]["removed"])} {html.escape(dropped)}</p>')
            inner.append(
                f'<p class="note">{html.escape(VOC["delta"]["unconfirmed"].format(name=entry["name"]))}</p>'
            )
            body.append(f'<div class="delta">{"".join(inner)}</div>')
        out.append(f"<section>{''.join(body)}</section>")
    return "".join(out)


def rarity_html(data):
    # FINAL declares no rarityList at all, and an empty panel is worse than no panel:
    # it renders as a heading and a legend explaining rows that are not there.
    if not data.get("crew_rarity"):
        return ""
    rows = []
    for crew in data["crew_rarity"]:
        filled = max(0, min(5, crew["rarity"]))
        pips = "".join(
            f'<i class="pip{"" if i < filled else " off"}"></i>' for i in range(5)
        )
        value = VOC["rarity"]["never"] if crew["rarity"] == 0 else str(crew["rarity"])
        zero = " zero" if crew["rarity"] == 0 else ""
        rows.append(
            f'<div class="rrow{zero}"><span>{html.escape(crew["label"])}</span>'
            f'<span class="pips">{pips}</span><span class="v">{html.escape(value)}</span></div>'
        )
    return (
        '<div class="panel"><h3>' + html.escape(VOC["headings"]["rarity"]) + "</h3>"
        f'<div class="rar">{"".join(rows)}</div>'
        f'<p class="note">{html.escape(VOC["rarity"]["note"])}</p></div>'
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
    rarity = rarity_html(data)
    if rarity:
        out.append(rarity)
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


def footnotes(data):
    notes = [VOC["footnotes"]["sources"].format(files=", ".join(SOURCE_FILES))]
    if data["rollup"]["unique"]:
        notes.append(VOC["footnotes"]["unique"])
    notes.append(VOC["footnotes"]["unweighted"])
    ambiguous = [e["name"] for e in data["entries"] if e.get("ambiguous")]
    if ambiguous:
        notes.append(VOC["footnotes"]["ambiguous"].format(names=", ".join(ambiguous)))
    anonymous = sum(e.get("anonymous_outcomes", 0) for e in data["entries"])
    if anonymous:
        notes.append(VOC["footnotes"]["anonymous"].format(count=anonymous))
    if data["rollup"]["no_card"]:
        notes.append(VOC["footnotes"]["no_card"].format(names=", ".join(data["rollup"]["no_card"])))
    return "<footer>" + "".join(f"<p>{html.escape(n)}</p>" for n in notes) + "</footer>"


def header_html(data, copy, titles, slug):
    facts = [
        (VOC["facts"]["min_sector"], str(data["min_sector"])),
        ("", VOC["facts"]["unique"] if data["unique"] else VOC["facts"]["repeatable"]),
    ]
    if data.get("start_event"):
        facts.append((VOC["facts"]["start"], data["start_event"]["id"]))
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


def stats_html(data, copy):
    tiles = "".join(
        f'<div class="stat"><div class="n">{html.escape(metric(data, t["metric"]))}</div>'
        f'<div class="k">{html.escape(t["label"])}</div></div>'
        for t in copy["stats"]
    )
    return f'<div class="stats">{tiles}</div>'


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

    parts = [header_html(data, copy, titles, slug), stats_html(data, copy)]

    budget = [
        f'<h2>{html.escape(VOC["headings"]["budget"])}'
        f'<span class="meta">{html.escape(VOC["headings"]["budget_meta"])}</span></h2>',
        budget_html(data),
        f'<p class="note">{html.escape(VOC["budget"]["legend"])}</p>',
    ]
    if data.get("start_event"):
        entry_note = VOC["budget"]["entry"].format(event=data["start_event"]["id"])
        budget.append(f'<p class="note">{html.escape(entry_note[0].upper() + entry_note[1:])}</p>')
    if copy.get("callout"):
        budget.append(f'<div class="callout">{inline(copy["callout"], titles, slug, "callout")}</div>')
    parts.append(f"<section>{''.join(budget)}</section>")

    parts.append(pool_sections(data, copy, titles, slug))
    parts.append(chain_html(copy, titles, slug))
    parts.append(panels_html(data, copy, titles, slug))
    parts.append(footnotes(data))
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
