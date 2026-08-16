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

# Blue-option names, shared with the card pipeline rather than duplicated: a gate can
# name a blueprintList (WEAPONS_ION, COMBAT_BEAM_DRONE_LIST) and a list has no <title>
# in the game files, so its player-facing name is authored in one place and read here.
GATE_LABELS = json.loads(
    (TOOLS / "card-vocab.json").read_text(encoding="utf-8")
).get("gate_labels", {})

MAX_LIST_DEPTH = 4  # a sector list nesting deeper than this is a data bug, not a pool

# The sector map is a 6x4 grid with an 80% chance of a beacon per cell, so 24 is the
# ceiling. No source here states the floor, so nothing infers one.
# (raw/wiki/sectors.md, "Technical details of sector generation and events")
GRID_BEACONS = 24
# The community wiki states a floor of 19 ("between 19 and 24 beacons"). Nothing else here
# derives it, so it is carried as data and reported, but never used to mark a line at risk.
GRID_BEACONS_MIN = 19

# The store's crew draw, read out of the game binary rather than any data file:
# weight = 6 - rarity, rarity 0 excluded before weighting, and the crew section is always
# three slots (all three hireable under AE, which is the data this pipeline reads).
# raw/modding/2026-08-16-store-crew-selection-disassembly.md
CREW_WEIGHT_BASE = 6
CREW_SLOTS = 3

# Which blueprint files are read for the two questions the event index does not answer:
# which ids name a ship *system* (so a gate's `lvl` means something), and which
# crewBlueprints are the engine's own dummies rather than a species a player can hire.
BLUEPRINT_FILES = ("blueprints.xml", "dlcBlueprints.xml")


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


def rarity_change(base, here):
    """How a sector's <rarityList> moves one blueprint off its base rarity.

    Reported as a verdict rather than a signed number, because the scale is not
    linear: 0 is a flag meaning "not in the random pool", not the low end of
    1–5 (wiki/concepts/blueprint-rarity.md). So base 2 → 0 is an exclusion and
    base 0 → 2 is the opposite, and a ±2 on both would say the same thing twice.
    A blueprint the files give no <rarity> at all answers "unknown", never a guess.
    """
    if base is None:
        return "unknown"
    if base == here:
        return "same"
    if base == 0:
        return "unlocked"
    if here == 0:
        return "excluded"
    return "more-common" if here < base else "rarer"


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


def blueprint_kinds():
    """(system ids, dummy crew ids) read from the blueprint files, never listed by hand.

    A gate's `req` may name a system, a crew species, an augment or a blueprintList,
    and only a system has a level to ask for — `lvl` is a floor on that system's level
    (wiki/concepts/blue-options.md), and every other kind of req carries none. The one
    thing in the files that says "this id is a system" is `<systemBlueprint name=…>`.

    The dummy set is the second half of the same question for crew: `battle` and
    `repair` are `crewBlueprint`s carrying `NOLOC="1"` and the desc "Dummy blueprint
    needed now." — the drone stand-ins the engine needs, not species a store could
    sell. `NOLOC` is the files' own mark that a blueprint is never shown to a player,
    so it is what separates them from Slug, Crystal and Lanius, which are real species
    a store simply may not stock.
    """
    systems, dummy_crew = set(), set()
    for name in BLUEPRINT_FILES:
        path = GAMEDATA / name
        if not path.exists():
            continue
        for el in EE.definitions(EE.parse_fragment(path)):
            if not isinstance(el.tag, str) or not el.get("name"):
                continue
            if el.tag == "systemBlueprint":
                systems.add(el.attrib["name"])
            elif el.tag == "crewBlueprint" and el.get("NOLOC") == "1":
                dummy_crew.add(el.attrib["name"])
    return systems, dummy_crew


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

        # Root flags describe the beacon itself rather than an outcome: <distressBeacon/>,
        # <store/> and <environment/> are properties of the stop, not of a branch. They are
        # what the map can mark a beacon with, so they are kept separate from `tags` —
        # and mirrored into `tags` as `distress` / `store-marker`, so a row anywhere on a
        # page can say what the map will show without cross-referencing rollup.markers.
        # Both are computed here, once, which is what keeps the two in step.
        root_flags = doc.get("flags") or {}
        marker = {}
        if root_flags.get("beacon"):
            marker["beacon"] = root_flags["beacon"]
        if root_flags.get("store") or flags["store"]:
            marker["store"] = True
        if root_flags.get("environment"):
            marker["environment"] = root_flags["environment"]

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
        if root_flags.get("unique"):
            tags.append("unique")
        # The two marker tags, derived from the same marker dict the rollup counts, so the
        # per-event tag and rollup.markers can never disagree. `store-marker` is not the
        # `store` tag above: that one means a store opens somewhere in the tree, this one
        # means the beacon is marked as a store on the map, which is the wider set.
        if marker.get("beacon") == "distress":
            tags.append("distress")
        if marker.get("store"):
            tags.append("store-marker")

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
            **({"marker": marker} if marker else {}),
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
        self.systems, self.dummy_crew = blueprint_kinds()
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

    def fallback_events(self):
        """Events the shared fallback list can produce, AE union vanilla.

        `NEUTRAL` fills any beacon left over once a sector's table is exhausted, and
        `OVERRIDE_NEUTRAL` replaces it under Advanced Edition. Both are unioned rather
        than one being chosen: the union is what a beacon on a running game can be,
        and picking a side would mean answering the OVERRIDE_X question per-install.
        """
        ids = []
        for name in ("NEUTRAL", "OVERRIDE_NEUTRAL"):
            for member in self.members(name):
                if member.get("id"):
                    ids.append(member["id"])
        return [self.event_record(i) for i in dict.fromkeys(ids)]

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

    # -- placement ---------------------------------------------------------

    def rank(self, entries):
        """Work out the order the game actually fills these lines in, and what that costs.

        Two rules from the community's reverse-engineering of the generator, both
        recorded in raw/wiki/sectors.md:

        - Every list whose name starts with NEBULA_ is processed **first**, out of file
          order, because the cloud graphics have to be drawn before anything else.
        - Everything else is processed in file order. A line is filled completely before
          the next begins, and when the map runs out of beacons the process simply stops —
          so a line near the bottom may receive nothing at all.

        The map holds at most 24 beacons (a 6x4 grid, each cell 80% likely to hold one).
        The floor is not stated by any source here, so only the ceiling is used: an entry
        is flagged at risk when the lines placed before it could, at their maxima, consume
        the whole map. That is a possibility, not a prediction.
        """
        def nebula_first(entry):
            # Fandom words the rule as "any event list that starts with NEBULA_", but the
            # reason it gives is that the cloud graphics must be drawn before anything
            # else — which applies just as much to the bare NEBULA list. Its own ordered
            # listing for the starting sector confirms it: STANDARD_SPACE's NEBULA line is
            # seventh in sector_data.xml and first in the "proper order" listing.
            return entry["name"] == "NEBULA" or entry["name"].startswith("NEBULA_")

        ordered = ([e for e in entries if nebula_first(e)]
                   + [e for e in entries if not nebula_first(e)])
        before_min = before_max = 0
        for position, entry in enumerate(ordered):
            entry["placement"] = {
                "position": position,
                "nebula_first": nebula_first(entry),
                "before_min": before_min,
                "before_max": before_max,
                # Could get nothing: everything above it, at maxima, fills the map.
                "at_risk": before_max >= GRID_BEACONS,
                # Cannot be satisfied even in the best case: the minima above it plus its
                # own minimum already exceed the map. Hidden Crystal Worlds asks for 25
                # beacons at minimum, so its last line is always short.
                "always_short": before_min + entry["min"] > GRID_BEACONS,
            }
            before_min += entry["min"]
            before_max += entry["max"]
        return ordered

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

        # Keyed by the name a player sees, not by req: WEAPONS_MISSILES and
        # WEAPONS_MISSILES_EVENTS are the same seven weapons under two ids (the AE file
        # redefines the vanilla list), so two rows reading "Missile weapon" would be one
        # option counted twice. Every req that merged in is kept in `reqs`.
        gates = {}
        # `levels` says which levels an option is asked for; it does not say how many
        # events ask for each, so Sensors 2 and Sensors 3 collapse into one row of 7
        # where the page wants two rows of 4 and 5. `levels_detail` is that breakdown,
        # de-duplicated by event id within each level — a count here is always "distinct
        # events that offer it", never a sum, so the same event gated twice at one level
        # still counts once and the rows do not have to add up to `events`.
        #
        # A system gate with no `lvl` folds into level 1: `lvl` is a floor, and a system
        # you merely have is at level 1. A non-system gate — crew, augment, weapon list —
        # has no level to ask for at all and gets a single row with `lvl: null`.
        detail = {}
        for record in events.values():
            for gate in record.get("gates") or []:
                label = GATE_LABELS.get(gate["req"]) or gate.get("label") or gate["req"]
                is_system = gate["req"] in self.systems
                slot = gates.setdefault(label, {"label": label, "reqs": [], "req": gate["req"],
                                                "system": False, "levels": [], "events": []})
                if gate["req"] not in slot["reqs"]:
                    slot["reqs"].append(gate["req"])
                slot["system"] = slot["system"] or is_system
                if gate.get("lvl") and gate["lvl"] not in slot["levels"]:
                    slot["levels"].append(gate["lvl"])
                if record["id"] not in slot["events"]:
                    slot["events"].append(record["id"])
                level = (gate.get("lvl") or "1") if is_system else None
                ids = detail.setdefault(label, {}).setdefault(level, [])
                if record["id"] not in ids:
                    ids.append(record["id"])

        def level_key(level):
            # Levels are numeric strings in every shipped file; anything else sorts by
            # its text rather than being coerced. A null level (non-system) leads.
            if level is None:
                return (0, 0, "")
            return (1, int(level) if level.isdigit() else 0, level)

        for label, rows in detail.items():
            gates[label]["levels_detail"] = [
                {"lvl": level, "events": rows[level]}
                for level in sorted(rows, key=level_key)
            ]

        def tagged(tag):
            return sorted(r["id"] for r in events.values() if tag in (r.get("tags") or []))

        # What the sector's beacons can be marked as, and — the part the allocation table
        # cannot answer — whether the marker agrees with the list an event was allocated from.
        # It does not: ASTEROID_DERELICT_SHIP carries <distressBeacon/> but is allocated from
        # NEUTRAL_*, so a distress beacon in a Rock or Engi sector can be the stasis pod;
        # and several events inside a DISTRESS_BEACON_* list carry no <distressBeacon/> at all.
        distress = sorted(r["id"] for r in events.values()
                          if (r.get("marker") or {}).get("beacon") == "distress")
        allocated = sorted({r["id"] for entry in entries
                            if entry["name"].startswith("DISTRESS_BEACON")
                            for r in entry["events"]})
        environments = {}
        for record in events.values():
            kind = (record.get("marker") or {}).get("environment")
            if kind:
                environments.setdefault(kind, []).append(record["id"])
        markers = {
            "distress": {
                "events": distress,
                "allocation_entries": sorted({e["name"] for e in entries
                                              if e["name"].startswith("DISTRESS_BEACON")}),
                "marked_outside_allocation": [i for i in distress if i not in allocated],
                "allocated_but_unmarked": [i for i in allocated if i not in set(distress)],
            },
            "store": sorted(r["id"] for r in events.values()
                            if (r.get("marker") or {}).get("store")),
            "environment": {k: sorted(v) for k, v in sorted(environments.items())},
        }

        return {
            "markers": markers,
            "distinct_events": len(events),
            "no_card": sorted(r["id"] for r in events.values() if not r.get("card")),
            "always_fight": tagged("fight"),
            "may_fight": tagged("may-fight"),
            "crew_loss": tagged("crew-loss"),
            "crew_gain": tagged("crew"),
            "boarders": tagged("boarders"),
            "unique": tagged("unique"),
            "quest_starts": tagged("quest"),
            "gates": sorted(gates.values(), key=lambda g: (-len(g["events"]), g["label"].lower())),
            "named_items": collect("items"),
            "crew_classes": collect("crew_classes"),
            "unlock_ships": collect("unlock_ship"),
            "quest_targets": collect("quests"),
        }

    def metrics(self, entries, rollup, rarity, crew_odds):
        """Every number a stat tile is allowed to show, precomputed and named.

        The page's copy picks tiles by metric id and supplies only the label, so a
        number on a sector page can never be typed by hand.
        """
        shifted = [r for r in rarity if r["change"] not in ("same", "unknown")]
        out = {
            "blue_options": len(rollup["gates"]),
            "blue_option_hits": sum(len(g["events"]) for g in rollup["gates"]),
            "store_rarity_changes": len(shifted),
            "crew_rarity_changes": sum(1 for r in shifted if r["crew"]),
            "crew_types_sold": len(crew_odds),
            "grid_beacons": GRID_BEACONS,
            "at_risk_entries": sum(1 for e in entries if e["placement"]["at_risk"]),
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

        # File order is kept, because it IS the placement order: the game fills a line
        # completely, moves to the next, and stops the moment the map runs out of beacons.
        # Sorting these into reading order — which this extractor used to do — throws away
        # the single most useful thing the table says. See SECTOR-PAGE.md §4.2.
        entries = []
        for index, child in enumerate(el):
            if isinstance(child.tag, str) and child.tag == "event" and child.get("name"):
                entry = self.entry(child)
                entry["order"] = len(entries)
                entries.append(entry)
        self.rank(entries)

        tracks = [t.text.strip() for t in el.findall("trackList/track") if t.text]
        rarity = []
        for bp in el.findall("rarityList/blueprint"):
            name = bp.get("name")
            here = int(bp.get("rarity", 0) or 0)
            base = self.idx.blueprint_rarity.get(name)
            rarity.append({
                "id": name,
                "label": self.idx.blueprint_titles.get(name) or name.title(),
                "crew": name in self.idx.crew_blueprints,
                "rarity": here,
                "base": base,
                "change": rarity_change(base, here),
            })

        # What a store here can actually sell, and how often. The engine builds its candidate
        # list from every crewBlueprint whose effective rarity is non-zero and weights each
        # one 6 - rarity, then draws one per slot -- read out of FTLGame_orig.exe, see
        # raw/modding/2026-08-16-store-crew-selection-disassembly.md. Effective rarity is the
        # sector's value where it names the species and the blueprint's base otherwise:
        # ResetRarities() restores base on sector entry and SetRarity() writes only the names
        # the sector lists, so an unlisted species keeps its base value.
        here = {r["id"]: r["rarity"] for r in rarity}
        crew_odds = []
        # The other side of the same filter: a species whose effective rarity here is
        # exactly 0 is not in the pool at all, so a store in this sector can never offer
        # it. Emitted beside the candidates so a page can show it without reading XML.
        # Rarity 0 is a flag, not a low value (wiki/concepts/blueprint-rarity.md), which
        # is why this is `== 0` and not "smallest". A species the files give no <rarity>
        # at all would be unknown rather than excluded, and is listed in neither.
        excluded = []
        for name in sorted(self.idx.crew_blueprints):
            value = here.get(name, self.idx.blueprint_rarity.get(name))
            if not value:  # 0 or unknown -- filtered out before weighting
                if value == 0 and name not in self.dummy_crew:
                    excluded.append({"id": name,
                                     "label": self.idx.blueprint_titles.get(name) or name.title()})
                continue
            crew_odds.append({
                "id": name,
                "label": self.idx.blueprint_titles.get(name) or name.title(),
                "rarity": value,
                "listed": name in here,
                "weight": CREW_WEIGHT_BASE - value,
            })
        total_weight = sum(c["weight"] for c in crew_odds)
        for crew in crew_odds:
            share = crew["weight"] / total_weight
            crew["share"] = round(share * 100, 1)
            # Three slots, each an independent count=1 draw, so a species can repeat.
            crew["in_store"] = round((1 - (1 - share) ** CREW_SLOTS) * 100, 1)
        crew_odds.sort(key=lambda c: (-c["weight"], c["label"].lower()))
        excluded.sort(key=lambda c: c["label"].lower())

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
            # minSector is zero-indexed: ENGI_HOME's 2 is Fandom's "sector 3 or higher",
            # and the +1 offset holds for every unique sector both sources describe.
            # The raw value is kept above; this is the number a player counts in.
            "earliest_sector": int(el.get("minSector", 0) or 0) + 1,
            "unique": el.get("unique") == "true",
            "tracks": tracks,
            "crew_rarity": rarity,
            "crew_store_odds": {"slots": CREW_SLOTS, "total_weight": total_weight,
                                "crew": crew_odds, "excluded": excluded},
            "start_event": self.event_record(start) if start else None,
            "entries": entries,
            "generation": {
                "grid_beacons": GRID_BEACONS,
                "grid_beacons_min": GRID_BEACONS_MIN,
                "allocated_min": sum(e["min"] for e in entries),
                "allocated_max": sum(e["max"] for e in entries),
                # More slots than the map can hold means the bottom of the table is a
                # wish list, not a guarantee.
                "can_exhaust_map": sum(e["max"] for e in entries) > GRID_BEACONS,
                "at_risk_entries": [e["name"] for e in entries if e["placement"]["at_risk"]],
                "always_short_entries": [e["name"] for e in entries
                                         if e["placement"]["always_short"]],
                "cannot_meet_minimum": sum(e["min"] for e in entries) > GRID_BEACONS,
                "nebula_first": [e["name"] for e in entries if e["placement"]["nebula_first"]],
                "fallback_list": "NEUTRAL",
                "fallback_list_ae": "OVERRIDE_NEUTRAL",
                # The events the fallback can actually produce. Every sector reaches
                # this list -- a beacon left over after the table is exhausted draws
                # from it -- but most sectors never name it in sector_data.xml, so
                # without this it is the one pool a consumer cannot see. Emitted as
                # event records so downstream can treat it like any other pool.
                "fallback_events": self.fallback_events(),
                # How many beacons the fallback can actually be asked to fill here. The
                # table never states this -- it is the gap the table leaves -- but those
                # beacons are as real as any allocated one, so the budget has to show it.
                #   max: a full map minus the smallest total the table can roll. A sector
                #        whose minima already cover the map leaves nothing, and clamps to 0
                #        (Hidden Crystal Worlds, 25 against 24).
                #   min: the smallest map minus the largest total the table can roll --
                #        what the fallback fills even on a bad roll. 0 for every shipped
                #        sector; computed rather than assumed, because a mod can change it.
                #   on_full_map: what it must fill when the grid comes out at 24. The Last
                #        Stand is the one sector where this is non-zero.
                "fallback_beacons": {
                    "min": max(0, GRID_BEACONS_MIN - sum(e["max"] for e in entries)),
                    "max": max(0, GRID_BEACONS - sum(e["min"] for e in entries)),
                    "on_full_map": max(0, GRID_BEACONS - sum(e["max"] for e in entries)),
                },
                "exit_list": "EXIT_LIST",
                "source": "raw/wiki/sectors.md",
            },
            "rollup": rollup,
            "metrics": self.metrics(entries, rollup, rarity, crew_odds),
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
