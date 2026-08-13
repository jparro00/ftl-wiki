---
id: item-drone-control
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-dock-drone-salesman]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [system, drones]
---

# Drone Control

## Summary
The `drones` system, displayed as **Drone Control** — *"Powers all of the ship's drones. Drones
are automated robots that perform tasks like attacking enemy ships or repairing systems."*
([[source-text-blueprints]]). Note the blueprint id collides with the `drones`
`<itemBlueprint>`, which is the [[item-drone-parts]] consumable.

## Stats
- Blueprint `drones` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 2, `maxPower` 8.
- Purchase cost: **60** scrap.
- Upgrade costs, levels 2→9: 10, 20, 30, 45, 60, 80, 100, 120 scrap. Level 9 is labelled *"Imaginary"*.
- `rarity` 1.

## How To Get It
- **Stores** — 60 scrap ([[source-blueprints]]).
- `DOCK_DRONE_SALESMAN` grants `<upgrade system="drones" amount="1"/>` — [[event-dock-drone-salesman]] ([[source-newevents]]).
- Starting system on the Engi and Federation drone layouts.

## Blue Options It Unlocks
- [[event-dock-drone-salesman]] — `DOCK_DRONE_SALESMAN` — three separate gates at `lvl="3"`, `lvl="5"` and `lvl="7"`, the only `req="drones"` choices in the game

## Strategy Notes
- Drone Control is nearly worthless as a *blue-option* key: one event, three gates, all on
  the same beacon. Its value is entirely in what it powers.
- Every drone needs a [[item-drone-parts]] to deploy, so Drone Control levels without a
  drone-part stock buy nothing.

## Related
- [[item-drone-parts]] — the consumable each deployment costs
- [[item-drones]] — alias page for this system
- [[item-defense-drone]], [[item-combat-drone-mark-i]], [[item-repair-drone]], [[item-hull-repair-drone]], [[item-anti-personnel-drone]], [[item-boarding-drone]], [[item-combat-beam-drone]] — what it powers

## Open Questions
- [ ] Whether `<upgrade system="drones">` appears in any event other than `DOCK_DRONE_SALESMAN`.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
