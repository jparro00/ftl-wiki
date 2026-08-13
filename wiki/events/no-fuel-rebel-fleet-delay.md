---
id: event-no-fuel-rebel-fleet-delay
type: event
event_name: FUEL_FLEET_DELAY
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rebel-fleet, recursive, no-choice, derived-odds]
---

# No fuel: Rebel fleet delay — `FUEL_FLEET_DELAY`

## Summary
The best possible outcome of waiting at a beacon with no fuel and your distress beacon
**off**: the Rebel fleet loses your trail for a jump *and* the game immediately rolls
another out-of-fuel event on top of it. It is the mechanical reward for not switching the
distress beacon on, and because the re-roll can land on itself, the delays stack.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list only — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-rebel-fleet-delay]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Derived odds.** `NO_FUEL` has 11 entries in AE and this event occupies one of them →
**1/11 (~9.1%)** per wait. *Assumes uniform selection across list entries.* Fandom
independently states **9%**, which matches ([[source-fandom-no-fuel-rebel-fleet-delay]]).
Vanilla, without the `<!-- DLC -->` `NO_FUEL_REFUGEE_FRIENDLY` entry, the list is 10 long →
**1/10 (10%)**.

## Text
Prose is drawn from `FUEL_FLEET_DELAY_LIST`, a `textList` of **7 variants** — rather than
quote one, note that all seven say the same thing: with no distress beacon and no FTL
signature, the fleet has lost you ([[source-text-events-xml]]). For example:

> Long range scanners indicate the Rebel fleet has temporarily paused its advance on your
> position. Your decision to leave the distress beacon deactivated was farsighted.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *(Continue — hidden, auto-labelled `continue`)* | — | `<modifyPursuit amount="-1"/>` → Rebel fleet pursuit **delayed by 1 jump**, then the event **re-loads `NO_FUEL`** and another out-of-fuel event fires immediately. | 100% |

The `modifyPursuit` fires on the event itself, before the choice — so the delay is
unconditional ([[source-events-fuel]]).

## Blue Options
None.

## Rewards & Risks
- **+1 jump of Rebel fleet delay.** No resources.
- The follow-on `NO_FUEL` roll is a full re-draw, so it can be another
  `FUEL_FLEET_DELAY` (delays accumulate correctly per
  [[source-fandom-no-fuel-rebel-fleet-delay]]), a harmless `FUEL_NOTHING`, or a fight.
  In effect this event is "free delay + one more free spin".
- No risk from the event itself; the risk is inherited from whatever it re-rolls into.

## Strategy Notes
- *Opinion:* this event is the single strongest argument for leaving the distress beacon
  **off** while stranded. The distress-on pool has no equivalent — its nearest analogue,
  `FUEL_FLEET_DISTRESS`, is not in any live list (see
  [[event-fuel-fleet-distress]]) and would have *increased* pursuit anyway.
- Balanced against that: the distress-on pool contains the paid-fuel vendors
  ([[event-no-fuel-automated-refueling-ship]], [[event-no-fuel-slug-fuel-depot]]) that can
  actually end the crisis. Beacon off buys time; beacon on buys fuel.

## Related
- [[event-fuel-fleet-distress]] — the unreachable distress-on twin, with inverted pursuit
- [[event-no-fuel-wait-fail-distress-off]] — the 4/11 "nothing" draw from the same list
- [[concept-rebel-fleet-advance]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Is the recursion depth bounded, or can a chain of delays run arbitrarily long?

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-rebel-fleet-delay]] (per raw/wiki/no-fuel-rebel-fleet-delay.md)
