---
id: source-fandom-store-crystal
type: source
source_kind: wiki
raw: raw/wiki/store-crystal.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, store, crew-purchase]
---

# Fandom — "Store (Crystal)"

## Summary
The community wiki page for `STORE_CRYSTAL`. Retrieved via the MediaWiki API at revision
73885. Short, but carries one claim of real strategic weight.

## Key Takeaways
- Names the in-game id: *"This event is called 'STORE_CRYSTAL' in the datafiles"*.
- **"These are the only stores you can normally buy crystal beings."** This is the page's
  load-bearing claim and it is corroborated structurally by `sector_data.xml`, where
  `CRYSTAL_HOME` is the only sector whose `rarityList` gives `crystal` a non-zero rarity
  ([[source-sector-data-xml]]).
- Lists four intro-text variants; the game's text list holds six strings, of which `_5`/`_6`
  are near-duplicates of `_3`/`_4`, so the page covers the distinct set.
- Location: Hidden Crystal Worlds, store beacon, **no ship** on Long-Range Scanners.

## Events Covered
- [[event-store-crystal]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]],
  [[event-crystal-scrap-collector]]

## Reliability Notes
`medium`. No game version stated. The Crystal-crew claim is a behavioural assertion the
game files support only indirectly (via the sector rarity table), so it is worth
re-checking in play.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Store_(Crystal)
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
