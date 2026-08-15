---
id: source-fandom-template-stores-number-of-stores-by-sectors
type: source
source_kind: wiki
raw: raw/wiki/template-stores-number-of-stores-by-sectors.md
game_version: unknown
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, store, economy, routing]
---

# Fandom — Template: "Stores: number of stores, by sectors"

## Summary
The table transcluded into [[source-fandom-stores-and-resources]], retrieved at revision
73433. One row of guaranteed stores and one row of guaranteed nebula stores, across all 13
sector types — the single most routing-relevant table on the Fandom wiki.

## Key Takeaways
- Guaranteed stores, by sector: Civilian (starting) **1–2**; Civilian **2–3**; Engi **2–3**;
  Zoltan **2**; Abandoned **2**; Mantis **1–2**; Pirate **1–2**; Rebel **1–2**; Rock **2**;
  Slug Nebulas **0–1**; Uncharted Nebula **0–1**; Hidden Crystal Worlds **2–3**;
  The Last Stand **1**.
- Nebula stores are additional and exist only in the two nebula sector types: Slug Nebulas
  **2**, Uncharted Nebula **1**. So the real totals are Slug **2–3** and Uncharted **1–2**.
- Footnote: "about 0.8% of Uncharted Nebulas have no stores at all", due to map-generation
  issues — cited to a Reddit thread.
- Practical ranking that falls out: Civilian / Engi / Crystal are the store-rich sectors;
  Mantis / Pirate / Rebel are the store-poor ones; Uncharted Nebula is the only sector that
  can strand you with none.

## Events Covered
- None.

## Other Pages Touched
- Every page in `wiki/sectors/`, [[source-fandom-stores-and-resources]]

## Reliability Notes
`medium` by convention, but this table is a direct transcription of the `STORE*` /
`NEBULA_STORE*` lines of `sector_data.xml` and **every cell checks out** against it —
including the commented-out vanilla `STORE min=2 max=4` lines in the Rock definitions being
ignored in favour of `STORE_ROCK 2–2`. Treat it as high-confidence.

## Contradictions Flagged
None. All 13 columns agree with `sector_data.xml`.

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Stores:_number_of_stores,_by_sectors
- [[source-fandom-stores-and-resources]], [[source-sector-data-xml]],
  [[source-fandom-sectors]]
