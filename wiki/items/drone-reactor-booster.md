---
id: item-drone-reactor-booster
type: item
item_kind: augment
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, drones]
---

# Drone Reactor Booster

## Summary
The `DRONE_SPEED` augment — *"Your shipboard drones have their movement speed increased by 25
percent."* ([[source-text-blueprints]]).

## Stats
- Blueprint `DRONE_SPEED` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **50** scrap. `bp` 9, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.25</value>`.

## How To Get It
- **[[event-the-engi-virus]]** — `ENGI_VIRUS` awards `<augment name="DRONE_SPEED"/>` ([[source-events-engi]]). The only named grant in the event data.
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- **None.** No `<choice req="DRONE_SPEED">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- "Shipboard" is the operative word: the description scopes it to drones walking around a
  ship, i.e. [[item-repair-drone]], [[item-anti-personnel-drone]] and [[item-boarding-drone]],
  not to combat drones in space. No file in `raw/` states the boundary more precisely.
- Byte-for-byte the drone twin of [[item-mantis-pheromones]].

## Related
- [[item-mantis-pheromones]] — the identical augment for crew
- [[item-repair-drone]] / [[item-anti-personnel-drone]] / [[item-boarding-drone]] — the drones that walk
- [[event-the-engi-virus]] — the named grant

## Open Questions
- [ ] Whether "shipboard" excludes combat and defence drones.
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
