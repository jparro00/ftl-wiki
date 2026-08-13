---
id: event-rock-fight-with-boarders-in-asteroid-field
type: event
event_name: ROCK_BOARDERS_ASTEROID
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rock, boarders, asteroid-field, environmental-hazard, crew-risk, default-rewards, unique]
---

# Rock fight with boarders in asteroid field — `ROCK_BOARDERS_ASTEROID`

## Summary
A Rock ship fight, plus 1–2 Rockman boarders on arrival, plus an asteroid field. Three
pressures at once and no choice offered. It carries **one fewer** maximum boarder than
[[event-rock-fight-with-boarders]] (1–2 rather than 1–3), which is the only mercy here.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `BOARDERS_ROCK`, allocated `min="1" max="2"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: hostile, ship present, asteroid hazard
  ([[source-fandom-rock-fight-with-boarders-in-asteroid-field]],
  `LRSmap=ship+asteroidfield`)
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_BOARDERS_ASTEROID"/>` over a two-entry `textList`
([[source-events-rock]]): evasive manoeuvres interrupted by a clunk that turns out to be a
teleport rather than a hull hit, or stumbling onto a Rock pirate stronghold mid-field.
Both are transcribed on
[[source-fandom-rock-fight-with-boarders-in-asteroid-field]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<boarders min="1" max="2" class="rock"/>` — 1–2 Rockmen board immediately — plus `<environment type="asteroid"/>` and `<ship load="ROCK_SHIP" hostile="true"/>`. Default rewards on victory. | 100% |

## Blue Options
None.

## Rewards & Risks
- Victory: **default rewards**
  ([[source-fandom-rock-fight-with-boarders-in-asteroid-field]]).
- Enemy is `ROCK_SHIP`, so the surrender branch can fire — see [[event-rock-fight]].
- Risk stack: asteroid impacts + 1–2 fire-immune boarders + an active enemy ship. Losing
  shields to asteroids while your crew is off fighting boarders is the failure mode.

## Strategy Notes
- The boarders arrive *before* the fight is joined, so the first decision is where to
  meet them, not what to shoot. *(Inference from event ordering in the XML, where
  `<boarders>` precedes `<ship>`; no source states a turn order.)*
- Asteroid damage is untargeted, so keeping a crew member in Shields is worth more here
  than in the plain boarding event.

## Related
- [[event-rock-fight-with-boarders]] — same idea, up to 3 boarders, no asteroids
- [[event-boarders-rockmen-near-sun]] — 2–3 boarders, no ship, solar hazard
- [[event-rock-fight-in-asteroid-field]] — same environment without boarders
- [[entity-rock-men]], [[concept-asteroid-fields]], [[concept-blue-options]]

## Open Questions
- [ ] Whether boarders land before, with, or after the enemy ship becomes active.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-fight-with-boarders-in-asteroid-field]] (per raw/wiki/rock-fight-with-boarders-in-asteroid-field.md)
