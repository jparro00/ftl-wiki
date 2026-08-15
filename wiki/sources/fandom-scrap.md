---
id: source-fandom-scrap
type: source
source_kind: wiki
raw: raw/wiki/scrap.md
game_version: unknown
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, economy, scrap, difficulty, routing]
---

# Fandom — "Scrap"

## Summary
Short mechanics page on the game's currency, retrieved at revision 73343. Its value for
sector work is one paragraph: scrap rewards are governed by a per-sector-number parameter
modified by difficulty, and **sector type** changes profitability separately, through which
events the sector's pool can roll.

## Key Takeaways
- **Scrap rewards scale with a "Scrap Sector parameter"** — a function of sector *number*,
  not sector type — and the difficulty setting shifts that parameter so that easier
  difficulties pay more in every sector. Full tables are hosted off-wiki at
  `mikehopley.github.io/ftl-scrap/` for easy / normal / hard.
- **Sector *type* affects profit independently**, "that depends on the events which can
  possibly occur in a particular sector type (e.g. double rewards events), but not in
  another sector type" — cited to the mekloz Reddit sector-profit dataset.
- Selling to stores returns half price, rounded **against** the player.
- Scrap can be spent outside stores on upgrades and reactor power, and is consumed or gained
  by trading events.

## Events Covered
- By reference: the `Trading Events` and `Scrap use Events` categories.

## Other Pages Touched
- All of `wiki/sectors/`, [[concept-scrap-economy]], [[source-fandom-stores-and-resources]]

## Reliability Notes
`medium`, and thin: the page **states no actual numbers**. Both quantitative claims are
outbound links this repo does not hold (`mikehopley.github.io/ftl-scrap`, and a Reddit
post of "200× sector 4 hard" samples). The sector-profit claim is a single community
dataset, not game files — the strongest thing that can be said from it is a direction, not
a figure.

## Contradictions Flagged
None. Nothing here conflicts with `sector_data.xml`, which carries no scrap values.

## Links
- Source URL: https://ftl.fandom.com/wiki/Scrap
- [[source-fandom-stores-and-resources]], [[source-fandom-sectors]],
  [[source-fandom-guides-and-tips]]
