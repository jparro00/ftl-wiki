---
id: source-fandom-sell-drone-parts-for-scrap
type: source
source_kind: wiki
raw: raw/wiki/sell-drone-parts-for-scrap.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, drone-parts, augment-interaction]
---

# Fandom — "Sell drone parts for scrap"

## Summary
The community wiki page for `SELL_DRONES_STATION`. Retrieved via the MediaWiki API at
revision 73860. A minimal transaction page, but it carries one mechanical claim the game
files cannot express: augment scaling on the scrap paid.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'SELL_DRONES_STATION' in the datafiles."*
- All three trades match the XML exactly: 3 parts / 12 scrap, 6 / 24, 12 / 48 — a flat
  4 scrap per part.
- **Augment claim**: *"the scrap rewards for selling drone parts are affected by the Scrap
  Recovery Arm and Repair Arm augments — you could get more or less scrap as a result"*,
  with *"[Repair Arm needs verification]"* attached by the wiki itself. The XML carries only
  fixed `min`/`max` scrap values, so any scaling must be applied outside the event
  definition. Recorded as a Fandom-only claim.
- Lists thirteen sectors and flags `alsooccur=exit`, consistent with `ITEMS` membership of
  `EXIT_LIST` / `NON_HOSTILE` ([[source-newevents]]). Federation space is not among them.
- `unique=true`, `LRSmap=noship`.

## Events Covered
- [[event-sell-drone-parts-for-scrap]] — prices, availability, augment caveat

## Other Pages Touched
- [[event-sell-missiles-for-scrap]], [[event-refueling-station]], [[event-repair-station]],
  [[item-scrap-recovery-arm]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. The numbers agree with the
extracted 1.6.x files; the augment interaction is unverifiable from them and the wiki flags
half of it as unverified itself.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] although
> `sector_data.xml` allocates `ITEMS min=1 max=1` in `STANDARD_SPACE`
> ([[source-sector-data-xml]]). Recorded on [[event-sell-drone-parts-for-scrap]]; game files
> trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Sell_drone_parts_for_scrap
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
