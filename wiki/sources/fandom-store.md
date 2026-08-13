---
id: source-fandom-store
type: source
source_kind: wiki
raw: raw/wiki/store.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [store, structural]
---

# Fandom — "Store"

## Summary
Community wiki page for the generic `STORE` beacon, retrieved at revision 73884. Short:
five intro-text variants and "a store opens". Its value is the independent sector list,
which matches the `sector_data.xml` allocations exactly.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'STORE' in the datafiles."*
- Locations: Civilian Sector, Slug Controlled Nebula, Slug Home Nebula, The Last Stand,
  Uncharted Nebula — plus `store=true` and `LRSmap=noship`. This is the same set as the
  six `sector_data.xml` allocations once `STANDARD_SPACE` is read as Federation space.
- Lists all five `STORE_TEXT` variants, but **flat** — it does not record that three of
  them are conditioned on the beacon's `planet=` value.
- No choices, no rewards beyond the store itself.

## Events Covered
- [[event-store]]

## Other Pages Touched
- [[sector-civilian-sector]], [[sector-federation-space]], [[sector-uncharted-nebula]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[sector-the-last-stand]], [[concept-stores]]

## Reliability Notes
`medium`. Accurate but thin. The omission of the `planet=` conditions means the page
implies a uniform five-way text draw that the files do not support.

## Contradictions Flagged
- Minor wording: Fandom has *"Greetings traveler"*, the game string *"Greetings,
  traveler."* Recorded on [[event-store]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Store
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
