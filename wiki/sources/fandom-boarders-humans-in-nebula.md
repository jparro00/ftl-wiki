---
id: source-fandom-boarders-humans-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, boarding, crew-risk, unique]
---

# Fandom — "Boarders: Humans in nebula"

## Summary
The community wiki page for `NEBULA_BOARDING`. Retrieved via the MediaWiki API at revision
73959. Three intro-text variants and a single no-choice outcome.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_BOARDING' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Uncharted Nebula. `nebula=true`,
  `alsooccur=nebulafiller`, `LRSmap=noship+nebula`, `unique=true`.
- Outcome: **2–4 human boarders** beam aboard. Matches
  `<boarders min="2" max="4" class="human"/>`.
- `LRSmap=noship+nebula` — long-range scanners show no ship, which is the trap: the
  boarders arrive anyway.
- No reward of any kind. Categorised `Boarding hazard`.

## Events Covered
- [[event-boarders-humans-in-nebula]]

## Other Pages Touched
- [[sector-uncharted-nebula]], [[sector-civilian-sector]],
  [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. Version unstated. Its location list omits **Federation Space**, which the
`NEBULA` event list reaches via `sector_data.xml` (`STANDARD_SPACE`, `NEBULA min=0 max=4`).

## Contradictions Flagged
- Sector coverage: Fandom lists three sectors, the event lists reach five (adds Federation
  Space, and Rebel sectors indirectly). Recorded on [[event-boarders-humans-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_in_nebula
- [[source-events-nebula]], [[source-text-events-xml]], [[source-sector-data-xml]]
