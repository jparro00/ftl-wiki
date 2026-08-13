---
id: event-fuel-escape-asteroids
type: event
event_name: FUEL_ESCAPE_ASTEROIDS
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, asteroid-field, orphan, engine-event, no-choice]
---

# Fuel escape (asteroid field) — `FUEL_ESCAPE_ASTEROIDS`

## Summary
A one-line resolution event: you were stranded without fuel in an asteroid field and have
now navigated clear of it on impulse engines. No choices, no rewards, no ship. One of the
three base-game members of the `FUEL_ESCAPE_*` family.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_ASTEROIDS` appears in `raw/gamedata/` only
as its own definition in `events.xml` (line 196) and its string in `text_events.xml`
([[source-events-xml]], [[source-text-events-xml]]).

The reasoning for how it is reached is set out on [[event-fuel-escape-sun]] and
[[event-fuel-escape-pulsar]] and applies identically: it sits in a block of one-line events
the engine invokes by hard-coded name (`BOSS_STALEMATE`, `CREW_STUCK`, `AUGMENT_FULL`,
`EQUIP_FULL`), and nothing in `events_fuel.xml` — where the out-of-fuel machinery lives —
references it ([[source-events-fuel]]). **No source in `raw/` states the trigger.**

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> While waiting, you managed to navigate out of the asteroid field using only your impulse
> engines.

(`event_FUEL_ESCAPE_ASTEROIDS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — a single `<text>` tag)_ | — | Message only. The asteroid barrage stops. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Strategy Notes
Nothing to play. Worth knowing that running dry in an asteroid field is survivable — the
game has a written escape for it.

## Related
- [[event-fuel-escape-sun]], [[event-fuel-escape-storm]] — the other two base-game members
  of the family
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]], [[event-fuel-escape-fleet]] —
  the Advanced Edition additions
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name.
- [ ] Whether engine level or Piloting affects it, given the prose credits impulse engines.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml — the out-of-fuel machinery that
  does *not* reference it)
