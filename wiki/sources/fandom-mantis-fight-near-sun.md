---
id: source-fandom-mantis-fight-near-sun
type: source
source_kind: wiki
raw: raw/wiki/mantis-fight-near-sun.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, combat, sun, environmental-hazard]
---

# Fandom — "Mantis fight near sun"

## Summary
The community wiki page for `MANTIS_SUN_FIGHT`. Retrieved via the MediaWiki API at
revision 74259. A four-line page: the single intro string, the fight, and the location
template.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_SUN_FIGHT' in the datafiles."*
- Locations: Mantis Controlled Sector, Mantis Homeworlds; `redgiant=true`,
  `LRSmap=ship+redgiant`, `unique=false`. The `redgiant` marker is Fandom's rendering of
  the files' `<environment type="sun"/>` and tells you the beacon is flagged as a hazard
  on the map before you jump — a detail the XML does not spell out.
- Confirms the enemy is the same `MANTIS_FIGHT` ship as [[event-mantis-fight]], with the
  same **no surrender, no escape** annotation citing `events_ships.xml`.
- States **default rewards**, i.e. the sun hazard adds no extra payout.
- Quotes the single intro string verbatim; it matches `event_MANTIS_SUN_FIGHT_text`.
- Categorised `Random_Events`, `Fights with Default Rewards`.
- Does **not** describe what the sun environment actually does mechanically.

## Events Covered
- [[event-mantis-fight-near-sun]]

## Other Pages Touched
- [[entity-mantis]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[concept-hazards]]

## Reliability Notes
`medium`. Version unstated. Thin but fully consistent with the game files.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_fight_near_sun
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
