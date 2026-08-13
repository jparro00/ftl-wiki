#!/usr/bin/env python3
"""Extract an event tree from raw/gamedata into ftl-event-tree/1 JSON.

    python tools/extract-event.py AUTO_CIVILIAN
    python tools/extract-event.py STRANDED_BEACON --slug single-life-form-on-moon

Reads the shipped XML only. Every string in the output is either verbatim from
raw/gamedata/text_events.xml or a structural value from the event files — nothing
is paraphrased here, and nothing is invented. Where the files state no weights,
the emitted odds_basis is "unweighted" and no share is written.

The event XML files are fragments (many roots, and <!--DLC--> comments that carry
meaning), so they are wrapped in a synthetic root and parsed with comments kept.
"""

import argparse
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
GAMEDATA = ROOT / "raw" / "gamedata"
SCHEMA = "ftl-event-tree/1"

# Load order mirrors the game's: base first, DLC overwrites last, so later
# definitions win in the index.
EVENT_FILES = [
    "events.xml", "events_boss.xml", "events_crystal.xml", "events_engi.xml",
    "events_fuel.xml", "events_mantis.xml", "events_nebula.xml", "events_pirate.xml",
    "events_rebel.xml", "events_rock.xml", "events_ships.xml", "events_slug.xml",
    "events_zoltan.xml", "newEvents.xml", "nameEvents.xml", "bosses.xml",
    "dlcEvents.xml", "dlcEvents_anaerobic.xml", "dlcEventsOverwrite.xml",
]

MAX_DEPTH = 24  # backstop; the deepest real tree is far shallower

# Branch prose the developers left as a marker rather than an outcome. GHOST_SHIP's
# deadCrew reads exactly this, on a hull that declares crew, so the crewCount rule in
# §4.4 cannot catch it.
PLACEHOLDER_TEXTS = {"should not be seen"}


def parse_fragment(path: pathlib.Path):
    """Parse a multi-root XML fragment, keeping comments (they mark DLC content)."""
    raw = path.read_text(encoding="utf-8", errors="replace").lstrip("﻿")
    raw = re.sub(r"^\s*<\?xml[^>]*\?>", "", raw)  # declaration cannot follow our root
    raw = raw.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    parser.feed("<ftlroot>")
    parser.feed(raw)
    parser.feed("</ftlroot>")
    return parser.close()


def definitions(root):
    """Top-level definitions, descending through the files' <FTL> wrapper."""
    for el in root:
        if isinstance(el.tag, str) and el.tag.upper() == "FTL":
            yield from el
        else:
            yield el


class Index:
    """Every named definition in the event files, plus the text table."""

    def __init__(self):
        self.events, self.lists, self.ships, self.text_lists, self.provenance = {}, {}, {}, {}, {}
        self.text = {}

        for name in EVENT_FILES:
            path = GAMEDATA / name
            if not path.exists():
                continue
            for el in definitions(parse_fragment(path)):
                if not isinstance(el.tag, str) or "name" not in el.attrib:
                    continue
                key = el.attrib["name"]
                bucket = {
                    "event": self.events, "eventList": self.lists,
                    "ship": self.ships, "textList": self.text_lists,
                }.get(el.tag)
                if bucket is not None:
                    bucket[key] = el
                    self.provenance[(el.tag, key)] = name

        for f in ("text_events.xml", "text_misc.xml"):
            if not (GAMEDATA / f).exists():
                continue
            for el in definitions(parse_fragment(GAMEDATA / f)):
                if isinstance(el.tag, str) and el.tag == "text" and "name" in el.attrib:
                    self.text.setdefault(el.attrib["name"], (el.text or "").strip())

        # A req= often names a blueprint (BEAM_BIO, BATTLE, ADV_SCANNERS) rather than a
        # system. Those carry the in-game title the player sees, so resolve it here
        # instead of maintaining a hand-written label per gate.
        strings = {}
        for f in ("text_blueprints.xml",):
            if (GAMEDATA / f).exists():
                for el in definitions(parse_fragment(GAMEDATA / f)):
                    if isinstance(el.tag, str) and el.tag == "text" and "name" in el.attrib:
                        strings[el.attrib["name"]] = (el.text or "").strip()

        self.blueprint_titles = {}
        # A <ship auto_blueprint="X"> naming a single shipBlueprint carries the class
        # name the player sees ("Energy Fighter"); a blueprintList has no single name.
        self.ship_classes = {}
        self.ship_crew = {}
        self.blueprint_lists = {}
        for f in ("blueprints.xml", "dlcBlueprints.xml", "dlcPirateBlueprints.xml",
                  "autoBlueprints.xml", "dlcBlueprintsOverwrite.xml"):
            if not (GAMEDATA / f).exists():
                continue
            for el in definitions(parse_fragment(GAMEDATA / f)):
                if not isinstance(el.tag, str) or not (
                    el.tag.endswith("Blueprint") or el.tag == "blueprintList"
                ):
                    continue
                name = el.attrib.get("name")
                if el.tag == "blueprintList":
                    self.blueprint_lists[name] = [n.text.strip() for n in el.findall("name") if n.text]
                    continue
                if el.tag == "shipBlueprint":
                    crew = el.find("crewCount")
                    if crew is not None:
                        self.ship_crew[name] = max(
                            int(crew.attrib.get("amount", 0) or 0),
                            int(crew.attrib.get("max", 0) or 0),
                        )
                    cls = el.find("class")
                    if cls is not None:
                        value = strings.get(cls.get("id"), "") if cls.get("id") else (cls.text or "")
                        if value.strip():
                            self.ship_classes[name] = collapse(value)
                    continue
                title = el.find("title")
                if title is None:
                    continue
                value = strings.get(title.get("id"), "") if title.get("id") else (title.text or "")
                if value.strip():
                    self.blueprint_titles[name] = collapse(value)

    def where(self, kind, name):
        return self.provenance.get((kind, name))

    def crewless(self, auto_blueprint):
        """True when every hull this ship can draw declares zero crew.

        <crewCount amount="0" max="0"/> on the blueprint is the game stating that an
        automated ship carries nobody, which makes its deadCrew branch unreachable.
        Unknown blueprints answer False — absence of data is not evidence.
        """
        candidates = [auto_blueprint] if auto_blueprint in self.ship_crew else (
            self.blueprint_lists.get(auto_blueprint) or []
        )
        counts = [self.ship_crew.get(c) for c in candidates]
        return bool(counts) and all(c == 0 for c in counts)

    def ship_label(self, auto_blueprint):
        """The class name(s) a <ship auto_blueprint=…> can present to the player.

        A single shipBlueprint has one class name. A blueprintList can hold several
        distinct ones (SHIPS_ZOLTAN is an Energy Fighter or an Energy Bomber), so the
        honest answer is all of them; the card joins them.
        """
        if not auto_blueprint:
            return {}
        single = self.ship_classes.get(auto_blueprint)
        if single:
            return {"ship_label": single}
        members = self.blueprint_lists.get(auto_blueprint) or []
        names, seen = [], set()
        for m in members:
            cls = self.ship_classes.get(m)
            if cls and cls not in seen:
                seen.add(cls)
                names.append(cls)
        if len(names) == 1:
            return {"ship_label": names[0]}
        if 2 <= len(names) <= 3:
            return {"ship_labels": names}
        return {}


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def dlc_marked(parent, child):
    """A <!--DLC--> comment immediately after an element marks it AE-only."""
    kids = list(parent)
    try:
        i = kids.index(child)
    except ValueError:
        return False
    for sib in kids[i + 1:i + 2]:
        if not isinstance(sib.tag, str) and "DLC" in (sib.text or "").upper():
            return True
    return False


def dlc_first_child(el):
    """A <!--DLC--> comment as an element's first child marks the element itself.

    `<choice req="LIFE_SCANNER"><!--DLC--> …` uses this placement; 11 markers across
    raw/gamedata/ are written this way and were missed while only siblings were checked.
    """
    for child in list(el)[:1]:
        if not isinstance(child.tag, str) and "DLC" in (child.text or "").upper():
            return True
    return False


def text_of(el, idx):
    """Resolve <text id=…/>, inline <text>…</text>, or <text load="LIST"/>."""
    node = el.find("text")
    if node is None:
        return None, None, 1
    if "id" in node.attrib:
        ref = node.attrib["id"]
        return collapse(idx.text.get(ref, "")) or None, ref, 1
    if "load" in node.attrib:
        ref = node.attrib["load"]
        lst = idx.text_lists.get(ref)
        if lst is not None:
            variants = [collapse(idx.text.get(t.get("id"), "") if t.get("id") else (t.text or ""))
                        for t in lst.findall("text")]
            variants = [v for v in variants if v]
            return (variants[0] if variants else None), ref, len(variants)
        return None, ref, 1
    return collapse(node.text or "") or None, None, 1


def effects_of(el, idx):
    """The closed set of effect tags, as typed records."""
    out = []
    for c in el:
        if not isinstance(c.tag, str):
            continue
        a, tag = c.attrib, c.tag
        dlc = dlc_marked(el, c) or dlc_first_child(c)

        def rec(**kw):
            e = dict(kw)
            if dlc:
                e["dlc"] = True
            out.append(e)

        if tag == "autoReward":
            rec(kind="reward", level=a.get("level", "RANDOM"), tier=collapse(c.text or "standard"))
        elif tag == "item_modify":
            for item in c.findall("item"):
                ia = item.attrib
                rec(kind="resource", resource=ia.get("type"),
                    min=int(ia.get("min", 0)), max=int(ia.get("max", 0)))
        elif tag == "crewMember":
            # amount is signed: <crewMember amount="-1" class="traitor"/> takes a crew
            # member away. The sign is kept here and read by the renderer.
            e = {"kind": "crew_gain", "amount": int(a.get("amount", 1))}
            if a.get("class"):
                e["class"] = a["class"]
            if a.get("all_skills"):
                e["all_skills"] = int(a["all_skills"])
            if a.get("id", "").startswith("name_"):
                e["name"] = a["id"][len("name_"):]
            skills = {k: int(v) for k, v in a.items()
                      if k in ("pilot", "engines", "shields", "weapons", "repair", "combat")}
            if skills:
                e["skills"] = skills
            rec(**e)
        elif tag == "removeCrew":
            cl = c.find("clone")
            # <clone>false</clone> exists and means the opposite of <clone>true</clone>;
            # testing presence alone promised a revive the game explicitly refuses.
            rec(kind="crew_loss", amount=1,
                clone=cl is not None and (cl.text or "").strip().lower() != "false",
                **({"class": a["class"]} if a.get("class") else {}))
        elif tag == "damage":
            amount = int(a.get("amount", 0))
            if a.get("system"):
                if amount:
                    rec(kind="system_damage", amount=amount, system=a["system"])
            elif amount < 0:
                rec(kind="hull_repair", amount=-amount)
            else:
                rec(kind="hull_damage", amount=amount)
            # effect="fire"/"breach"/… is a second payload, not a modifier on the damage
            if a.get("effect"):
                rec(kind="hazard", hazard=a["effect"])
        elif tag == "boarders":
            rec(kind="boarders", min=int(a.get("min", 1)), max=int(a.get("max", 1)),
                **({"class": a["class"]} if a.get("class") else {}))
        elif tag in ("augment", "weapon", "drone"):
            # An awarded blueprint has a display name, same as a gate does — resolve it
            # here so the card never shows a raw id like ROCK_ARMOR for "Rock Plating".
            item_id = a.get("name")
            # <weapon name="WEAPONS_CRYSTAL"/> names a blueprintList, not a blueprint: the
            # game rolls one member. Flag it so the card says so instead of printing the id.
            rec(kind="item", item_kind=tag, id=item_id,
                label=idx.blueprint_titles.get(item_id) or item_id,
                **({"from_list": True} if item_id in idx.blueprint_lists
                   and item_id not in idx.blueprint_titles else {}))
        elif tag == "upgrade":
            rec(kind="upgrade", system=a.get("system"), amount=int(a.get("amount", 1)))
        elif tag == "status":
            rec(kind="status", status=a.get("type"), target=a.get("target") or "player",
                system=a.get("system"), amount=int(a.get("amount", 0)))
        elif tag == "quest":
            rec(kind="quest", event=a.get("event"))
        elif tag == "unlockShip":
            rec(kind="unlock_ship", id=a.get("id"))
        elif tag == "modifyPursuit":
            rec(kind="fleet_delay", amount=int(a.get("amount", 0)))
        elif tag == "reveal_map":
            rec(kind="reveal_map")
        elif tag == "repair":
            rec(kind="repair_all")
        elif tag == "remove":
            removed = a.get("name")
            rec(kind="remove_augment", id=removed,
                label=idx.blueprint_titles.get(removed) or removed)
        elif tag == "secretSector":
            rec(kind="secret_sector")
        elif tag == "store":
            rec(kind="store")
        elif tag == "environment":
            # Also recorded in flags; emitted as an effect so the row can say the fight
            # happens inside a hazard.
            rec(kind="environment", environment=a.get("type"),
                target=a.get("target") or "player")
        elif tag == "ship" and not (a.get("load") or a.get("name")):
            # A bare <ship hostile="true"/> does not introduce a ship — it flips the
            # one already at the beacon. 96 uses; whose outcomes are the parent
            # event's ship branches, so this records the flip as an effect.
            rec(kind="ship_hostility", hostile=a.get("hostile") == "true")
    return out


def flags_of(el):
    f = {}
    if el.get("unique"):
        f["unique"] = el.attrib["unique"] == "true"
    if el.find("distressBeacon") is not None:
        f["beacon"] = "distress"
    if el.find("store") is not None:
        f["store"] = True
    env = el.find("environment")
    if env is not None:
        f["environment"] = env.attrib.get("type")
        f["environment_target"] = env.attrib.get("target") or "player"
    return f


def gate_of(choice, idx):
    a = choice.attrib
    if "req" not in a:
        return None
    g = {"req": a["req"]}
    title = idx.blueprint_titles.get(a["req"])
    if title:
        g["label"] = title
    for k in ("lvl", "max_lvl", "min_level", "max_group", "blue"):
        if k in a:
            g[k] = a[k]
    return g


class Extractor:
    def __init__(self, idx):
        self.idx = idx

    def event(self, el, stack, depth, name=None):
        """One <event> element → an event record: text, effects, and one node."""
        idx = self.idx
        # An entry may delegate wholesale: <event load="GHOST_BOARDING"/>. Only choices
        # used to be checked for this, so list entries collapsed to an empty record.
        if el.get("load") and len(el) == 0:
            return self.load(el.attrib["load"], stack, depth)
        value, ref, variants = text_of(el, idx)
        rec = {}
        if value:
            rec["text"] = {"value": value, **({"ref": ref} if ref else {}),
                           **({"variants": variants} if variants > 1 else {})}
        if name:
            rec["name"] = name
            src = idx.where("event", name)
            if src:
                rec["source"] = f"raw/gamedata/{src}"

        if dlc_first_child(el):
            rec["dlc"] = True
        rec["effects"] = effects_of(el, idx)
        flags = flags_of(el)
        if flags:
            rec["flags"] = flags

        node = self.node(el, stack, depth)
        if node:
            rec["node"] = node
        return rec

    def load(self, target, stack, depth):
        """An <event load="X"/> — X is either an eventList (chance) or an event."""
        idx = self.idx
        if target in stack or depth > MAX_DEPTH:
            return {"node": {"kind": "ref", "target": target}}

        if target in idx.lists:
            return {"effects": [], "node": self.chance(target, stack, depth)}
        if target in idx.events:
            return self.event(idx.events[target], stack | {target}, depth + 1, name=target)
        return {"effects": [], "node": {"kind": "ref", "target": target, "unresolved": True}}

    def chance(self, name, stack, depth):
        lst = self.idx.lists[name]
        entries = [e for e in lst if isinstance(e.tag, str) and e.tag == "event"]
        src = self.idx.where("eventList", name)
        return {
            "kind": "chance",
            "list": name,
            **({"dlc": True} if dlc_first_child(lst) else {}),
            "source": f"raw/gamedata/{src}" if src else None,
            # No entry in the shipped files carries a weight attribute.
            "odds_basis": "unweighted" if not any("prop" in e.attrib for e in entries) else "file-weight",
            "options": [
                {"share": e.attrib.get("prop"),
                 **({"dlc": True} if dlc_marked(lst, e) or dlc_first_child(e) else {}),
                 "child": self.event(e, stack | {name}, depth + 1)}
                for e in entries
            ],
        }

    def node(self, el, stack, depth):
        """Continuation: decision, combat, or terminal.

        An event can carry both — ROCK_UNLOCK1 puts a ship at the beacon *and*
        offers a menu. Treating them as exclusive drops one of them, so a decision
        that also has a ship keeps it under `combat`.
        """
        ship = el.find("ship")
        combat = None
        if ship is not None and (ship.get("load") or ship.get("name")):
            combat = self.combat(ship, stack, depth)

        choices = [c for c in el if isinstance(c.tag, str) and c.tag == "choice"]
        if not choices and combat and ship.get("hostile") != "true":
            # No menu at all, so nothing here can flip it. The guard used to live only on
            # the decision path, which let choice-less events render phantom fights.
            flips = any(isinstance(c.tag, str) and c.tag == "ship"
                        and not (c.get("load") or c.get("name"))
                        and c.get("hostile") == "true" for c in el)
            if not flips:
                combat["reachable"] = False
                combat["unreachable_because"] = "nothing in this event turns the ship hostile"
        if not choices:
            # <event><text/><event load="GHOST_SPACE"/>…</event> — the inner event is what
            # happens next. Represented as a one-option sequence so it renders as "Then".
            nested = [c for c in el if isinstance(c.tag, str) and c.tag == "event"]
            if nested:
                inner = nested[0]
                child = (self.load(inner.attrib["load"], stack, depth + 1)
                         if inner.get("load") and len(inner) == 0
                         else self.event(inner, stack, depth + 1))
                seq = {"kind": "sequence", "options": [{"label": None, "child": child}]}
                if combat:
                    seq["combat"] = combat
                return seq
            return combat

        options = []
        for c in choices:
            label, label_ref, _ = text_of(c, self.idx)
            inner = c.find("event")
            if inner is None:
                child = {"effects": []}
            elif inner.get("load"):
                child = self.load(inner.attrib["load"], stack, depth + 1)
            else:
                child = self.event(inner, stack, depth + 1)
            own = effects_of(c, self.idx)          # payload attached to the choice itself
            if own:
                child = dict(child)
                child["effects"] = own + (child.get("effects") or [])
            opt = {"label": label, "gate": gate_of(c, self.idx), "child": child}
            if label_ref:
                opt["label_ref"] = label_ref
            if c.get("hidden"):
                opt["hidden"] = c.attrib["hidden"] == "true"
            if (dlc_first_child(c) or dlc_marked(el, c)
                    or (dlc_marked(c, inner) if inner is not None else False)):
                opt["dlc"] = True
            options.append(opt)
        decision = {"kind": "decision", "options": options}
        if combat:
            # A ship parked at the beacon and never turned hostile by any option in
            # this event cannot be fought through the menu. Its branches stay in the
            # record, marked, rather than being presented as something reachable.
            if ship.get("hostile") != "true" and not turns_hostile(decision):
                combat["reachable"] = False
                combat["unreachable_because"] = "no option in this event turns the ship hostile"
            decision["combat"] = combat
        return decision

    def combat(self, ship_el, stack, depth):
        name = ship_el.get("load") or ship_el.get("name")
        defn = self.idx.ships.get(name)
        if defn is None:
            return {"kind": "combat", "ship": name, "branches": [], "unresolved": True}

        branches = []
        for on, sub in ((t, e) for t in ("destroyed", "deadCrew", "surrender", "escape", "gotaway")
                        for e in defn.findall(t)):
            if sub is None:
                continue
            b = {"on": on, "child": self.event(sub, stack | {name}, depth + 1)}
            body = ((b["child"].get("text") or {}).get("value") or "").strip().lower()
            if body in PLACEHOLDER_TEXTS:
                b["reachable"] = False
                b["unreachable_because"] = "the branch text is a developer placeholder"
            if on == "deadCrew" and self.idx.crewless(defn.get("auto_blueprint")):
                b["reachable"] = False
                b["unreachable_because"] = "the ship blueprint declares no crew"
            for attr in ("chance", "min", "max"):
                if attr in sub.attrib:
                    b[attr] = sub.attrib[attr]
            if sub.get("load"):
                b["child"] = self.load(sub.attrib["load"], stack | {name}, depth + 1)
            branches.append(b)

        src = self.idx.where("ship", name)
        label = self.idx.ship_label(defn.get("auto_blueprint"))
        return {
            "kind": "combat",
            "ship": name,
            **label,
            "hostile": ship_el.get("hostile") == "true",
            "auto_blueprint": defn.get("auto_blueprint"),
            "source": f"raw/gamedata/{src}" if src else None,
            "branches": branches,
        }


PAGE_TITLE = re.compile(r"^#\s+(.*?)\s+—\s+`[A-Z0-9_]+`\s*$")
PAGE_ID = re.compile(r"^event_name:\s*(\S+)\s*$", re.MULTILINE)


def page_index():
    """event id → (slug, title), read from the wiki pages.

    The game files carry no human title — FTL never shows the player an event
    name — but every wiki/events/*.md page declares the id it documents in its
    frontmatter, and its H1 is "<Title> — `ID`". That join makes both fields data
    rather than arguments. A title may itself contain an em dash, so only the
    trailing backticked id is stripped.
    """
    index = {}
    pages = ROOT / "wiki" / "events"
    if not pages.is_dir():
        return index
    for path in sorted(pages.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        found = PAGE_ID.search(text)
        if not found:
            continue
        title = None
        for line in text.splitlines():
            if line.startswith("# "):
                m = PAGE_TITLE.match(line.strip())
                title = m.group(1) if m else line[2:].strip()
                break
        index[found.group(1)] = (path.stem, title or path.stem.replace("-", " ").capitalize())
    return index


def turns_hostile(record):
    """True if anything under this record flips the beacon's ship hostile."""
    for e in record.get("effects") or []:
        if e.get("kind") == "ship_hostility" and e.get("hostile"):
            return True
    node = record if record.get("kind") else (record.get("node") or {})
    children = [o.get("child") for o in (node.get("options") or [])]
    children += [b.get("child") for b in (node.get("branches") or [])]
    return any(isinstance(c, dict) and turns_hostile(c) for c in children)


def quest_targets(record, out):
    """Every <quest event="X"/> reachable inside one extracted event record.

    A quest effect does not resolve at this beacon — it marks a destination the
    player flies to later. Those stages are collected as a separate chain rather
    than nested into the tree, because they are a different encounter.
    """
    for e in record.get("effects") or []:
        if e.get("kind") == "quest" and e.get("event") and e["event"] not in out:
            out.append(e["event"])
    node = record.get("node") or {}
    combat = node.get("combat") or {}
    children = [o.get("child") for o in (node.get("options") or [])]
    children += [b.get("child") for b in (node.get("branches") or [])]
    children += [b.get("child") for b in (combat.get("branches") or [])]
    for c in children:
        if isinstance(c, dict):
            quest_targets(c, out)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("event", help="in-game event name, e.g. AUTO_CIVILIAN")
    ap.add_argument("--slug", help="override the slug (default: from the wiki page for this event id)")
    ap.add_argument("--title", help="override the title (default: from the wiki page H1)")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output .tree.json")
    args = ap.parse_args()

    idx = Index()
    if args.event not in idx.events:
        sys.exit(f"{args.event}: no <event name=…> with that name in raw/gamedata")

    pages = page_index()
    page_slug, page_title = pages.get(args.event, (None, None))
    slug = args.slug or page_slug or args.event.lower().replace("_", "-")
    title = args.title or page_title or slug.replace("-", " ").capitalize()

    ex = Extractor(idx)
    root = ex.event(idx.events[args.event], {args.event}, 0, name=args.event)

    # Follow quest markers breadth-first: a stage can hand out another marker
    # (MERCHANT_INVESTIGATE → MERCHANT_INVESTIGATE_DELIVER), and a target may be an
    # event or an event list — load() resolves either.
    chain, seen, frontier = [], {args.event}, [(args.event, root)]
    while frontier:
        parent, record = frontier.pop(0)
        for target in quest_targets(record, []):
            if target in seen:
                chain.append({"id": target, "from": parent, "repeat": True})
                continue
            seen.add(target)
            stage_slug, stage_title = pages.get(target, (None, None))
            stage = {
                "id": target, "from": parent,
                **({"slug": stage_slug} if stage_slug else {}),
                **({"title": stage_title} if stage_title else {}),
                **ex.load(target, set(), 0),
            }
            chain.append(stage)
            frontier.append((target, stage))

    doc = {
        "schema": SCHEMA,
        "id": args.event,
        "slug": slug,
        "title": title,
        "extracted_from": f"raw/gamedata/{idx.where('event', args.event)}",
        **root,
        **({"chain": chain} if chain else {}),
    }

    # Trees live beside the cards they build, not in wiki/: they are generated data, and
    # keeping them out of the wiki layer keeps wiki searches free of machine output.
    out = args.out or ROOT / "cards" / "trees" / f"{slug}.tree.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
