---
id: item-combat-beam-drone
type: item
item_kind: drone
rarity: 3
unlocks_blue: [[[event-crushed-pirate]], [[event-rock-live-mine]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [drone, combat, beam]
---

# Anti-Ship Beam Drone I

## Summary
The `COMBAT_BEAM` drone — *"Combat drone that repeatedly attacks with a small beam weapon."*
([[source-text-blueprints]]). Event pages also link it as [[item-beam-drone]].

## Stats
- Blueprint `COMBAT_BEAM` (`<droneBlueprint>`), `<type>COMBAT</type>`, [[source-blueprints]].
- Power **2**, `speed` 15, `dodge` 0.
- Fires the `DRONE_BEAM` internal weapon blueprint.
- Cost **50** scrap, `bp` 3, `rarity` 3.
- The AE `COMBAT_BEAM_2` (Anti-Ship Beam Drone II) in [[source-dlcblueprints]] is the larger-beam variant.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `COMBAT_BEAM` by name.

## Blue Options It Unlocks
- [[event-crushed-pirate]] — `DISTRESS_TRAPPED_MINER` via `req="COMBAT_BEAM_DRONE_LIST"` — the list is `COMBAT_BEAM` or `COMBAT_BEAM_2` ([[source-autoblueprints]])
- [[event-rock-live-mine]] — `ROCK_STARSHIP_MINE` via `req="COMBAT_BEAM_DRONE_LIST"`

## Strategy Notes
- Both gates are precision-cutting problems — free a trapped miner, defuse a mine — where
  the blue option is "we have a beam we can aim remotely".
- [[event-crushed-pirate]] accepts either this drone (`COMBAT_BEAM_DRONE_LIST`) or a beam
  weapon (`WEAPONS_BEAM_DAMAGE`) on two separate choices, so the two lists overlap in
  purpose but never in membership.

## Related
- [[item-beam-drone]] — alias page for the same drone
- [[item-beam-weapons]] — the weapon-slot list that gates the same beacon separately
- [[item-combat-drone-mark-i]] — the laser equivalent

## Open Questions
- [ ] Whether `COMBAT_BEAM_2` is available in vanilla — it is defined only in [[source-dlcblueprints]] but the list that names it lives in the base [[source-autoblueprints]].

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
