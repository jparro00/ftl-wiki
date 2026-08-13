---
id: event-rock-fight-in-asteroid-field
type: event
event_name: ROCK_FIGHT_ASTEROID
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, asteroid-field, environmental-hazard, default-rewards, unique]
---

# Rock fight in asteroid field — `ROCK_FIGHT_ASTEROID`

## Summary
[[event-rock-fight]] with an asteroid field bolted on. Same enemy (`ROCK_SHIP`), same
lack of choices, but `<environment type="asteroid"/>` means both ships take continuous
asteroid impacts for the whole engagement. Marked `unique="true"`, so it fires at most
once per sector.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `HOSTILE_ROCK` (allocated `min="6" max="8"` per Rock sector,
  [[source-sector-data-xml]])
- Beacon: hostile, ship present, asteroid hazard
  ([[source-fandom-rock-fight-in-asteroid-field]], `LRSmap=ship+asteroidfield`)
- `unique="true"` — once per sector at most ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_FIGHT_ASTEROID"/>` over a three-entry `textList`
([[source-events-rock]]): a Rock mining vessel treating you as a transgressor, a rookie
cargo ship that routed straight through the field, and a fatalistic lost freighter
captain ("What must be must be. Death to all."). All three are transcribed on
[[source-fandom-rock-fight-in-asteroid-field]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | Fight a Rock ship (`<ship load="ROCK_SHIP" hostile="true"/>`) inside an asteroid field. Default rewards. | 100% |

## Blue Options
None.

## Rewards & Risks
- Victory: **default rewards** ([[source-fandom-rock-fight-in-asteroid-field]]).
- Because the enemy is `ROCK_SHIP`, the `<surrender chance="0.7" min="3" max="4">` branch
  applies here too — see [[event-rock-fight]] for the surrender outcomes
  ([[source-events-ships]]).
- Risk: asteroids hit shields and hull continuously and will start fires. Neither source
  states the asteroid damage rate — that is a general environment mechanic, not part of
  this event.

## Strategy Notes
- The asteroid field cuts both ways: it also chews the Rock ship, and a defence drone or
  a spare shield layer converts the hazard into an advantage. This is inference from the
  event structure, **not** a sourced claim.
- Do not linger to farm the surrender offer here — every extra second is free hull damage.

## Related
- [[event-rock-fight]] — the plain version, same enemy ship
- [[event-rock-pirates-fight-in-asteroid-field]] — pirate twin, same environment
- [[event-rock-fight-with-boarders-in-asteroid-field]] — same environment plus boarders
- [[concept-asteroid-fields]], [[entity-rock-men]]

## Open Questions
- [ ] Asteroid impact rate and damage in AE (belongs on [[concept-asteroid-fields]]).
- [ ] Whether the surrender offer actually fires in an environment beacon.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-fight-in-asteroid-field]] (per raw/wiki/rock-fight-in-asteroid-field.md)
