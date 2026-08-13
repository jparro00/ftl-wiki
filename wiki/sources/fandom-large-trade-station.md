---
id: source-fandom-large-trade-station
type: source
source_kind: wiki
raw: raw/wiki/large-trade-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [store, rebel, blue-option, mind-control, advanced-edition]
---

# Fandom — "Large trade station"

## Summary
Community wiki page for `STORE_REBELSIDE`, retrieved via the MediaWiki API at revision 74568.
Documents the search gamble, the duplicated auto-ship entry, and all three Mind Control tiers
— and supplies the thirteen-sector location list the game files do not state directly.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'STORE_REBELSIDE' in the datafiles."*
- **Sectors**: Civilian, Engi Controlled, Engi Homeworlds, Mantis Controlled, Mantis
  Homeworlds, Pirate Controlled, Rebel Controlled, Rebel Stronghold, Rock Controlled, Rock
  Homeworlds, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula — plus
  `alsooccur=exit`. `LRSmap=noship`, `unique=true`. This matches the sector definitions that
  allocate `ITEMS` beacons, and correctly omits the Zoltan sectors (no `ITEMS` allocation)
  and the Abandoned Sector (uses `ITEM_LANIUS`).
- **Flags the duplicated list entry** with its `DuplicateEvent|2` template on the auto-ship
  outcome — independently confirming the 2-in-4 weighting derivable from
  `STORE_REBELSIDE_SEARCH`.
- All three Mind Control tiers transcribed with their levels and rewards: store only,
  store + medium scrap with resources, store + high scrap with resources.
- Auto-ship destruction reward given as *"medium scrap with resources"*, matching
  `DESTROYED_DEFAULT`.
- Categorised *Store Opening opportunity*, *Auto-ship fights*, *Advanced Edition Content
  Events*.

## Events Covered
- [[event-large-trade-station]]

## Other Pages Touched
- The thirteen sectors listed above, [[entity-rebels]], [[item-mind-control]],
  [[concept-stores]], [[concept-blue-options]]

## Reliability Notes
`medium`, but this is one of the more useful Fandom pages in the batch: the sector list and
the duplicate-entry flag are both things the game files only imply.

## Contradictions Flagged
- *"it's better **not to** push your luck"* vs the files' *"it's better **to not** push your
  luck"*.
- *"Hopefully you **have** enough time to shop"* vs the files' *"Hopefully you **will have**
  enough time to shop"* (all three Mind Control outcomes).

Both are transcription smoothing, not version differences.

## Links
- Source URL: https://ftl.fandom.com/wiki/Large_trade_station
- [[source-dlcevents]], [[source-dlceventsoverwrite]], [[source-text-events-xml]],
  [[source-sector-data-xml]]
