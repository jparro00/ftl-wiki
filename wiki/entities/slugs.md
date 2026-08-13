---
id: entity-slugs
type: entity
entity_kind: species
hostility: varies
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [species, faction, crew, nebula, telepathy, sensors]
---

# Slugs

## Summary
Telepathic con artists who live in nebulas. Slug crew see through walls without sensors —
which matters enormously because their own home sectors are nebula sectors where sensors
don't work — and are immune to mind control. Slug ships self-repair hull breaches. Slug
events are the wiki's densest cluster of scams, tolls, fake stores and shakedowns.
In-game description:

> These telepathic Slugs were shunned in the Galactic Federation for their constant thievery
> and attempts at manipulation.

(`crew_slug_desc`, per [[source-text-blueprints]])

Slug ships use the `JELLY_*` internal prefix and `jelly_*` layouts. Grep for both.

## Traits / Stats

### As crew — `crewBlueprint name="slug"`
| Field | Value |
|---|---|
| Display name | **Slug** (`crew_slug_title` / `crew_slug_short`) |
| Cost | 45 — tied with Human for the cheapest |
| `bp` | 2 |
| `rarity` | 0 |
| Powers | *"Telepathic powers reveal rooms and lifeforms even when sensors are down."* · *"Immune to mind control."* |

(per [[source-blueprints]], [[source-text-blueprints]])

The mind-control immunity is an Advanced Edition-relevant power (mind control is an AE
system), but the string sits in the base `blueprints.xml` power list, so this page records it
without asserting a vanilla/AE split.

### As ships

| Blueprint | Class name | Sector range | Hull | Max power | Crew | Aug |
|---|---|---|---|---|---|---|
| `JELLY_BUTTON` | Slug Interceptor | `maxSector` 4 | 9 | 7 | 2/3 | `SLUG_GEL` |
| `JELLY_CROISSANT` | Slug Light-Cruiser | `minSector` 1 | 10 | 7 | 3/6 | `SLUG_GEL` |
| `JELLY_TRUFFLE` | Slug Assault | `minSector` 4 | 11 | 10 | 4/7 | `SLUG_GEL` |

All three draw from `WEAPONS_JELLY` (lasers 1–3, `LASER_HEAVY_1/2`, `MISSILES_2`,
`MISSILES_BREACH`, `BEAM_1/2/3`, `BEAM_LONG`, `BEAM_FIRE`, `BOMB_FIRE`, `BOMB_BREACH`,
`ION_1`, `ION_4`), carry crew class `slug`, run `boardingAI: sabotage`, and make up
`SHIPS_JELLY`. `JELLY_TRUFFLE` spawns with 14 missiles rather than the usual 10 and has a
1-power cloak (off at start). `JELLY_BUTTON` is also the sole Slug entry in
`SHIPS_CIVILIAN`. (per [[source-autoblueprints]], [[source-text-blueprints]])

Note what `WEAPONS_JELLY` **lacks**: `MISSILES_1`, `MISSILES_3` and `BOMB_1`. What it adds
that few others have: `BOMB_BREACH` and `BEAM_LONG`.

**`SLUG_GEL` — "Slug Repair Gel":** *"Slug ships excrete a thick gel that automatically
repairs any hull breaches."* ([[source-text-blueprints]]) On all three hulls, so breach
weapons are largely wasted against Slugs.

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `JELLY_BUTTON_DLC` → **Slug Scout**; loadout otherwise unchanged, crew still 2/3.
> - `JELLY_CROISSANT_DLC` → **Slug Light-Surveyor**; gains `mind` control (1/2, off at
>   start), medbay → `clonebay`; crew 3/**7**.
> - `JELLY_TRUFFLE_DLC` → **Slug Instigator**; gains `mind` control (1/2), medbay →
>   `clonebay`, cloak moved rooms; crew 4/**8**.
>
> Slugs are the one faction whose AE variants **raise** max crew rather than lowering
> starting crew. Two of three hulls gain mind control — thematically consistent with a
> telepathic species, and worth knowing since your own Slug crew are immune to it.

**Pirate reskins:** all three — `JELLY_BUTTON_P`, `JELLY_CROISSANT_P`, `JELLY_TRUFFLE_P`
(*Pirate Interceptor*, *Pirate Light-Cruiser*, *Pirate Assault*), crew `class="random"`
([[source-dlcpirateblueprints]], [[source-text-blueprints]]).

## Where They Appear
- [[sector-slug-controlled-nebula]] (`SLUG_SECTOR`, `minSector` 3)
- [[sector-slug-home-nebula]] (`SLUG_HOME`, `minSector` 3, `unique`) — adds a
  `NEBULA_SLUG_FIGHT_UNLOCK` beacon

Both sectors' event pools are built from `NEBULA_*_SLUG` and `STORM_SLUG` lists — i.e. the
whole sector is nebula terrain, so **your sensors are down by default and theirs aren't**
([[source-sector-data-xml]]). This is the single most important fact about fighting in Slug
space.

Slug hulls also turn up in [[sector-uncharted-nebula]]-style nebula content and as pirates
anywhere.

## Events Involving Them

**Slug-sector furniture**
- [[event-start-beacon-slug]] · [[event-empty-beacon-slug]] · [[event-empty-nebula-beacon-slug]] ·
  [[event-store-in-nebula-slug]]

**Scams, tolls and manipulations — the Slug signature**
- [[event-slug-store-ship]] (the fake store) · [[event-slug-repair-station]] ·
  [[event-slug-comm-tapping]] · [[event-slug-drink]] · [[event-slug-moons-question]] ·
  [[event-slocknog]] · [[event-the-black-raven]] · [[event-intelligent-ponies]]
- [[event-slug-hacker-choice]] → [[event-slug-hacker-doors]] /
  [[event-slug-hacker-medical]] / [[event-slug-hacker-oxygen]]
- [[event-slug-oxygen-malfunction]] · [[event-slug-distress-piloting]] ·
  [[event-single-life-form-on-moon]] · [[event-secret-word-abadoth]]

**Fights and surrenders**
- [[event-slug-fight]] · [[event-slug-fight-in-nebula]] · [[event-slug-fight-in-plasma-storm]] ·
  [[event-mantis-fight-in-nebula-slug]] · [[event-mantis-fight-slug]] ·
  [[event-pirate-fight-slug]] · [[event-rebel-fight-slug]]
- [[event-slug-surrender]] · [[event-slug-home-nebula-surrender]] ·
  [[event-slug-unlock-surrender]] · [[event-slug-unlock-1]] — see
  [[chain-slug-cruiser-unlock]]

**Fuel, trade and refugees**
- [[event-no-fuel-slug-fuel-depot]] · [[event-no-fuel-slug-fuel-trader]] ·
  [[event-refugee-slug]] · [[event-refugee-distress-slug]] · [[event-refugee]] ·
  [[event-refugee-distress]] · [[event-pirate-ship-selling-drones]]

**Cross-faction**
- [[event-rock-and-slug-standoff]] · [[event-slug-and-rock-standoff-in-nebula]] ·
  [[event-slug-ship-boarding-rock-ship]] · [[event-mantis-ship-attacking-slug-ship]] ·
  [[event-lanius-ship-attacking-slug]] · [[event-zoltan-security-checkpoint]] ·
  [[event-zoltan-wise-man]] · [[event-nebula-wreckage]] ·
  [[event-auto-ship-carrying-shield-virus]]

### Blue options gated on Slug crew (`req="slug"`)
| Event id | Page |
|---|---|
| `STRANDED` | sub-event of [[event-single-life-form-on-moon]] |
| `DONOR_PONY` | [[event-intelligent-ponies]] |
| `DONOR_BLACK_RAVEN` | [[event-the-black-raven]] |
| `FUEL_ON_SLUG_CHUCKLE` | [[event-no-fuel-slug-fuel-trader]] |
| `ROCK_LOOTING` | [[event-disabled-rock-ship]] |
| `NEBULA_SLUG_FAKE_STORE` | [[event-slug-store-ship]] |
| `SLUG_UNLOCK_2` | see [[event-slug-unlock-surrender]] / [[event-slug-home-nebula-surrender]] |
| `NEBULA_BATTLEFIELD` | [[event-nebula-wreckage]] |
| `SECRET_WORD_ABADOTH` | [[event-secret-word-abadoth]] |
| `ZOLTAN_CREW_SCAN` | [[event-zoltan-security-checkpoint]] |
| `CONTACT_PIRATE_SALESMAN` | see [[event-dock-bomb-salesman]] / [[event-dock-drone-salesman]] |

11 occurrences of `req="slug"` — tied with `req="engi"` for the most-used species gate.
(per [[source-events-xml]], [[source-events-fuel]], [[source-events-rock]],
[[source-events-slug]], [[source-events-zoltan]], [[source-newevents]])

## How To Fight / Deal With Them
- **You are blind and they are not.** Slug sectors are nebula sectors; your sensors don't
  function, and Slug crew see your rooms regardless ([[source-sector-data-xml]],
  [[source-text-blueprints]]). Carrying one Slug of your own is the cheapest fix.
- **Breach weapons are near-useless.** `SLUG_GEL` repairs hull breaches automatically on
  every Slug hull — and `WEAPONS_JELLY` is one of only two pools carrying `BOMB_BREACH`, so
  they can do to you what you cannot do to them ([[source-text-blueprints]]).
- Fire is their other tool: `BOMB_FIRE` and `BEAM_FIRE` are both in the pool. Consider
  [[entity-rock-men]] crew, who are fire-immune.
- In AE, two of three hulls can mind-control your crew — but not your Slug crew
  ([[source-dlcblueprintsoverwrite]], [[source-text-blueprints]]).
- Slug missile pressure is light: only `MISSILES_2` and `MISSILES_BREACH` are in the pool.

## Related
- [[entity-rock-men]] — the recurring standoff partner
- [[entity-zoltan]] — Slugs are the natural counter to Zoltan checkpoint scans
- [[entity-pirates]] — all three Slug hulls have pirate reskins
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] Whether Slug telepathy has a range limit (the string implies whole-ship vision).
- [ ] Whether mind-control immunity applies in vanilla at all, given mind control is an AE
      system — the power string is in the base file.
- [ ] What `rarity` 0 means; Slug, Crystal and Lanius all share it.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
