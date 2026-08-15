---
id: source-fandom-beacons
type: source
source_kind: wiki
raw: raw/wiki/beacons.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, beacon, quest-marker, store, exit]
---

# Fandom — "Beacons"

## Summary
The page describing beacons as map objects, retrieved at revision 71696. It covers what
each beacon *type* looks like on the sector map, what is visible from how far, and — most
usefully — the placement rules for quest markers, which `sector_data.xml` does not
express at all.

## Key Takeaways
- **Visibility**: every beacon except the sector's starting beacon begins unexplored.
  Distress and store beacons reveal themselves only within 1 jump (adjacent). The exit
  beacon is visible from the start, from any distance, and sits on the opposite side of
  the sector from the start. Quest markers, once spawned, are visible from any distance.
- **A jump costs**: a charged FTL drive, working engines and piloting, 1 fuel, and a
  crewmember in the piloting room.
- **Distress beacons do not expire** except by being overtaken by the Rebels — "a player
  does not need to rush to visit these beacons".
- **Quest marker placement rules** (the substantial content here):
  - normally placed in the current sector; if you have too few jumps left the game pushes
    it into the **next** sector, and it appears whichever sector you pick;
  - triggered in sector 7, the quest is **cancelled outright** — sector 8 allows no quests;
  - a marker **overwrites** whatever event was at the beacon, *unless* that beacon is a
    store, an exit, or another quest marker;
  - a marker **cannot be placed in a nebula area**; if only nebula lies to the right of the
    ship, or no suitable beacon exists, it goes to the next sector instead.
- **Every sector type has a number of possible quest events, but their appearance on the
  map is not guaranteed** — except the ship-unlocking quests in the Homeworlds sectors,
  which are.
- **Exit beacons**: present in every sector except The Last Stand. If the Rebels have
  reached the exit you must fight or flee a Rebel ship, usually with an Anti-Ship Battery
  present. Non-hostile exit events occur only when the Rebels have not reached it and the
  exit is not inside a nebula.
- **Repair beacons**: 3 in The Last Stand, each 15 hull repairs plus 22–44 scrap, 5 fuel,
  4 missiles, 5 drone parts.
- **Stores gained 2 pages in Advanced Edition**, "increasing their convenience
  significantly".
- **Long-Ranged Scanners caveat**: it warns of hazards and detects ship presence on
  adjacent beacons, but "not necessarily … the most accurate data on ship presence, and,
  sometimes, even the environment can drastically change due to the flow of an event".

## Events Covered
- None directly; points at the `Distress Beacon Events`, `Store Opening Rewards`,
  `Events with Quest Markers` and `Exit Beacon Events` categories.

## Other Pages Touched
- All of `wiki/sectors/`, [[sector-the-last-stand]], [[concept-blue-options]] (adjacent),
  [[item-long-ranged-scanners]]

## Reliability Notes
`medium`. The quest-marker rules are stated flatly with no citation and are not derivable
from anything in `raw/gamedata/` — they read as accumulated player testing. The page
itself carries two `@to-do: test and verify` HTML comments against exactly these claims,
so treat the overwrite-exclusion list as incomplete rather than authoritative.

## Contradictions Flagged
None against the game files — `sector_data.xml` says nothing about beacon visibility or
quest placement, so there is nothing to disagree with.

## Links
- Source URL: https://ftl.fandom.com/wiki/Beacons
- [[source-fandom-sectors]], [[source-fandom-rebel-fleet]],
  [[source-fandom-stores-and-resources]], [[source-sector-data-xml]]
