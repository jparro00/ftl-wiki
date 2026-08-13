---
id: event-rock-pirates-fight-near-sun
type: event
event_name: ROCK_PIRATE_SUN
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, pirate, sun, environmental-hazard, fire-hazard, default-rewards, unique]
---

# Rock pirates fight near sun — `ROCK_PIRATE_SUN`

## Summary
[[event-rock-pirates-fight]] with `<environment type="sun"/>`: an unavoidable fight
against a `ROCK_PIRATE` ship next to a star, with solar flares periodically setting rooms
on fire. The environment is the whole difference, and it is a bad one — the enemy crew is
all Rockmen, who are immune to fire.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `HOSTILE_ROCK` (`min="6" max="8"` per Rock sector,
  [[source-sector-data-xml]])
- Beacon: hostile, ship present, red giant hazard
  ([[source-fandom-rock-pirates-fight-near-sun]], `redgiant=true`,
  `LRSmap=ship+redgiant`)
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_PIRATE_SUN"/>` over a two-entry `textList`
([[source-events-rock]]): unusual solar activity with a pirate who won't let you leave, or
a Rock ship silhouetted against a supernova hailing *"Even out here you follow us! We only
wish to be left alone!"* Both are transcribed on
[[source-fandom-rock-pirates-fight-near-sun]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | Fight a Rock pirate ship (`<ship load="ROCK_PIRATE" hostile="true"/>`) beside a sun. Default rewards. | 100% |

## Blue Options
None.

## Rewards & Risks
- Victory: **default rewards** ([[source-fandom-rock-pirates-fight-near-sun]]).
- **No surrender offer** — `ROCK_PIRATE` has no `<surrender>` element
  ([[source-events-ships]]).
- Risk: solar flares start fires on *your* ship. The enemy crew is
  `<crewMember type="rock" prop="1"/>` — Rockmen take no fire damage
  ([[entity-rock-men]]), so the hazard is asymmetric against you unless your own crew is
  Rock or you have a Fire Suppression augment.

## Strategy Notes
- The asymmetry is the point: sun beacons are usually "both sides burn", but against an
  all-Rock crew only you burn. Kill fast or vent aggressively.
  *(Inference from the crew composition; no source states the asymmetry directly.)*

## Related
- [[event-rock-pirates-fight]] — plain version
- [[event-rock-pirates-fight-in-asteroid-field]] — asteroid variant
- [[event-boarders-rockmen-near-sun]] — the other Rock sun beacon, boarders instead of a ship
- [[concept-solar-flares]], [[entity-rock-men]]

## Open Questions
- [ ] Flare frequency and fire severity in AE (belongs on [[concept-solar-flares]]).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-pirates-fight-near-sun]] (per raw/wiki/rock-pirates-fight-near-sun.md)
