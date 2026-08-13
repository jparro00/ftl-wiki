---
id: entity-zoltan
type: entity
entity_kind: species
hostility: neutral
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [species, faction, crew, energy, super-shield, federation-allied]
---

# Zoltan

## Summary
An energy-bodied species allied to the [[entity-engi]] and, through them, to the Federation.
Zoltan crew are walking power conduits — one bar of free power to whatever room they stand
in — with only 70 max health and a death explosion that hurts enemy boarders. Zoltan ships
are the only ones that come with a **Zoltan Shield** (`ENERGY_SHIELD`) as standard. Their
sectors are bureaucratic and inspection-heavy rather than hostile. In-game description:

> The 'Zoltan' are allies of the 'Engi.' Their innate energy can power ship systems.

(`crew_energy_desc`, per [[source-text-blueprints]])

The species is `energy` internally — `crewBlueprint name="energy"`, ship prefix `ZOLTAN_*`,
hull layouts `energy_fighter` / `energy_bomber`, display class names "Energy Fighter" /
"Energy Bomber". Grep for both.

## Traits / Stats

### As crew — `crewBlueprint name="energy"`
| Field | Value |
|---|---|
| Display name | **Zoltan** (`crew_energy_title` / `crew_energy_short`) |
| Cost | 60 (a code comment records the old value as 65) |
| `bp` | 4 |
| `rarity` | **5** — the highest of any crew blueprint |
| Powers | *"Provides power to occupied system"* · *"Max health reduced to 70"* · *"15 damage to enemy crew on death"* |

(per [[source-blueprints]], [[source-text-blueprints]])

70 is the lowest stated max health in the game ([[entity-rock-men]] 150,
[[entity-crystal-men]] 125).

### As ships

| Blueprint | Class name | Sector range | Hull | Max power | Crew | Aug |
|---|---|---|---|---|---|---|
| `ZOLTAN_FIGHTER` | Energy Fighter | — | 7 | 7 | 2/3 | `ENERGY_SHIELD` |
| `ZOLTAN_BOMBER` | Energy Bomber | `minSector` 3 | 7 | 9 | 3/6 | `ENERGY_SHIELD` |
| `ZOLTAN_PEACE` | Energy Fighter | — | 7 | **12** | 2/3 | **none** |

`ZOLTAN_PEACE` is the notable one: it has **no shields system, no weapons system and no
weapon list at all** — only pilot, doors, medbay, oxygen and engines, on 12 max power. It is
the unarmed diplomatic hull ([[source-autoblueprints]]). See
[[event-unarmed-zoltan-transport]] and [[event-zoltan-peace-quest2]].

The two armed hulls draw from `WEAPONS_ZOLTAN` (lasers 1–5, `LASER_HEAVY_1/2`,
`MISSILES_1/2/3`, `BEAM_1/2/3`, `BEAM_LONG`, `BEAM_FIRE`, `ION_1/2`, `BOMB_1`, `BOMB_ION`,
`BEAM_HULL`) — the widest weapon pool of any faction. `ZOLTAN_BOMBER` also carries 2 combat
drones from `DRONES_COMBAT`. Crew class `energy`; `boardingAI: sabotage`; both are in
`SHIPS_ZOLTAN`.

**`ENERGY_SHIELD` — "Zoltan Shield":** *"An unexplained technology creates this nearly
impenetrable shield. Only the energy outburst from an FTL engine is powerful enough to
recharge it."* ([[source-text-blueprints]])

Advanced Edition adds a counter-augment, `ZOLTAN_BYPASS` — **"Zoltan Shield Bypass"**:
*"Allows crew/bomb teleportation and mind control to work through Super Shields."* (cost 55,
`bp` 8, `rarity` 3, non-stackable) ([[source-dlcblueprints]], [[source-text-blueprints]]).
Its existence is the clearest statement in the data that the Zoltan shield otherwise blocks
teleporters, bombs and mind control.

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `ZOLTAN_FIGHTER_DLC` → **Energy Instigator**; gains `mind` control (1/1, off at start),
>   medbay → `clonebay`.
> - `ZOLTAN_BOMBER_DLC` → **Energy Hacker**; gains `hacking` (1/2, off at start), medbay →
>   `clonebay`, drone pool raised from 2 to 5.
> - `ZOLTAN_PEACE` has **no `_DLC` variant**.
>
> Both keep `ENERGY_SHIELD`. So in AE a Zoltan ship can mind-control or hack you from behind
> a super shield; in vanilla it can do neither.

**Pirate reskins:** `ZOLTAN_FIGHTER_P` and `ZOLTAN_BOMBER_P` (*Pirate Fighter*,
*Pirate Bomber*), crew `class="random"`, in list `SHIPS_ZOLTAN_PIRATE`
([[source-dlcpirateblueprints]]).

> ⚠️ **Data oddity.** The live `SHIPS_PIRATE` list contains `ZOLTAN_FIGHTER_P` but **not**
> `ZOLTAN_BOMBER_P`, while the commented-out `P_REPLACE` version of the list directly above
> it contains both (as the un-reskinned `ZOLTAN_FIGHTER` / `ZOLTAN_BOMBER`)
> ([[source-autoblueprints]]). `ZOLTAN_BOMBER_P` is fully defined but only reachable through
> `SHIPS_ZOLTAN_PIRATE`. Whether that is deliberate is not stated.

## Where They Appear
- [[sector-zoltan-controlled-sector]] (`ZOLTAN_SECTOR`, `minSector` 1) — runs a
  `ZOLTAN_CREW_STUDY` beacon on top of the usual pool
- [[sector-zoltan-homeworlds]] (`ZOLTAN_HOME`, `minSector` 2, `unique`) — adds
  `ZOLTAN_PEACE_QUEST`

(per [[source-sector-data-xml]])

Zoltan hulls are **not** in `SHIPS_CIVILIAN`, so they are largely confined to Zoltan space
and pirate encounters.

## Events Involving Them

**Zoltan-sector furniture**
- [[event-start-beacon-zoltan]] · [[event-empty-beacon-zoltan]] · [[event-store-zoltan]] ·
  [[event-free-scrap-with-resources-zoltan]]

**Zoltan officialdom — the sector's signature**
- [[event-zoltan-security-checkpoint]] (`ZOLTAN_CREW_SCAN`) · [[event-zoltan-border-police]] ·
  [[event-zoltan-ship-asks-to-dock]] · [[event-zoltan-trade-hub]] ·
  [[event-zoltan-free-map]] · [[event-zoltan-free-augment]]

**Fights**
- [[event-zoltan-fight]] · [[event-zoltan-fight-in-asteroid-field]] ·
  [[event-mantis-fight-zoltan]] · [[event-pirate-fight-zoltan]]

**Zoltan mysticism and quests**
- [[event-zoltan-great-eye]] · [[event-zoltan-odd-moon]] · [[event-zoltan-wise-man]] ·
  [[event-zoltan-research-facility]] · [[event-zoltan-quest-primitives]] ·
  [[event-zoltan-rift-success]] · [[event-zoltan-retake-the-ship]] ·
  [[event-zoltan-peace-quest2]] · [[event-secret-word-abadoth]] ·
  [[chain-zoltan-cruiser-unlock]]
- [[event-unarmed-zoltan-transport]] · [[event-zoltan-ship-follows-mantis-ship]] ·
  [[event-rock-zoltan-help]]

**Refugees and cross-faction**
- [[event-refugee]] · [[event-refugee-zoltan]] · [[event-refugee-distress]] ·
  [[event-refugee-distress-zoltan]] · [[event-nebula-wreckage]]

### Blue options gated on Zoltan crew (`req="energy"`)
| Event id | Page |
|---|---|
| `ZOLTAN_TRADE_HUB` | [[event-zoltan-trade-hub]] |
| `TERRAFORMING_SCAN` | [[event-terraforming-scan]] |

Only 2 occurrences of `req="energy"` in the whole data set — the rarest species gate after
`req="crystal"` (3) and `req="human"` (1). (per [[source-events-zoltan]],
[[source-newevents]])

## How To Fight / Deal With Them
- **The Zoltan Shield comes first.** Both armed hulls spawn with `ENERGY_SHIELD`, and the AE
  bypass augment's description says teleporting crew, teleporting bombs and mind control all
  fail against a super shield until it is down ([[source-text-blueprints]]).
- Their weapon pool is the broadest in the game — you cannot pre-empt what they bring the way
  you can with [[entity-engi]] (no missiles) or [[entity-crystal-men]] (crystal-only).
- Zoltan crew have 70 HP, the lowest in the game: boarding a Zoltan ship is cheap once the
  super shield is gone. Note the 15-damage death burst — killing them costs your boarders
  health whether you want it or not.
- `ZOLTAN_PEACE` cannot shoot back at all. Treat any "unarmed Zoltan" encounter as literally
  unarmed ([[source-autoblueprints]]).

## Related
- [[entity-engi]] — declared allies in `crew_energy_desc`
- [[entity-federation]] — Zoltan space is Federation-aligned
- [[item-crystal-vengeance]] — unrelated augment, but the same "augment as blue-option key"
  pattern applies to `ENERGY_SHIELD`
- [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]

## Open Questions
- [ ] Whether `rarity` 5 means Zoltan are the *most* or *least* commonly offered crew — the
      scale is undefined in `raw/gamedata/`.
- [ ] Whether `ZOLTAN_BOMBER_P`'s absence from the live `SHIPS_PIRATE` list is a bug.
- [ ] How much power a Zoltan actually supplies (the string says only "provides power").

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
