---
id: source-fandom-store-mantis
type: source
source_kind: wiki
raw: raw/wiki/store-mantis.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, store]
---

# Fandom — "Store (Mantis)"

## Summary
The community wiki page for `STORE_MANTIS`. Retrieved via the MediaWiki API at revision
73888. A transcription page: six store-intro variants and "A store opens."

## Key Takeaways
- **Names the in-game id:** *"This event is called 'STORE_MANTIS' in the datafiles."*
  (under a `Trivia` heading).
- Locations: Mantis Controlled Sector, Mantis Homeworlds; `store=true`, `LRSmap=noship`.
- Transcribes all six `text_STORE_MANTIS_*` variants verbatim; they match
  `text_events.xml`.
- Confirms the outcome is simply *"A store opens"* — matching the bare `<store/>` element
  in the event definition. Notably this means the "malfunctioning Rebel supply ship stuck
  in vending mode" variant is **flavour only** and does not alter stock.
- Says nothing about how store inventory is generated, or whether the Mantis sector
  `rarityList` affects it.

## Events Covered
- [[event-store-mantis]]

## Other Pages Touched
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[concept-stores]]

## Reliability Notes
`medium`. Version unstated. A text dump with a null mechanical claim; nothing here
conflicts with the files.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Store_(Mantis)
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
