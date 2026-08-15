---
id: event-sell-missiles-for-scrap
type: event
event_name: SELL_MISSILES_STATION
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, unique, missiles, scrap-reward, no-risk]
---

# Sell missiles for scrap — `SELL_MISSILES_STATION`

## Summary
A black-market buyer for missiles: **3 scrap per missile**, in lots of 5, 10 or 15. The
mechanical twin of [[event-sell-drone-parts-for-scrap]] at a lower rate. No ship, no risk,
no blue options — worth taking only on a build with no missile weapon.

## Trigger & Where It Appears
- Event lists: `ITEMS`, plus `OVERRIDE_ITEMS` under AE ([[source-newevents]],
  [[source-dlceventsoverwrite]]). Not in any faction `ITEMS_*` variant, which is why
  [[sector-hidden-crystal-worlds]] and the Zoltan sectors are absent from the sector list.
- `sector_data.xml` allocates `ITEMS` in fourteen sector descriptions at 0–3 beacons each
  ([[source-sector-data-xml]])
- `ITEMS` is also in `EXIT_LIST` and `NON_HOSTILE` ([[source-newevents]]);
  [[source-fandom-sell-missiles-for-scrap]] records `alsooccur=exit`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; Fandom marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `ITEMS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists thirteen sectors and omits Federation space
>   ([[source-fandom-sell-missiles-for-scrap]]).
>
> Trusting the game files (`high` vs `medium`); the same omission recurs on every
> `ITEMS`-list event.

**Pool size differs between editions.** Base `ITEMS` has 9 non-DLC members; AE's
`OVERRIDE_ITEMS` has 14 ([[source-newevents]], [[source-dlceventsoverwrite]]). Assuming
uniform selection ([[concept-event-list-weighting]]), a single `ITEMS` draw is **1/9** in
vanilla and **1/14** in AE, before uniqueness filtering.

## Text
> There is a black market hub here. You receive a message, "These are dangerous times. If
> you have extra military-grade explosives, we'll gladly pay you for them."

(`event_SELL_MISSILES_STATION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Sell 5 missiles for 15 scrap. | — | *"Thank you, this will help greatly."* → **−5 missiles, +15 scrap** | 100% |
| 2 | Sell 10 missiles for 30 scrap. | — | same text → **−10 missiles, +30 scrap** | 100% |
| 3 | Sell 15 missiles for 45 scrap. | — | same text → **−15 missiles, +45 scrap** | 100% |
| 4 | Ignore the station. | — | Nothing happens. | 100% |

The three selling options are `hidden="true"`; the ignore option is not. All three reuse the
outcome text id `event_SELL_MISSILES_STATION_c1_text` ([[source-events-xml]]).
[[source-fandom-sell-missiles-for-scrap]] gives identical numbers.

The rate is a flat **3 scrap per missile** at every quantity — no bulk bonus, and a full
scrap-point per unit worse than the drone-part station.

## Blue Options
None.

## Rewards & Risks
- No risk: no ship, no damage, no crew involvement.
- [[source-fandom-sell-missiles-for-scrap]] adds the same augment caveat as its drone-part
  twin: *"the scrap rewards for selling missiles are affected by the Scrap Recovery Arm and
  Repair Arm augments"*, with the Repair Arm half flagged as needing verification. The XML
  contains only fixed scrap values, so any scaling happens outside the event definition —
  treat it as a Fandom-only claim.
- Selling 15 missiles is a large commitment; missiles are the resource you cannot buy back
  cheaply mid-sector.

## Strategy Notes
- Sell only if you have no missile weapon and no plan to pick one up. At 3 scrap each, this
  is the worst conversion rate of the four station events, and missiles regain value the
  moment you find a launcher. *(Opinion; the sources give rates, not the judgement.)*
- If you *are* going to dump missiles, note the drone-part station pays 4 each — prefer that
  beacon if both appear.

## Related
- [[event-sell-drone-parts-for-scrap]] — the identical event for drone parts, 4 scrap each
- [[event-refueling-station]], [[event-repair-station]] — the buying side of the same pool
- [[item-scrap-recovery-arm]]
- [[concept-event-list-weighting]]

## Open Questions
- [ ] Verify the Scrap Recovery Arm / Repair Arm interaction — Fandom flags half of it as
      unverified and the XML supports neither.
- [ ] Are the selling options hidden if you hold fewer missiles than the lot size?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sell-missiles-for-scrap]] (per raw/wiki/sell-missiles-for-scrap.md)
