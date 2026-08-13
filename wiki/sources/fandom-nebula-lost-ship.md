---
id: source-fandom-nebula-lost-ship
type: source
source_kind: wiki
raw: raw/wiki/nebula-lost-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, crew-reward, blue-option, teleporter, long-ranged-scanners, unique]
---

# Fandom — "Nebula lost ship"

## Summary
The community wiki page for `NEBULA_LOST_SHIP`. Retrieved via the MediaWiki API at
revision 74843. Enumerates all four choices and both sub-event lists in full.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_LOST_SHIP' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula, Zoltan
  Controlled Sector, Zoltan Homeworlds. `nebula=true`, `alsooccur=nebulafiller`,
  `LRSmap=noship+nebula`, `unique=true`.
- Choice 1 (`NEBULA_LOST_SHIP_LIST`): three outcomes — crewmember, a Rebel fight with
  default rewards, or nothing. Matches the XML three-for-three.
- Choice 3 (Teleporter): **crewmember + medium scrap only**. Matches
  `<crewMember amount="1"/>` + `autoReward level="MED">scrap_only`.
- Choice 4 (Long-Ranged Scanners, `NEBULA_LOST_SHIP_LIST2`): two outcomes — crewmember, or
  medium scrap only. Matches the XML.
- Categorised `Fights with Default Rewards`, `Crew reward opportunity`.
- Writes the enemy as "rebel ship" in lower case where the XML text says "Rebel ship" —
  a wiki transcription slip, not a content difference.

## Events Covered
- [[event-nebula-lost-ship]]

## Other Pages Touched
- [[item-teleporter]], [[item-long-ranged-scanners]], [[concept-rebel-fleet-advance]],
  [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. Version unstated. Its outcome list is a complete and accurate match to the XML;
this is one of the better pages in the set.

## Contradictions Flagged
None of substance. Minor: it lower-cases "Rebel" inside a quoted string that the game
files capitalise.

## Links
- Source URL: https://ftl.fandom.com/wiki/Nebula_lost_ship
- [[source-events-nebula]], [[source-events-ships]], [[source-text-events-xml]]
