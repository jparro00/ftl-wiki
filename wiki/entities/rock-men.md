---
id: entity-rock-men
type: entity
entity_kind: species
hostility: varies
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 11
tags: [species, faction, crew, fire-immune, tanky]
---

# Rock Men (Rockmen)

## Summary
A heavy, slow, fire-proof species from Vrachos IV. Rockmen crew have the highest max health
in the game (150) and move at half speed; Rock ships all carry hull plating and lean on
missiles. Their sectors are asteroid-heavy and their quest content is religious — the
Rock/Crystal schism runs through [[event-rock-atheists]], [[event-ancient-device]] and
[[chain-crystal-cruiser-unlock]]. In-game description:

> The 'Rockmen' of Vrachos IV are rarely seen and are known for their fortitude.

(`crew_rock_desc`, per [[source-text-blueprints]])

The display name is **Rockman** (singular) in `text_blueprints.xml`; this wiki's slug
`entity-rock-men` follows the Fandom-style plural used across the event pages.

## Traits / Stats

### As crew — `crewBlueprint name="rock"`
| Field | Value |
|---|---|
| Display name | **Rockman** (`crew_rock_title` / `crew_rock_short`) |
| Cost | 55 (a code comment records the old value as 65) |
| `bp` | 4 |
| `rarity` | 3 |
| Powers | *"Immune to fire"* · *"Movement speed is halved"* · *"Max Health is increased to 150"* |

(per [[source-blueprints]], [[source-text-blueprints]])

150 max health is the highest stated for any crew blueprint — [[entity-crystal-men]] are
125, [[entity-zoltan]] 70, and everyone else's is unstated.

### As ships
Every Rock hull carries `ROCK_ARMOR`, and their weapon pool is the most missile-heavy of any
faction (it is the only pool besides the Rebel/Federation ones to include `MISSILES_BREACH`
alongside all three standard missiles).

| Blueprint | Class name | Sector range | Hull | Max power | Crew | Notable |
|---|---|---|---|---|---|---|
| `ROCK_SCOUT` | Rock Scout | `maxSector` 5 | 8 | 10 | 2/5 | — |
| `ROCK_FIGHT` | Rock Fighter | `minSector` 2 | 10 | 7 | 3/5 | — |
| `ROCK_ASSAULT` | Rock Assault | `minSector` 5 | 12 | 7 | 3/6 | cloaking + teleporter, both off at start |
| `ROCK_ASSAULT_ELITE` | Rock Assault | `minSector` 5 | 12 | **12** | **4/5** | **cloaking on at start**, weapons 2/10 |

All draw from `WEAPONS_ROCK` (lasers 1–5, `LASER_HEAVY_1/2`, `MISSILES_1/2/3`,
`MISSILES_BREACH`, `BEAM_1/2`, `BOMB_1`, `ION_2`), crew class `rock`, `boardingAI: sabotage`.
`SHIPS_ROCK` contains the first three; `ROCK_ASSAULT_ELITE` is not in it.
`ROCK_SCOUT` also carries only 6 missiles at spawn where most ships carry 10.
(per [[source-autoblueprints]], [[source-text-blueprints]])

**`ROCK_ARMOR` — "Rock Plating":** *"Superior hull armor provides a 15 percent chance to
negate incoming hull damage (hit systems will still be damaged)."*
([[source-text-blueprints]]) This is on all four Rock hulls, so ~15% of your hull damage
against a Rock ship is simply erased.

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `ROCK_SCOUT_DLC` → **Rock Investigator**; gains a `teleporter` (1/2, off at start),
>   medbay → `clonebay`; crew 2/4.
> - `ROCK_FIGHT_DLC` → **Rock Interceptor**; gains `teleporter` (1/2) *and* `cloaking`
>   (1/1), medbay → `clonebay`; crew 2/5.
> - `ROCK_ASSAULT_DLC` → **Rock Aggressor**; medbay → `clonebay`, cloaking raised to 1/2;
>   crew 2/6.
> - `ROCK_ASSAULT_ELITE` has **no `_DLC` variant** — it is the same ship in both editions.
>
> The pattern: in AE every Rock hull can board you and the scout/fighter gain cloaking they
> did not have in vanilla, while starting crew drops by one.

**Pirate reskins:** `ROCK_SCOUT_P` and `ROCK_FIGHT_P` (*Pirate Scout*, *Pirate Fighter*),
crewed `class="random"`. They have their own list, `SHIPS_ROCK_PIRATE`, used by the Rock
sector's pirate events ([[source-autoblueprints]], [[source-dlcpirateblueprints]]).

## Where They Appear
- [[sector-rock-controlled-sector]] (`ROCK_SECTOR`, `minSector` 1)
- [[sector-rock-homeworlds]] (`ROCK_HOME`, `minSector` 4, `unique`) — same pool plus
  guaranteed `ROCK_CRYSTAL_BEACON` and `ROCK_UNLOCK1` beacons
- Rock hulls also appear outside Rock space via `SHIPS_CIVILIAN` and `SHIPS_PIRATE`

(per [[source-sector-data-xml]], [[source-autoblueprints]])

## Events Involving Them

**Rock-sector furniture**
- [[event-start-beacon-rock]] · [[event-empty-beacon-rock]] · [[event-store-rock]]

**Fights and boardings**
- [[event-rock-fight]] · [[event-rock-fight-in-asteroid-field]] · [[event-rock-fight-in-nebula]]
- [[event-rock-fight-with-boarders]] · [[event-rock-fight-with-boarders-in-asteroid-field]]
- [[event-boarders-rockmen-near-sun]] · [[event-rock-ship-in-plasma-storm]]
- [[event-rock-pirates-fight]] · [[event-rock-pirates-fight-in-asteroid-field]] ·
  [[event-rock-pirates-fight-near-sun]]

**Rock society, trade and hazards**
- [[event-rock-bride]] · [[event-rock-nursery]] · [[event-rock-atheists]] ·
  [[event-rock-live-mine]] · [[event-disabled-rock-ship]] · [[event-lone-shuttle]]
- [[event-no-fuel-drifting-debris]] · [[event-fire-on-research-station]] ·
  [[event-unknown-disease-on-mining-colony]]

**Unlock / quest content**
- [[chain-rock-cruiser-unlock]] — [[event-rock-unlock1]] → [[event-rock-unlock3]]
- [[event-ancient-device]] (`ROCK_CRYSTAL_BEACON`, guaranteed in the Homeworlds) →
  [[chain-crystal-cruiser-unlock]] · [[event-crystalline-research-facility]]
- [[event-rock-zoltan-help]] · [[event-zoltan-wise-man]]

**Cross-faction**
- [[event-mantis-ship-with-rock-body-parts]] · [[event-mantis-ships-battle-for-rock-freighter]]
- [[event-slug-ship-boarding-rock-ship]] · [[event-rock-and-slug-standoff]] ·
  [[event-slug-and-rock-standoff-in-nebula]] · [[event-slug-drink]]
- [[event-lanius-ship-attacking-rock]] · [[event-slaver-friendly]] · [[event-slaver-hostile]]

### Blue options gated on Rockman crew (`req="rock"`)
| Event id | Page |
|---|---|
| `DISTRESS_STATION_FIRE` | [[event-fire-on-research-station]] |
| `DISTRESS_STATION_DISEASE` | [[event-unknown-disease-on-mining-colony]] |
| `CRYSTAL_HUMAN_TESTS` | [[event-crystalline-research-facility]] |
| `NEBULA_ROCK_RACIST` | [[event-rock-ship-in-plasma-storm]] |
| `ROCK_MANTIS_HUNTER` | [[event-mantis-ship-with-rock-body-parts]] |
| `SLUG_DRINK` | [[event-slug-drink]] |

6 occurrences of `req="rock"`. Note that two of them (`DISTRESS_STATION_FIRE`,
`DISTRESS_STATION_DISEASE`) are fire/disease situations where the Rockman's fire immunity is
the point. (per [[source-events-xml]], [[source-events-crystal]], [[source-events-nebula]],
[[source-events-rock]], [[source-events-slug]])

Separately, the augment `ROCK_ARMOR` is itself a blue-option key in three places
(`req="ROCK_ARMOR"`) — see [[concept-blue-options]] if that page is created.

## How To Fight / Deal With Them
- **Fire is worthless.** Rockmen are immune to it, so fire bombs and beams do nothing to
  their crew ([[source-text-blueprints]]). Their hulls' weapon pool has no fire weapon in
  return.
- `ROCK_ARMOR` erases ~15% of incoming hull hits, so a long grind is longer than it looks.
  Systems still take the damage, which favours targeting rooms over racing the hull bar.
- Expect missiles. `WEAPONS_ROCK` carries all three standard missiles plus
  `MISSILES_BREACH`; a defence drone earns its slot here more than against any other faction
  except [[entity-rebels]].
- Rockmen move at half speed, so their crew are slow to respond to a boarding party or a
  fire in a far room — but with 150 HP each they win most straight melees.
- `ROCK_ASSAULT_ELITE` is the outlier: 12 max power and cloaking already running at spawn.

## Related
- [[entity-crystal-men]] — *"Ancient ancestors of the Rockmen"* (`crew_crystal_desc`); the
  two species share the whole [[chain-crystal-cruiser-unlock]] storyline
- [[entity-slugs]] — the standoff events run both ways
- [[entity-mantis]] — Rockmen are Mantis prey in several events
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]

## Open Questions
- [ ] Where `ROCK_ASSAULT_ELITE` is actually drawn from — it is in no `SHIPS_*` list in
      `autoBlueprints.xml`.
- [ ] Whether Rockmen's half move speed has an exact multiplier beyond the word "halved".
- [ ] What `rarity` 3 means for hiring Rockmen at stores.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
