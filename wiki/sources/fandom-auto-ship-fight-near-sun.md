---
id: source-fandom-auto-ship-fight-near-sun
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-fight-near-sun.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, sun-hazard]
---

# Fandom — "Auto-ship fight near sun"

## Summary
Community wiki page for `AUTO_SUN`, retrieved via the MediaWiki API at revision 73943. One
text, one fight, one reward — the shortest page in this batch.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'AUTO_SUN' in the datafiles."*
- Locations: **Civilian Sector only**; `redgiant=true`, `LRSmap=ship+redgiant`,
  `unique=true` — the `unique` flag matches `unique = "true"` in the file.
- Confirms the reward as *medium scrap with resources* = `autoReward level="MED"` `standard`
  via `DESTROYED_DEFAULT`.
- Intro text matches `event_AUTO_SUN_text` exactly.
- Says nothing about whether the auto-ship is mechanically immune to solar flares, despite
  the flavour text calling it *"impervious to the heat"*.

## Events Covered
- [[event-auto-ship-fight-near-sun]]

## Other Pages Touched
- [[event-auto-ship-fight-in-asteroid-field]], [[event-auto-ship-fight]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. No version stated. The event has no version-dependent tags.

## Contradictions Flagged
One, recorded on [[event-auto-ship-fight-near-sun]]: Civilian Sector only, although
`HOSTILE_CIVILIAN` is allocated `min=4 max=6` in `STANDARD_SPACE` = Federation Space. Same
systematic omission as the other generic-hostile pages.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_fight_near_sun
- [[source-events-xml]], [[source-newevents]], [[source-events-ships]], [[source-sector-data-xml]]
