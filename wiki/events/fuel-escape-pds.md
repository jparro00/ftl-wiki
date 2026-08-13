---
id: event-fuel-escape-pds
type: event
event_name: FUEL_ESCAPE_PDS
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [out-of-fuel, pds, orphan, engine-event, no-choice, advanced-edition]
---

# Fuel escape (planetary defence) — `FUEL_ESCAPE_PDS`

## Summary
A one-line resolution event: you were stranded without fuel under a hostile planet's
Anti-Ship Battery and have now pulled out of its range on impulse power. No choices, no
rewards, no ship.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_PDS` appears exactly once in
`raw/gamedata/` — its own definition in `dlcEvents.xml` — with nothing referencing it
([[source-dlcevents]]).

The reasoning for how it is reached is set out in full on
[[event-fuel-escape-pulsar]] and applies identically here: it matches the
`FUEL_ESCAPE_SUN` / `_STORM` / `_ASTEROIDS` family in `events.xml`, which sits among
events the engine calls by hard-coded name (`BOSS_STALEMATE`, `CREW_STUCK`,
`AUGMENT_FULL`) rather than through event pools ([[source-events-xml]]). PDS hazards are
an Advanced Edition addition, which is why this one lives in the AE file. **No source in
`raw/` states the trigger**; this is inference from structure.

> ⚠️ **Placement caveat.** It sits under the *"Events For Testing"* comment block in
> `dlcEvents.xml`, next to the obvious stub `PDS_TEST` (*"Oh no! This planet is friendly to
> the Rebels and is shooting at us!"*). Its own prose is finished, shipped-quality text,
> which is the main reason for treating it as real content rather than a stub — but the
> ambiguity is recorded, not resolved.

## Text
> Using your impulse engines, you were able to pull to a safe distance from the hostile
> planet.

Written inline in `dlcEvents.xml` rather than in `text_events.xml`
([[source-dlcevents]]).

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
- [[event-fuel-escape-pulsar]] — the fullest write-up of this family's provenance
- [[event-fuel-escape-fleet]] — the third AE addition
- [[event-lanius-fight-with-friendly-asb-support]] — the one PDS encounter in this batch
  where the battery is on your side
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — the sibling `FUEL_ESCAPE_*` events)
