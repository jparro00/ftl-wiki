---
id: item-hull-repair-drone
type: item
item_kind: drone
rarity: 4
unlocks_blue: [[[event-lanius-ship-absorbing-jump-beacon]], [[event-no-fuel-engi-ship-repair]], [[event-mantis-ships-battle-for-rock-freighter]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [drone, repair]
---

# Hull Repair Drone

## Summary
The `SHIP_REPAIR` drone, titled **Hull Repair** in game — *"Automatically repairs 3-5 damage to
your hull per drone part."* ([[source-text-blueprints]]). Distinct from the
[[item-repair-drone]] (`REPAIR`), which repairs systems.

## Stats
- Blueprint `SHIP_REPAIR` (`<droneBlueprint>`), `<type>SHIP_REPAIR</type>`, [[source-blueprints]].
- Power **2**, `speed` 20. Cost **85** scrap (`<!--was 100-->`), `bp` 5, `rarity` **4**.
- Repairs **3–5 hull per drone part** ([[source-text-blueprints]]) — the only place in the
  blueprint data where a drone's effect is given as a numeric range.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `SHIP_REPAIR` by name.

## Blue Options It Unlocks
- [[event-lanius-ship-absorbing-jump-beacon]] — `LANIUS_BEACON_EATER`
- [[event-no-fuel-engi-ship-repair]] — `FUEL_OFF_ENGI_DUBIOUS` — spend a drone part instead of trusting the Engi
- [[event-mantis-ships-battle-for-rock-freighter]] — `ROCK_MANTIS_FREIGHTER`

## Strategy Notes
- 3–5 hull for one 8-scrap [[item-drone-parts]] is the cheapest hull in the game by a wide
  margin; the 85-scrap entry price is what you pay for the privilege.
- All three blue options are "repair yourself rather than take the deal" beacons — the drone
  is the self-sufficiency answer where the alternative is trusting a stranger.
- `rarity` 4 is high; do not plan a run around finding one.

## Related
- [[item-repair-drone]] — systems rather than hull, a different `req`
- [[item-drone-parts]] — the running cost
- [[item-scrap-recovery-arm]] — the other "free value from routine play" purchase

## Open Questions
- [ ] Whether the 3–5 range is per part or per deployment.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
