---
id: entity-engi
type: entity
entity_kind: species
hostility: friendly
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 11
tags: [species, faction, crew, repair, federation-allied]
---

# Engi

## Summary
A machine-or-machine-adjacent species allied to the Federation, and the wiki's best-covered
"friendly" faction. Engi appear three ways: as **crew** (the best repairers in the game and
the worst fighters), as **enemy/neutral ships** built around ion weapons, beams and defence
drones, and as the **owners of two sectors**. Their in-game description is deliberately
non-committal about what they are:

> It's unclear if the 'Engi' are partly organic or entirely mechanical, but it's well known
> that they make exceptional engineers.

(`crew_engi_desc`, per [[source-text-blueprints]])

## Traits / Stats

### As crew — `crewBlueprint name="engi"`
| Field | Value |
|---|---|
| Display name | **Engi** (`crew_engi_title` / `crew_engi_short`) |
| Cost | 50 |
| `bp` | 2 |
| `rarity` | 2 |
| Powers | *"Repair speed is doubled"* · *"Combat damage inflicted is halved"* |

(per [[source-blueprints]], [[source-text-blueprints]])

No numeric health, move-speed or damage multiplier is stored in the XML for any species —
the two `power` strings above are the whole of what the data files say about Engi crew
mechanics. The Engi blueprint carries no `colorList`, unlike most other species.

> The `rarity` scale's meaning (0–5) is not defined anywhere in `raw/gamedata/`. Engi are
> `2`, the same as [[entity-mantis]]; [[entity-zoltan]] are `5` and
> [[entity-slugs]]/[[entity-crystal-men]]/[[entity-lanius]] are `0`. Recording the numbers,
> not an interpretation.

### As ships
Engi hulls use the `CIRCLE_*` internal prefix. They are the only faction whose weapon pool
contains **no missiles and no bombs**.

| Blueprint | Class name | Sector range | Hull | Max power | Notable systems | Aug |
|---|---|---|---|---|---|---|
| `CIRCLE_SCOUT` | Engi Scout | `maxSector` 7 | 7 | 8 | drones 2/8, shields 2/8, weapons 2/8 | `NANO_MEDBAY` |
| `CIRCLE_BOMBER` | Engi Bomber | `minSector` 1 | 9 | 8 | drones 2/8, shields 2/10, weapons 2/10 | `NANO_MEDBAY` |

Both draw weapons from `WEAPONS_CIRCLE` (lasers 1–3, `LASER_HEAVY_1`, `BEAM_1/2/3`,
`BEAM_LONG`, `BEAM_FIRE`, `ION_1/2/4`) and drones from `DRONES_DEFENSE`
(`DEFENSE_1`, `DEFENSE_2_ENEMY`). Crew class is `engi`; `boardingAI` is `sabotage`.
Both are members of the `SHIPS_CIRCLE` and `SHIPS_CIVILIAN` blueprint lists.
(per [[source-autoblueprints]], [[source-text-blueprints]])

**`NANO_MEDBAY` — "Engi Med-bot Dispersal":** *"Engi nano med-bots heal the crew outside of
the med-bay (at a reduced speed)."* ([[source-text-blueprints]]) Every Engi hull carries it,
so an Engi ship's crew heals wherever they are standing.

> **Advanced Edition differences.** `dlcBlueprintsOverwrite.xml` redefines both hulls
> ([[source-dlcblueprintsoverwrite]]):
> - `CIRCLE_SCOUT_DLC` — renamed **Engi Outrider**, gains `hacking` (1/2, off at start) and
>   `clonebay` (1/3, off at start) in place of the medbay.
> - `CIRCLE_BOMBER_DLC` — renamed **Engi Hacker**, gains `hacking` (1/3) and `clonebay`
>   (1/3), both off at start.
>
> Hull, crew counts and augments are unchanged. So in AE an Engi ship can hack you; in
> vanilla it cannot.

Engi hulls are **not** in `SHIPS_PIRATE` — there is no Engi pirate reskin, unlike
[[entity-rock-men]], [[entity-mantis]], [[entity-slugs]], [[entity-zoltan]],
[[entity-federation]] and [[entity-rebels]] ([[source-autoblueprints]],
[[source-dlcpirateblueprints]]). `engi` *is* in the `CREW_RANDOM` list, so Engi can crew a
pirate ship even though no pirate ship is an Engi hull.

## Where They Appear
- [[sector-engi-controlled-sector]] (`ENGI_SECTOR`, `minSector` 0) — the standard Engi
  sector; every event list is the `_ENGI` variant.
- [[sector-engi-homeworlds]] (`ENGI_HOME`, `minSector` 2, `unique`) — same pool plus a
  guaranteed `ENGI_UNLOCK_1` beacon.
- Engi ships also appear outside Engi space via `SHIPS_CIVILIAN`.

(per [[source-sector-data-xml]])

## Events Involving Them

**Engi-sector furniture**
- [[event-start-beacon-engi]] · [[event-empty-beacon-engi]] · [[event-store-engi]] ·
  [[event-free-scrap-with-resources-engi]] · [[event-engi-cache]]

**Engi ships and stations**
- [[event-engi-fight]] — the standard Engi hostile encounter
- [[event-engi-surrender]] · [[event-engi-smashed-ships]] · [[event-engi-research-station]]
- [[event-engi-ship-attacked-by-mantis-ship]] · [[event-engi-distress-rebel-fight]]
- [[event-no-fuel-engi-ship-repair]] · [[event-no-fuel-refugee-damaged]]
- [[event-engi-refugees]] · [[event-engi-monster]]
- [[event-malfunctioning-defense-system]] · [[event-distress-engi-rebel-result]]

**The Engi Cruiser unlock line**
- [[event-engi-fleet-discussion]] (`ENGI_UNLOCK_1`, guaranteed in the Homeworlds) →
  [[event-engi-unlock-2real]] / [[event-engi-unlock-2fake]]
  (+ [[event-engi-unlock-2real-surrender]], [[event-engi-unlock-2fake-surrender]]) →
  [[event-engi-unlock-3]] → [[event-engi-unlock-4]]
- [[event-the-engi-virus]] — `ENGI_VIRUS`, also gates on [[entity-lanius]] crew in AE

**Cross-faction appearances**
- [[event-confused-mantis]] · [[event-mantis-fight-engi]] · [[event-mantis-capture-commando]] ·
  [[event-mantis-fugitive]] · [[event-quest-mantis-invasion]] ·
  [[event-mantis-ship-attacking-civilian]]
- [[event-pirate-fight-engi]] · [[event-pirate-engine-hacker]] · [[event-empty-beacon-pirate]] ·
  [[event-slaver-friendly]] · [[event-slaver-hostile]]
- [[event-rebel-fight-engi]] · [[event-last-stand-start]]
- [[event-intelligent-ponies]] · [[event-unknown-disease-on-mining-colony]]

### Blue options gated on Engi crew (`req="engi"`)
| Event id | Page |
|---|---|
| `DISTRESS_SATELLITE_DEFENSE` | [[event-malfunctioning-defense-system]] |
| `DISTRESS_STATION_DISEASE` | [[event-unknown-disease-on-mining-colony]] |
| `DISTRESS_STATION_FIRE`… see [[entity-rock-men]] | — |
| `SAVE_ENGI_STATION` | sub-event of [[event-engi-ship-attacked-by-mantis-ship]] |
| `ENGI_UNLOCK_1` | [[event-engi-fleet-discussion]] |
| `ENGI_SEX` | [[event-engi-smashed-ships]] |
| `ENGI_VIRUS` | [[event-the-engi-virus]] |
| `NO_FUEL_REFUGEE_DAMAGED` | [[event-no-fuel-refugee-damaged]] |
| `SECRET_WORD_ABADOTH_CONCLUSION` | sub-event of [[event-secret-word-abadoth]] |
| `ENGI_REFUGEES` | [[event-engi-refugees]] |
| `DERELICT_TREASURE` | [[event-derelict-treasure]] (`nameEvents.xml`) |
| `BIG_NAME_TEST` | *no page — dev/test stub* (`nameEvents.xml`) |

(scan of `req="engi"` across `raw/gamedata/*.xml`: [[source-events-xml]],
[[source-events-engi]], [[source-events-fuel]], [[source-events-slug]],
[[source-nameevents]])

`req="engi"` is tied for the most-used species gate in the game (11 occurrences, level with
`req="slug"`).

## How To Fight / Deal With Them
- Engi ships bring **no missiles and no bombs** — a defence drone is wasted against them,
  and a plain shield stack answers most of their pool ([[source-autoblueprints]]).
- Both hulls run a defence drone of their own, so your missiles and boarding drones are the
  things at risk, not theirs.
- In AE both hulls can carry Hacking ([[source-dlcblueprintsoverwrite]]); in vanilla they
  cannot.
- Engi crew are `combat damage halved`, so an Engi-crewed ship is unusually soft to boarding
  — and conversely Engi are the worst species to board *with* ([[source-text-blueprints]]).
- Engi ships are `boardingAI: sabotage`, i.e. boarders go for systems rather than crew.

## Related
- [[entity-zoltan]] — *"The 'Zoltan' are allies of the 'Engi'"* (`crew_energy_desc`,
  [[source-text-blueprints]])
- [[entity-mantis]] — the antagonist in most Engi-sector quest content
- [[entity-federation]] — Engi space is Federation-aligned
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] What the `rarity` scale means for crew blueprints (Engi are `2`).
- [ ] Engi crew's actual repair multiplier and combat multiplier as numbers — the XML only
      gives the words "doubled" and "halved".
- [ ] Whether `DERELICT_TREASURE` (`nameEvents.xml`) is live content; it has an Engi blue
      option but no wiki page.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
