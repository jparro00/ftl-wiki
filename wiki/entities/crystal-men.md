---
id: entity-crystal-men
type: entity
entity_kind: species
hostility: varies
version: both
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 9
tags: [species, faction, crew, lockdown, hidden-sector, unlock, oxygen]
---

# Crystal Men

## Summary
The ancestors of the [[entity-rock-men]], sealed away in a hidden sector that most runs
never see. Crystal crew are the game's second-tankiest (125 HP) and carry the only *active*
crew ability in the data — Lockdown, which seals a room. Crystal ships fire crystal weapons
nobody else has. Reaching them at all is a quest chain, not a sector roll. In-game
description:

> Ancient ancestors of the Rockmen.

(`crew_crystal_desc`, per [[source-text-blueprints]])

## Traits / Stats

### As crew — `crewBlueprint name="crystal"`
| Field | Value |
|---|---|
| Display name | **Crystal** (`crew_crystal_title` / `crew_crystal_short`) |
| Cost | 60 (a code comment records the old value as 65) |
| `bp` | 4 |
| `rarity` | 0 |
| Powers | *"Lockdown power (activate in crew box)"* · *"Reduced suffocation damage"* · *"Movement speed reduced by 20 percent"* · *"Max Health is increased to 125"* |

(per [[source-blueprints]], [[source-text-blueprints]])

Four powers — more than any other species. Lockdown is the only power in any crew blueprint
described as *activated* rather than passive. Note the movement penalty is stated precisely
(−20%) where [[entity-rock-men]]'s is only "halved".

**"Reduced suffocation damage" = 50%**, per [[source-fandom-oxygen]] — 3.2 HP/sec against the
standard 6.4. The game files state the power but never the amount. It **stacks with
[[item-emergency-respirators]]**, taking a Crystal crew member to 25% (1.6 HP/sec) — the lowest
non-zero suffocation rate available to any crew. Full table:
[[concept-oxygen-and-suffocation]].

Combined with the 125 max health above, a vented Crystal survives roughly four times as long as
a standard crew member — though see that page's open question on the unconfirmed base rate.

### As ships

| Blueprint | Class name | Sector range | Hull | Max power | Crew | Aug |
|---|---|---|---|---|---|---|
| `CRYSTAL_SCOUT` | Crystal Scout | — | 7 | 9 | 2/3 | none |
| `CRYSTAL_BOMBER` | Crystal Bomber | — | 9 | 9 | 2/5 | none |

`CRYSTAL_SCOUT` spawns with **weapons already at power 4** — the highest starting weapon
power of any non-boss enemy hull in `autoBlueprints.xml`, and unusual for a "scout".

Both draw from `WEAPONS_CRYSTAL`, which is unique and tiny: `BOMB_LOCK`, `CRYSTAL_BURST_1`,
`CRYSTAL_BURST_2`, `CRYSTAL_HEAVY_1`, `CRYSTAL_HEAVY_2`. **No lasers, no beams, no missiles,
no ion, no drones.** Crew class `crystal`, `boardingAI: sabotage`, list `SHIPS_CRYSTAL`.
(per [[source-autoblueprints]], [[source-text-blueprints]])

Crystal hulls are in **no** other list — not `SHIPS_CIVILIAN`, not `SHIPS_PIRATE`. There is
no Crystal pirate reskin and `crystal` is **not** in the `CREW_RANDOM` pool that supplies
pirate crews ([[source-autoblueprints]], [[source-dlcpirateblueprints]]). Crystal Men appear
only where the events put them.

> **Advanced Edition differences** ([[source-dlcblueprintsoverwrite]]):
> - `CRYSTAL_SCOUT_DLC` → **Crystal Outrider**; medbay → `clonebay` (1/3, off at start).
> - `CRYSTAL_BOMBER_DLC` → **Crystal Instigator**; medbay → `clonebay`, plus **`cloaking`
>   (1/2, powered) and `teleporter` (1/2, powered)** — neither of which the vanilla bomber
>   has.
>
> So in AE the Crystal Bomber cloaks and boards; in vanilla it does neither.

## Where They Appear
- [[sector-hidden-crystal-worlds]] (`CRYSTAL_HOME`, `minSector` 0, `unique`) — the only
  Crystal sector. Its pool is six lists, all `_CRYSTAL`: `STORE_CRYSTAL`, `ITEMS_CRYSTAL`,
  `NOTHING_CRYSTAL`, `HOSTILE_CRYSTAL`, `BOARDERS_CRYSTAL`, `NEUTRAL_CRYSTAL`. There is no
  `DISTRESS_BEACON_CRYSTAL` and no `QUESTS_CRYSTAL` ([[source-sector-data-xml]]).
- Individual Crystal ships also appear in other sectors through specific events (see below).

Getting to the sector is itself the [[chain-crystal-cruiser-unlock]] storyline, which starts
at [[event-ancient-device]] in [[sector-rock-homeworlds]].

## Events Involving Them

**Crystal-sector furniture**
- [[event-start-beacon-crystal]] · [[event-empty-beacon-crystal]] · [[event-store-crystal]]

**Crystal encounters**
- [[event-crystal-fight]] · [[event-crystal-fight-choice]] · [[event-boarders-crystal]] ·
  [[event-auto-ship-fight-crystal]] · [[event-rebel-fight-crystal]]
- [[event-crystal-fight-with-surrender-offer-hull-repairs]] ·
  [[event-crystal-fight-with-surrender-offer-human-crew]] — see [[concept-surrender-offers]]
- [[event-crystal-chat]] · [[event-crystal-scrap-collector]] ·
  [[event-crystalline-ship-messaging-about-rebels]] ·
  [[event-crystal-ship-attacking-federation-loyalists]]

**The unlock chain and Crystal lore**
- [[event-ancient-device]] → [[chain-crystal-cruiser-unlock]] → [[event-crystal-unlock]]
- [[event-crystalline-cache]] · [[event-crystalline-men-buried]] ·
  [[event-crystalline-research-facility]] · [[event-zoltan-research-facility]]

**Crystal ships as third parties**
- [[event-mantis-ship-attacking-crystal]] · [[event-pirate-ship-attacking-crystal]] ·
  [[event-rebel-ship-attacking-crystal-ship]]

### Blue options gated on Crystal crew (`req="crystal"`)
| Event id | Page |
|---|---|
| `ROCK_CRYSTAL_BEACON` | [[event-ancient-device]] |
| `CRYSTAL_CACHE` | [[event-crystalline-cache]] |
| `CRYSTAL_CHATTY` | [[event-crystal-chat]] |

Only 3 occurrences of `req="crystal"` — and one of them (`ROCK_CRYSTAL_BEACON`) is the
entry point to the chain that gets you Crystal crew in the first place.
(per [[source-events-xml]], [[source-events-crystal]])

## How To Fight / Deal With Them
- **Their weapon pool is five weapons wide and all of them are crystal.** No missiles means
  a defence drone is dead weight; no ion means your shields stay up if they hold. Whether
  crystal weapons pierce shields is not stated in the files examined here — recorded as an
  open question rather than assumed.
- `BOMB_LOCK` is in their pool: they can lock down your rooms the way Crystal crew can.
- Crystal crew have 125 HP and reduced suffocation damage, so venting a Crystal boarding
  party is slow and melee against them is expensive.
- No faction augment on either hull — unlike [[entity-rock-men]] (`ROCK_ARMOR`),
  [[entity-slugs]] (`SLUG_GEL`) or [[entity-zoltan]] (`ENERGY_SHIELD`), there is no passive
  to play around.
- In AE the bomber cloaks and teleports; in vanilla it does neither
  ([[source-dlcblueprintsoverwrite]]).

## Related
- [[entity-rock-men]] — Crystal Men are their stated ancestors; the schism drives
  [[event-rock-atheists]] and [[event-crystalline-men-buried]]
- [[chain-crystal-cruiser-unlock]] — how you reach them
- [[item-crystal-vengeance]] — the augment named for them
- [[sector-hidden-crystal-worlds]]
- [[concept-oxygen-and-suffocation]] — where their 50% suffocation reduction sits

## Open Questions
- [ ] Whether `CRYSTAL_BURST_*` / `CRYSTAL_HEAVY_*` pierce shields — not stated in the
      blueprint fields examined here.
- [ ] Whether Crystal Men can ever be hired at a store (`rarity` 0, and they are excluded
      from `CREW_RANDOM`).
- [ ] Why `CRYSTAL_SCOUT` starts at weapon power 4.
- [x] ~~What "reduced suffocation damage" is as a number.~~ **Answered 2026-08-14: 50%**, i.e.
      3.2 HP/sec of the standard 6.4 ([[source-fandom-oxygen]]). Community-sourced, not from the
      game files — see [[concept-oxygen-and-suffocation]] for the caveat on the base rate.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-dlcpirateblueprints]] (per raw/gamedata/dlcPirateBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
