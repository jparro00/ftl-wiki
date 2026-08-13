---
id: item-defense-drone
type: item
item_kind: drone
rarity: 1
unlocks_blue: [[[event-asteroid-belt-distress]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [drone, defence]
---

# Defense Drone Mark I

## Summary
The `DEFENSE_1` drone — *"Shoots down incoming missiles, asteroids, and flak debris."*
([[source-text-blueprints]]). Event pages link it as both `item-defense-drone` and
[[item-defense-drone-mark-i]].

## Stats
- Blueprint `DEFENSE_1` (`<droneBlueprint>`), `<type>DEFENSE</type>` `<level>1</level>`, [[source-blueprints]].
- Power **2**, `speed` 5, `cooldown` 1000 ms between intercepts.
- Fires the `DRONE_LASER` internal weapon blueprint.
- Cost **50** scrap, `bp` 2, `rarity` 1.
- The Mark II (`DEFENSE_2`) is a separate blueprint that also shoots down lasers.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `DEFENSE_1` by name.

## Blue Options It Unlocks
- [[event-asteroid-belt-distress]] — `CIVILIAN_ASTEROIDS_BEACON_2` via `req="DRONES_DEFENSE_LIST"` — the list is `DEFENSE_1` **or** `DEFENSE_2` ([[source-autoblueprints]]), so either mark satisfies it

## Strategy Notes
- The gate is on the *list*, not the blueprint, so a Defense Drone Mark II works equally
  well — one of only six list-based `req` values in the game.
- Shooting down asteroids is the reason its single blue option is an asteroid-belt beacon.
- It is also the counter to [[item-flak-artillery]] and to any missile weapon.

## Related
- [[item-defense-drone-mark-i]] — alias page under the in-game title
- [[item-flak-artillery]] / [[item-breach-missiles]] — what it shoots down
- [[item-drone-control]] / [[item-drone-parts]]

## Open Questions
- [ ] Whether `DEFENSE_2` (Mark II) is stocked in stores at a different rarity — it has its own blueprint but is not linked from any event page yet.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
