---
id: source-fandom-lanius-craftsmen
type: source
source_kind: wiki
raw: raw/wiki/lanius-craftsmen.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, item-event, trading, blue-option, advanced-edition]
---

# Fandom — "Lanius craftsmen"

## Summary
Community wiki page for `LANIUS_RESEARCHER_CRAFT`, retrieved via the MediaWiki API at
revision 74219. Transcribes the full nested crafting menu with all three prices and confirms
the Lanius blue option is a flat 10-scrap discount.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'LANIUS_RESEARCHER_CRAFT' in the
  datafiles."*
- Location: Abandoned Sector; `LRSmap=noship`, `unique=true`.
- Prices match the XML exactly: 45 augment / 50 weapon / 40 drone, and 35 / 40 / 30 with the
  Lanius crew member. Renders the blue-option effect as *"Same options as above with a
  10 scrap discount."*
- Correctly represents the blue option as **nested inside choice 1**, not offered on the
  opening screen.
- States the reward pools are *Advanced Edition Content* items, matching the XML's
  `DLC_AUGMENTS` / `DLC_WEAPONS` / `DLC_DRONES` blueprint lists.
- Categorised *Trading Events* and *Advanced Edition Content Events*.

## Events Covered
- [[event-lanius-craftsmen]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-blue-options]]

## Reliability Notes
`medium`. Unusually precise for a Fandom event page — every number matches the game files.

## Contradictions Flagged
None. This page agrees with `raw/gamedata/dlcEvents_anaerobic.xml` on every price and
outcome.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_craftsmen
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]], [[source-dlcblueprints]]
