---
id: source-fandom-rebel-fight-chance-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-chance-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, blue-option, sensors, fleet-advance, unique]
---

# Fandom — "Rebel fight chance in nebula"

## Summary
The community wiki page for `NEBULA_REBEL_CHASE`. Retrieved via the MediaWiki API at
revision 73793. Five choices including three separate scanner-flavoured blue options.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_REBEL_CHASE' in the
  datafiles."*
- Locations: Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula. `nebula=true`,
  `LRSmap=ship+nebula`, `unique=true`. Matches the XML exactly — the event's only lists
  are `NEBULA_NEUTRAL` and `NEBULA_NEUTRAL_SLUG`.
- Choice 2 (`NEBULA_REBEL_CHASE_LIST`): fight / nothing / **pursuit doubled**. The last is
  the wiki's reading of `<modifyPursuit amount="1"/>`.
- Blue options recorded as **Sensors level 3**, **Long-Ranged Scanners**, and **Lifeform
  Scanner** — matching `req="sensors" lvl="3"`, `req="ADV_SCANNERS"`, `req="LIFE_SCANNER"`.
  All three lead to the same fight.
- Categorised `Fights with Default Rewards`, `Rebel Fleet advancement risk`.
- Lower-cases "rebel" in transcribed strings the game files capitalise.

## Events Covered
- [[event-rebel-fight-chance-in-nebula]]

## Other Pages Touched
- [[item-sensors]], [[item-long-ranged-scanners]], [[item-lifeform-scanner]],
  [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]], [[sector-slug-home-nebula]]

## Reliability Notes
`medium`. Version unstated, but it documents the Lifeform Scanner option, which is
AE-only (`<!--DLC-->` in the XML), so it describes at least an AE build.

## Contradictions Flagged
- Minor transcription drift: Fandom writes *"keep track of them enough to get in firing
  range"* where the game text reads *"keep track of them long enough to get in firing
  range"*. Recorded on [[event-rebel-fight-chance-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_chance_in_nebula
- [[source-events-nebula]], [[source-events-slug]], [[source-text-events-xml]]
