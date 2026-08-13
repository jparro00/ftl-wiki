---
id: item-crystal-burst-mark-ii
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

# Crystal Burst Mark II

## Summary
The `CRYSTAL_BURST_2` weapon — *"Modified projectile weapon that fires 3 shield piercing
crystals."* Tooltip: *"Pierces 1 shield; fires 3 crystals that deal 1 damage each."*
([[source-text-blueprints]]).

## Stats
- Blueprint `CRYSTAL_BURST_2` (`<weaponBlueprint>`), `<type>MISSILES</type>` but consumes **no missiles**, [[source-blueprints]].
- Damage **1** × **3 shots**, `sp` **1** (pierces one shield layer).
- `breachChance` 1, `stunChance` 1, `fireChance` 0.
- Power **3**, cooldown **17**, projectile `speed` 50.
- Cost **20** scrap, `bp` 2, **`rarity` 0**.

## How To Get It
- **[[event-crystal-scrap-collector]]** — the `CRYSTAL_SCRAP_EXCITED_LIST` pool awards `<weapon name="CRYSTAL_BURST_2"/>` ([[source-events-crystal]]).
- Starting weapon on the Crystal Cruiser layouts.
- `rarity` 0.

## Blue Options It Unlocks
- **None.** No `<choice req="CRYSTAL_BURST_2">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Filed under `<type>MISSILES</type>` in the blueprint but with no `<missiles>` tag, so it
  fires free — the Crystal weapons are ammo-less shield-piercers.
- 20 scrap listed cost against 65 for a [[item-halberd-beam]]: the Crystal set is priced as
  quest loot, not as store stock.

## Related
- [[item-heavy-crystal-mark-ii]] — the heavy variant
- [[item-crystal-lockdown-bomb]] — the utility piece of the same set
- [[chain-crystal-cruiser-unlock]]

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
