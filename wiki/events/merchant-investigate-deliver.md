---
id: event-merchant-investigate-deliver
type: event
event_name: MERCHANT_INVESTIGATE_DELIVER
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-merchant-s-request]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [quest-destination, drone-schematic, no-choice, payoff]
---

# Deliver to the station — `MERCHANT_INVESTIGATE_DELIVER`

## Summary
The terminal payoff of the investigation branch of [[event-merchant-s-request]]. It is a
**pure reward beacon**: no choices, no ship, no risk — you arrive and receive a drone
schematic with medium scrap.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via `<quest event="MERCHANT_INVESTIGATE_DELIVER"/>`,
  which fires from four places inside [[event-merchant-investigate]]
  ([[source-events-xml]]):
  - `MERCHANT_INVESTIGATE_LIST` entry 1 — "Take the cargo and head to its original destination"
  - `MERCHANT_INVESTIGATE_LIST` entry 2 — "Promise to deliver the cargo…"
  - `MERCHANT_INVESTIGATE_CARGO_LIST` entry 1 — the food-and-medical-supplies roll
- Sectors depend on where the marker is placed, so the frontmatter list is deliberately
  empty.
- [[source-fandom-merchant-s-request]] documents it as that page's "Deliver to the Station
  quest marker" section and marks it `nolrs+noship` — it does not even show on long-range
  scanners.

## Text
> You find the station that had ordered your cargo. You drop it off and they respond,
> "Ignoring the fact that this is days late, we really appreciate that you delivered our
> materials. We realize how dangerous this sector is these days. Take this as payment."

(`event_MERCHANT_INVESTIGATE_DELIVER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `autoReward level="MED"` **`drone`** — a drone schematic with medium scrap. | 100% |

The entire event body is one text id and one `autoReward` ([[source-events-xml]]).
[[source-fandom-merchant-s-request]] states the same: *"You receive a drone schematic with
medium scrap."*

## Blue Options
None.

## Rewards & Risks
- `MED drone` — guaranteed, unconditional, with no way to fail it.
- No ship, no damage, no crew risk. The only cost is the jumps spent reaching the marker.
- Note it does **not** consume the cargo mechanically — there is no `item_modify` here, so
  nothing is deducted.

## Strategy Notes
Worth the detour if the marker is on your route: a free drone schematic is a real pickup,
and this is one of very few beacons in the game with a strictly positive, choice-free
outcome. *(Opinion; the sources give the reward, not the recommendation.)*

## Related
- [[event-merchant-investigate]] — the only event that places this marker
- [[event-merchant-s-request]] — the quest start
- [[event-merchant-deliver]] — the parallel errand's destination
- [[chain-merchant-s-request]]

## Open Questions
- [ ] What drone type does `autoReward level="MED" drone` roll from — the general drone
      blueprint pool, or a restricted list?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-merchant-s-request]] (per raw/wiki/merchant-s-request.md)
