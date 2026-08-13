---
id: item-repair-drone
type: item
item_kind: drone
rarity: 1
unlocks_blue: [[[event-asteroid-belt-distress]], [[event-fire-on-research-station]], [[event-mantis-ships-battle-for-rock-freighter]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [drone, repair]
---

# System Repair Drone

## Summary
The `REPAIR` drone — *"Will seek out damaged systems and repair them automatically."*
([[source-text-blueprints]]). A shipboard drone that walks your own hull, not a combat drone.
Distinct from the [[item-hull-repair-drone]] (`SHIP_REPAIR`), which repairs hull instead.

## Stats
- Blueprint `REPAIR` (`<droneBlueprint>`), `<type>REPAIR</type>`, [[source-blueprints]].
- Power **1**, cost **30** scrap — the cheapest drone in the file on both counts.
  `bp` 2, `rarity` 1.
- No `cooldown`, `speed` or `weaponBlueprint` entries: it has no attack.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `REPAIR` by name.

## Blue Options It Unlocks
- [[event-asteroid-belt-distress]] — `CIVILIAN_ASTEROIDS_BEACON_2`
- [[event-fire-on-research-station]] — `DISTRESS_STATION_FIRE` — send the drone into the fire instead of your crew
- [[event-mantis-ships-battle-for-rock-freighter]] — `ROCK_MANTIS_FREIGHTER` — the same beacon also accepts [[item-hull-repair-drone]] on a separate choice

## Strategy Notes
- At 1 power and 30 scrap it is the cheapest way to hold a drone-gated blue option, which
  matters because its three gates are all "send something expendable in" beacons.
- The `req` is on the specific blueprint `REPAIR`, not a list — a [[item-hull-repair-drone]]
  will **not** satisfy `req="REPAIR"` and vice versa. [[event-mantis-ships-battle-for-rock-freighter]]
  is the one beacon that offers both as separate choices.

## Related
- [[item-hull-repair-drone]] — the other repair drone, a different `req`
- [[item-drone-control]] / [[item-drone-parts]] — the prerequisites
- [[item-drone-reactor-booster]] — speeds up shipboard drones

## Open Questions
- [ ] Whether a System Repair Drone puts out fires, or only repairs systems — the description says only the latter.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
