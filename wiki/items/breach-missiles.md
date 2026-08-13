---
id: item-breach-missiles
type: item
item_kind: weapon
rarity: 3
unlocks_blue: [[[event-crystalline-cache]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [weapon, missile]
---

# Breach Missiles

## Summary
The `MISSILES_BREACH` weapon — *"These missiles are designed to cause maximum destruction to
ship hull armor."* Tooltip: *"Fires 1 missile; 4 damage; pierces all shields; high breach
chance."* ([[source-text-blueprints]]).

## Stats
- Blueprint `MISSILES_BREACH` (`<weaponBlueprint>`), `<type>MISSILES</type>`, [[source-blueprints]].
- Damage **4**, 1 shot, consumes 1 missile, `sp` **5** (pierces all shields).
- `breachChance` **8**, `fireChance` 3, `stunChance` 1.
- Power **3**, cooldown **22**. Cost **65** scrap (`<!--was 70 -->`), `bp` 7, `rarity` 3.

## How To Get It
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.
- No event in `raw/gamedata/` awards `MISSILES_BREACH` by name.

## Blue Options It Unlocks
- [[event-crystalline-cache]] — `CRYSTAL_CACHE` — the only `req="MISSILES_BREACH"` choice in the game: blow the cache open

## Strategy Notes
- The highest single-shot damage of any missile-consuming launcher in [[source-blueprints]] (4, against
  Hermes' 3 and Artemis' 2), at the cost of a 22-second cooldown and 3 power.
- Note the gate is on the *specific* blueprint, not on the `WEAPONS_MISSILES` category —
  carrying an [[item-artemis-missiles]] does not open [[event-crystalline-cache]].

## Related
- [[item-artemis-missiles]] — the standard missile; satisfies the category gate, not this one
- [[item-missile-weapon]] — the `WEAPONS_MISSILES` category (which does include this blueprint)
- [[item-slug-repair-gel]] — the counter to breaches

## Open Questions
- [ ] Whether `breachChance` 8 and `fireChance` 3 share a scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
