---
id: entity-federation
type: entity
entity_kind: faction
hostility: friendly
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [faction, player-side, endgame, civilian]
---

# The Galactic Federation

## Summary
The side you fly for. The Federation is the losing power in the war against
[[entity-rebels]]: your ship is a Federation cruiser carrying stolen intelligence to the
Federation fleet, and the run ends when you deliver it at the Federation Base in
[[sector-the-last-stand]]. Mechanically the Federation appears as a small number of friendly
or neutral warships, the civilian shipping they protect, and the endgame framing.

Like the Rebels, the Federation is a **political faction with no `crewBlueprint`** — its
ships are crewed `class="human"` ([[source-autoblueprints]]). It is described in
`crew_slug_desc` as the body that shunned the [[entity-slugs]], and in `crew_energy_desc` the
[[entity-zoltan]] and [[entity-engi]] are named as allies ([[source-text-blueprints]]).

## Traits / Stats

### Federation warships

| Blueprint | Class name | Sector range | Hull | Max power | Crew |
|---|---|---|---|---|---|
| `FED_SCOUT` | Federation Scout | `maxSector` 6 | 7 | 10 | 2/3 |
| `FED_BOMBER` | Federation Bomber | `minSector` 1 | 9 | 7 | 2/6 |

Both draw from `WEAPONS_FED` (lasers 1–5, `LASER_HEAVY_1/2`, `MISSILES_1/2/3`,
`MISSILES_BREACH`, `BEAM_1/2`, `BOMB_1`) — the same pool as `WEAPONS_REBEL`, which is
consistent with a civil war fought between two halves of the same navy. Crew class `human`,
no faction augment, `SHIPS_FED` = both. `FED_SCOUT` also runs `boardingAI: sabotage`;
`FED_BOMBER` does not declare one. (per [[source-autoblueprints]],
[[source-text-blueprints]])

Both hulls are also in `SHIPS_CIVILIAN`, the pool used for neutral/civilian shipping.

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `FED_SCOUT_DLC` → **Federation Outrider**; doors replaced by `hacking` (1/1, off at
>   start).
> - `FED_BOMBER_DLC` → **Federation Hacker**; doors → `hacking` (1/1, off), medbay →
>   `clonebay` (1/3, off).

**Pirate reskins:** `FED_SCOUT_P` (*Pirate Scout*) and `FED_BOMBER_P` (*Pirate Bomber*), crew
`class="random"` ([[source-dlcpirateblueprints]]). Federation hulls are therefore among the
ones you fight as [[entity-pirates]].

### The player's ships
Every playable cruiser is a `PLAYER_SHIP_*` blueprint in `blueprints.xml`, including
`PLAYER_SHIP_FED` / `_FED_2` / `_FED_3` — display class **Federation Cruiser**
([[source-blueprints]], [[source-text-blueprints]]). The other playable hulls carry the
species names (Kestrel, Engi, Zoltan, Mantis, Rock, Slug, Stealth, Crystal, Lanius Cruiser),
but all of them are flying for the Federation in fiction.

## Where They Appear
- [[sector-federation-space]] (`STANDARD_SPACE`, `minSector` 0) — the default sector type,
  running the generic `NEUTRAL_CIVILIAN` / `HOSTILE_CIVILIAN` / `QUESTS` pools
- [[sector-civilian-sector]] (`CIVILIAN_SECTOR`, `minSector` 0) — a near-identical pool
- [[sector-the-last-stand]] (`FINAL`, `minSector` 7, `unique`) — the Federation Base and the
  fleet you are trying to reach

(per [[source-sector-data-xml]])

Federation hulls also appear anywhere `SHIPS_CIVILIAN` or `SHIPS_PIRATE` is drawn from.

## Events Involving Them

**The endgame**
- [[event-last-stand-start]] · [[event-federation-base]] · [[event-empty-beacon-last-stand]] ·
  [[event-repair-station-in-last-stand]] · [[event-fight-in-last-stand]] ·
  [[event-boss-destroyed]] — see [[entity-flagship]]

**Federation ships and loyalists in the field**
- [[event-federation-deserters]] · [[event-encrypted-federation-signal]] ·
  [[event-rebel-ship-attacking-federation-loyalists]] ·
  [[event-crystal-ship-attacking-federation-loyalists]] ·
  [[event-rebel-ship-attacking-civilians-in-last-stand]] ·
  [[event-rebel-fight-among-federation-and-rebel-fleets]] ·
  [[event-lanius-with-federation-science-craft]] · [[event-unarmed-zoltan-transport]]

**Civilian shipping under Federation protection**
Most `*-attacking-civilian` and refugee events are Federation-space content by placement
rather than by naming — see [[sector-federation-space]] and [[sector-civilian-sector]] for
the full pools.

### Blue options gated on the Federation
None as a faction. `req="human"` occurs exactly once, in `CONFUSED_MANTIS`
([[event-confused-mantis]]) — the only place in the game where being human is itself the key
([[source-newevents]]).

## How To Fight / Deal With Them
You mostly don't. Federation ships appear as allies, victims or neutral traffic. When one
does turn hostile it is a `WEAPONS_FED` ship — missiles including `MISSILES_BREACH`, lasers,
two beams, one bomb, and **no ion and no drones**, which makes them the least tricky
opposition in the game. The reskinned `FED_*_P` pirate versions are the common way to end up
shooting at a Federation hull ([[source-autoblueprints]],
[[source-dlcpirateblueprints]]).

## Related
- [[entity-rebels]] — the enemy; same weapon pool, opposite side
- [[entity-flagship]] — what stands between you and the Federation fleet
- [[entity-engi]], [[entity-zoltan]] — named allies
- [[entity-slugs]] — named as shunned by the Federation
- [[sector-federation-space]], [[sector-civilian-sector]], [[sector-the-last-stand]]

> **Naming note.** Some event pages link `entity-federation-cruiser`; that refers to the
> playable `PLAYER_SHIP_FED` hull rather than to the faction. If a ship-level page is wanted,
> it should be a separate `entity_kind: ship` page.

## Open Questions
- [ ] Whether the Federation fleet has any ship blueprint of its own beyond `FED_SCOUT` /
      `FED_BOMBER` — the "Federation fleet" of the endgame text has no blueprint in the files
      read here.
- [ ] Why `FED_BOMBER` declares no `boardingAI` when nearly every other hull does.
- [ ] Which sector pools actually place Federation-hulled neutral ships, as opposed to
      generic civilians.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
