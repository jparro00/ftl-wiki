#!/usr/bin/env python3
"""Extract a sector profile from raw/gamedata into ftl-sector-profile/1 JSON.

    python tools/extract-sector.py ENGI_HOME
    python tools/extract-sector.py --all

Reads the shipped XML only. Every number here is stated by sector_data.xml; every
event title comes from the wiki page join; every per-event tag is derived from that
event's already-extracted tree in cards/trees/. Nothing is inferred and nothing is
invented — where the data is silent (odds inside a list, whether OVERRIDE_X replaces
X) the output says so rather than guessing.

See tools/SECTOR-PAGE.md for the spec this implements.
"""

import argparse
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
GAMEDATA = ROOT / "raw" / "gamedata"
TREES = ROOT / "cards" / "trees"
SCHEMA = "ftl-sector-profile/1"

MAX_LIST_DEPTH = 4  # a sector list nesting deeper than this is a data bug, not a pool


def _load_extractor():
    """Reuse extract-event.py's XML index; its module name is not importable."""
    spec = importlib.util.spec_from_file_location("ftl_extract_event", TOOLS / "extract-event.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EE = _load_extractor()

# Sector list names are highly regular, so a section's role is read off the name.
# Order here is display order: what is guaranteed first, then what shoots at you,
# then everything else, then the filler. "special" is the fallback, deliberately —
# an unrecognised name is a named one-off beacon, which is exactly what leads a page.
SECTION_RULES = [
    ("hostile",  (r"^HOSTILE", r"^NEBULA_HOSTILE", r"^BOSS_HOSTILE")),
    ("boarders", (r"^BOARDERS", r"^HOSTILE_BOARDING")),
    ("neutral",  (r"^NEUTRAL", r"^NEBULA_NEUTRAL", r"^BOSS_NEUTRAL")),
    ("nebula",   (r"^NEBULA$", r"^NEBULA_[A-Z]+$", r"^STORM")),
    ("distress", (r"^DISTRESS_BEACON",)),
    ("items",    (r"^ITEMS", r"^ITEM_")),
    ("store",    (r"^STORE", r"^NEBULA_STORE", r"^BOSS_REPAIR_STATION")),
    ("quests",   (r"^QUESTS",)),
    ("empty",    (r"^NOTHING", r"^NEBULA_EMPTY", r"^NEBULA_NOTHING")),
]
SECTION_ORDER = ["special", "hostile", "boarders", "neutral", "nebula",
                 "distress", "items", "store", "quests", "empty"]


def section_of(name):
    for section, patterns in SECTION_RULES:
        if any(re.match(p, name) for p in patterns):
            return section
    return "special"


def sector_pages():
    """sector id → (slug, title), read from wiki/sectors/*.md.

    Same join as the event pipeline (EVENT-CARD.md §4.7): the game files hold no
    human sector title beyond text_sectorname.xml's display name, and the wiki page
    is what fixes the slug. A page listing several ids (the vestigial stubs) is
    skipped — it documents no single sector.
    """
    index = {}
    pages = ROOT / "wiki" / "sectors"
    if not pages.is_dir():
        return index
    for path in sorted(pages.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        found = re.search(r"^sector_id:\s*(.+?)\s*$", text, re.MULTILINE)
        if not found or "," in found.group(1):
            continue
        sid = found.group(1).strip()
        title = None
        for line in text.splitlines():
            if line.startswith("# "):
                title = re.sub(r"\s+—\s+`.*`$", "", line[2:].strip())
                break
        index[sid] = (path.stem, title or path.stem.replace("-", " ").title())
    return index


def sector_names():
    """id → (display name, short name) from text_sectorname.xml."""
    out = {}
    path = GAMEDATA / "text_sectorname.xml"
    if not path.exists():
        return out
    strings = {}
    for el in EE.definitions(EE.parse_fragment(path)):
        if isinstance(el.tag, str) and el.tag == "text" and "name" in el.attrib:
            strings[el.attrib["name"]] = (el.text or "").strip()
    for key, value in strings.items():
        if key.startswith("sectorname_short_"):
            out.setdefault(key[len("sectorname_short_"):], [None, None])[1] = value
        elif key.startswith("sectorname_"):
            out.setdefault(key[len("sectorname_"):], [None, None])[0] = value
    return {k: tuple(v) for k, v in out.items()}


class Trees:
    """The built event trees, indexed by event id — the source of every per-event tag."""

    def __init__(self):
        self.by_id = {}
        if not TREES.is_dir():
            return
        for path in sorted(TREES.glob("*.tree.json")):
            try:
                doc = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if doc.get("id"):
                self.by_id[doc["id"]] = doc

    def profile(self, event_id):
        """What one event does, reduced to the facts a pool row can show.

        Tags are derived, never asserted: 'fight' means the root node is combat,
        'may-fight' means a combat node exists somewhere below a choice. The
        distinction is the whole point of the hostile/neutral split, so it is read
        from the tree rather than from which list the event sits in.
        """
        doc = self.by_id.get(event_id)
        if not doc:
            return {"card": False}

        found = {
            "gates": [], "items": [], "crew_classes": [], "quests": [],
            "boarders": [], "unlock_ship": [], "fleet_delay": [],
        }
        flags = {"combat": False, "crew_gain": False, "crew_loss": False,
                 "store": False, "reward": False, "cost": False, "environment": False}

        def walk(node):
            if isinstance(node, dict):
                kind = node.get("kind")
                if kind == "combat":
                    # A <ship> that arrives hostile="false" is not a fight: ZOLTAN_FREE_MAP
                    # loads a ship and then hands over the map. Counting it made a friendly
                    # encounter render as a forced fight.
                    if node.get("hostile") is not False:
                        flags["combat"] = True
                    else:
                        flags["passive_ship"] = True
                elif kind == "ship_hostility" and node.get("hostile"):
                    # …unless something in the tree turns that ship on you.
                    flags["combat"] = True
                elif kind == "crew_gain":
                    # Signed: amount="-1" is a crew member walking off the ship.
                    if (node.get("amount") or 0) < 0:
                        flags["crew_loss"] = True
                    else:
                        flags["crew_gain"] = True
                        if node.get("class"):
                            found["crew_classes"].append(node["class"])
                elif kind == "crew_loss":
                    flags["crew_loss"] = True
                elif kind == "item" and node.get("id") and node.get("id") != "RANDOM":
                    found["items"].append({"id": node["id"], "kind": node.get("item_kind"),
                                           "label": node.get("label")})
                elif kind == "reward":
                    flags["reward"] = True
                elif kind == "resource":
                    if (node.get("amount") or node.get("min") or 0) < 0:
                        flags["cost"] = True
                    else:
                        flags["reward"] = True
                elif kind == "store":
                    flags["store"] = True
                elif kind == "boarders":
                    found["boarders"].append({k: node.get(k) for k in ("class", "min", "max")})
                elif kind == "quest" and node.get("event"):
                    found["quests"].append(node["event"])
                elif kind == "unlock_ship":
                    found["unlock_ship"].append(node.get("id"))
                elif kind == "fleet_delay":
                    found["fleet_delay"].append(node.get("amount"))
                elif kind == "environment":
                    flags["environment"] = True
                gate = node.get("gate")
                if isinstance(gate, dict) and gate.get("req"):
                    found["gates"].append({
                        "req": gate["req"],
                        "label": gate.get("label") or gate["req"],
                        **({"lvl": gate["lvl"]} if gate.get("lvl") else {}),
                    })
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(doc.get("node"))
        walk(doc.get("effects"))
        # Quest stages hang off the root as chain[], not under node — walking them is
        # what makes a multi-stage unlock (ENGI_UNLOCK_1 → 2 → 3 → 4) visible as a whole.
        walk(doc.get("chain"))

        root = doc.get("node") or {}
        tags = []
        # "fight" means arriving starts one. A root <ship hostile="false"> does not:
        # ZOLTAN_FREE_MAP loads a ship at the beacon and then hands over the map.
        if root.get("kind") == "combat" and root.get("hostile") is not False:
            tags.append("fight")
        elif flags["combat"]:
            tags.append("may-fight")
        if found["boarders"]:
            tags.append("boarders")
        if flags["crew_loss"]:
            tags.append("crew-loss")
        if flags["crew_gain"]:
            tags.append("crew")
        if flags["store"]:
            tags.append("store")
        if found["quests"]:
            tags.append("quest")
        if flags["reward"] and not flags["combat"]:
            tags.append("reward")
        if flags["cost"]:
            tags.append("cost")
        if (doc.get("flags") or {}).get("unique"):
            tags.append("unique")

        def uniq(seq):
            seen, out = set(), []
            for x in seq:
                key = json.dumps(x, sort_keys=True) if isinstance(x, dict) else x
                if key not in seen:
                    seen.add(key)
                    out.append(x)
            return out

        return {
            "card": True,
            "slug": doc.get("slug"),
            "title": doc.get("title"),
            "tags": tags,
            "gates": uniq(found["gates"]),
            "items": uniq(found["items"]),
            "crew_classes": uniq(found["crew_classes"]),
            "quests": uniq(found["quests"]),
            "boarders": uniq(found["boarders"]),
            "unlock_ship": uniq([s for s in found["unlock_ship"] if s is not None]),
            "fleet_delay": uniq(found["fleet_delay"]),
        }


class SectorExtractor:
    def __init__(self):
        self.idx = EE.Index()
        self.trees = Trees()
        self.pages = sector_pages()
        self.event_pages = EE.page_index()
        self.names = sector_names()
        self.descriptions = {}
        for el in EE.definitions(EE.parse_fragment(GAMEDATA / "sector_data.xml")):
            if isinstance(el.tag, str) and el.tag == "sectorDescription" and el.get("name"):
                self.descriptions[el.attrib["name"]] = el

    # -- pool resolution ---------------------------------------------------

    def members(self, list_name, depth=0, seen=None):
        """Event ids an eventList can produce, flattening nested lists.

        A list entry is normally <event load="X"/>. Two other shapes exist and both
        are recorded rather than dropped: an entry that loads another *list*
        (flattened, with `via` naming the inner list), and an anonymous <event> body
        that is an outcome written inline, which has no id to point at.
        """
        seen = seen if seen is not None else set()
        if list_name in seen or depth > MAX_LIST_DEPTH:
            return []
        seen.add(list_name)
        el = self.idx.lists.get(list_name)
        if el is None:
            return []
        out = []
        for child in el:
            if not isinstance(child.tag, str) or child.tag != "event":
                continue
            target = child.get("load")
            if not target:
                out.append({"id": None, "anonymous": True})
                continue
            if target in self.idx.lists:
                for inner in self.members(target, depth + 1, seen):
                    out.append({**inner, "via": inner.get("via") or target})
            else:
                out.append({"id": target})
        return out

    def event_record(self, event_id):
        slug, title = self.event_pages.get(event_id, (None, None))
        profile = self.trees.profile(event_id)
        return {
            "id": event_id,
            "slug": profile.get("slug") or slug,
            "title": profile.get("title") or title or event_id.lower().replace("_", " ").capitalize(),
            **{k: v for k, v in profile.items() if k not in ("slug", "title")},
        }

    def entry(self, el):
        """One <event name= min= max=/> allocation inside a sectorDescription."""
        name = el.attrib["name"]
        low = int(el.get("min", 0) or 0)
        high = int(el.get("max", low) or low)

        is_list = name in self.idx.lists
        is_event = name in self.idx.events
        kind = "list" if is_list else ("event" if is_event else "missing")

        if kind == "list":
            raw_members = self.members(name)
        elif kind == "event":
            raw_members = [{"id": name}]
        else:
            raw_members = []

        events, anonymous = [], 0
        for member in raw_members:
            if member.get("anonymous") or not member.get("id"):
                anonymous += 1
                continue
            record = self.event_record(member["id"])
            if member.get("via"):
                record["via"] = member["via"]
            events.append(record)

        # Duplicate loads are the file's own weighting (EVENT-CARD.md I2 — the shipped
        # lists carry no numeric weights, so a repeated entry is the only weight there is).
        counts = {}
        for record in events:
            counts[record["id"]] = counts.get(record["id"], 0) + 1
        deduped, seen = [], set()
        for record in events:
            if record["id"] in seen:
                continue
            seen.add(record["id"])
            if counts[record["id"]] > 1:
                record["weight"] = counts[record["id"]]
            deduped.append(record)

        entry = {
            "name": name,
            "min": low,
            "max": high,
            "kind": kind,
            "section": section_of(name),
            "events": deduped,
        }
        if anonymous:
            entry["anonymous_outcomes"] = anonymous
        if is_list and is_event:
            entry["ambiguous"] = "defined as both an eventList and an event"

        override = f"OVERRIDE_{name}"
        if override in self.idx.lists:
            base_ids = {r["id"] for r in deduped}
            over = []
            for member in self.members(override):
                if member.get("id"):
                    over.append(member["id"])
            added = [i for i in dict.fromkeys(over) if i not in base_ids]
            removed = [i for i in base_ids if i not in set(over)]
            entry["override"] = {
                "list": override,
                "added": [self.event_record(i) for i in added],
                "removed": removed,
                # Whether the engine substitutes this list is an open question in
                # wiki/concepts/sector-event-allocation.md. Recorded as a delta, never
                # merged into the pool.
                "applies": "unconfirmed",
            }
        return entry

    # -- rollups -----------------------------------------------------------

    def rollup(self, entries):
        events = {}
        for entry in entries:
            for record in entry["events"]:
                slot = events.setdefault(record["id"], {**record, "lists": []})
                if entry["name"] not in slot["lists"]:
                    slot["lists"].append(entry["name"])

        def collect(field):
            out = {}
            for record in events.values():
                for value in record.get(field) or []:
                    key = json.dumps(value, sort_keys=True) if isinstance(value, dict) else value
                    out.setdefault(key, {"value": value, "events": []})
                    out[key]["events"].append(record["id"])
            return sorted(out.values(), key=lambda x: (-len(x["events"]), json.dumps(x["value"], sort_keys=True)))

        gates = {}
        for record in events.values():
            for gate in record.get("gates") or []:
                slot = gates.setdefault(gate["req"], {"req": gate["req"], "label": gate["label"],
                                                      "levels": [], "events": []})
                if gate.get("lvl") and gate["lvl"] not in slot["levels"]:
                    slot["levels"].append(gate["lvl"])
                if record["id"] not in slot["events"]:
                    slot["events"].append(record["id"])

        def tagged(tag):
            return sorted(r["id"] for r in events.values() if tag in (r.get("tags") or []))

        return {
            "distinct_events": len(events),
            "no_card": sorted(r["id"] for r in events.values() if not r.get("card")),
            "always_fight": tagged("fight"),
            "may_fight": tagged("may-fight"),
            "crew_loss": tagged("crew-loss"),
            "crew_gain": tagged("crew"),
            "boarders": tagged("boarders"),
            "unique": tagged("unique"),
            "quest_starts": tagged("quest"),
            "gates": sorted(gates.values(), key=lambda g: (-len(g["events"]), g["req"])),
            "named_items": collect("items"),
            "crew_classes": collect("crew_classes"),
            "unlock_ships": collect("unlock_ship"),
            "quest_targets": collect("quests"),
        }

    def metrics(self, entries, rollup):
        """Every number a stat tile is allowed to show, precomputed and named.

        The page's copy picks tiles by metric id and supplies only the label, so a
        number on a sector page can never be typed by hand.
        """
        out = {
            "beacons_min": sum(e["min"] for e in entries),
            "beacons_max": sum(e["max"] for e in entries),
            "distinct_events": rollup["distinct_events"],
            "always_fight_events": len(rollup["always_fight"]),
            "may_fight_events": len(rollup["may_fight"]),
            "crew_loss_events": len(rollup["crew_loss"]),
            "crew_gain_events": len(rollup["crew_gain"]),
            "boarder_events": len(rollup["boarders"]),
            "unique_events": len(rollup["unique"]),
            "gated_events": len({e for g in rollup["gates"] for e in g["events"]}),
            "quest_start_events": len(rollup["quest_starts"]),
        }
        for section in SECTION_ORDER:
            picked = [e for e in entries if e["section"] == section]
            if picked:
                out[f"section:{section}:min"] = sum(e["min"] for e in picked)
                out[f"section:{section}:max"] = sum(e["max"] for e in picked)
        for entry in entries:
            out[f"entry:{entry['name']}:min"] = entry["min"]
            out[f"entry:{entry['name']}:max"] = entry["max"]
        return out

    # -- the document ------------------------------------------------------

    def sector(self, sector_id):
        el = self.descriptions.get(sector_id)
        if el is None:
            sys.exit(f"{sector_id}: no <sectorDescription name=…> with that name")

        page_slug, page_title = self.pages.get(sector_id, (None, None))
        display, short = self.names.get(sector_id, (None, None))
        slug = page_slug or sector_id.lower().replace("_", "-")
        title = page_title or display or slug.replace("-", " ").title()

        entries = [self.entry(child) for child in el
                   if isinstance(child.tag, str) and child.tag == "event" and child.get("name")]
        entries.sort(key=lambda e: (SECTION_ORDER.index(e["section"]), e["name"]))

        tracks = [t.text.strip() for t in el.findall("trackList/track") if t.text]
        rarity = []
        for bp in el.findall("rarityList/blueprint"):
            name = bp.get("name")
            rarity.append({
                "id": name,
                "label": self.idx.blueprint_titles.get(name) or name.title(),
                "rarity": int(bp.get("rarity", 0) or 0),
            })

        start = el.findtext("startEvent")
        start = start.strip() if start else None
        rollup = self.rollup(entries)

        return {
            "schema": SCHEMA,
            "id": sector_id,
            "slug": slug,
            "title": title,
            "display_name": display,
            "short_name": short,
            "extracted_from": "raw/gamedata/sector_data.xml",
            "min_sector": int(el.get("minSector", 0) or 0),
            "unique": el.get("unique") == "true",
            "tracks": tracks,
            "crew_rarity": rarity,
            "start_event": self.event_record(start) if start else None,
            "entries": entries,
            "rollup": rollup,
            "metrics": self.metrics(entries, rollup),
        }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sector", nargs="?", help="sector id, e.g. ENGI_HOME")
    ap.add_argument("--all", action="store_true", help="every sector with a wiki/sectors page")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output .sector.json (single sector only)")
    args = ap.parse_args()

    ex = SectorExtractor()
    if args.all:
        targets = [s for s in ex.descriptions if s in ex.pages]
    elif args.sector:
        targets = [args.sector]
    else:
        ap.error("give a sector id or --all")

    for sector_id in targets:
        doc = ex.sector(sector_id)
        out = args.out or ROOT / "sectors" / "data" / f"{doc['slug']}.sector.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
