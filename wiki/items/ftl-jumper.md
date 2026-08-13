---
id: item-ftl-jumper
type: item
item_kind: augment
rarity: 3
unlocks_blue: [[[event-escort-civilians-ftl-haywire]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, navigation]
---

# Adv. FTL Navigation

## Summary
The `FTL_JUMPER` augment, titled **Adv. FTL Navigation** in game — *"Allows the ship to jump to
any previously visited Beacon."* ([[source-text-blueprints]]). Event pages link it under the
blueprint id, hence the slug.

## Stats
- Blueprint `FTL_JUMPER` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **50** scrap (`<!--was 60-->`). `bp` 5, `rarity` 3. `<stackable>false</stackable>`.
- Not to be confused with `FTL_BOOSTER` (FTL Recharge Booster) or `FTL_JAMMER` (FTL Jammer),
  which are separate blueprints in the same file.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `FTL_JUMPER` by name.

## Blue Options It Unlocks
- [[event-escort-civilians-ftl-haywire]] — `ESCORT_BEACON` — the only `req="FTL_JUMPER"` choice in the game

## Strategy Notes
- A single blue option, and it is on the escort quest whose whole problem is a broken FTL
  drive — the augment is the literal answer to the beacon.
- `rarity` 3 makes it one of the more commonly stocked augments among those recorded here.

## Related
- [[event-escort-civilians-ftl-haywire]] — its only gate
- [[item-distraction-buoys]] — the other map-manipulating augment

## Open Questions
- [ ] Whether the game ever refers to this augment by its blueprint id in the UI (the wiki slug does).

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
