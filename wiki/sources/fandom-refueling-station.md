---
id: source-fandom-refueling-station
type: source
source_kind: wiki
raw: raw/wiki/refueling-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, fuel]
---

# Fandom — "Refueling station"

## Summary
The community wiki page for `REFUEL_STATION`. Retrieved via the MediaWiki API at revision
74707. A minimal transaction page; its value is the id join, the sector list, and the
`alsooccur=exit` flag.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'REFUEL_STATION' in the datafiles."*
- All three prices match the XML exactly: 6 fuel / 12 scrap, 3 / 6, 1 / 2 — a flat 2 scrap
  per fuel.
- Lists sixteen sectors and flags `alsooccur=exit`, consistent with `ITEMS` being a member of
  `EXIT_LIST` and `NON_HOSTILE` in `newEvents.xml` ([[source-newevents]]). Federation space
  is not among the sixteen.
- `unique=true`, `LRSmap=noship`.
- Categorised `Random_Events`, `Unique_Events`, `Trading_Events`.
- Says nothing about the XML's own dev note that affordability checking is unimplemented.

## Events Covered
- [[event-refueling-station]] — prices and availability

## Other Pages Touched
- [[event-repair-station]], [[event-sell-drone-parts-for-scrap]],
  [[event-sell-missiles-for-scrap]], [[sector-hidden-crystal-worlds]],
  and the fourteen other sectors listed on the event page

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Every number agrees with the
extracted 1.6.x files.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — lists sixteen sectors and omits
> [[sector-federation-space]], although `sector_data.xml` allocates `ITEMS min=1 max=1` in
> `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on [[event-refueling-station]];
> game files trusted. Same omission pattern as every other `ITEMS`-list event.

## Links
- Source URL: https://ftl.fandom.com/wiki/Refueling_station
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
