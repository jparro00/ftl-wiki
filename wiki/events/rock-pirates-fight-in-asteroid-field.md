---
id: event-rock-pirates-fight-in-asteroid-field
type: event
event_name: ROCK_PIRATE_ASTEROID
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, pirate, asteroid-field, environmental-hazard, default-rewards, unique]
---

# Rock pirates fight in asteroid field — `ROCK_PIRATE_ASTEROID`

## Summary
[[event-rock-pirates-fight]] with `<environment type="asteroid"/>` attached: an
unavoidable fight against a `ROCK_PIRATE` ship while asteroids batter both hulls. No
choices, no surrender offer, `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `HOSTILE_ROCK` (`min="6" max="8"` per Rock sector,
  [[source-sector-data-xml]])
- Beacon: hostile, ship present, asteroid hazard
  ([[source-fandom-rock-pirates-fight-in-asteroid-field]], `LRSmap=ship+asteroidfield`)
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_PIRATE_ASTEROID"/>` over a two-entry `textList`
([[source-events-rock]]): shields sparking in the wake of a huge asteroid with a lost
aggressive pirate behind it, or a shot that "was no asteroid". Both are transcribed on
[[source-fandom-rock-pirates-fight-in-asteroid-field]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | Fight a Rock pirate ship (`<ship load="ROCK_PIRATE" hostile="true"/>`) inside an asteroid field. Default rewards. | 100% |

## Blue Options
None.

## Rewards & Risks
- Victory: **default rewards**
  ([[source-fandom-rock-pirates-fight-in-asteroid-field]]).
- **No surrender.** `ROCK_PIRATE` carries no `<surrender>` element, unlike `ROCK_SHIP`
  ([[source-events-ships]]). The fight runs to
  destruction or dead crew.
- All-Rockman crew (`<crewMember type="rock" prop="1"/>`) — fire-immune, tough boarders.
- Risk: continuous asteroid damage on top of an enemy you cannot buy off. This is the
  more dangerous of the two asteroid Rock fights for exactly that reason.

## Strategy Notes
- Combines the two things that make Rock beacons expensive — an environment hazard and a
  no-surrender all-Rock crew. If you are already hurt, this is the beacon to route around.
  *(Opinion, inferred from the event structure; no source states it.)*

## Related
- [[event-rock-pirates-fight]] — the plain version
- [[event-rock-pirates-fight-near-sun]] — solar variant
- [[event-rock-fight-in-asteroid-field]] — non-pirate twin, same environment
- [[concept-asteroid-fields]], [[entity-rock-men]]

## Open Questions
- [ ] Whether `SHIPS_ROCK_PIRATE` differs from `SHIPS_ROCK` in loadout or hull, beyond the
      crew composition and the missing surrender branch.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-pirates-fight-in-asteroid-field]] (per raw/wiki/rock-pirates-fight-in-asteroid-field.md)
