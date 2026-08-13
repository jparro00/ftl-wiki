---
id: item-titanium-system-casing
type: item
item_kind: augment
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, defence, engi]
---

# Titanium System Casing

## Summary
The `SYSTEM_CASING` augment — *"All ship systems have additional plating that provides a 15
percent chance to negate damage when hit (hull will still be damaged)"*
([[source-text-blueprints]]). The mirror image of [[item-rock-plating]].

## Stats
- Blueprint `SYSTEM_CASING` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **80** scrap (`<!--was 100-->`). `bp` 15, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.15</value>`.
- A commented-out `<title>Reinforced System Casing</title>` survives in the file — an older name.

## How To Get It
- **[[event-engi-unlock-4]]** — `ENGI_UNLOCK_4` awards `<augment name="SYSTEM_CASING"/>` ([[source-events-engi]]).
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- **None.** No `<choice req="SYSTEM_CASING">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Purely a combat augment; it opens no beacons. [[item-rock-plating]], with the identical
  15 percent and the identical 80-scrap price, opens three.

## Related
- [[item-rock-plating]] — same mechanic, hull instead of systems, and it does gate events
- [[event-engi-unlock-4]] — the named grant

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.
- [ ] Whether the old "Reinforced System Casing" name appears in any shipped build.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
