---
id: item-slug-repair-gel
type: item
item_kind: augment
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [augment, slug, defence]
---

# Slug Repair Gel

## Summary
The `SLUG_GEL` augment — *"Slug ships excrete a thick gel that automatically repairs any hull
breaches."* ([[source-text-blueprints]]).

## Stats
- Blueprint `SLUG_GEL` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **60** scrap. `bp` 12, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.25</value>` — the file does not say what the figure scales.

## How To Get It
- **[[event-slug-unlock-1]]** — destroying the `JELLY_UNLOCK3` escort at the end of the Slug
  Cruiser unlock awards `<augment name="SLUG_GEL"/>`. The ship's destruction text reads
  *"…you discover a unique augment that duplicates the Slug's ability to heal breaches!"*
  ([[source-events-ships]], [[source-text-events-xml]])
- Starting augment on the Slug Cruiser layouts.
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- **None.** No `<choice req="SLUG_GEL">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Breach repair is the one job crew are worst at, so the augment's value scales with how
  breach-heavy the enemies are — but it opens no beacons.
- Note the contrast with [[item-rock-plating]], the other species-flavoured defensive
  augment at a similar price, which gates three events.

## Related
- [[item-slug-crew]] — the species whose ability it copies
- [[event-slug-unlock-1]] — where it is awarded
- [[item-breach-missiles]] — what it is a counter to

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.
- [ ] What `<value>0.25</value>` scales.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
