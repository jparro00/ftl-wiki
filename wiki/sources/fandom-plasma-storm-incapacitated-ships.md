---
id: source-fandom-plasma-storm-incapacitated-ships
type: source
source_kind: wiki
raw: raw/wiki/plasma-storm-incapacitated-ships.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [plasma-storm, salvage, crew-risk, crew-reward, blue-option, piloting, unique]
---

# Fandom — "Plasma storm incapacitated ships"

## Summary
The community wiki page for `STORM_ITEMS`. Retrieved via the MediaWiki API at revision
74844. The most detailed page in this batch: all five manual-search outcomes and all four
piloting outcomes, with resource ranges.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'STORM_ITEMS' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `plasmastorm=true`, `alsooccur=nebulafiller`, `LRSmap=noship+plasmastorm`, `unique=true`.
- Manual search (`STORM_ITEMS_LIST`) — five outcomes, all matching the XML:
  4 hull damage + random-system breach + **high "stuff"**; crew + low standard;
  **crew loss** + low standard (Clone Bay can revive); medium drone; medium weapon.
- Expands the `autoReward level="HIGH">stuff` payload as *"fuel: 3-6 ; missiles: 4-8 ;
  drone parts: 1-2"* — a numeric gloss the XML does not contain.
- Piloting branch (`STORM_ITEMS_PILOTING`) — four outcomes: crew + low standard;
  medium drone; **low** weapon; nothing. Matches the XML, including the fact that the
  piloting weapon reward is `LOW` where the manual-search one is `MED`.
- **Safety note:** *"The outcome with hull damage and breach does not destroy any system.
  (it is safe for crew being cloned)"*.
- Categorised `Hull damage risk`, `Hull breach risk`, `Crew loss risk`,
  `Clone Bay revival`, `Crew reward chance`, `Weapon reward chance`,
  `Events with Stuff rewards`.

## Events Covered
- [[event-plasma-storm-incapacitated-ships]]

## Other Pages Touched
- [[item-piloting]], [[item-clone-bay]], [[sector-uncharted-nebula]],
  [[concept-crew-loss-risk]]

## Reliability Notes
`medium`, but this is the strongest page in the batch — outcome-for-outcome accurate
against `events_nebula.xml`, and it adds numbers and safety notes the files do not state.
Version unstated; it documents the `<!--DLC-->` breach effect, so at least an AE build.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Plasma_storm_incapacitated_ships
- [[source-events-nebula]], [[source-text-events-xml]], [[source-sector-data-xml]]
