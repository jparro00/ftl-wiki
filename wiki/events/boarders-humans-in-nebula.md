---
id: event-boarders-humans-in-nebula
type: event
event_name: NEBULA_BOARDING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, boarding, crew-risk, no-choice, no-reward, unique]
---

# Boarders: Humans in nebula — `NEBULA_BOARDING`

## Summary
The nebula's ambush. No ship on the map, no choices, no reward — 2 to 4 human boarders
simply appear inside your hull. It is the pure-downside member of the nebula pool, and the
only thing separating it from its plasma-storm twin
[[event-boarders-humans-in-plasma-storm]] is that the storm version at least pays you.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_HOSTILE` and `NEBULA_PIRATE`
  ([[source-events-nebula]], [[source-events-pirate]]).
- Allocation: `NEBULA` 0–4 in [[sector-federation-space]] and 0–8 in
  [[sector-civilian-sector]]; `NEBULA_PIRATE` 0–5 in [[sector-pirate-controlled-sector]];
  `NEBULA_HOSTILE` 5–6 in [[sector-uncharted-nebula]] ([[source-sector-data-xml]]).
- **Long-range scanners show no ship** (`LRSmap=noship+nebula`,
  [[source-fandom-boarders-humans-in-nebula]]) — the beacon looks empty right up until the
  boarders land.

## Text
The prose is drawn from the `NEBULA_BOARDING_TEXT` list and **varies across three
strings** ([[source-events-nebula]], [[source-text-events-xml]]):

> You see a small station nearby and feel the shudder of shots ringing through the ship.
> You can't be sure without sensors, but it seems there may be intruders on the ship!

> You arrive in the nebula and immediately receive a message from an unknown source,
> "Prepare to be boarded!" With the static from the nebula, there's no way to tell where
> they came from, but you hear shots fired on board the ship.

> You see a number of derelict ships near this beacon. After a short time you hear the
> tell-tale sounds of a teleporter and shouts coming from within the ship. You've been
> boarded!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | `<boarders min="2" max="4" class="human"/>` — 2–4 human intruders beam aboard. No enemy ship, no scrap, no reward of any kind. | 100% |

The complete event body is a text list, an environment tag, and that one `boarders`
element ([[source-events-nebula]]).

## Blue Options
None.

## Rewards & Risks
- **Reward: none.** The event attaches no `autoReward`.
- Risk: 2–4 boarders, fought with your sensors offline so you cannot see which rooms they
  occupy from the ship view. Human boarders have no special traits, which makes this the
  mildest of the boarding events by species — but 4 of them is still a real threat to a
  thin crew.

## Strategy Notes
- Because there is no ship to shoot, nothing about your weapon loadout matters; this event
  is decided entirely by crew count, Medbay/Clone Bay, and door control.
- The `unique="true"` flag means surviving it once removes it from the pool for the rest
  of the run.

## Related
- [[event-boarders-humans-in-plasma-storm]] — 3–4 boarders, storm environment, **and** a
  medium reward
- [[event-empty-nebula-beacon]] — what this beacon looks like on the map right before it
  isn't
- [[sector-uncharted-nebula]], [[sector-civilian-sector]]

## Open Questions
- [ ] Whether the three text variants are equally weighted.

## Notes on sector coverage
> ⚠️ **CONTRADICTION:** [[source-fandom-boarders-humans-in-nebula]] lists three sectors
> (Civilian, Pirate Controlled, Uncharted Nebula). The event lists in the game files also
> put it in [[sector-federation-space]], because `sector_data.xml` allocates the `NEBULA`
> list to `STANDARD_SPACE` at `min=0 max=4` ([[source-sector-data-xml]],
> [[source-newevents]]).
>
> Trusting the game files — reliability `high` vs `medium`. The same omission appears on
> several sibling Fandom pages in this batch, which suggests the wiki's `{{Locations}}`
> template simply does not model Federation Space's nebula allocation.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-humans-in-nebula]] (per raw/wiki/boarders-humans-in-nebula.md)
