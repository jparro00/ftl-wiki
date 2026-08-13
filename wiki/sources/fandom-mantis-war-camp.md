---
id: source-fandom-mantis-war-camp
type: source
source_kind: wiki
raw: raw/wiki/mantis-war-camp.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest, blue-option, crew-reward, mantis, bugged]
---

# Fandom — "Mantis war camp"

## Summary
The community wiki page for `QUEST_MANTIS_INVASION_START`. Retrieved via the MediaWiki API
at revision 74270. Covers both the quest start and the encampment marker in one document,
and reports a requirement bug that the game files cannot express.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'QUEST_MANTIS_INVASION_START' in the
  datafiles."*
- Accepting pays **medium scrap** and places the marker — matching
  `autoReward level="MED">scrap_only` plus `<quest>`.
- At the marker, documents all three routes: leave (50/50 fight or clean escape), missile
  bombardment (costs a missile *and* starts the fight), and the Fire Bomb route (free Engi
  crew member plus high resources-with-scrap, no fight).
- **Reports a bug** on the missile option: *"bugged: Hull Missile doesn't count"* toward the
  `WEAPONS_MISSILES` requirement. Nothing in the XML expands that requirement token, so this
  is a Fandom-only observation.
- `MANTIS_LANDING_PARTY` **never surrenders and never escapes** — matching the absence of
  both elements in the ship definition.
- Fight rewards: `destroyed` → medium scrap with resources; `deadCrew` → high.
- `unique=true`, `LRSmap=noship`; the marker is `shipdetected=noship`.

## Events Covered
- [[event-mantis-war-camp]] — the quest start
- [[event-quest-mantis-invasion]] — the encampment marker and all three routes

## Other Pages Touched
- [[item-fire-bomb]], [[item-missile-weapon]], [[entity-mantis]], [[entity-engi]],
  [[sector-civilian-sector]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Everything mechanical agrees
with the extracted 1.6.x files; the Hull Missile bug is unverifiable from them.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `QUESTS min=1 max=1` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-mantis-war-camp]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_war_camp
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
