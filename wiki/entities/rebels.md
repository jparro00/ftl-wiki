---
id: entity-rebels
type: entity
entity_kind: faction
hostility: hostile
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [faction, antagonist, fleet, automated-ships, endgame]
---

# Rebels (the Rebel Fleet)

## Summary
The run's antagonist and the only faction you can never make peace with. The Rebels are
present in three distinct forms: the **fleet** that chases you across every sector and
converts beacons into hostile ones behind you; the **rebel warships** you fight at those
beacons; and the **automated (auto-)ships** they field with no crew aboard. Their flagship
gets its own page, [[entity-flagship]].

Unlike every species page in this folder, the Rebels have **no `crewBlueprint`** — they are a
political faction, not a species. Every Rebel hull is crewed `class="human"`
([[source-autoblueprints]]).

## Traits / Stats

### Crewed warships

| Blueprint | Class name | Hull | Max power | Crew | Notable |
|---|---|---|---|---|---|
| `REBEL_FAT` | Rebel Rigger | 9 | 8 | 3/5 | drones 2/8, full `DRONES_STANDARD` pool |
| `REBEL_SKINNY` | Rebel Fighter | 10 | 7 | 3/6 | teleporter 1/1 (off at start) |
| `REBEL_SKINNY_ELITE` | Elite Fighter | 14 | 13 | 3/8 | shields 4 at spawn, weapons 4/10 |
| `REBEL_TRANSPORT` | Rebel Transport | 9 | 8 | 3/4 | `DRONES_DEFENSE` only |

All draw from `WEAPONS_REBEL` (lasers 1–5, `LASER_HEAVY_1/2`, `MISSILES_1/2/3`,
`MISSILES_BREACH`, `BEAM_1/2`, `BOMB_1`) and run `boardingAI: sabotage`. `SHIPS_REBEL` =
{`REBEL_FAT`, `REBEL_SKINNY`}; `SHIPS_REBEL_ELITE` lists `REBEL_SKINNY_ELITE` twice.
(per [[source-autoblueprints]], [[source-text-blueprints]])

`blueprints.xml` adds three more Rebel-hulled ships used by specific events rather than by
list: `DEFAULT` (*Rebel Rigger*, hull 10, 15 power, 3 human crew), `LONG_ELITE_MED`
(*Rebel Elite*, hull 20, 21 power, 4 crew) and `LONG_ELITE_HARD` (*Rebel Elite*, hull **30**,
24 power, 5 crew) ([[source-blueprints]], [[source-text-blueprints]]). `LONG_ELITE_HARD` is
the toughest non-boss hull in the data.

### Automated ships
The Rebels' crewless drones-with-a-hull. Both have `crewCount amount="0" max="0"`, so
boarding, mind control and crew-kill wins are all off the table.

| Blueprint | Class name | Hull | Max power | Notable |
|---|---|---|---|---|
| `AUTO_BASIC` | Auto-Scout | 6 | 6 | **starts with shields off** (`start="false"`), cloaking 1/3 off |
| `AUTO_ASSAULT` | Auto-Assault | 8 | 7 | weapons start at power **0**, drones 2/6 on, 5 combat drones |

Weapons come from `WEAPONS_AUTO` — the only faction pool built around ion
(`ION_1/2/4`, `BOMB_ION`) alongside lasers, missiles and bombs.
The list `SHPS_REBEL_AND_AUTO` (spelled without the `I`, in the file) mixes both auto ships
with `REBEL_FAT` and `REBEL_SKINNY` — that is the pool the fleet-pursuit and boss-scout
events draw from ([[source-autoblueprints]], [[source-events-boss]]).

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `REBEL_FAT_DLC` → **Rebel Disruptor**; medbay → `clonebay`, gains `hacking` (1/1, off).
> - `REBEL_SKINNY_DLC` → **Rebel Invader**; medbay → `clonebay`.
> - `REBEL_SKINNY_ELITE_DLC` → **Elite Assault**; medbay → `clonebay` (powered).
> - `AUTO_BASIC_DLC` → **Auto-Surveyor**; gains `mind` control (1/2, off at start).
> - `AUTO_ASSAULT_DLC` → **Auto-Hacker**; gains `hacking` (1/2, **powered at start**), loses
>   the `DRONES_COMBAT` list binding.
> - `REBEL_TRANSPORT` has **no `_DLC` variant**.
>
> A crewless AE auto-ship that mind-controls your pilot is the sharpest edge here: you cannot
> board it to stop it, because there is nobody aboard to fight.

**Pirate reskins:** `REBEL_FAT_P` (*Pirate Rigger*) and `REBEL_SKINNY_P` (*Pirate Fighter*),
crew `class="random"` ([[source-dlcpirateblueprints]]).

## Where They Appear
- [[sector-rebel-controlled-sector]] (`REBEL_SECTOR`, `minSector` 0)
- [[sector-rebel-stronghold]] (`REBEL_SECTOR_MINIBOSS`, `minSector` 4, `unique`) — the same
  pool plus a guaranteed `FLAGSHIP_CONSTRUCTION` beacon
- [[sector-the-last-stand]] (`FINAL`, `minSector` 7, `unique`) — `BOSS_HOSTILE`,
  `BOSS_NEUTRAL`, `BOSS_REPAIR_STATION`, `STORE`
- **Everywhere else** — the fleet pursuit is not a sector property. Rebel and auto ships also
  reach other sectors through `SHIPS_CIVILIAN`-adjacent event ships and the `FLEET_*` events.

(per [[source-sector-data-xml]], [[source-events-boss]])

## Events Involving Them

**The fleet pursuit**
- [[event-fleet-easy]] · [[event-fleet-easy-dlc]] · [[event-fleet-hard]] ·
  [[event-fleet-easy-beacon]] · [[event-fleet-easy-beacon-dlc]] · [[event-fleet-easy-nebula]]
- [[event-rebel-pds]] · [[event-rebel-auto-pds]] · [[event-no-fuel-rebel-fleet-delay]]

**Rebel-sector furniture**
- [[event-start-beacon-rebel]] · [[event-empty-beacon-rebel]] · [[event-store-rebel]]

**Rebel warship encounters**
- [[event-rebel-fight]] · [[event-rebel-fight-chance]] · [[event-rebel-fight-chance-in-nebula]] ·
  [[event-rebel-fight-in-nebula]] · [[event-rebel-fight-choice-in-nebula]] ·
  [[event-rebel-fight-in-plasma-storm]] · [[event-rebel-fight-near-pulsar]] ·
  [[event-rebel-fight-with-boarders]] · [[event-boarders-rebels-in-nebula]] ·
  [[event-no-fuel-rebel-fight]]
- Faction-flavoured variants: [[event-rebel-fight-crystal]] · [[event-rebel-fight-engi]] ·
  [[event-rebel-fight-lanius]] · [[event-rebel-fight-slug]] ·
  [[event-rebel-fight-among-rebel-fleet]] ·
  [[event-rebel-fight-among-federation-and-rebel-fleets]]

**Automated ships**
- [[event-auto-ship-fight]] · [[event-auto-ship-fight-in-nebula]] ·
  [[event-auto-ship-fight-in-asteroid-field]] · [[event-auto-ship-fight-near-sun]] ·
  [[event-auto-ship-fight-in-plasma-storm]] · [[event-auto-ship-fight-crystal]]
- [[event-auto-ship-warning]] · [[event-auto-ship-warning-in-nebula]] ·
  [[event-auto-ship-attacking-civilian]] · [[event-auto-ship-attacking-outpost]] ·
  [[event-auto-ship-carrying-shield-virus]] · [[event-deactivated-auto-ship]] ·
  [[event-auto-bait]]
- [[event-auto-ship-near-radar-station]] · [[event-auto-ship-near-sensor-station]] ·
  [[event-auto-ship-near-storage-station]] · [[event-auto-ship-near-storage-station-in-nebula]]

**Rebel occupation and infrastructure**
- [[event-rebel-checkpoint]] · [[event-rebel-ship-warning]] · [[event-rebel-transport-ship]] ·
  [[event-rebel-shipyard]] · [[event-rebel-ship-supplying-civilians]] ·
  [[event-rebel-ship-attacking-refueling-outpost]] · [[event-rebel-ship-attacking-crystal-ship]] ·
  [[event-rebel-ship-attacking-federation-loyalists]] ·
  [[event-rebel-ship-attacking-civilians-in-last-stand]] · [[event-large-trade-station]] ·
  [[event-space-station-under-construction]] · [[event-lone-shuttle]]
- [[event-rebel-defector]] · [[event-encrypted-federation-signal]] ·
  [[event-escort-civilians-ftl-haywire]] · [[event-quest-store-rescue]] ·
  [[event-store-rescue]] · [[event-nebula-lost-ship]] · [[event-pirate-briber]] ·
  [[event-distress-engi-rebel-result]] · [[event-engi-distress-rebel-fight]]

**The endgame**
- [[event-fight-in-last-stand]] · [[event-boss-text-1]] · [[event-boss-text-2]] ·
  [[event-boss-text-3]] — see [[entity-flagship]]

**Seen from other factions**
- [[event-engi-unlock-2real]] · [[event-engi-unlock-2fake]] · [[event-engi-unlock-3]] ·
  [[event-crystal-chat]] · [[event-crystal-fight-choice]] ·
  [[event-crystalline-ship-messaging-about-rebels]] ·
  [[event-lanius-ship-absorbing-rebel-base]] ·
  [[event-lanius-ship-absorbing-automated-scout]] · [[event-zoltan-peace-quest2]] ·
  [[event-zoltan-quest-primitives]]

### Blue options gated on Rebels
None. There is no `req="rebel"` — the Rebels are never a key, only a lock
(scan of `req=` across `raw/gamedata/*.xml`).

## How To Fight / Deal With Them
- **Auto-ships have no crew.** Boarding, mind control, and killing the crew to end the fight
  all fail; you must take the hull down ([[source-autoblueprints]]).
- `AUTO_BASIC` spawns with **shields unpowered** and `AUTO_ASSAULT` with **weapons at power
  0** — both are soft in the opening seconds if you can hit first.
- `WEAPONS_AUTO` is the game's ion pool. Expect systems locked out rather than hull damage.
- Crewed Rebel ships bring all three missiles plus `MISSILES_BREACH`; `REBEL_FAT` also runs
  the full `DRONES_STANDARD` pool, which includes a boarding drone.
- `REBEL_SKINNY_ELITE` is a step change: hull 14, 13 max power, shields already at 4.
  `LONG_ELITE_HARD` (hull 30) is harder still.
- In AE, `AUTO_ASSAULT_DLC` starts with **hacking already powered**
  ([[source-dlcblueprintsoverwrite]]).

## Related
- [[entity-flagship]] — the Rebel Flagship, three phases, its own page
- [[entity-federation]] — the other side of the war; you fly for them
- [[entity-pirates]] — two Rebel hulls are reskinned as pirate ships
- [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-the-last-stand]]

> **Naming note.** Event pages in this wiki link the Rebels under several slugs:
> `entity-rebels` (this page), `entity-rebel`, `entity-rebel-ships`, and — most commonly —
> `entity-rebel-fleet`. Whether the fleet pursuit deserves a separate page from the faction
> is an open call; see Open Questions.

## Open Questions
- [ ] Whether `[[concept-rebel-fleet-advance]]` should be a distinct page (the pursuit mechanic) or an
      alias of this one. It currently has ~82 inbound links and no target.
- [ ] Which blueprint list the fleet-pursuit `FLEET_*` events actually draw from —
      `SHPS_REBEL_AND_AUTO` is the obvious candidate but is not confirmed by the files read
      here.
- [ ] Where `DEFAULT`, `LONG_ELITE_MED` and `LONG_ELITE_HARD` are used; they are in no
      `SHIPS_*` list.
- [ ] Whether the Rebel fleet's advance rate is defined in any data file.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
