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


def read_store_shelf(r, fmt):
    item_type = r.int()
    if item_type not in (0, 1, 2, 3, 4):
        raise SaveFormatError("unknown store item type: %d" % item_type)
    for _ in range(3):
        available = r.int()
        if available < 0:
            continue                # -1 means the slot holds no item
        r.string()                  # itemId
        if fmt in (8, 9, 11):
            r.int()                 # extraData


def read_beacon(r, fmt):
    if r.int() > 0:                 # visitCount
        r.string()                  # bgStarscapeImageInnerPath
        r.string()                  # bgSpriteImageInnerPath
        r.skip_ints(3)              # spritePosX, spritePosY, spriteRotation

    r.bool()                        # seen

    if r.bool():                    # enemyPresent
        r.string()                  # shipEventId
        r.string()                  # autoBlueprintId
        r.int()                     # shipEventSeed

    fleet = r.int()
    if fleet not in (0, 1, 2, 3):
        raise SaveFormatError("unknown fleet presence: %d" % fleet)

    r.bool()                        # underAttack

    if r.bool():                    # storePresent
        shelf_count = r.int() if fmt in ADVANCED_FORMATS else 2
        for _ in range(shelf_count):
            read_store_shelf(r, fmt)
        r.skip_ints(3)              # fuel, missiles, droneParts


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

    for _ in range(r.int()):
        read_beacon(r, fmt)

    quest_events = []
    for _ in range(r.int()):
        quest_events.append((r.string(), r.int()))
    for _ in range(r.int()):
        r.string()                  # distant quest events

    r.int()                         # unknownMu
    encounter = read_encounter(r, fmt)

    return {
        "file_format": fmt,
        "dlc_enabled": dlc_enabled,
        "difficulty": ["EASY", "NORMAL", "HARD"][difficulty],
        "sector_number": sector_number,      # zero-based
        "current_beacon_id": current_beacon_id,
        "waiting": waiting,
        "ship": ship,
        "encounter": encounter,
        "bytes_consumed": r.pos,
        "file_size": len(data),
    }


def default_ftl_dat():
    candidates = [
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
