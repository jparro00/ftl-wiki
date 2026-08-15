---
id: entity-lanius
type: entity
entity_kind: species
hostility: varies
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 11
tags: [species, faction, crew, oxygen, advanced-edition, scavenger]
---

# Lanius

## Summary
Advanced Edition's added species: anaerobic metal scavengers who **drain the oxygen out of
any room they stand in**. They are the only faction introduced entirely by the DLC — every
Lanius blueprint, ship, sector and event lives in a `dlc*` file — and they behave less like a
government than like weather, absorbing derelicts, beacons and each other. In-game
description:

> These anaerobic beings seem friendly enough.

(`crew_anaerobic_desc`, per [[source-text-blueprints]])

The species is `anaerobic` internally — `crewBlueprint name="anaerobic"`, ships
`ANAEROBIC_SCOUT` / `ANAEROBIC_BOMBER`, blue-option gate `req="anaerobic"`, but the display
name is **Lanius**. Grep for both.

## Traits / Stats

### As crew — `crewBlueprint name="anaerobic"`
| Field | Value |
|---|---|
| Display name | **Lanius** (`crew_anaerobic_title` / `crew_anaerobic_short`) |
| Cost | 50 |
| `bp` | 2 |
| `rarity` | 0 |
| Powers | *"Drains oxygen from rooms."* · *"Slow movement but no damage from lack of oxygen."* |

(per [[source-dlcblueprints]], [[source-text-blueprints]])

Defined in `dlcBlueprints.xml`, not `blueprints.xml` — this is the mechanical basis for
`version: ae` on this page.

### As ships

| Blueprint | Class name | Sector range | Hull | Max power | Crew | Aug |
|---|---|---|---|---|---|---|
| `ANAEROBIC_SCOUT` | Lanius Scout | `maxSector` 7 | 7 | 7 | 2/3 | `O2_MASKS` |
| `ANAEROBIC_BOMBER` | Lanius Bomber | `minSector` 3 | 9 | 7 | 3/5 | `O2_MASKS` |

Both list `SHIPS_LANIUS`, crew class `anaerobic`, `boardingAI: sabotage`.

- `ANAEROBIC_SCOUT` — pilot, `clonebay` (off), shields 2/8, engines, weapons 2/8, doors
  (off), **`hacking` 1/3 (off at start)**. No oxygen system, no medbay.
- `ANAEROBIC_BOMBER` — pilot, doors, `clonebay` (off), shields 2/8, engines, weapons 2/8,
  **`mind` control 1/2 (off)**, **`teleporter` 1/3 (powered at start)**, **`cloaking` 1/3
  (off)**. No oxygen system.

Neither hull has an `oxygen` system at all — consistent with an anaerobic crew, and unique
among enemy hulls. Both use `clonebay` rather than a medbay in *both* editions, because both
are AE-only ships to begin with. (per [[source-dlcblueprints]], [[source-text-blueprints]])

Weapons come from `WEAPONS_ANAEROBIC` (lasers 1–5, `LASER_HEAVY_1/2`, **`SHOTGUN`,
`SHOTGUN_2`**, `ION_2`, `MISSILES_1/2/3`, `MISSILES_BREACH`, `BEAM_1/2`, `BOMB_1`). The two
shotguns appear in no other faction's pool.

**`O2_MASKS` — "Emergency Respirators":** *"Crew take half damage from low oxygen."*
([[source-text-blueprints]]) On both hulls — which reads as belt-and-braces, since Lanius
crew take no suffocation damage at all.

> ⚠️ **Data note — no Lanius pirates.** The commented-out `P_REPLACE` version of
> `SHIPS_PIRATE` in `autoBlueprints.xml` lists `ANAEROBIC_BOMBER` and `ANAEROBIC_SCOUT`; the
> **live** `SHIPS_PIRATE` immediately below it does not, and no `ANAEROBIC_*_P` blueprint
> exists in `dlcPirateBlueprints.xml`. `anaerobic` is also absent from the `CREW_RANDOM` list
> that supplies pirate crews. So Lanius ships and Lanius pirate crew are both unreachable
> through the pirate system ([[source-autoblueprints]], [[source-dlcpirateblueprints]]).

## Where They Appear
- [[sector-abandoned-sector]] (`LANIUS_SECTOR`, `minSector` 1) — the only Lanius sector, and
  the one with the largest event-list count in the game: `STORE_LANIUS`, `NOTHING_LANIUS`,
  `DISTRESS_BEACON_LANIUS`, `NEBULA_LANIUS`, `HOSTILE_LANIUS`,
  **`HOSTILE_ENVIRONMENT_LANIUS`** (a category no other sector has), `BOARDERS_LANIUS`,
  `ITEM_LANIUS`, `QUESTS_LANIUS`, `NEUTRAL_LANIUS` ([[source-sector-data-xml]]).
- Individual Lanius ships also appear in other sectors through specific events.

> Note: `sector_data.xml` also contains a vestigial `ABANDONED_SECTOR` description with a
> single `STORE` list — see [[sector-vestigial-definitions]]. The playable Abandoned Sector
> is `LANIUS_SECTOR`.

## Events Involving Them

**Lanius-sector furniture**
- [[event-start-beacon-lanius]] · [[event-empty-beacon-lanius]] · [[event-store-lanius]] ·
  [[event-free-scrap-with-resources-lanius]] · [[event-lanius-empty-distress-beacon-1]] ·
  [[event-lanius-empty-distress-beacon-2]]

**Fights**
- [[event-lanius-fight]] · [[event-lanius-fight-distress]] ·
  [[event-lanius-fight-in-asteroid-field]] · [[event-lanius-fight-near-pulsar]] ·
  [[event-lanius-fight-with-friendly-asb-support]] · [[event-pirate-fight-lanius]] ·
  [[event-rebel-fight-lanius]]

**Lanius as scavengers — the signature behaviour**
- [[event-lanius-ship-absorbing-automated-scout]] · [[event-lanius-ship-absorbing-jump-beacon]] ·
  [[event-lanius-ship-absorbing-rebel-base]] · [[event-lanius-ship-in-rich-debris-field]] ·
  [[event-lanius-ship-salvager]] · [[event-lanius-powered-down-ship]] ·
  [[event-lanius-lone-ship]]

**Contact, trade and quests**
- [[event-lanius-trader]] · [[event-lanius-trader-with-translator]] ·
  [[event-lanius-craftsmen]] · [[event-lanius-with-federation-science-craft]]
- [[event-space-station-under-construction]] · [[event-refueling-platform-garbled-broadcast]] ·
  [[event-malfunctioning-defense-system]] · [[event-the-engi-virus]]

**Lanius preying on other factions**
- [[event-lanius-ship-attacking-civilian]] · [[event-lanius-ship-attacking-civilian-distress]] ·
  [[event-lanius-ship-attacking-mantis]] · [[event-lanius-ship-attacking-rock]] ·
  [[event-lanius-ship-attacking-slug]] · [[event-pirate-ship-attacking-civilian-lanius]]

### Blue options gated on Lanius crew (`req="anaerobic"`)
| Event id | Page |
|---|---|
| `LANIUS_DISTRESS_FIGHT` | [[event-lanius-ship-attacking-civilian-distress]] |
| `LANIUS_RESEARCHER_CONTACT` | [[event-lanius-with-federation-science-craft]] |
| `LANIUS_RESEARCHER_CRAFT` | [[event-lanius-craftsmen]] |
| `LANIUS_TRADER` | [[event-lanius-trader]] |
| `LANIUS_SOLO_SALVAGE` | [[event-lanius-ship-salvager]] |
| `LANIUS_SCARED_CIVILIAN` | [[event-lanius-lone-ship]] |
| `LANIUS_GROUP_AUTO` | [[event-lanius-ship-absorbing-rebel-base]] |
| `LANIUS_BEACON_EATER` | [[event-lanius-ship-absorbing-jump-beacon]] |
| `LANIUS_DORMANT_INVESTIGATE` | sub-event of [[event-lanius-powered-down-ship]] |
| `DISTRESS_SATELLITE_DEFENSE` | [[event-malfunctioning-defense-system]] |
| `ENGI_VIRUS` | [[event-the-engi-virus]] |
| `QUEST_CONSTRUCTIONYARD` | [[event-space-station-under-construction]] |

12 occurrences of `req="anaerobic"` — the **most-used species gate in the game**, ahead of
`engi` and `slug` at 11 each. Nine of the twelve are inside `dlcEvents_anaerobic.xml` itself,
i.e. Lanius crew are mostly a key to Lanius content.
(per [[source-dlcevents-anaerobic]], [[source-events-xml]], [[source-events-engi]],
[[source-newevents]])

## How To Fight / Deal With Them
- **Lanius boarders suffocate your ship, not themselves.** The bomber's teleporter is
  *powered at spawn*, and Lanius crew drain the air from whatever room they occupy
  ([[source-dlcblueprints]], [[source-text-blueprints]]). Venting the room does nothing to
  them.
- Their hulls have **no oxygen system to shoot** — the standard "knock out their O2 and
  wait" line of play does not exist against a Lanius ship.
- Both hulls carry a clonebay, not a medbay, so crew kills don't stick unless you take the
  clonebay down.
- Weapon pool is broad and includes the two shotguns nobody else has, plus all three
  missiles and `MISSILES_BREACH`.
- Scout can hack (AE only content by definition); bomber can cloak, mind-control *and*
  board.

## Related
- [[entity-engi]] — [[event-the-engi-virus]] gates on both species
- [[entity-rebels]] — [[event-lanius-ship-absorbing-rebel-base]],
  [[event-lanius-ship-absorbing-automated-scout]]
- [[entity-federation]] — [[event-lanius-with-federation-science-craft]]
- [[sector-abandoned-sector]], [[sector-vestigial-definitions]]
- [[concept-oxygen-and-suffocation]] — their 8%/sec drain among every other O₂ rate
- [[item-lanius-crew]] — the crew blueprint page

## Open Questions
- [ ] Whether the omission of Lanius from the live `SHIPS_PIRATE` list is deliberate.
- [x] ~~The rate at which Lanius crew drain oxygen, and whether it scales with crew count.~~
      **Answered 2026-08-14: 8% O₂/sec each — the engine runs anaerobic crew through the same
      `OxygenSystem::ComputeAirLoss` path as a hull breach, calling them "equivalent"**
      ([[source-xftl-oxygen-mechanics]]). It **does** scale: that source notes level-3 Oxygen
      sustains one Lanius room but breaks if two such rooms are connected by an open door,
      *"since they both vent each other's rooms"*. See [[concept-oxygen-and-suffocation]].
- [ ] Whether `HOSTILE_ENVIRONMENT_LANIUS` is a hazard category unique to this sector or a
      general mechanism used only here.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-xftl-oxygen-mechanics]] (per raw/modding/2026-08-14-xftl-oxygen-mechanics.txt)
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
