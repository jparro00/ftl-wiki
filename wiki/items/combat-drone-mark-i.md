---
id: item-combat-drone-mark-i
type: item
item_kind: drone
rarity: 2
unlocks_blue: [[[event-auto-ship-near-radar-station]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [drone, combat]
---

# Combat Drone Mark I

## Summary
The `COMBAT_1` drone — *"Powerful drone that continually attacks the enemy ship."*
([[source-text-blueprints]]).

## Stats
- Blueprint `COMBAT_1` (`<droneBlueprint>`), `<type>COMBAT</type>`, [[source-blueprints]].
- Power **2**, `speed` 15 (`<!-- was 20-->`), `dodge` 0.
- Fires the `DRONE_LASER` internal weapon blueprint.
- Cost **50** scrap, `bp` 3, `rarity` 2.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `COMBAT_1` by name.

## Blue Options It Unlocks
- [[event-auto-ship-near-radar-station]] — `AUTO_DEFENSE_RADAR` via `req="COMBAT_DRONE_LIST"` — the list is `COMBAT_1`, `COMBAT_2`, `COMBAT_BEAM`, `COMBAT_BEAM_2` or `DRONE_FIREBEAM` ([[source-autoblueprints]]), so any combat drone satisfies it

## Strategy Notes
- Its one blue option is a category gate that five different drones satisfy — the Mark I is
  simply the cheapest and most common member.
- Combat drones fire on their own schedule and are the only offence that keeps working while
  [[item-weapons]] is depowered or hacked.

## Related
- [[item-combat-beam-drone]] — another member of `COMBAT_DRONE_LIST`
- [[item-defense-drone]] — the defensive counterpart
- [[item-drone-control]] / [[item-drone-parts]]

## Open Questions
- [ ] Whether the `COMBAT_DRONE_LIST` gate checks owned schematics or deployed drones.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
