---
id: event-rebel-ship-attacking-refueling-outpost
type: event
event_name: SQUAT_REFUEL_STATION
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-the-last-stand]]]
beacon_type: hostile
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, unique, optional-fight, fuel-reward, stacked-reward]
---

# Rebel ship attacking refueling outpost — `SQUAT_REFUEL_STATION`

## Summary
The crewed twin of [[event-auto-ship-attacking-outpost]]: intervene against a Rebel scout
threatening a fuel depot, and the depot pays you in **fuel** on top of the combat reward.
One of the few reliable fuel sources outside a store, and it is one of only five entries in
the `BOSS_NEUTRAL` list — so it can also turn up in [[sector-the-last-stand]].

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-the-last-stand]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), `OVERRIDE_HOSTILE2` ([[source-dlceventsoverwrite]]), and
  `BOSS_NEUTRAL` ([[source-events-boss]]) — one of five entries in the Last Stand's neutral
  pool.
- `NEUTRAL_REBEL` is allocated `min=5 max=6` per Rebel sector ([[source-sector-data-xml]]).
- `unique="true"` — at most once per run.
- `<img planet="PLANET_POPULATED_SMALL"/>` ([[source-events-rebel]]).
- Long-range scanners show a ship ([[source-fandom-rebel-ship-attacking-refueling-outpost]]).

## Text
> You detect a Rebel scout on an attack approach to a small refueling outpost. Their weapons
> are charged, but they're not firing yet.

(`event_SQUAT_REFUEL_STATION_text`, per [[source-text-events-xml]])

The event loads `<ship load="SQUAT_REFUEL_STATION" hostile="false"/>` — present but not
hostile until you commit ([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Intervene to defend the outpost. | — | *"The rebel responds to your threat, 'I don't know who you are, but no one defies the Rebel Fleet!' They move in to engage."* → the ship turns hostile. Destroy it → `autoReward level="MED"` `standard`; kill the crew → `autoReward level="HIGH"` `standard`. Either way a hidden follow-up adds `autoReward level="MED"` `fuel`. | 100% (deterministic) |
| 2 | Avoid the conflict. | — | *"The Rebel ship fires some warning shots but eventually powers down their weapons. The outpost seems to have given them what they demanded."* → nothing happens. | 100% |

### The `SQUAT_REFUEL_STATION` ship
`auto_blueprint="SHIPS_REBEL"`. **No surrender and no escape branch** — both the file and
[[source-fandom-rebel-ship-attacking-refueling-outpost]] agree
([[source-events-ships]]):

| Branch | Text | Reward |
|---|---|---|
| `destroyed` | *"The ship breaks apart and you quickly salvage what you can."* | `MED` `standard` |
| `deadCrew` | *"With the crew dead you quickly salvage what you can."* | `HIGH` `standard` |

Both then offer the same hidden `continue`:

> The outpost hails you, "The pompous bastards expected free service just because they
> defeated the Federation. Take this for the help."

→ `autoReward level="MED"` `fuel`. Fandom reads `MED` `fuel` as **2–4 fuel**
([[source-fandom-rebel-ship-attacking-refueling-outpost]]); the game file states only the
level, not a number ([[source-events-ships]]).

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` (hull kill) or `HIGH` (crew kill) `standard`, **plus** `MED` `fuel` — the
  fuel is unconditional once you win.
- Risk: a crewed Rebel warship at sector strength, with **no surrender and no escape** to
  end the fight early. Unlike the auto-ship version, boarding you is possible if the
  blueprint rolls a teleporter.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* Take it whenever fuel is anything less than comfortable — a guaranteed 2–4
  fuel with a `MED`/`HIGH` scrap payout attached is better than most store trips, and the
  fuel arrives without spending scrap.
- The crew-kill branch pays a full reward tier more than the hull kill. If you board, board
  early; the ship will not surrender to save itself.
- In [[sector-the-last-stand]] it is one of five `BOSS_NEUTRAL` entries — a rare chance to
  top up fuel while dodging the flagship.

## Related
- [[event-auto-ship-attacking-outpost]] — the unmanned twin, no fuel, lower risk
- [[event-rebel-fight]] — the plain Rebel fight
- [[sector-the-last-stand]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Numeric values of `MED`/`HIGH` `standard` and `MED` `fuel` (Fandom's 2–4 is a
      community reading, not a file value).
- [ ] Whether the `SHIPS_REBEL` roll here can include a teleporter at low sector depth.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-boss]] (per `raw/gamedata/events_boss.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-ship-attacking-refueling-outpost]] (per `raw/wiki/rebel-ship-attacking-refueling-outpost.md`)
