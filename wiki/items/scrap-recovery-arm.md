---
id: item-scrap-recovery-arm
type: item
item_kind: augment
rarity: 1
unlocks_blue: [[[event-large-asteroid-field]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, economy]
---

# Scrap Recovery Arm

## Summary
The `SCRAP_COLLECTOR` augment — *"Allows the ship to collect 10 percent more scrap from any
source."* ([[source-text-blueprints]]). One of only two augments in the file marked
`<stackable>true</stackable>`.

## Stats
- Blueprint `SCRAP_COLLECTOR` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **50** scrap. `bp` 8, `rarity` 1.
- `<stackable>true</stackable>` — multiple copies are allowed. `<value>0.10</value>`.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `SCRAP_COLLECTOR` by name.

## Blue Options It Unlocks
- [[event-large-asteroid-field]] — `ASTEROID_EXPLORE` — the only `req="SCRAP_COLLECTOR"` choice in the game

## Strategy Notes
- Stackability is the interesting property: the blueprint file explicitly permits more than
  one, unlike almost every other augment ([[source-blueprints]]).
- Its single blue option is thematically apt — a scrap-collecting arm in an asteroid field.
- Only two augments in [[source-blueprints]] carry `<stackable>true</stackable>`: this one
  and [[item-damaged-stasis-pod]]. Everything else is explicitly one-per-ship.

## Related
- [[item-damaged-stasis-pod]] — the other augment flagged `<stackable>true</stackable>` in [[source-blueprints]]
- [[event-large-asteroid-field]] — its only gate

## Open Questions
- [ ] Whether stacked copies multiply or add — the file gives one `<value>` and no stacking rule.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
