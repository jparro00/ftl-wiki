---
id: event-no-fuel-wait-fail-distress-on
type: event
event_name: FUEL_NOTHING_DISTRESS
sectors: []
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, distress-beacon, no-choice, filler, derived-odds]
---

# No fuel: wait fail (distress on) — `FUEL_NOTHING_DISTRESS`

## Summary
The "no one came" draw for waiting at a beacon with no fuel and the distress beacon
**on**. It is the heaviest single weight in the `NO_FUEL_DISTRESS` pool, but at two entries
out of twelve it is only about half as common as its distress-off counterpart — the
clearest single argument that lighting the beacon gets results.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the distress-beacon-**on**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distresson`
  ([[source-fandom-no-fuel-wait-fail-distress-on]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** `<event load="FUEL_NOTHING_DISTRESS"/>` is listed **twice** in a 12-entry
`NO_FUEL_DISTRESS` list → **2/12 (~16.7%)** per wait. *This assumes uniform selection across
list entries* — Fandom independently states **16.7%**, which matches exactly
([[source-events-fuel]], [[source-fandom-no-fuel-wait-fail-distress-on]]).

In vanilla the list has 11 entries (the `NO_FUEL_REFUGEE` entry carries a `<!-- DLC -->`
comment) → **2/11 (~18.2%)**.

## Text
Prose is drawn from `FUEL_NOTHING_DISTRESS_LIST`, a `textList` of **7 variants**
([[source-text-events-xml]]). All are flavour for an unanswered distress call:

> The distress beacon's light is the only movement visible outside the ship.

> A few passing ships seem oblivious to your distress call and ignore all hails.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a bare `<text load=…/>`)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither, beyond the fleet advance that waiting always costs.

## Strategy Notes
- *Opinion:* the ~16.7% dead-draw rate versus ~36.4% with the beacon off
  ([[event-no-fuel-wait-fail-distress-off]]) is the core trade. Beacon on: roughly ten of
  twelve draws are *something*, but three of them are outright fights
  (`FUEL_ON_MANTIS_ATTACK`, `FUEL_ON_REBEL_ATTACK`, `FUEL_ON_REBEL_WARNING`) and one of
  those advances the fleet if it escapes.
- Beacon on is also the only way to reach the guaranteed-fuel vendors
  ([[event-no-fuel-automated-refueling-ship]] gives free `LOW` fuel every time it appears).

## Related
- [[event-no-fuel-wait-fail-distress-off]] — the distress-off equivalent (`FUEL_NOTHING`)
- [[event-no-fuel-automated-refueling-ship]] — the reliable good draw from the same list
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Whether the 7 text variants are uniformly drawn.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-wait-fail-distress-on]] (per raw/wiki/no-fuel-wait-fail-distress-on.md)
