---
id: item-backup-dna-bank
type: item
item_kind: augment
rarity: 2
unlocks_blue: [[[event-crystalline-research-facility]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, advanced-edition, crew]
---

# Backup DNA Bank

## Summary
The `BACKUP_DNA` augment, added in Advanced Edition — *"Your crew is safe in clone storage even
if the system is off or broken."* ([[source-text-blueprints]]). Insurance for a
[[item-clone-bay]] ship.

## Stats
- Blueprint `BACKUP_DNA` (`<augBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Cost: **40** scrap (`<!-- Was 35-->`). `bp` 8, `rarity` 2. `<stackable>false</stackable>`, `<value>0.0</value>`.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `BACKUP_DNA` by name.

## Blue Options It Unlocks
- [[event-crystalline-research-facility]] — `CRYSTAL_HUMAN_TESTS`, tagged `<!--DLC-->` — the only `req="BACKUP_DNA"` choice in the game

## Strategy Notes
- Only meaningful on a Clone Bay ship: the augment protects stored crew when the system is
  off or destroyed, which is the Clone Bay's one catastrophic failure mode.
- Its single blue option is on a Crystal-sector genetics beacon — thematic, not mechanical.

## Related
- [[item-clone-bay]] — the system it insures
- [[event-crystalline-research-facility]] — its only gate

## Open Questions
- [ ] Whether the augment does anything at all on a ship with a [[item-medbay]] instead.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
