---
id: event-asteroid-belt-distress
type: event
event_name: CIVILIAN_ASTEROIDS_BEACON
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: [[[item-defense-drone]], [[item-repair-drone]], [[item-teleporter]], [[item-rock-plating]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 11
tags: [distress, unique, blue-option, crew-reward-chance, quest-marker, hull-damage-risk, fire-risk, fleet-advance-risk, drone-parts-cost]
---

# Asteroid belt distress — `CIVILIAN_ASTEROIDS_BEACON`

## Summary
A civilian miner is being torn apart by an asteroid belt with its shields down. It is one of
the most blue-option-dense events in the game — **four** separate gates, each opening a
different outcome pool: a Defense or Repair Drone can uncover the Hidden Federation Base
quest, a Teleporter can hand you a free crewmember, and Rock Plating turns the rescue into a
guaranteed clean payout. Even walking away has a cost. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_ENGI`
  ([[source-events-engi]]), `DISTRESS_BEACON_PIRATE` ([[source-events-pirate]]),
  `DISTRESS_BEACON_REBEL` ([[source-events-rebel]]), `DISTRESS_BEACON_ROCK`
  ([[source-events-rock]])
- Allocation: `DISTRESS_BEACON` 1–2 in `STANDARD_SPACE` and `CIVILIAN_SECTOR` and 1–3 in
  `NEBULA_SECTOR`; `DISTRESS_BEACON_ENGI` 1–3; `DISTRESS_BEACON_PIRATE` 1–2;
  `DISTRESS_BEACON_REBEL` 1–2; `DISTRESS_BEACON_ROCK` 1–2 ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>` — shows the distress icon
- Long-range scanners show **no ship** ([[source-fandom-asteroid-belt-distress]])
- `unique="true"` — once per run

## Text
> You follow the distress beacon to a tiny asteroid belt. You find a small ship struggling to
> maneuver through the field.

Hailing them (`CIVILIAN_ASTEROIDS_BEACON_2`):

> They respond: "Help! Our shields are down and we won't last long!"

(`event_CIVILIAN_ASTEROIDS_BEACON_text`, `…_2_text`, per [[source-text-events-xml]])

## Choices & Outcomes

The first screen has a single choice — *Hail them to offer assistance* — which loads
`CIVILIAN_ASTEROIDS_BEACON_2`. There is **no option to ignore the beacon** at that point.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Try to shield their ship with yours. | — | Rolls `…_LIST1` (3 entries) | 1/3 each |
| 2 | Don't risk our ship. Leave them to their fate. | — | Rolls `…_LIST4` (2 entries) | 1/2 each |
| 3 | **(Defense Drone)** Use a Defense Drone to protect their ship. | `req="DRONES_DEFENSE_LIST"` | Rolls `…_LIST2` (2 entries) | 1/2 each |
| 4 | **(Repair Drone)** Send a Repair Drone to fix their Shields. | `req="REPAIR"` | Rolls the **same** `…_LIST2` | 1/2 each |
| 5 | **(Teleporter)** Offer to beam them aboard your ship. | `req="teleporter"` | Rolls `…_LIST3` (2 entries) | 1/2 each |
| 6 | **(Rock Armor)** Shield their ship with yours and escort them out. | `req="ROCK_ARMOR"` | *"…your improved hull taking the brunt of the asteroids…"* → `autoReward level="MED"` `fuel` | 100% |

All fractions are derived from entry counts in each `<eventList>` and **assume uniform
selection across list entries** ([[source-events-xml]]).

### Choice 1 → `CIVILIAN_ASTEROIDS_BEACON_LIST1`

| Entry | Outcome |
|---|---|
| 1 | *"You succeed in preventing them from being entirely destroyed, but your ship took a number of hits…"* → `autoReward level="HIGH"` `fuel` + `damage 1 room effect="fire"` (AE only) |
| 2 | *"…one stray rock hits a key structure in their ship. It breaks apart…"* → `autoReward level="LOW"` `scrap_only` |
| 3 | *"Despite your best efforts, the civilian ship breaks apart…"* → `damage 4` + `autoReward level="LOW"` `scrap_only` |

### Choice 2 → `CIVILIAN_ASTEROIDS_BEACON_LIST4`

| Entry | Outcome |
|---|---|
| 1 | *"…'I'll be sure to tell them where you are the next time I see them!'"* → `modifyPursuit amount="1"` |
| 2 | *"You watch helplessly as their ship smashes against a cruiser-sized rock..."* → nothing |

Walking away is therefore a **coin flip on a Rebel fleet advance** — not free.

### Choices 3 & 4 → `CIVILIAN_ASTEROIDS_BEACON_LIST2`

Both drone options load the identical list, and **both spend a drone part**
(`<item_modify><item type="drones" min="-1" max="-1"/></item_modify>`).

| Entry | Outcome |
|---|---|
| 1 | *"Your drone succeeds in keeping their ship from breaking apart…They offer you some military supplies…"* → `autoReward level="MED"` **`weapon`** + `damage 2` + `damage 1 random system` (AE only) + `damage 1 room effect="fire"` − 1 drone part |
| 2 | *"…I heard there was a Federation loyalist base nearby. Maybe they can help you?"* → `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` − 1 drone part |

### Choice 5 → `CIVILIAN_ASTEROIDS_BEACON_LIST3`

| Entry | Outcome |
|---|---|
| 1 | *"…As the Captain, I feel obligated to help you with your mission."* → `<crewMember amount="1"/>` — **no `class` attribute**, so the species is whatever the game picks |
| 2 | *"…I'm sure we can muster up a reward if you take us home."* → a follow-up choice, *Take them to the nearby planet, where they're from*, which loads `FAMILY_RETURN` |

### `FAMILY_RETURN` (3 entries, 1/3 each)

| Entry | Outcome |
|---|---|
| 1 | *"…the patron of the family offers you a substantial reward."* → `autoReward level="HIGH"` `scrap_only` |
| 2 | *"The survivor's family is of modest means…"* → `autoReward level="MED"` `scrap_only` |
| 3 | *"…the family of the survivor arranges to repair your ship's hull…"* → `damage amount="-10"` — i.e. **+10 hull repaired** |

`FAMILY_RETURN` is a shared list, not exclusive to this event ([[source-events-xml]]).

### The Hidden Federation Base quest
`HIDDEN_FEDERATION_BASE_LIST` is a five-entry quest pool in `events.xml`: `HIGH` `drone`;
`LOW` `standard` plus a crewmember; `MED` `standard` plus `damage amount="-35"` (**+35
hull**); a sensors/`ADV_SCANNERS`-gated branch paying `MED` `standard` or `MED` `weapon`;
and a load of `FEDERATION_BASE_ASSIST` ([[source-events-xml]]). It is a separate event in its
own right and is not documented in full here. Do not confuse it with
[[event-federation-base]], the Last Stand arrival text.

## Blue Options
- **[[item-defense-drone]]** (`req="DRONES_DEFENSE_LIST"`) — the list resolves to
  `DEFENSE_1` and `DEFENSE_2` ([[source-autoblueprints]]). Costs 1 drone part.
- **[[item-repair-drone]]** (`req="REPAIR"`, the drone blueprint —
  [[source-blueprints]]). Costs 1 drone part. Mechanically **identical** to the Defense
  Drone option: same list, same cost.
- **[[item-teleporter]]** (`req="teleporter"`, the system) — the only route to a free
  crewmember or the hull repair. Costs nothing.
- **[[item-rock-plating]]** (`req="ROCK_ARMOR"`, an augment) — the only guaranteed-clean
  outcome: `MED` `fuel` with no damage and no roll.

## Rewards & Risks
- **Rewards on offer:** `MED` `fuel` (Rock Plating, guaranteed); `HIGH` or `LOW`
  `scrap_only`; a `MED` `weapon`; a free crewmember; +10 or +35 hull; the Hidden Federation
  Base quest marker.
- **Costs:** up to 4 hull plus a system and a fire; one drone part on either drone branch;
  or a Rebel fleet advance for walking away.
- The teleporter branch is the standout: **no downside outcome exists in `LIST3`** — one
  entry is a crewmember, the other leads to a list whose worst result is `MED scrap_only`.

## Version Differences
Base-`events.xml` event, present in both editions. Two `<!--DLC-->`-marked tags, both
Advanced Edition only ([[source-events-xml]]):

- `LIST1` entry 1: `<damage amount="1" system="room" effect="fire"/>` — vanilla takes **no
  damage** on the best rescue outcome; AE takes 1 hull and a fire.
- `LIST2` entry 1: `<damage amount="1" system="random"/>` — vanilla takes 3 hull and a fire;
  AE takes 4 hull, a fire and a knocked-out system.

## Strategy Notes
- *(Opinion.)* With a Teleporter, take choice 5 — it is the only branch with no bad outcome.
- With Rock Plating and no Teleporter, choice 6 is the safe pick; with neither, choice 1 is a
  2/3 chance of a small payout against a 1/3 chance of 4 hull.
- The drone branches are worth a drone part chiefly for the coin-flip at the Hidden
  Federation Base quest, not for the `MED weapon` — that entry also costs you 4 hull.
- Choice 2 is never strictly free: half the time it advances the fleet.

## Related
- [[event-dense-asteroid-field-distress]], [[event-large-asteroid-field]] — the other
  asteroid-field events in this batch
- [[event-crushed-pirate]] — the other asteroid-belt distress call, with a pirate on the
  receiving end
- [[event-federation-base]] — **not** the target of this event's quest; different id
- [[item-teleporter]], [[item-rock-plating]], [[item-defense-drone]], [[item-repair-drone]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? Every fraction above assumes it.
- [ ] What species `<crewMember amount="1"/>` with no `class` produces.
- [ ] Full outcome table for `HIDDEN_FEDERATION_BASE_LIST` — it deserves its own page.
- [ ] Fandom shows the drone-part cost on the Defense/Repair options; other events in this
      batch carry a documented bug where the part is not actually deducted if the reward
      includes drone parts. Whether that applies here is unstated.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml` — `DRONES_DEFENSE_LIST`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml` — the `REPAIR` drone)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-asteroid-belt-distress]] (per `raw/wiki/asteroid-belt-distress.md`)
