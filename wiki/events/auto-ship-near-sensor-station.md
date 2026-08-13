---
id: event-auto-ship-near-sensor-station
type: event
event_name: AUTO_DEFENSE_MAP
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: false
blue_options: [[[item-sensors]], [[item-teleporter]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, unique, map-reveal, blue-option, optional-fight]
---

# Auto-ship near sensor station — `AUTO_DEFENSE_MAP`

## Summary
A map-reveal beacon guarded by an auto-ship. Fight it for scrap and the map, or use one of
two blue options to take the map without a fight — **Teleporter is a guaranteed free
reveal**, while **Sensors 3** is a coin-flip that can start the fight anyway. The only
event in `events_rebel.xml` with two separate blue options.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]) and `NEUTRAL_CIVILIAN`
  ([[source-newevents]] — the list drawn before the generic `NEUTRAL` pool in civilian
  sectors). It has **no AE `OVERRIDE_*` entry**, unlike most of its siblings.
- `NEUTRAL_REBEL` is allocated `min=5 max=6` per Rebel sector
  ([[source-sector-data-xml]]).
- `unique="true"` — at most once per run.
- `<img planet="PLANET_POPULATED"/>` ([[source-events-rebel]]).
- Long-range scanners show a ship ([[source-fandom-auto-ship-near-sensor-station]]).

## Text
> You detect a Rebel automated ship nearby. It does not engage and seems to be patrolling
> around a long-range sensor station.

(`event_AUTO_DEFENSE_MAP_text`, per [[source-text-events-xml]])

The event loads `<ship load="REBEL_AUTO_MAP" hostile="false"/>` — the ship is present but
passive ([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the automated ship to get to the sensor station. | — | The ship turns hostile. Destroy it → *"You access the recent scans from the unguarded station. Your map has been updated with details of the surrounding area."* → `<reveal_map/>` **and** `autoReward level="LOW"` `scrap_only`. | 100% |
| 2 | Avoid provoking the ship. | — | No text, no effect — nothing happens. | 100% |
| 3 | **(Sensors)** Use your sensors to attempt to access the data. | `req="sensors"`, `lvl="3"`, `hidden="true"` | Rolls the two-entry `AUTO_DEFENSE_MAP_SENSORS` list: **(a)** *"Your improved Sensors are able to remotely access and download the public radar station's local map data."* → `<reveal_map/>`, no fight; **(b)** *"The automated ship must be remotely connected to the station; as soon as you attempt to log on, the ship activates and charges you."* → the ship turns hostile, resolving as choice 1. | unknown — two entries, no weights stated |
| 4 | **(Teleporter)** Beam directly onto the station to try to avoid detection. | `req="teleporter"`, `hidden="true"` | *"Once on board, your crew is able to access and download the long-range scanner's archived information. Your map has been updated."* → `<reveal_map/>`. No fight, no scrap. | 100% |

### The `REBEL_AUTO_MAP` ship
`auto_blueprint="SHIPS_AUTO"`. Only a `destroyed` branch is defined — **no surrender, no
escape, no `deadCrew`** ([[source-events-ships]]). Its reward is `scrap_only`, not
`standard`: no fuel/missiles/drone parts come with it.

## Blue Options
- **[[item-sensors]] level 3** (`req="sensors" lvl="3"`) — an *attempt*, not a guarantee.
  Half the branch (one of two list entries) reveals the map for free; the other half
  provokes the fight you were trying to avoid. Note that Sensors 3 is the maximum level of
  the system, so this is a fully-upgraded-Sensors gate, not a cheap one.
- **[[item-teleporter]]** (`req="teleporter"`, no level) — **strictly the best option
  present**: a guaranteed map reveal, no fight, no roll. Owning the system is the whole
  requirement.

## Rewards & Risks
- Reward: the current sector map revealed, on every path except "avoid". Choice 1 adds
  `LOW` `scrap_only`.
- Risk: only choice 1 (and the bad half of choice 3) commits you to an auto-ship fight —
  no crew, no surrender, no escape.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* With a Teleporter, take choice 4 without thinking — free map, zero risk.
  Without one, choice 3 at Sensors 3 is a strictly better gamble than choice 1 *only if*
  you do not want the scrap; if you want the scrap you have to fight anyway, so choice 1 is
  the honest option.
- Map reveal in a Rebel sector is worth more than usual: it lets you plan a route that
  minimises exposure to the fleet.

## Related
- [[event-auto-ship-near-radar-station]] — the sibling with a Combat Drone gate and fleet-delay outcomes
- [[event-auto-ship-near-storage-station]] — the sibling with a Cloaking gate and item loot
- [[event-deactivated-auto-ship]] — another Sensors-3 map-reveal beacon
- [[item-sensors]], [[item-teleporter]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Split between the two `AUTO_DEFENSE_MAP_SENSORS` entries — the file states no weights.
- [ ] Numeric value of `LOW` `scrap_only`.
- [ ] Why this event has no AE `OVERRIDE_*` list entry when its siblings do.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-auto-ship-near-sensor-station]] (per `raw/wiki/auto-ship-near-sensor-station.md`)
