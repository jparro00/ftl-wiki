---
id: source-fandom-remote-settlement
type: source
source_kind: wiki
raw: raw/wiki/remote-settlement.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [blue-option, drone-schematic, pirate-fight, surrender]
---

# Fandom — "Remote settlement"

## Summary
The community wiki page for `PIRATE_STATION_CROPS`. Retrieved via the MediaWiki API at
revision 73835. Notable for spelling out the `stuff` reward tiers as concrete resource
ranges and for giving surrender/escape percentages that corroborate the `1 − chance` reading.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_STATION_CROPS' in the datafiles."*
- Both fire-weapon blue options give **a drone schematic with high scrap**, which is how the
  page renders `autoReward level="HIGH">drone`.
- Surrender: *"50% chance for surrender offer at 20–40% hull"*; escape: *"50% chance for
  escape attempt at 30–40% hull"*. Both agree with `chance="0.5"` under `1 − chance`
  ([[concept-surrender-offers]]), and read the `min`/`max` attributes as **hull-percentage
  thresholds** — a reading the XML itself does not label.
- Expands the reward tiers: `LOW stuff` ≈ *fuel 1–3, missiles 1–2, drone parts 1*;
  `MED stuff` ≈ *fuel 2–4, missiles 2–4, drone parts 1*. Useful calibration for every
  `stuff` reward elsewhere in the wiki.
- Documents the `gotaway` path: even if the pirate escapes, the settlement still pays
  `LOW stuff` via `PIRATE_STATION_CROPS_RESULT`.
- `unique=true`, `LRSmap=ship`, Civilian Sector only.

## Events Covered
- [[event-remote-settlement]] — choices, blue options, and the full fight tree

## Other Pages Touched
- [[item-fire-beam]], [[item-fire-bomb]], [[entity-pirates]],
  [[sector-civilian-sector]], [[concept-surrender-offers]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. The mechanical content matches
the extracted 1.6.x files; the resource ranges for the `stuff` tiers appear nowhere in the
XML and are presumably measured from play.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** choice-4 outcome wording. Fandom writes *"into **their** settlement"*
> and *"**almost** laughably easy"*; the game files write *"into **the** settlement"* and
> *"laughably easy"* ([[source-text-events-xml]]). Recorded on [[event-remote-settlement]];
> game files trusted. Cosmetic, most likely pre-AE wording.

> ⚠️ **CONTRADICTION:** sector coverage — lists Civilian Sector only, but `NEUTRAL_CIVILIAN`
> is allocated `min=2 max=4` in **both** `STANDARD_SPACE` and `CIVILIAN_SECTOR`
> ([[source-sector-data-xml]]). Recorded on [[event-remote-settlement]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Remote_settlement
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
