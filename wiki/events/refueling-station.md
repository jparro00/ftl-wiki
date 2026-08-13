---
id: event-refueling-station
type: event
event_name: REFUEL_STATION
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-hidden-crystal-worlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [trading, unique, fuel, scrap-cost, no-risk]
---

# Refueling station — `REFUEL_STATION`

## Summary
A flat-rate fuel vendor: **2 scrap per fuel**, in lots of 1, 3 or 6. No ship, no risk, no
blue options — the only decision is how much you buy. It is the game's baseline reference
price for fuel and appears in almost every sector type.

## Trigger & Where It Appears
- Event lists: `ITEMS` and its faction variants `ITEMS_CRYSTAL` ([[source-events-crystal]]),
  `ITEMS_ENGI` ([[source-events-engi]]), `ITEM_ZOLTAN` ([[source-events-zoltan]]), plus
  `OVERRIDE_ITEMS` under AE ([[source-newevents]], [[source-dlceventsoverwrite]])
- `sector_data.xml` allocates `ITEMS` in fourteen sector descriptions at 0–3 beacons each,
  `ITEMS_ENGI` at 3–3 in both Engi sectors, `ITEM_ZOLTAN` at 1–2 in both Zoltan sectors, and
  `ITEMS_CRYSTAL` at 2–2 in [[sector-hidden-crystal-worlds]] ([[source-sector-data-xml]])
- `ITEMS` is also a member of `EXIT_LIST` and `NON_HOSTILE` in `newEvents.xml`, so it reaches
  exit beacons too — [[source-fandom-refueling-station]] records this as `alsooccur=exit`
- `unique="true"` — at most once per run ([[source-events-xml]])
- Beacon: no ship staged; Fandom marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `ITEMS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists sixteen sectors and omits Federation space
>   ([[source-fandom-refueling-station]]).
>
> Trusting the game files (`high` vs `medium`). The same omission recurs on every
> `ITEMS`-list event, so it reads as a wiki location-template convention rather than a
> version difference.

**Pool size differs between editions.** The base `ITEMS` list has 9 non-DLC members plus 4
marked `<!--DLC-->`; AE replaces it with `OVERRIDE_ITEMS`, which has 14
([[source-newevents]], [[source-dlceventsoverwrite]]). Assuming uniform selection across
`eventList` entries ([[concept-event-list-weighting]]), a single `ITEMS` draw is **1/9** in
vanilla and **1/14** in AE — before uniqueness filtering removes already-seen events from
the pool.

## Text
> A ship refueling station is stationed at this beacon. We can purchase fuel here.

(`event_REFUEL_STATION_text`, per [[source-text-events-xml]])

The event definition carries a dev note: `<!-- NEED - checks to see if you have enough
scrap!-->` ([[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Buy 6 fuel for 12 scrap. | — | *"Thank you for your business."* → **+6 fuel, −12 scrap** | 100% |
| 2 | Buy 3 fuel for 6 scrap. | — | *"Thank you for your business."* → **+3 fuel, −6 scrap** | 100% |
| 3 | Buy 1 fuel for 2 scrap. | — | *"Thank you for your business."* → **+1 fuel, −2 scrap** | 100% |
| 4 | Ignore the station. | — | Nothing happens. | 100% |

All three purchase options are explicitly `hidden="false"`, so the trade is previewed before
you commit. All three reuse the same outcome text id (`event_REFUEL_STATION_c1_text`)
([[source-events-xml]]). [[source-fandom-refueling-station]] gives identical numbers.

The rate is a flat **2 scrap per fuel** at every quantity — there is no bulk discount.

## Blue Options
None.

## Rewards & Risks
- No risk whatsoever: no ship, no damage, no crew involvement.
- The only downside is opportunity cost — 12 scrap is meaningful early.
- The dev comment above suggests the event does **not** verify you can afford the purchase.
  Whether the UI blocks unaffordable options at runtime is not answerable from the files.

## Strategy Notes
- 2 scrap/fuel is the reference price. Compare it against [[event-trade-fuel-for-drone-parts]] and store
  prices before buying in bulk. *(Opinion; the sources give the price, not the comparison.)*
- Because the event is `unique="true"`, you get at most one of these per run — buy what you
  need when you see it.

## Related
- [[event-repair-station]] — the same "flat-rate service station" pattern, for hull
- [[event-sell-drone-parts-for-scrap]], [[event-sell-missiles-for-scrap]] — the selling side
- [[event-trade-fuel-for-drone-parts]] — the barter alternative in the same `ITEMS` pool
- [[concept-event-list-weighting]]

## Open Questions
- [ ] Does the game block the purchase options when you cannot afford them, or can scrap go
      negative? The XML's own comment flags this as unimplemented.
- [ ] Are the fuel amounts affected by any augment, the way the selling events are?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-refueling-station]] (per raw/wiki/refueling-station.md)
