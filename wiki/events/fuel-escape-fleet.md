---
id: event-fuel-escape-fleet
type: event
event_name: FUEL_ESCAPE_FLEET
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rebel-fleet, orphan, engine-event, no-choice, advanced-edition]
---

# Fuel escape (Rebel fleet) — `FUEL_ESCAPE_FLEET`

## Summary
A one-line resolution event: your pilot is dodging fleet artillery while you work out what
to do next. No choices, no rewards, no ship. Unlike its two siblings this one describes an
ongoing predicament rather than a clean getaway, which makes its exact trigger the least
obvious of the three.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_FLEET` appears exactly once in
`raw/gamedata/` — its own definition in `dlcEvents.xml` ([[source-dlcevents]]).

The provenance argument is on [[event-fuel-escape-pulsar]]: this is the third of three
`FUEL_ESCAPE_*` events added by the AE file, completing the vanilla set of
`FUEL_ESCAPE_SUN` / `_STORM` / `_ASTEROIDS` in `events.xml`, all of which are likewise
unreferenced and sit among hard-coded engine events ([[source-events-xml]]). The matching
fleet-side out-of-fuel events do exist and are live — `NO_FUEL_FLEET` and its AE variant
`NO_FUEL_FLEET_DLC`, which adds `<environment type="PDS" target="player"/>`
([[source-events-fuel]]) — but neither references this id. **No source states the
trigger.**

> ⚠️ **Placement caveat.** As with its siblings, it sits under the *"Events For Testing"*
> comment block in `dlcEvents.xml`, among genuine dev stubs. Its prose is finished text,
> which is the argument for treating it as shipped content; the ambiguity is recorded
> rather than resolved.

## Text
> Your pilot deftly avoids the artillery fire from the surrounding fleet while you try to
> sort out exactly what your plan is....

Written inline in `dlcEvents.xml`, not in `text_events.xml` ([[source-dlcevents]]). The
trailing four-dot ellipsis is in the file.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — a single `<text>` tag)_ | — | Message only. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Strategy Notes
Nothing to play.

## Related
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]] — the other two AE additions
- [[concept-rebel-fleet-advance]] — the fleet mechanic this references
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name.
- [ ] Why this one reads as an ongoing state rather than an escape, unlike the other five
      `FUEL_ESCAPE_*` events.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — the sibling `FUEL_ESCAPE_*` events)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml — `NO_FUEL_FLEET`,
  `NO_FUEL_FLEET_DLC`)
