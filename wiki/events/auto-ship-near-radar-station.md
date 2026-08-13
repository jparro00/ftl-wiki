---
id: event-auto-ship-near-radar-station
type: event
event_name: AUTO_DEFENSE_RADAR
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: false
blue_options: [[[item-combat-drone-mark-i]], [[item-hacking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, unique, blue-option, drone-parts-cost, fleet-delay, fleet-advance-risk, map-reveal, optional-fight]
---

# Auto-ship near radar station — `AUTO_DEFENSE_RADAR`

## Summary
The most branching event in `events_rebel.xml`, and the only one that can **delay the Rebel
fleet**. A dormant auto-ship guards a relay station; get to the station's console — by
killing the ship, or by baiting it away with a combat drone — and you roll on
`DEFENSE_RADAR_LIST`, which can buy a pursuit turn back, reveal the map, do nothing, or
*advance* the fleet. A Hacking blue option on the post-fight branch skips the gamble
entirely and takes the two good outcomes together.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]] **only**.
- Event list: `NEUTRAL_REBEL` and nothing else — no generic pool, no AE `OVERRIDE_*` entry
  ([[source-events-rebel]]). `NEUTRAL_REBEL` is allocated `min=5 max=6` per Rebel sector
  ([[source-sector-data-xml]]).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-auto-ship-near-radar-station]]).

## Text
> A Rebel automated ship sits dormant near a Rebel forward radar station.

(`event_AUTO_DEFENSE_RADAR_text`, per [[source-text-events-xml]])

The event loads `<ship load="REBEL_AUTO_RADAR" hostile="false"/>` — dormant, not hostile
([[source-events-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Approach the station. | — | *"The ship powers up and targets you."* → fight `REBEL_AUTO_RADAR`. On destruction: `MED` `scrap_only` and a **three-way follow-up** (see below). | 100% |
| 2 | Keep your distance and wait for the FTL to charge. | — | No text, no effect — nothing happens. | 100% |
| 3 | **(Combat Drone)** Send a drone to distract the automated ship. | `req="COMBAT_DRONE_LIST"`, `hidden="true"` | Rolls the three-entry `AUTO_DEFENSE_RADAR_COMBAT` list. **Every entry costs 1 drone part.** Two of three reach the station → `DEFENSE_RADAR_LIST`; one is a failure → the ship turns hostile, resolving as choice 1. | unknown — three entries, no weights stated |

### Choice 3 — `AUTO_DEFENSE_RADAR_COMBAT`
Each of the three entries carries `<item_modify><item type="drones" min="-1" max="-1"/></item_modify>`
— **the drone part is spent whatever happens** ([[source-events-rebel]]):

| Entry | Text | Result |
|---|---|---|
| 1 | *"Your combat drone attacks the automated ship and then retreats, luring it away. You quickly move up to the radar station to access it."* | −1 drone part → `DEFENSE_RADAR_LIST` |
| 2 | *"Your combat drone repeatedly fires at the automated ship. It can't break through its shields, but is at least enough of a distraction to allow you to access the radar station."* | −1 drone part → `DEFENSE_RADAR_LIST` |
| 3 | *"Before your drone has a chance to attack, the automated ship activates and shoots it down. It then detects your ship and moves in on your position."* | −1 drone part → **fight**, as choice 1 |

### The `REBEL_AUTO_RADAR` ship and its follow-up
`auto_blueprint="SHIPS_AUTO"`, only a `destroyed` branch — no surrender, no escape, no
`deadCrew` ([[source-events-ships]]):

> You salvage what you can and approach the station. It is used to relay information to the
> Rebel Fleet. You could attempt to hack it to give the Rebels false information.

→ `autoReward level="MED"` `scrap_only`, then three choices:

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| a | Attempt to manually hack into the station. | — | Rolls `DEFENSE_RADAR_LIST` |
| b | Don't risk it. Leave the station. | — | Nothing |
| c | **(Hacking)** Use a drone to hack into the station. | `req="hacking"`, `hidden="true"` | *"You successfully hack into their system and transmit false information about your location… You also are able to download data about the surrounding beacons."* → `<reveal_map/>` **and** `<modifyPursuit amount="-1"/>` **and** −1 drone part. Guaranteed — no roll. |

### `DEFENSE_RADAR_LIST` — the console gamble
Four entries, one drawn at random; the file states no weights, so odds are **unknown**
([[source-events-rebel]], [[source-text-events-xml]]):

| Entry | Text | Result |
|---|---|---|
| 1 | *"You successfully hack into their system and transmit false information about your location. That should hold off the fleet for at least a little while."* | `<modifyPursuit amount="-1"/>` — **fleet delayed** |
| 2 | *"The firewalls prove too difficult to bypass… you stumble across unprotected information about the surrounding beacons. Your map is updated."* | `<reveal_map/>` |
| 3 | *"You are unable to penetrate the computer's defenses. You give up and return to the ship."* | nothing |
| 4 | *"As you attempt to hack in, you set off a hidden alarm system… the Rebels must surely be aware of your position!"* | `<modifyPursuit amount="1"/>` — **fleet advanced** |

One entry in four is actively harmful.

## Blue Options
- **Combat drone** (`req="COMBAT_DRONE_LIST"`, `hidden="true"`) — the requirement is a
  *blueprint list*, not a system. `COMBAT_DRONE_LIST` in `raw/gamedata/autoBlueprints.xml`
  contains `COMBAT_1`, `COMBAT_2`, `COMBAT_BEAM`, `COMBAT_BEAM_2`, `DRONE_FIREBEAM`
  ([[source-autoblueprints]]). [[source-fandom-auto-ship-near-radar-station]] names the
  first four as Combat Drone Mark I, Combat Drone Mark II, Anti-Ship Beam Drone I and
  Anti-Ship Beam Drone II. It **omits `DRONE_FIREBEAM`** — and that is probably correct in
  effect, because `DRONE_FIREBEAM` is a `weaponBlueprint` (the Fire Beam carried *by* the
  Fire Drone `COMBAT_FIRE`), not a drone the player can own
  (per `raw/gamedata/dlcBlueprints.xml`, which has no source page in this wiki yet).
  Recorded as a data oddity
  rather than a contradiction; it is not established here whether owning a Fire Drone
  satisfies the check.
  Costs **1 drone part** on every branch.
- **[[item-hacking]]** (`req="hacking"`, `hidden="true"`) — appears only *after* you destroy
  the ship, on the station follow-up. It is the best outcome in the event: map reveal **and**
  fleet delay together, guaranteed, for 1 drone part — versus a 1-in-4 chance of either one
  alone (and a 1-in-4 chance of making things worse) on the manual hack.

## Rewards & Risks
- Reward: `MED` `scrap_only` from the kill; then some combination of map reveal and
  `modifyPursuit -1`.
- Cost: **drone parts**. Choice 3 always spends one; the Hacking follow-up spends one more.
- Risk: `DEFENSE_RADAR_LIST` entry 4 advances the fleet. The failure branch of choice 3
  spends a drone part *and* starts the fight.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* If you have Hacking, the correct line is **choice 1 → kill the ship →
  choice (c)**: it converts a four-way gamble into a guaranteed map + fleet delay, and the
  fleet delay is worth more in a Rebel sector than anywhere else. Choice 3 is for ships
  that cannot win the fight cheaply.
- If you have neither Hacking nor spare drone parts, choice (b) — walk away after the kill —
  is defensible: you keep the `MED` scrap and skip a table with a live downside.
- Note the asymmetry: `modifyPursuit -1` and `+1` are the same magnitude, so the manual
  hack is roughly EV-neutral on fleet position with a free map reveal attached.

## Related
- [[event-auto-ship-near-sensor-station]] — sibling, map reveal, Sensors/Teleporter gates
- [[event-auto-ship-near-storage-station]] — sibling, item cache, Cloaking gate
- [[item-hacking]], [[item-drones]]
- [[concept-rebel-fleet-advance]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Weights inside `AUTO_DEFENSE_RADAR_COMBAT` (3 entries) and `DEFENSE_RADAR_LIST`
      (4 entries) — no `prop` attributes in the file.
- [ ] Does owning the Fire Drone (`COMBAT_FIRE`) satisfy `req="COMBAT_DRONE_LIST"` via
      `DRONE_FIREBEAM`?
- [ ] What `modifyPursuit ±1` is worth in beacons/jumps.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-auto-ship-near-radar-station]] (per `raw/wiki/auto-ship-near-radar-station.md`)
