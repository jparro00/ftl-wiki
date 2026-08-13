---
id: source-fandom-boarders-humans-near-sun
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-near-sun.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, boarding-hazard, sun-hazard]
---

# Fandom — "Boarders: Humans near sun"

## Summary
Community wiki page for `BOARDERS_SUN`, retrieved via the MediaWiki API at revision 73962.
Very short: one text, one outcome — 2–4 human boarders, no enemy ship.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'BOARDERS_SUN' in the datafiles."*
- Locations: Mantis Controlled Sector, Mantis Homeworlds, Pirate Controlled Sector, Rebel
  Controlled Sector, Rebel Stronghold; `redgiant=true`, `LRSmap=noship+redgiant`,
  `unique=true` — matching `unique="true"` in the files.
- **Notably omits Federation Space**, whose only route to this event is the
  `HOSTILE_BOARDING` list that `sector_data.xml` allocates `min=0 max=0`. That omission is
  corroborating evidence that the list is dead.
- Confirms 2–4 human boarders and gives **no reward** — matching the game file, which has
  no `<autoReward>` and no `<ship>`.
- Intro text matches `event_BOARDERS_SUN_text` exactly.

## Events Covered
- [[event-boarders-humans-near-sun]]

## Other Pages Touched
- [[event-boarders-asteroid]], [[entity-pirates]], [[sector-pirate-controlled-sector]],
  [[sector-mantis-controlled-sector]], [[sector-rebel-controlled-sector]]

## Reliability Notes
`medium`. No version stated.

## Contradictions Flagged
None. Its sector list matches the live `BOARDERS_*` allocations in `sector_data.xml`.

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_near_sun
- [[source-events-pirate]], [[source-sector-data-xml]], [[source-newevents]]
