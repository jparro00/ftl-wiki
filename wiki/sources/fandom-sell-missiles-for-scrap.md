---
id: source-fandom-sell-missiles-for-scrap
type: source
source_kind: wiki
raw: raw/wiki/sell-missiles-for-scrap.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, missiles, augment-interaction]
---

# Fandom — "Sell missiles for scrap"

## Summary
The community wiki page for `SELL_MISSILES_STATION`. Retrieved via the MediaWiki API at
revision 73859. The mechanical twin of the drone-part page, carrying the same augment claim.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'SELL_MISSILES_STATION' in the
  datafiles."*
- All three trades match the XML exactly: 5 missiles / 15 scrap, 10 / 30, 15 / 45 — a flat
  3 scrap per missile, one point per unit worse than the drone-part station.
- **Augment claim**: *"the scrap rewards for selling missiles are affected by the Scrap
  Recovery Arm and Repair Arm augments"*, with *"[Repair Arm needs verification]"* attached
  by the wiki itself. Nothing in the XML expresses this — the scrap values are fixed
  `min`/`max` pairs. Recorded as a Fandom-only claim.
- Lists thirteen sectors and flags `alsooccur=exit`, consistent with `ITEMS` membership of
  `EXIT_LIST` / `NON_HOSTILE` ([[source-newevents]]). Federation space is not among them.
- `unique=true`, `LRSmap=noship`.

## Events Covered
- [[event-sell-missiles-for-scrap]] — prices, availability, augment caveat

## Other Pages Touched
- [[event-sell-drone-parts-for-scrap]], [[event-refueling-station]], [[event-repair-station]],
  [[item-scrap-recovery-arm]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. The numbers agree with the
extracted 1.6.x files; the augment interaction is unverifiable from them.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] although
> `sector_data.xml` allocates `ITEMS min=1 max=1` in `STANDARD_SPACE`
> ([[source-sector-data-xml]]). Recorded on [[event-sell-missiles-for-scrap]]; game files
> trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Sell_missiles_for_scrap
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
