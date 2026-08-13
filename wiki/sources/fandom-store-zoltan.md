---
id: source-fandom-store-zoltan
type: source
source_kind: wiki
raw: raw/wiki/store-zoltan.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, store, varies-text]
---

# Fandom — "Store (Zoltan)"

## Summary
The community wiki page for `STORE_ZOLTAN`. Retrieved via the MediaWiki API at revision
73892. Its sole content is the three store intro variants, transcribed accurately.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'STORE_ZOLTAN' in the
  datafiles."*
- Lists **three** intro variants, matching the three ids
  (`text_STORE_ZOLTAN_1` … `_3`) the game file references, in the same order. Verified
  string by string against `text_events.xml`.
- Confirms the only outcome is **a store opens** — the varied flavour (Zoltan
  knick-knack shop, human trader, Mantis black market in a dead space-whale) has no
  mechanical effect.
- Locations template: both Zoltan sectors, `store=true`, Long-Ranged Scanners `noship`.

## Events Covered
- [[event-store-zoltan]]

## Other Pages Touched
- [[concept-stores]]

## Reliability Notes
`medium`. States no game version. Does not mention the sector allocation
(`min=2 max=2`, i.e. exactly two stores per Zoltan sector) — that comes from
[[source-sector-data-xml]] and is the more strategically important fact.

## Contradictions Flagged
None. All three strings match `text_events.xml` verbatim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Store_(Zoltan)
- [[source-events-zoltan]], [[source-text-events-xml]], [[source-sector-data-xml]]
