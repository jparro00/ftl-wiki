---
id: event-crushed-pirate
type: event
event_name: DISTRESS_TRAPPED_MINER
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: [[[item-beam-weapons]], [[item-combat-beam-drone]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 11
tags: [distress, unique, blue-option, moral-choice, hull-damage-risk, pirate, drone-parts-cost]
---

# Crushed pirate — `DISTRESS_TRAPPED_MINER`

## Summary
A pirate ship is pinned between two asteroids, having mined the belt without the gear for
it. Every branch pays: helping and looting both average out to `MED` `standard`, and the
"good" and "evil" options are near-identical in expected value. The real difference is the
tail — helping can cost you 2 hull and 2 system damage; looting can summon a second pirate
ship. Two beam-flavoured blue options make the rescue clean. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_ENGI`
  ([[source-events-engi]]), `DISTRESS_BEACON_MANTIS` ([[source-events-mantis]]),
  `DISTRESS_BEACON_PIRATE` ([[source-events-pirate]]), `DISTRESS_BEACON_ROCK`
  ([[source-events-rock]])
- Allocation: 1–2 in most sectors, 1–3 in `NEBULA_SECTOR`, both Engi sectors and both
  Mantis sectors ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>`
- Long-range scanners show **no ship** ([[source-fandom-crushed-pirate]]) — worth noting,
  since one branch produces one
- `unique="true"` — once per run

## Text
> You arrive at the distress beacon near a small asteroid belt and find a ship with pirate
> markings partially crushed between two large rocks. It must have been illegally mining the
> belt without proper equipment.

(`event_DISTRESS_TRAPPED_MINER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Try to dislodge the ship by shooting at the rocks. | — | Rolls `DISTRESS_TRAPPED_MINER_SHOOT` (2 entries) | 1/2 each |
| 2 | Destroy and loot the ship. They're just pirates. | — | Rolls `DISTRESS_TRAPPED_MINER_LOOT` (2 entries) | 1/2 each |
| 3 | **(Beam Weapon)** Carefully cut the ship out. | `req="WEAPONS_BEAM_DAMAGE"` | *"You use your beam to make a few precision cuts in the asteroid…"* → `autoReward level="MED"` `standard` | 100% |
| 4 | **(Beam Drone)** Have your drone cut the ship out. | `req="COMBAT_BEAM_DRONE_LIST"` | *"You program the drone to work carefully around the trapped ship…"* → `autoReward level="MED"` `standard` **− 1 drone part** | 100% |

### Choice 1 → `DISTRESS_TRAPPED_MINER_SHOOT`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…you expose a mineral patch in the rock that reacts violently with your weapon…there is not much left of the ship."* → `autoReward level="LOW"` `scrap_only` + `damage 2 system="random"` (**AE only**) | 1/2 |
| 2 | *"…the pirate ship takes a beating but eventually pulls free. They thank you for your assistance."* → `autoReward level="MED"` `standard` | 1/2 |

### Choice 2 → `DISTRESS_TRAPPED_MINER_LOOT`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…causing the ship to depressurize and break apart. You move in to loot the remains."* → `autoReward level="MED"` `standard` | 1/2 |
| 2 | *"…another pirate ship flashes on your radar…they're charging weapons!"* → `<ship load="PIRATE" hostile="true"/>` | 1/2 |

Both splits are derived from entry counts and **assume uniform selection across list
entries** ([[source-events-xml]]).

### The ambush ship (choice 2, entry 2)
`<ship name="PIRATE" auto_blueprint="SHIPS_PIRATE">` with `<surrender chance="0.5" min="3"
max="4" load="PIRATE_SURRENDER"/>`, `<escape chance="0.5" min="2" max="4"
load="PIRATE_ESCAPE"/>` and default destroyed/deadCrew rewards ([[source-events-ships]]).
Per [[concept-surrender-offers]], `chance="0.5"` is a **50%** surrender offer. There is no
`<environment>` tag, so this fight happens **outside** the asteroid hazard despite the
setting.

## Blue Options
- **[[item-beam-weapons]]** (`req="WEAPONS_BEAM_DAMAGE"`) — the blueprint list resolves to
  `BEAM_HULL`, `BEAM_3`, `BEAM_2`, `BEAM_1`, `BEAM_LONG` and `ARTILLERY_FED`
  ([[source-autoblueprints]]). Fandom adds that the **Anti-Bio Beam and Fire Beam are
  excluded** and the Federation Artillery Beam **is** eligible — which the blueprint list
  confirms exactly ([[source-fandom-crushed-pirate]]).
- **[[item-combat-beam-drone]]** (`req="COMBAT_BEAM_DRONE_LIST"`) — the list resolves to
  `COMBAT_BEAM` and `COMBAT_BEAM_2`; Fandom notes the **Anti-Ship Fire Drone is excluded**,
  again matching the list ([[source-autoblueprints]]). Costs 1 drone part.

Both pay exactly the same `MED` `standard`, so the beam weapon is strictly better than the
drone whenever you have both.

## Rewards & Risks
- **Rewards:** `MED` `standard` on three of the four branches' good halves and on both blue
  options.
- **Risks:** 2 hull and **2 points of random system damage** on choice 1's bad half (AE
  only); or an unprovoked Pirate fight on choice 2's bad half.
- There is **no option to leave** — the event has no "move on" choice at all, which is
  unusual for a distress beacon. You must pick one of the four.

## Version Differences
Base-`events.xml` event, present in both editions. One `<!--DLC-->`-marked tag:
`<damage amount="2" system="random"/>` in `SHOOT` entry 1 ([[source-events-xml]]). That is
the **entire** damage payload of the outcome, so in vanilla choice 1's bad half costs
nothing but a reduced reward, while in AE it costs 2 hull and knocks 2 points off a random
system. Fandom's "2 hull damage, 2 damage to a random system" is the AE reading.

## Strategy Notes
- *(Opinion.)* With any qualifying beam, choice 3 is free `MED standard` and ends it.
- Without one, choice 2 is the lower-variance pick if your ship can beat a Pirate fight
  outright — the fight itself pays default rewards on top. Choice 1's downside in AE is
  2 points of system damage, which is worse than it sounds mid-run.
- Nothing here is morally punished mechanically: the game pays the same `MED standard` for
  saving the pirate and for murdering him.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[event-asteroid-belt-distress]] — the other asteroid-belt distress call, with a civilian
  in the trap
- [[event-pirate-fight]] — the same `PIRATE` ship as a standalone fight
- [[event-large-asteroid-field]] — also spawns the `PIRATE` ship out of an asteroid field
- [[event-giant-alien-spiders]], [[event-fire-on-research-station]],
  [[event-malfunctioning-defense-system]], [[event-unknown-disease-on-mining-colony]] — the
  rest of the shared `DISTRESS_BEACON` pool
- [[item-beam-weapons]], [[item-combat-beam-drone]], [[concept-surrender-offers]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? Both 1/2 figures assume it.
- [ ] Fandom reports the drone-part cost is **not** deducted when the reward includes drone
      parts — a runtime bug the files do not describe. Unconfirmed for 1.6.x.
- [ ] Numeric values behind `MED standard` and `LOW scrap_only`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml` — the `PIRATE` ship)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml` — `WEAPONS_BEAM_DAMAGE`, `COMBAT_BEAM_DRONE_LIST`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-crushed-pirate]] (per `raw/wiki/crushed-pirate.md`)
