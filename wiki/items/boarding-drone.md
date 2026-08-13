---
id: item-boarding-drone
type: item
item_kind: drone
rarity: 4
unlocks_blue: [[[event-giant-alien-spiders]], [[event-zoltan-odd-moon]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [drone, boarding]
---

# Boarding Drone

## Summary
The `BOARDER` drone — *"Breaches through the enemy hull and wreaks havoc. Awesome."*
([[source-text-blueprints]]; the enthusiasm is the developers').

## Stats
- Blueprint `BOARDER` (`<droneBlueprint>`), `<type>BOARDER</type>`, [[source-blueprints]].
- Power **3** — only `COMBAT_2` (Combat Drone Mark II, power 4) costs more to run. `speed` 18.
- Cost **70** scrap, `rarity` **4** (`<!--was 5-->`).

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `BOARDER` by name.

## Blue Options It Unlocks
- [[event-giant-alien-spiders]] — `DISTRESS_INFESTATION`
- [[event-zoltan-odd-moon]] — `ZOLTAN_ODD_MOON`

## Strategy Notes
- The drone-bay substitute for a [[item-teleporter]]: it puts a body on the enemy ship
  without risking crew, and both of its blue options are exactly that trade.
- 3 power plus a drone part per launch makes it the costliest way to board; the AE
  `BOARDER_ION` (Ion Intruder Drone, [[source-dlcblueprints]]) is a variant that satisfies
  no `req` at all.

## Related
- [[item-teleporter]] — the crewed alternative, with eleven blue options to this drone's two
- [[item-anti-personnel-drone]] — the defensive counterpart
- [[item-drone-control]] / [[item-drone-parts]]

## Open Questions
- [ ] Whether a Boarding Drone counts as "crew aboard the enemy ship" for events that check for it.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
