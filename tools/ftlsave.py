"""Read-only parser for FTL's `continue.sav`, as far as the current encounter.

Port of Vhati/ftl-profile-editor, src/main/java/net/blerf/ftl/parser/SavedGameParser.java
(`readSavedGame` and its sub-readers) plus DatParser.readLayout for the ship layout
grammar. Those two files are the normative format spec; every field order and every
version conditional below is copied from them, not inferred from bytes.

Scope is deliberate: the parse stops at `EncounterState`, which is all a caller needs
to know which event is on screen. Everything after the encounter -- nearby ship,
projectiles, environment -- is left unread. That is not laziness, it is what makes
this work at all: FTL 1.6.14 saves carry a projectile type flag (6) that the
reference parser rejects outright (ftl-profile-editor issue #119), and every one of
those bytes sits *after* the encounter block.

Layout data (room count, room square dimensions, door ordering) is not in the save;
it is read live from the game's `ftl.dat` via ftlpkg. Ship blueprints (layout id and
multi-room system counts) come from this repo's immutable `raw/gamedata/`.

All integers are 4-byte little-endian signed. Strings are a length int followed by
that many bytes, UTF-8 in file format 11 (FTL 1.6.1+).

Usage:
  python ftlsave.py <continue.sav> [--ftl-dat PATH] [--json]
"""

import argparse
import json
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ftlpkg

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAMEDATA = os.path.join(REPO, "raw", "gamedata")

# Blueprint files that can define a <shipBlueprint>. Later files win, matching the
# game's load order -- the same rule tools/extract-event.py applies to events.
BLUEPRINT_FILES = [
    "blueprints.xml",
    "autoBlueprints.xml",
    "dlcBlueprints.xml",
    "dlcBlueprintsOverwrite.xml",
    "dlcPirateBlueprints.xml",
]

# System order on disk, from SavedGameParser.readShip. The first twelve are present
# in every format; the last four arrived with FTL 1.5.4 (formats 7, 8, 9, 11). The
# names are the <systemList> child tag names in blueprints.xml, which is how we count
# how many rooms hold each system.
SYSTEM_TYPES_BASE = [
    "shields", "engines", "oxygen", "weapons", "drones", "medbay",
    "pilot", "sensors", "doors", "teleporter", "cloaking", "artillery",
]
SYSTEM_TYPES_AE = ["battery", "clonebay", "mind", "hacking"]

ADVANCED_FORMATS = (7, 8, 9, 11)


class SaveFormatError(Exception):
    """The save did not match the documented layout."""


class Reader:
    """Sequential cursor over the save bytes."""

    def __init__(self, data, unicode_strings):
        self.data = data
        self.pos = 0
        self.unicode = unicode_strings

    def int(self):
        if self.pos + 4 > len(self.data):
            raise SaveFormatError("ran off the end of the file reading an int")
        (v,) = struct.unpack_from("<i", self.data, self.pos)
        self.pos += 4
        return v

    def bool(self):
        v = self.int()
        if v not in (0, 1):
            raise SaveFormatError("not a bool: %d (at offset %d)" % (v, self.pos - 4))
        return v == 1

    def string(self):
        length = self.int()
        if length < 0 or self.pos + length > len(self.data):
            raise SaveFormatError(
                "string length %d at offset %d would run past the end"
                % (length, self.pos - 4)
            )
        raw = self.data[self.pos:self.pos + length]
        self.pos += length
        return raw.decode("utf-8" if self.unicode else "latin-1")

    def skip_ints(self, n):
        for _ in range(n):
            self.int()


# --------------------------------------------------------------------------
# Game data the save format depends on
# --------------------------------------------------------------------------

def load_layout(ftl_dat, layout_id):
    """Return (rooms, doors) for a ship layout, read from ftl.dat.

    rooms: list of (squaresH, squaresV) in roomId order.
    doors: list of (roomIdA, roomIdB) in the order they appear in the file.

    Grammar per DatParser.readLayout: a keyword line followed by its fields, one per
    line. ROOM is roomId/x/y/hSquares/vSquares; DOOR is x/y/roomIdA/roomIdB/vertical.
    """
    inner = "data/%s.txt" % layout_id
    with open(ftl_dat, "rb") as fh:
        entries, _, _ = ftlpkg.read_index(fh)
        match = next((e for e in entries if e.path == inner), None)
        if match is None:
            raise SaveFormatError("no layout %r in %s" % (inner, ftl_dat))
        text = ftlpkg.read_data(fh, match).decode("utf-8", "replace")

    lines = [ln.strip() for ln in text.splitlines()]
    rooms_by_id = {}
    doors = []
    i = 0
    while i < len(lines):
        token = lines[i]
        if token == "ROOM":
            room_id, _x, _y, h, v = (int(lines[i + k]) for k in range(1, 6))
            rooms_by_id[room_id] = (h, v)
            i += 6
        elif token == "DOOR":
            _x, _y, room_a, room_b, _vertical = (int(lines[i + k]) for k in range(1, 6))
            doors.append((room_a, room_b))
            i += 6
        else:
            i += 1

    if not rooms_by_id:
        raise SaveFormatError("layout %s declared no rooms" % layout_id)
    rooms = [rooms_by_id[r] for r in sorted(rooms_by_id)]
    return rooms, doors


def load_ship_blueprint(blueprint_id):
    """Return (layout_id, {system_tag: room_count}) for a ship blueprint.

    Scans raw/gamedata in load order and keeps the last definition, since a later
    file overriding an earlier one is how the game resolves duplicates.
    """
    found = None
    for name in BLUEPRINT_FILES:
        path = os.path.join(GAMEDATA, name)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        pattern = re.compile(
            r'<shipBlueprint\s+name="%s"[^>]*>(.*?)</shipBlueprint>' % re.escape(blueprint_id),
            re.DOTALL,
        )
        for m in pattern.finditer(text):
            header_end = text.index(">", m.start())
            header = text[m.start():header_end]
            layout_m = re.search(r'layout="([^"]+)"', header)
            if layout_m:
                found = (layout_m.group(1), m.group(1))

    if found is None:
        raise SaveFormatError("no <shipBlueprint name=%r> in raw/gamedata" % blueprint_id)

    layout_id, body = found
    system_list = ""
    sl = re.search(r"<systemList>(.*?)</systemList>", body, re.DOTALL)
    if sl:
        system_list = sl.group(1)

    counts = {}
    for tag in SYSTEM_TYPES_BASE + SYSTEM_TYPES_AE:
        counts[tag] = len(re.findall(r"<%s[\s/>]" % tag, system_list))
    return layout_id, counts


# --------------------------------------------------------------------------
# Sub-readers, one per method in SavedGameParser
# --------------------------------------------------------------------------

def read_anim(r):
    r.bool(); r.bool()
    r.skip_ints(5)


def read_crew_member(r, fmt):
    r.string()                      # name
    race = r.string()
    r.bool()                        # enemyBoardingDrone
    r.skip_ints(5)                  # health, spriteX, spriteY, roomId, roomSquare
    r.bool()                        # playerControlled

    if fmt in ADVANCED_FORMATS:
        r.int()                     # cloneReady
        r.int()                     # deathOrder
        for _ in range(r.int()):    # sprite tint indeces
            r.int()
        r.bool()                    # mindControlled
        r.skip_ints(2)              # savedRoomSquare, savedRoomId

    r.skip_ints(6)                  # pilot/engine/shield/weapon/repair/combat skill
    r.bool()                        # male
    r.skip_ints(5)                  # repairs, kills, evasions, jumps, masteries earned

    if fmt in ADVANCED_FORMATS:
        r.skip_ints(6)              # stun, healthBoost, clonebayPriority, damageBoost, ?, deaths
        if fmt in (8, 9, 11):
            for _ in range(12):     # two mastery flags for each of six skills
                r.bool()
        r.bool()                    # unknownNu
        read_anim(r)                # teleport anim
        r.bool()                    # unknownPhi
        if race == "crystal":
            r.skip_ints(3)          # lockdown recharge ticks, goal, unknownOmega


def read_system(r, fmt):
    """Returns the system's capacity. Zero means the ship lacks it and no
    further bytes were written for it."""
    capacity = r.int()
    if capacity > 0:
        r.skip_ints(6)              # power, damagedBars, ionizedBars,
                                    # deionizationTicks, repairProgress, damageProgress
        if fmt in ADVANCED_FORMATS:
            r.skip_ints(2)          # batteryPower, hackLevel
            r.bool()                # hacked
            r.skip_ints(3)          # temporary capacity cap / loss / divisor
    return capacity


def read_room(r, squares_h, squares_v, fmt):
    oxygen = r.int()
    if oxygen < 0 or oxygen > 100:
        raise SaveFormatError("unsupported room oxygen: %d" % oxygen)
    r.skip_ints(squares_h * squares_v * 3)
    if fmt in ADVANCED_FORMATS:
        r.int()                     # stationSquare
        direction = r.int()
        if direction not in (0, 1, 2, 3, 4):
            raise SaveFormatError("unsupported station direction: %d" % direction)


def read_door(r, fmt):
    if fmt in ADVANCED_FORMATS:
        r.skip_ints(3)              # currentMaxHealth, health, nominalHealth
    r.bool()                        # open
    r.bool()                        # walkingThrough
    if fmt in ADVANCED_FORMATS:
        r.skip_ints(2)              # unknownDelta, unknownEpsilon


def read_ship(r, fmt, ftl_dat):
    blueprint_id = r.string()
    r.string()                      # shipName
    r.string()                      # shipGfxBaseName

    layout_id, system_rooms = load_ship_blueprint(blueprint_id)
    rooms, doors = load_layout(ftl_dat, layout_id)

    for _ in range(r.int()):        # starting crew
        r.string()                  # race
        r.string()                  # name

    if fmt in ADVANCED_FORMATS:
        r.bool()                    # hostile
        r.int()                     # jumpChargeTicks
        r.bool()                    # jumping
        r.int()                     # jumpAnimTicks

    r.skip_ints(5)                  # hull, fuel, droneParts, missiles, scrap

    for _ in range(r.int()):
        read_crew_member(r, fmt)

    system_types = list(SYSTEM_TYPES_BASE)
    if fmt in ADVANCED_FORMATS:
        system_types += SYSTEM_TYPES_AE

    r.int()                         # reservePowerCapacity
    capacities = {}
    for system in system_types:
        capacities[system] = read_system(r, fmt)
        # A system spanning several rooms writes one SystemState per room.
        for _ in range(max(0, system_rooms.get(system, 0) - 1)):
            read_system(r, fmt)

    if fmt in ADVANCED_FORMATS:
        if capacities.get("clonebay", 0) > 0:
            r.skip_ints(3)          # buildTicks, buildTicksGoal, doomTicks
        if capacities.get("battery", 0) > 0:
            r.bool()                # active
            r.skip_ints(2)          # usedBattery, dischargeTicks

        # Shields info is always written, even with no shields system.
        r.skip_ints(4)              # layers, energyLayers, energyMax, rechargeTicks
        r.bool(); r.int()           # shield drop anim
        r.bool(); r.int()           # shield raise anim
        r.bool(); r.int()           # energy shield anim
        r.skip_ints(2)              # unknownLambda, unknownMu

        if capacities.get("cloaking", 0) > 0:
            r.skip_ints(4)          # unknownAlpha, unknownBeta, goal, cloakTicks

    for squares_h, squares_v in rooms:
        read_room(r, squares_h, squares_v, fmt)

    for _ in range(r.int()):        # breaches
        r.skip_ints(3)

    # Doors are stored in layout order, except that vacuum-adjacent doors (either
    # side opening onto space) are plucked out and appended at the end.
    vacuum = [d for d in doors if d[0] == -1 or d[1] == -1]
    interior = [d for d in doors if d[0] != -1 and d[1] != -1]
    for _ in interior + vacuum:
        read_door(r, fmt)

    if fmt in ADVANCED_FORMATS:
        r.int()                     # cloakAnimTicks

    if fmt in (8, 9, 11):
        for _ in range(r.int()):    # lockdown crystals
            r.skip_ints(5)          # x, y, speed, goalX, goalY
            r.bool(); r.bool()      # arrived, done
            r.int()                 # lifetime
            r.bool()                # superFreeze
            r.skip_ints(3)          # lockingRoom, animDirection, shardProgress

    weapons = []
    for _ in range(r.int()):
        weapons.append(r.string())
        r.bool()                    # armed
        if fmt == 2:
            r.int()                 # cooldownTicks

    for _ in range(r.int()):        # drones
        r.string()                  # droneId
        r.bool(); r.bool()          # armed, playerControlled
        r.skip_ints(5)              # bodyX, bodyY, roomId, roomSquare, health

    augments = [r.string() for _ in range(r.int())]

    return {
        "blueprint_id": blueprint_id,
        "layout_id": layout_id,
        "weapons": weapons,
        "augments": augments,
    }


STORE_SHELF_TYPES = ["weapon", "drone", "augment", "crew", "system"]


def read_store_shelf(r, fmt):
    item_type = r.int()
    if item_type not in (0, 1, 2, 3, 4):
        raise SaveFormatError("unknown store item type: %d" % item_type)
    items = []
    for _ in range(3):
        available = r.int()
        if available < 0:
            continue                # -1 means the slot holds no item
        items.append(r.string())    # itemId
        if fmt in (8, 9, 11):
            r.int()                 # extraData
    return {"type": STORE_SHELF_TYPES[item_type], "items": items}


def read_beacon(r, fmt):
    """Read one BeaconState. Returns what the save knows about that beacon.

    None of these fields name the beacon's event — the save does not hold it, it is
    regenerated from sectorLayoutSeed. What is here is a ship/store/fleet spoiler only;
    see raw/modding/2026-08-15-beacon-name-labels-mod.md §4.
    """
    beacon = {}
    beacon["visit_count"] = r.int()
    if beacon["visit_count"] > 0:
        r.string()                  # bgStarscapeImageInnerPath
        r.string()                  # bgSpriteImageInnerPath
        r.skip_ints(3)              # spritePosX, spritePosY, spriteRotation

    beacon["seen"] = r.bool()

    beacon["enemy_present"] = r.bool()
    if beacon["enemy_present"]:
        beacon["ship_event_id"] = r.string()
        beacon["auto_blueprint_id"] = r.string()
        r.int()                     # shipEventSeed

    fleet = r.int()
    if fleet not in (0, 1, 2, 3):
        raise SaveFormatError("unknown fleet presence: %d" % fleet)
    beacon["fleet"] = fleet

    beacon["under_attack"] = r.bool()

    beacon["store"] = None
    if r.bool():                    # storePresent
        shelf_count = r.int() if fmt in ADVANCED_FORMATS else 2
        shelves = [read_store_shelf(r, fmt) for _ in range(shelf_count)]
        fuel, missiles, drone_parts = r.int(), r.int(), r.int()
        beacon["store"] = {
            "shelves": shelves,
            "fuel": fuel,
            "missiles": missiles,
            "drone_parts": drone_parts,
        }

    return beacon


def read_encounter(r, fmt):
    encounter = {}
    r.int()                                     # shipEventSeed
    encounter["surrender_event"] = r.string()
    encounter["escape_event"] = r.string()
    encounter["destroyed_event"] = r.string()
    encounter["dead_crew_event"] = r.string()
    encounter["got_away_event"] = r.string()
    encounter["last_event"] = r.string()
    if fmt == 11:
        r.int()                                 # unknownAlpha
    encounter["text"] = r.string()
    r.int()                                     # affectedCrewSeed
    encounter["choices"] = [r.int() for _ in range(r.int())]
    return encounter


# --------------------------------------------------------------------------
# Top level
# --------------------------------------------------------------------------

def parse(path, ftl_dat):
    """Parse a continue.sav as far as the encounter. Returns a dict."""
    with open(path, "rb") as fh:
        data = fh.read()

    if len(data) < 4:
        raise SaveFormatError("file is too small to be a saved game")

    (fmt,) = struct.unpack_from("<i", data, 0)
    if fmt not in (2, 7, 8, 9, 11):
        raise SaveFormatError("unexpected first byte (%d) for a saved game" % fmt)
    if fmt != 11:
        raise SaveFormatError(
            "save file format %d is not supported; this parser targets FTL 1.6.1+ "
            "(format 11)" % fmt
        )

    r = Reader(data, unicode_strings=fmt >= 11)
    r.int()                         # fileFormat, already read

    r.bool()                        # randomNative
    dlc_enabled = r.bool()
    difficulty = r.int()
    if difficulty not in (0, 1, 2):
        raise SaveFormatError("unsupported difficulty flag: %d" % difficulty)

    r.skip_ints(4)                  # ships defeated, beacons explored, scrap, crew hired
    r.string()                      # playerShipName (redundant)
    r.string()                      # playerShipBlueprintId (redundant)
    r.int()                         # oneBasedSectorNumber (redundant)
    r.int()                         # unknownBeta

    for _ in range(r.int()):        # state vars
        r.string()
        r.int()

    ship = read_ship(r, fmt, ftl_dat)

    for _ in range(r.int()):        # cargo
        r.string()

    r.skip_ints(5)                  # sectorTreeSeed, sectorLayoutSeed,
                                    # rebelFleetOffset, rebelFleetFudge, rebelPursuitMod

    current_beacon_id = r.int()
    waiting = r.bool()
    r.int()                         # waitEventSeed
    r.string()                      # unknownEpsilon
    r.bool()                        # sectorHazardsVisible
    r.bool()                        # rebelFlagshipVisible
    r.int()                         # rebelFlagshipHop
    r.bool()                        # rebelFlagshipMoving
    r.bool()                        # rebelFlagshipRetreating
    r.int()                         # rebelFlagshipBaseTurns

    for _ in range(r.int()):        # sector visitation
        r.bool()

    sector_number = r.int()
    r.bool()                        # sectorIsHiddenCrystalWorlds

    beacons = [read_beacon(r, fmt) for _ in range(r.int())]

    quest_events = []               # eventName -> beaconId, for quest markers already placed
    for _ in range(r.int()):
        quest_events.append((r.string(), r.int()))
    distant_quest_events = []
    for _ in range(r.int()):
        distant_quest_events.append(r.string())

    r.int()                         # unknownMu
    encounter = read_encounter(r, fmt)

    return {
        "file_format": fmt,
        "dlc_enabled": dlc_enabled,
        "difficulty": ["EASY", "NORMAL", "HARD"][difficulty],
        "sector_number": sector_number,      # zero-based
        "current_beacon_id": current_beacon_id,
        "waiting": waiting,
        "beacons": beacons,
        "quest_events": quest_events,
        "distant_quest_events": distant_quest_events,
        "ship": ship,
        "encounter": encounter,
        "bytes_consumed": r.pos,
        "file_size": len(data),
    }


TEXT_ID_RE = re.compile(r"^(?:event|text)_[A-Za-z0-9_]{1,90}$")


def scan_encounter_text(path):
    """Find the encounter's text id without walking the save's structure.

    `parse` reaches the encounter by walking every preceding byte, which requires
    knowing the exact layout of the ship. Under Hyperspace that layout is not FTL's:
    six mods hook `ShipManager::ExportShip`, one hooks `CrewMember::SaveState`, and
    another six hook `StarMap::SaveGame`, each splicing variable-length data into the
    stream (`tools/SAVE-WATCH.md` section 6). Tracking all of it in Python would be a
    reimplementation of Hyperspace's serialisation, and would break whenever it gains
    a field.

    So for those saves we do not walk -- we look. Every FTL string is a length-prefixed
    UTF-8 blob, and `EncounterState.text` in 1.6.1+ holds a string-table id
    (`event_AUTO_CIVILIAN_c2_text`, `text_START_BEACON_ENGI_1`). Scanning for
    length-prefixed strings of exactly that shape finds it and nothing else: measured
    on a real Hyperspace save, the whole 5524-byte file yields exactly one candidate.

    This is deliberately narrow. It cannot see prose-valued encounter text, and it
    recovers no sector or beacon number -- it answers only the question the watcher
    actually asks. Returns a list of (offset, string), in file order.
    """
    with open(path, "rb") as fh:
        data = fh.read()

    found, pos, end = [], 0, len(data) - 4
    while pos <= end:
        (length,) = struct.unpack_from("<i", data, pos)
        if 3 <= length <= 200 and pos + 4 + length <= len(data):
            try:
                text = data[pos + 4:pos + 4 + length].decode("utf-8")
            except UnicodeDecodeError:
                pos += 1
                continue
            if TEXT_ID_RE.match(text):
                found.append((pos, text))
        pos += 1
    return found


def default_ftl_dat():
    """Where the game is, tried in order. `None` means say so rather than guess.

    `FTL_DIR` comes first and is the same variable the mod builders and
    `launch-ftl.cmd` read (`SETUP.md` §6) -- one name for one directory. The two paths
    after it are guesses at a stock Steam install; the first is the machine this was
    written on, and is a fallback, not a default.
    """
    candidates = []
    if os.environ.get("FTL_DIR"):
        candidates.append(os.path.join(os.environ["FTL_DIR"], "ftl.dat"))
    candidates += [
        r"D:\Steam\steamapps\common\FTL Faster Than Light\ftl.dat",
        r"C:\Program Files (x86)\Steam\steamapps\common\FTL Faster Than Light\ftl.dat",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("save", help="path to continue.sav")
    ap.add_argument("--ftl-dat", default=default_ftl_dat(), help="path to ftl.dat")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--beacons", action="store_true",
                    help="report what the save gives away about each beacon in the sector")
    args = ap.parse_args()

    if not args.ftl_dat:
        ap.error("could not find ftl.dat; pass --ftl-dat")

    state = parse(args.save, args.ftl_dat)

    if args.json:
        print(json.dumps(state, indent=2))
        return 0

    enc = state["encounter"]
    print("ship          %s (%s)" % (state["ship"]["blueprint_id"], state["ship"]["layout_id"]))
    print("difficulty    %s   sector %d   beacon %d"
          % (state["difficulty"], state["sector_number"] + 1, state["current_beacon_id"]))
    print("consumed      %d of %d bytes" % (state["bytes_consumed"], state["file_size"]))
    print()
    print("last_event    %r" % enc["last_event"])
    print("text          %r" % enc["text"])
    print("choices       %s" % enc["choices"])
    for key in ("surrender_event", "escape_event", "destroyed_event",
                "dead_crew_event", "got_away_event"):
        if enc[key]:
            print("%-13s %r" % (key, enc[key]))

    if args.beacons:
        print()
        print_beacon_report(state)
    return 0


FLEET_NAMES = {0: "-", 1: "rebel", 2: "federation", 3: "?"}


def print_beacon_report(state):
    """How much of the sector the save gives away, split by whether we have been there.

    The measurement this exists for: of the beacons the player has NOT visited, how many
    already name a ship event or a store? Anything true here is a map spoiler available
    with no game modification at all.
    """
    beacons = state["beacons"]
    quest_at = {beacon_id: name for name, beacon_id in state["quest_events"]}
    unvisited = [b for b in beacons if not b["visit_count"]]

    print("beacons       %d total, %d unvisited" % (len(beacons), len(unvisited)))
    for label, pool in (("unvisited", unvisited), ("all", beacons)):
        ships = sum(1 for b in pool if b["enemy_present"])
        named = sum(1 for b in pool if b.get("ship_event_id"))
        stores = sum(1 for b in pool if b["store"])
        seen = sum(1 for b in pool if b["seen"])
        print("  %-10s ships %d (named %d) | stores %d | seen-flag %d"
              % (label, ships, named, stores, seen))
    if quest_at:
        print("quest markers %s" % ", ".join(
            "%s@%d" % (name, bid) for bid, name in sorted(quest_at.items())))
    if state["distant_quest_events"]:
        print("deferred      %s" % ", ".join(state["distant_quest_events"]))

    print()
    print("  id  vis seen fleet  ship event / store")
    for i, b in enumerate(beacons):
        bits = []
        if b.get("ship_event_id"):
            bits.append("%s (%s)" % (b["ship_event_id"], b["auto_blueprint_id"]))
        elif b["enemy_present"]:
            bits.append("enemy, unnamed")
        if b["store"]:
            stock = [item for shelf in b["store"]["shelves"] for item in shelf["items"]]
            bits.append("STORE: %s" % (", ".join(stock) if stock else "empty"))
        if i in quest_at:
            bits.append("quest %s" % quest_at[i])
        if b["under_attack"]:
            bits.append("under attack")
        print("  %3d %3d %4s %-6s %s"
              % (i, b["visit_count"], "y" if b["seen"] else "-",
                 FLEET_NAMES[b["fleet"]], " | ".join(bits)))


if __name__ == "__main__":
    sys.exit(main())
