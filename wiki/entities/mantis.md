---
id: entity-mantis
type: entity
entity_kind: species
hostility: hostile
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [species, faction, crew, boarding, hostile]
---

# Mantis

## Summary
The game's dedicated boarding faction. Mantis crew hit 1.5× as hard as anyone else and move
faster; Mantis ships carry teleporters as standard and their AI is written to put bodies on
your deck. They own two sectors, and outside them they show up mostly as slavers, raiders
and the antagonists of the Engi quest lines. Their in-game description:

> The Mantis disregard for individual lives led to their evolution as a vicious warrior race.

(`crew_mantis_desc`, per [[source-text-blueprints]])

## Traits / Stats

### As crew — `crewBlueprint name="mantis"`
| Field | Value |
|---|---|
| Display name | **Mantis** (`crew_mantis_title` / `crew_mantis_short`) |
| Cost | 55 (a code comment records the old value as 45) |
| `bp` | 2 |
| `rarity` | 2 |
| Powers | *"Inflict 1.5x damage in combat"* · *"1.2x move speed"* · *"Halved repair speed"* |

(per [[source-blueprints]], [[source-text-blueprints]])

The three `power` strings are the whole of what the data files say about Mantis crew
mechanics; no health value is stored, so Mantis are presumed to use the unstated default
(unlike [[entity-rock-men]], [[entity-crystal-men]] and [[entity-zoltan]], whose blueprints
explicitly restate max health).

### As ships
Mantis hulls carry a **teleporter on every blueprint** — the only faction for which that is
true — and use a weapon pool heavy on missiles and bombs.

| Blueprint | Class name | Sector range | Hull | Max power | Teleporter | Medbay |
|---|---|---|---|---|---|---|
| `MANTIS_SCOUT` | Mantis Scout | `maxSector` 5 | 7 | 10 | 1/3, off at start | off at start |
| `MANTIS_FIGHTER` | Mantis Fighter | `minSector` 1 | 9 | 11 | **1/3, powered at start** | **on at start** |
| `MANTIS_BOMBER` | Mantis Bomber | `minSector` 4 | 11 | 11 | **1/3, powered at start** | off at start |

All three draw from `WEAPONS_MANTIS` (lasers 1–5, `LASER_HEAVY_1/2`, `MISSILES_1/2/3`,
`MISSILES_BREACH`, `BEAM_1/2`, `BOMB_1`, `BOMB_FIRE`, `BOMB_ION`), carry crew class
`mantis`, run `boardingAI: sabotage`, and are members of `SHIPS_MANTIS`. Crew counts are
3/5, 3/5 and 4/6. **No faction augment** — Mantis are the only major faction whose hulls
carry none. (per [[source-autoblueprints]], [[source-text-blueprints]])

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `MANTIS_SCOUT_DLC` → **Mantis Interceptor**; medbay replaced by `clonebay` (1/2, off at
>   start), crew 2/4.
> - `MANTIS_FIGHTER_DLC` → **Mantis Assault**; medbay replaced by `clonebay` (1/3, on at
>   start), crew 2/5.
> - `MANTIS_BOMBER_DLC` → **Mantis Aggressor**; `clonebay` (1/1, off at start), crew 3/6.
>
> Every AE variant swaps the medbay for a clonebay and **starts with a lower crew count**
> than its vanilla counterpart. Teleporters and hull values are unchanged.

**Pirate reskins** exist for all three: `MANTIS_SCOUT_P`, `MANTIS_FIGHTER_P`,
`MANTIS_BOMBER_P` — same hulls, renamed *Pirate Scout / Pirate Fighter / Pirate Bomber*, and
crewed by `class="random"` instead of `mantis` ([[source-dlcpirateblueprints]],
[[source-text-blueprints]]). See [[entity-pirates]].

## Where They Appear
- [[sector-mantis-controlled-sector]] (`MANTIS_SECTOR`, `minSector` 0)
- [[sector-mantis-homeworlds]] (`MANTIS_HOME`, `minSector` 2, `unique`) — same pool plus a
  guaranteed `MANTIS_NAMED_THIEF` beacon

(per [[source-sector-data-xml]])

Both sectors run a `BOARDERS_MANTIS` list on top of `HOSTILE_MANTIS`, so boarding is a
sector-level hazard, not just a per-ship one.

## Events Involving Them

**Mantis-sector furniture**
- [[event-start-beacon-mantis]] · [[event-empty-beacon-mantis]] · [[event-store-mantis]]

**Straight fights and boardings**
- [[event-mantis-fight]] · [[event-mantis-fight-choice]] · [[event-mantis-fight-in-nebula]] ·
  [[event-mantis-fight-choice-in-nebula]] · [[event-mantis-fight-near-sun]] ·
  [[event-mantis-fight-engi]] · [[event-mantis-fight-zoltan]] ·
  [[event-mantis-fight-in-nebula-slug]] · [[event-mantis-fight-slug]]
- [[event-boarders-mantis]] · [[event-no-fuel-mantis-fight]]

**Raiders, slavers and predation**
- [[event-mantis-ship-attacking-civilian]] · [[event-mantis-ship-attacking-crystal]] ·
  [[event-mantis-ship-attacking-slug-ship]] · [[event-mantis-ships-battle-for-rock-freighter]]
- [[event-mantis-ship-collectors]] · [[event-mantis-ship-with-rock-body-parts]] ·
  [[event-mantis-war-camp]] · [[event-mantis-gamble]] · [[event-mantis-outcasts]]
- [[event-slaver-friendly]] · [[event-slaver-hostile]] · [[event-escape-pod]]

**Quest and unlock content**
- [[chain-mantis-cruiser-unlock]] — the Mantis Cruiser line
- [[event-legendary-thief-kazaaakplethkilik]] (`MANTIS_NAMED_THIEF`, guaranteed in the
  Homeworlds) → [[event-mantis-named-thief-stash]]
- [[event-quest-mantis-invasion]] · [[event-mantis-capture-commando]] ·
  [[event-mantis-fugitive]] · [[event-confused-mantis]]
- [[event-engi-ship-attacked-by-mantis-ship]] · [[event-engi-unlock-3]]

**Seen from other factions' pages**
- [[event-lanius-ship-attacking-mantis]] · [[event-zoltan-ship-follows-mantis-ship]] ·
  [[event-zoltan-wise-man]] · [[event-slug-oxygen-malfunction]]

### Blue options gated on Mantis crew (`req="mantis"`)
| Event id | Page |
|---|---|
| `MANTIS_CAPTURE_COMMANDO` | [[event-mantis-capture-commando]] |
| `MANTIS_NAMED_THIEF` | [[event-legendary-thief-kazaaakplethkilik]] |
| `SLUG_DISTRESS_TRICK` | [[event-slug-oxygen-malfunction]] |
| `CONFUSED_MANTIS` | [[event-confused-mantis]] |

Only 4 occurrences of `req="mantis"` in the whole data set — Mantis are a common *enemy*
but a rare *key* (compare 11 each for `engi` and `slug`). (per [[source-events-mantis]],
[[source-events-slug]], [[source-newevents]])

## How To Fight / Deal With Them
- Assume boarders. `MANTIS_FIGHTER` and `MANTIS_BOMBER` have their teleporter **powered at
  spawn**; the scout's is off at start ([[source-autoblueprints]]).
- Mantis crew fight at 1.5× and repair at 0.5×, so Mantis boarders are lethal but Mantis
  ships mend slowly once you breach or burn them ([[source-text-blueprints]]).
- Their weapon pool contains missiles *and* three bomb types, so a defence drone helps but
  does not cover bombs (bombs teleport, they are not projectiles the drone can shoot — that
  mechanic is not stated in the files examined here; recorded as an open question).
- Mantis hulls carry no faction augment, so nothing about them resists fire, breaches or
  hull damage the way [[entity-rock-men]] and [[entity-slugs]] ships do.

## Related
- [[entity-engi]] — the Mantis's usual victim in quest content, and their mechanical
  opposite (0.5× combat / 2× repair)
- [[entity-rock-men]] — [[event-mantis-ship-with-rock-body-parts]],
  [[event-mantis-ships-battle-for-rock-freighter]]
- [[entity-pirates]] — three Mantis hulls are reskinned as pirate ships
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]

## Open Questions
- [ ] Whether Mantis crew have a non-default max health (their blueprint states none).
- [ ] What `rarity` 2 means for crew availability in stores.
- [ ] Whether the AE clonebay swap plus lower starting crew makes Mantis ships easier or
      harder to board — the files state the loadouts but nothing about the trade.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
