---
id: source-fandom-store-in-nebula-uncharted
type: source
source_kind: wiki
raw: raw/wiki/store-in-nebula-uncharted.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, store, uncharted-nebula]
---

# Fandom — "Store in nebula (Uncharted)"

## Summary
The community wiki page for `NEBULA_STORE`. Retrieved via the MediaWiki API at revision
73894. Five intro-text variants and a store.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_STORE' in the datafiles."*
- Locations: **Uncharted Nebula only**. `store=nebula`, `LRSmap=noship+nebula`.
- Transcribes all five `text_NEBULA_STORE_*` variants; they match `text_events.xml`.
- Outcome: a store opens. Matches the bare `<store/>` element in the event.
- The "(Uncharted)" disambiguator in the title separates it from the Slug-sector store
  event `NEBULA_STORE_SLUG`, which has its own page.

## Events Covered
- [[event-store-in-nebula-uncharted]]

## Other Pages Touched
- [[sector-uncharted-nebula]], [[concept-stores]]

## Reliability Notes
`medium`. Version unstated. It does not mention that `sector_data.xml` allocates this
event `min=1 max=1` in `NEBULA_SECTOR`, i.e. exactly one guaranteed nebula store per
Uncharted Nebula — that fact comes from [[source-sector-data-xml]].

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Store_in_nebula_(Uncharted)
- [[source-events-nebula]], [[source-text-events-xml]], [[source-sector-data-xml]]
