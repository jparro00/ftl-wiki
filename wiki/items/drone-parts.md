---
id: item-drone-parts
type: item
item_kind: unknown
rarity: 3
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [consumable, drones]
---

# Drone Part

## Summary
The `drones` `<itemBlueprint>` — *"Allows you to deploy drone schematics you've found. Each
deployment costs one drone part."* ([[source-text-blueprints]]). A consumable resource, not a
weapon/drone/augment/system, so `item_kind` has no correct value in the schema.

## Stats
- Blueprint `drones`, `<itemBlueprint>` with `<type>ITEM_DRONE</type>`, [[source-blueprints]].
- Cost: **8** scrap each. `rarity` 3.
- For comparison: fuel is 3 scrap, a missile 6 ([[source-blueprints]]).

## How To Get It
- **Stores**, and as `<item_modify>` / `autoReward` payloads in a large number of events.
- Events pay drone parts through `autoReward` type strings rather than named blueprints, so
  a per-event list is not derivable from the blueprint files alone.

## Blue Options It Unlocks
- None. `req="drones"` in events refers to the **system** (see [[item-drone-control]]),
  not to this consumable. ([[source-newevents]])

## Strategy Notes
- Every drone launch and every [[item-hacking]] hack consumes one, so drone parts are the
  hidden running cost of both systems.
- The [[item-hull-repair-drone]] converts one part into 3–5 hull ([[source-text-blueprints]]),
  which is the cheapest hull-per-scrap in the game at 8 scrap a part.

## Related
- [[item-drone-control]] — the system that spends them
- [[item-hacking]] — also spends them
- [[item-hull-repair-drone]] — the highest-value sink

## Open Questions
- [ ] A full list of events that pay drone parts — needs the `autoReward` payload tables, not the blueprint files.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
