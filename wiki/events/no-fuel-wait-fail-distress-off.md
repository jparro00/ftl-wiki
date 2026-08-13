---
id: event-no-fuel-wait-fail-distress-off
type: event
event_name: FUEL_NOTHING
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, no-choice, filler, derived-odds]
---

# No fuel: wait fail (distress off) — `FUEL_NOTHING`

## Summary
The single most likely thing to happen when you wait at a beacon with no fuel and your
distress beacon off: nothing at all. It occupies **four of the eleven** entries in the
`NO_FUEL` list, making it by far the heaviest weight in the pool — the mechanical cost of
keeping the beacon dark.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-wait-fail-distress-off]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Derived odds.** `<event load="FUEL_NOTHING"/>` is listed **four times** in an 11-entry
`NO_FUEL` list → **4/11 (~36.4%)** per wait. *This assumes uniform selection across list
entries* — and Fandom independently states **36.4%**, which matches exactly, confirming the
assumption ([[source-events-fuel]], [[source-fandom-no-fuel-wait-fail-distress-off]]).

In vanilla the list has 10 entries (the `NO_FUEL_REFUGEE_FRIENDLY` entry carries a
`<!-- DLC -->` comment) → **4/10 (40%)**.

## Text
Prose is drawn from `FUEL_NOTHING_LIST`, a `textList` of **11 variants**
([[source-text-events-xml]]). They are all flavour for "no help arrives"; a representative
sample:

> No ship is in scanning range and no one arrives at the beacon.

> A freighter suddenly arrives nearby. They are so close you can almost wave at them, but
> your hails are ignored and the ship quickly jumps away.

> Cabin fever begins to spread among your crew.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a bare `<text load=…/>`)* | — | Nothing happens. The wait consumes one Rebel-fleet advance. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The only cost is the fleet advance that waiting itself incurs.

## Strategy Notes
- *Opinion:* this is the number that makes being stranded dangerous. With the beacon off,
  ~36% of waits do nothing while the fleet closes; only ~9% (`FUEL_FLEET_DELAY`) buy time
  back, and only a handful of the remaining draws actually produce fuel.
- Compare the distress-on pool, where the equivalent dead draw is only ~16.7%
  ([[event-no-fuel-wait-fail-distress-on]]) — turning the beacon on roughly halves your
  wasted waits, at the price of Rebel and Mantis attack draws.

## Related
- [[event-no-fuel-wait-fail-distress-on]] — the distress-on equivalent (`FUEL_NOTHING_DISTRESS`)
- [[event-no-fuel-rebel-fleet-delay]] — the good draw from the same list
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Are the 11 text variants weighted, or uniformly drawn? The `textList` lists each once,
      implying uniform.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-wait-fail-distress-off]] (per raw/wiki/no-fuel-wait-fail-distress-off.md)
