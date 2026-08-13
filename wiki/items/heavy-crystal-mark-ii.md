---
id: item-heavy-crystal-mark-ii
type: item
item_kind: weapon
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, crystal]
---

# Heavy Crystal Mark II

## Summary
The `CRYSTAL_HEAVY_2` weapon — *"Modified projectile weapon that fires a shield piercing large
crystal."* Tooltip: *"Pierces 1 shield; fires 1 crystal that deals 4 damage and causes a hull
breach."* ([[source-text-blueprints]]).

## Stats
- Blueprint `CRYSTAL_HEAVY_2` (`<weaponBlueprint>`), `<type>MISSILES</type>` but consumes **no missiles**, [[source-blueprints]].
- Damage **4**, 1 shot, `sp` **1**, `breachChance` **10** (the maximum value in the weapon
  data, shared with the two Breach Bombs and the AE `PDS_SHOT`), `stunChance` 2.
- Power **3**, cooldown **19**, projectile `speed` 50.
- Cost **20** scrap, `bp` 2, **`rarity` 0**.

## How To Get It
- **[[event-crystalline-men-buried]]** — `CRYSTAL_HELP_DIG` awards `<weapon name="CRYSTAL_HEAVY_2"/>` ([[source-events-crystal]]). The only named grant in the event data.
- `rarity` 0.

## Blue Options It Unlocks
- **None.** No `<choice req="CRYSTAL_HEAVY_2">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- 4 damage plus the maximum `breachChance` of 10, ammo-free, at 3 power. Among
  `<type>MISSILES</type>` blueprints it ties [[item-breach-missiles]] for damage without
  spending ammunition; the file records no weapon of any type with higher single-shot damage.
- Matches [[item-breach-missiles]] for damage and beats it on breach chance, without the
  ammunition cost, but pierces only one shield layer rather than all of them.

## Related
- [[item-breach-missiles]] — the missile-based equivalent
- [[item-crystal-burst-mark-ii]] / [[item-crystal-lockdown-bomb]] — the rest of the set
- [[event-crystalline-men-buried]] — where it is awarded

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
