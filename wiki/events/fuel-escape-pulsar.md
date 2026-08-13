---
id: event-fuel-escape-pulsar
type: event
event_name: FUEL_ESCAPE_PULSAR
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, pulsar, orphan, engine-event, no-choice, advanced-edition]
---

# Fuel escape (pulsar) — `FUEL_ESCAPE_PULSAR`

## Summary
A one-line resolution event: you were stranded without fuel at a pulsar and have now pulled
clear of it. No choices, no rewards, no ship — a single text tag whose only job is to tell
you the hazard is over. It belongs to the small family of hazard "escape" lines the game
holds for out-of-fuel situations.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_PULSAR` appears exactly once in the whole
of `raw/gamedata/` — its own definition in `dlcEvents.xml` — and no `<eventList>`,
`sectorDescription` or `load=` reference points at it ([[source-dlcevents]]).

How it is actually reached is an **inference, not a sourced fact**:

- Three sibling events with the same `FUEL_ESCAPE_*` naming exist in `events.xml`:
  `FUEL_ESCAPE_SUN`, `FUEL_ESCAPE_STORM`, `FUEL_ESCAPE_ASTEROIDS`. They are also in no
  list, and they sit in a block of one-line events alongside `BOSS_STALEMATE`,
  `CREW_STUCK` and `AUGMENT_FULL` — events the game engine plainly invokes by hard-coded
  name rather than through the event pools ([[source-events-xml]]).
- The three `dlcEvents.xml` additions cover exactly the hazards the base three do not:
  pulsar, planetary defence, and the Rebel fleet. Pulsars and PDS are Advanced Edition
  hazards, so the file that adds AE hazards adding their escape lines fits.
- The out-of-fuel machinery lives in `events_fuel.xml` (`NO_FUEL`, `NO_FUEL_DISTRESS`,
  `NO_FUEL_FLEET`, `NO_FUEL_FLEET_DLC`), none of which references these ids either
  ([[source-events-fuel]]).

Conclusion recorded, with the uncertainty: this reads as **engine-called text for
escaping a pulsar while out of fuel**, but no source in `raw/` states the trigger.

> ⚠️ **Placement caveat.** In `dlcEvents.xml` this event sits under a comment block headed
> *"Events For Testing"*, alongside unmistakable dev stubs — `PULSAR` (*"Oh no! A
> pulsar!"*), `PDS_TEST`, and `NEWSHIP1`/`NEWSHIP2` (*"whatever"* / *"Yay"*). Unlike those,
> its prose is finished, in-voice, shipped text. Two readings are possible: a real engine
> hook that was simply typed into the scratch area of the file, or leftover test content.
> The polished wording and the exact match to the `events.xml` family favour the first.

## Text
> Taking advantage of the last of your fuel reserves, you were able to navigate to a safe
> distance from the pulsar.

The string is written **inline** in `dlcEvents.xml` rather than referenced from
`text_events.xml`, unlike its `events.xml` siblings, whose text lives at
`event_FUEL_ESCAPE_SUN_text` and friends ([[source-dlcevents]], [[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event is a single `<text>` tag)_ | — | Message only. No reward, no damage, no ship. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. It is a status message.

## Strategy Notes
Nothing to play. Recorded so the id is not mistaken for a live encounter.

## Related
- [[event-fuel-escape-pds]], [[event-fuel-escape-fleet]] — the other two AE additions,
  identical in structure
- `FUEL_ESCAPE_SUN` / `FUEL_ESCAPE_STORM` / `FUEL_ESCAPE_ASTEROIDS` — the vanilla
  originals in `events.xml`, not yet paged
- [[concept-out-of-fuel]] — the mechanic these belong to

## Open Questions
- [ ] Confirm the engine actually loads these three by hard-coded name (would need code or
      in-game observation, not the XML).
- [ ] Whether a pulsar beacon can strand you out of fuel at all in normal play.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — the sibling `FUEL_ESCAPE_*` events)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml — the out-of-fuel machinery)
