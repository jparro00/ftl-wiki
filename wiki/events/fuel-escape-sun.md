---
id: event-fuel-escape-sun
type: event
event_name: FUEL_ESCAPE_SUN
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, sun, orphan, engine-event, no-choice]
---

# Fuel escape (sun) — `FUEL_ESCAPE_SUN`

## Summary
A one-line resolution event: you were stranded without fuel next to a star and have now
drifted clear of it on residual power. No choices, no rewards, no ship — a single text tag
whose only job is to tell you the hazard is over. It is the **base-game original** of the
`FUEL_ESCAPE_*` family; the pulsar, PDS and fleet versions are Advanced Edition additions
in `dlcEvents.xml`.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_SUN` appears in `raw/gamedata/` only as its
own definition in `events.xml` (line 188) and its string in `text_events.xml`. No
`<eventList>`, `sectorDescription` or `load=` points at it ([[source-events-xml]],
[[source-text-events-xml]]).

How it is reached is an **inference, not a sourced fact**, and it is the same inference set
out in full on [[event-fuel-escape-pulsar]]:

- It sits in a block of one-line events in `events.xml` alongside `BOSS_STALEMATE`,
  `CREW_STUCK`, `AUGMENT_FULL`, `EQUIP_FULL`, `START_GAME` and `START_DEMO` — events the
  engine plainly invokes by hard-coded name rather than through the event pools
  ([[source-events-xml]]).
- Its two immediate neighbours, `FUEL_ESCAPE_STORM` and `FUEL_ESCAPE_ASTEROIDS`, cover the
  other two base-game beacon hazards; the AE file later adds exactly the hazards AE
  introduced. That is a complete, deliberate set, not stray test content.
- The out-of-fuel machinery itself lives in `events_fuel.xml` (`NO_FUEL`,
  `NO_FUEL_DISTRESS`, `NO_FUEL_FLEET`), none of which references these ids either
  ([[source-events-fuel]]).

Unlike the AE members of the family, this one is **not** filed under a *"Events For
Testing"* comment block — it sits in the structural/system section of `events.xml`, which
strengthens the engine-hook reading.

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> While waiting for help, you drained what little power you had left to pull away to a safe
> distance from the sun.

(`event_FUEL_ESCAPE_SUN_text`, per [[source-text-events-xml]]. Note the difference from the
AE members of the family, whose strings are written inline in `dlcEvents.xml` rather than
referenced from `text_events.xml`.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — a single `<text>` tag)_ | — | Message only. The hazard stops. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The event's value is that it *removes* a hazard, not that it grants anything.

## Strategy Notes
Nothing to play.

## Related
- [[event-fuel-escape-storm]], [[event-fuel-escape-asteroids]] — the other two base-game
  members of the family
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]], [[event-fuel-escape-fleet]] —
  the three Advanced Edition additions, and the fullest write-up of the family's provenance
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name when a fuel-stranded ship at a sun
      beacon survives long enough.
- [ ] Whether it fires automatically after a fixed time or on the rescue roll.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml — the out-of-fuel machinery that
  does *not* reference it)
