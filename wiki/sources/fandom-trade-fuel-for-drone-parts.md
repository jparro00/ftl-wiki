---
id: source-fandom-trade-fuel-for-drone-parts
type: source
source_kind: wiki
raw: raw/wiki/trade-fuel-for-drone-parts.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, fuel, drone-parts]
---

# Fandom — "Trade fuel for drone parts"

## Summary
The community wiki page for the event the game files call `FUEL_FOR_DRONE`. Retrieved via
the MediaWiki API at revision 73899. A two-choice trade with no risk and no branching.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FUEL_FOR_DRONE' in the
  datafiles."* This is the join key.
- Lists all three intro variants, matching the three-entry `FUEL_FOR_DRONE` textList in the
  files exactly, with **no DLC-marked additions** — so the pool is identical in both
  editions.
- Renders the trade as **lose 2–4 fuel, gain 1–3 drone parts**, matching
  `<item type="fuel" min="-4" max="-2"/>` and `<item type="drones" min="1" max="3"/>`.
- Adds the UI detail the files can't express: *"the actual trade offer is shown prior to
  making the choice"* — so the exchange rate is never a blind gamble.
- Confirms availability in sixteen sectors, `alsooccur=exit`, `LRSmap=noship`,
  `unique=false`.
- Categorised `Random_Events`, `Trading_Events`, `Drone Parts reward opportunity`.

## Events Covered
- [[event-trade-fuel-for-drone-parts]]

## Other Pages Touched
- [[concept-fuel]], [[item-drone-control]]

## Reliability Notes
`medium`. No game version stated, but nothing on this page is version-sensitive.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Trade_fuel_for_drone_parts
- [[source-events-xml]], [[source-text-events-xml]]
