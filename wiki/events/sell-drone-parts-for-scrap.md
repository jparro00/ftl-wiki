---
id: event-sell-drone-parts-for-scrap
type: event
event_name: SELL_DRONES_STATION
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, unique, drone-parts, scrap-reward, no-risk]
---

# Sell drone parts for scrap — `SELL_DRONES_STATION`

## Summary
A flat-rate buyer for drone parts: **4 scrap per part**, in lots of 3, 6 or 12. No ship, no
risk, no blue options. It is the only reliable way to convert surplus drone parts into scrap
outside a store, and it is worth knowing the rate before you decide whether to hoard parts.

## Trigger & Where It Appears
- Event lists: `ITEMS`, plus `OVERRIDE_ITEMS` under AE ([[source-newevents]],
  [[source-dlceventsoverwrite]]). It is **not** in any of the faction `ITEMS_*` variants,
  which is why [[sector-hidden-crystal-worlds]] and the Zoltan sectors are absent from the
  sector list.
- `sector_data.xml` allocates `ITEMS` in fourteen sector descriptions at 0–3 beacons each
  ([[source-sector-data-xml]])
- `ITEMS` is also in `EXIT_LIST` and `NON_HOSTILE` ([[source-newevents]]);
  [[source-fandom-sell-drone-parts-for-scrap]] records `alsooccur=exit`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; Fandom marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `ITEMS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists thirteen sectors and omits Federation space
>   ([[source-fandom-sell-drone-parts-for-scrap]]).
>
> Trusting the game files (`high` vs `medium`); the same omission recurs on every
> `ITEMS`-list event.

**Pool size differs between editions.** Base `ITEMS` has 9 non-DLC members; AE's
`OVERRIDE_ITEMS` has 14 ([[source-newevents]], [[source-dlceventsoverwrite]]). Assuming
uniform selection ([[concept-event-list-weighting]]), a single `ITEMS` draw is **1/9** in
vanilla and **1/14** in AE, before uniqueness filtering.

## Text
> You see a civilian space station with heavy damage. You receive a message, "We've been hit
> hard by the war. We need more drone parts to speed up our repairs. We'll buy some from you
> if you have extra."

(`event_SELL_DRONES_STATION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Sell 3 drone parts for 12 scrap. | — | *"Thank you for your business."* → **−3 drone parts, +12 scrap** | 100% |
| 2 | Sell 6 drone parts for 24 scrap. | — | same text → **−6 drone parts, +24 scrap** | 100% |
| 3 | Sell 12 drone parts for 48 scrap. | — | same text → **−12 drone parts, +48 scrap** | 100% |
| 4 | Ignore the station. | — | Nothing happens. | 100% |

The three selling options are `hidden="true"`; the ignore option is not. All three reuse the
outcome text id `event_SELL_DRONES_STATION_c1_text` ([[source-events-xml]]).
[[source-fandom-sell-drone-parts-for-scrap]] gives identical numbers.

The rate is a flat **4 scrap per drone part** at every quantity — no bulk bonus.

## Blue Options
None.

## Rewards & Risks
- No risk: no ship, no damage, no crew involvement.
- [[source-fandom-sell-drone-parts-for-scrap]] adds a mechanic the game files do not
  express: *"the scrap rewards for selling drone parts are affected by the Scrap Recovery
  Arm and Repair Arm augments — you could get more or less scrap as a result"*, with the
  Repair Arm half flagged as needing verification. The XML shows only fixed
  `<item type="scrap" min="12" max="12"/>`-style values, so any augment scaling is applied
  outside the event definition. Treat the augment interaction as a Fandom-only claim.
- The real cost is opportunity: 12 parts is a lot of drone uptime to trade for 48 scrap.

## Strategy Notes
- 4 scrap per part is the reference rate. Sell only what you cannot use — on a ship with no
  Drone Control, sell everything; on a drone-heavy build, this beacon is close to worthless.
  *(Opinion; the sources give the rate, not the judgement.)*
- If Fandom's augment claim holds, a [[item-scrap-recovery-arm]] makes this beacon
  meaningfully better and is worth routing for.

## Related
- [[event-sell-missiles-for-scrap]] — the identical event for missiles, 3 scrap each
- [[event-refueling-station]], [[event-repair-station]] — the buying side of the same pool
- [[item-scrap-recovery-arm]]
- [[concept-event-list-weighting]]

## Open Questions
- [ ] Verify the Scrap Recovery Arm / Repair Arm interaction — Fandom itself flags the
      Repair Arm half as unverified, and nothing in the XML supports either.
- [ ] Are the selling options hidden if you do not hold enough drone parts, or do they show
      and fail?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sell-drone-parts-for-scrap]] (per raw/wiki/sell-drone-parts-for-scrap.md)
