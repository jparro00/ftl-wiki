---
id: event-repair-station
type: event
event_name: REPAIR_STATION
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-hidden-crystal-worlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [trading, unique, hull-repair, scrap-cost, no-risk]
---

# Repair station — `REPAIR_STATION`

## Summary
A flat-rate hull repair vendor: **2 scrap per hull point**, in lots of 5, 10 or 20. No ship,
no risk, no blue options. It is the cheapest guaranteed repair in the game outside a store,
and the 20-point option is the single largest one-shot repair available anywhere.

## Trigger & Where It Appears
- Event lists: `ITEMS`, `ITEMS_CRYSTAL` ([[source-events-crystal]]), `ITEM_ZOLTAN`
  ([[source-events-zoltan]]), plus `OVERRIDE_ITEMS` under AE ([[source-newevents]],
  [[source-dlceventsoverwrite]]). Note it is **not** in `ITEMS_ENGI`, unlike
  [[event-refueling-station]].
- `sector_data.xml` allocates `ITEMS` in fourteen sector descriptions at 0–3 beacons each,
  `ITEM_ZOLTAN` at 1–2 in both Zoltan sectors, and `ITEMS_CRYSTAL` at 2–2 in
  [[sector-hidden-crystal-worlds]] ([[source-sector-data-xml]])
- `ITEMS` is also in `EXIT_LIST` and `NON_HOSTILE` ([[source-newevents]]);
  [[source-fandom-repair-station]] records `alsooccur=exit`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; Fandom marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `ITEMS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists sixteen sectors and omits Federation space
>   ([[source-fandom-repair-station]]).
>
> Trusting the game files (`high` vs `medium`); the same omission recurs on every
> `ITEMS`-list event.

**Pool size differs between editions.** Base `ITEMS` has 9 non-DLC members; AE's
`OVERRIDE_ITEMS` has 14 ([[source-newevents]], [[source-dlceventsoverwrite]]). Assuming
uniform selection ([[concept-event-list-weighting]]), a single `ITEMS` draw is **1/9** in
vanilla and **1/14** in AE, before uniqueness filtering.

## Text
> You see a small station fitted with hundreds of Repair drones. You receive an automated
> message, "We don't know who you are and we don't care, but this is the right place for
> some ship repair!"

(`event_REPAIR_STATION_text`, per [[source-text-events-xml]])

The definition carries the same dev note as the refueling station:
`<!-- NEED - checks to see if you have enough scrap!-->` ([[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Repair 20 damage. | — | *"Thank you for your business, no refunds!"* → `<damage amount="-20"/>` (**+20 hull**), **−40 scrap** | 100% |
| 2 | Repair 10 damage. | — | same text → **+10 hull**, **−20 scrap** | 100% |
| 3 | Repair 5 damage. | — | same text → **+5 hull**, **−10 scrap** | 100% |
| 4 | Ignore the station. | — | Nothing happens. | 100% |

All three purchases reuse the outcome text id `event_REPAIR_STATION_c1_text`
([[source-events-xml]]). [[source-fandom-repair-station]] gives identical numbers.

The rate is a flat **2 scrap per hull point** at every quantity — no bulk discount. The
"no refunds!" line is flavour, but it matches the mechanic: repairs are capped at your hull
maximum and there is no rebate for over-buying.

## Blue Options
None.

## Rewards & Risks
- No risk: no ship, no damage, no crew involvement.
- The real risk is **over-buying**. Repairing 20 when you are only 8 damaged still costs 40
  scrap; the choices are fixed amounts, not "repair to full".
- Choice 4 costs nothing.

## Strategy Notes
- Match the lot size to your actual damage. Buying "Repair 20" at 8 hull missing wastes 24
  scrap. *(Opinion; derived from the fixed `damage amount` values — no source states a cap
  refund.)*
- 2 scrap/hull is competitive with store repair rates and available in sectors where you may
  never find a store, which makes this a good beacon to route toward when limping.
- `unique="true"` means one per run, so spend the visit well.

## Related
- [[event-refueling-station]] — the same vendor pattern, for fuel
- [[event-repair-station-in-last-stand]] — the Last Stand variant
- [[event-sell-drone-parts-for-scrap]], [[event-sell-missiles-for-scrap]] — the selling side of the same pool
- [[concept-event-list-weighting]]

## Open Questions
- [ ] Does the game refund or block repair beyond your hull maximum? The XML's own dev
      comment flags affordability checking as unimplemented, and says nothing about capping.
- [ ] Is the repair amount affected by the Repair Arm augment, the way the selling events
      are said to be?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-repair-station]] (per raw/wiki/repair-station.md)
