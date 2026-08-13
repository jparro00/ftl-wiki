---
id: event-boarders-rockmen-near-sun
type: event
event_name: ROCK_BOARDERS_SUN
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rock, boarders, sun, environmental-hazard, fire-hazard, crew-risk, no-enemy-ship, unique]
---

# Boarders: Rockmen near sun — `ROCK_BOARDERS_SUN`

## Summary
The purest boarding beacon in Rock space: **no enemy ship at all**, just 2–3 Rockmen in
your corridors while a star sets your rooms on fire. The absence of a ship is not relief —
it removes every reward from the encounter and leaves only the crew fight.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `BOARDERS_ROCK`, allocated `min="1" max="2"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: **no ship present**, red giant hazard
  ([[source-fandom-boarders-rockmen-near-sun]], `redgiant=true`, `LRSmap=noship+redgiant`
  — and the game files agree: the event has no `<ship>` element at all,
  [[source-events-rock]])
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
Varies — `<text load="ROCK_BOARDERS_SUN"/>` over a two-entry `textList`
([[source-events-rock]]): a teleporter and shouts of *"Prepare to burn, fleshy meat-sack
aliens!"*, or drifting past a hidden outlaw Rock settlement that has settled close to the
star because of their heat resistance. Both are transcribed on
[[source-fandom-boarders-rockmen-near-sun]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<boarders min="2" max="3" class="rock"/>` — 2–3 Rockmen board — under `<environment type="sun"/>`. **No enemy ship, no `autoReward`.** | 100% |

## Blue Options
None.

## Rewards & Risks
- **No reward.** The event grants nothing: no `autoReward`, no ship to destroy, no items
  ([[source-events-rock]]). [[source-fandom-boarders-rockmen-near-sun]] likewise lists no
  reward and does **not** carry the `Fights with Default Rewards` category its siblings do.
- Risk: the highest guaranteed boarder floor of the three `BOARDERS_ROCK` events — a
  minimum of **2**, up to 3 — plus solar flares. Rockmen are fire-immune
  ([[entity-rock-men]]), so the flares hurt only you and your ship, never the boarders.
  You cannot burn them out and you cannot vent-and-ignite.

## Strategy Notes
- This is the worst risk/reward beacon in the Rock event pool: maximum boarders, an
  environmental hazard that is asymmetric against you, and zero payout. If long-range
  scanners show a red giant with **no ship** in a Rock sector, this is a strong candidate
  for what is waiting. *(Opinion, from the event's own contents; the sources state the
  facts but not the judgement.)*
- Suffocation in a vented room is the realistic answer — Rockmen do not breathe faster
  than anyone else, but they will not burn.

## Related
- [[event-rock-fight-with-boarders]] — 1–3 boarders, but with a ship and rewards
- [[event-rock-fight-with-boarders-in-asteroid-field]] — 1–2 boarders, asteroids
- [[event-rock-pirates-fight-near-sun]] — the other Rock sun beacon, ship instead of boarders
- [[entity-rock-men]], [[concept-solar-flares]], [[concept-blue-options]]

## Open Questions
- [ ] Confirm no reward on a played run — a zero-payout boarding beacon is unusual enough
      to be worth verifying against the game rather than the file alone.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-rockmen-near-sun]] (per raw/wiki/boarders-rockmen-near-sun.md)
