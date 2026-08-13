---
id: item-anti-personnel-drone
type: item
item_kind: drone
rarity: 2
unlocks_blue: [[[event-giant-alien-spiders]], [[event-research-station-with-no-response]], [[event-merchant-deliver]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [drone, anti-crew]
---

# Anti-Personnel Drone

## Summary
The `BATTLE` drone — *"Will seek out and attempt to destroy any intruders on-board your ship."*
([[source-text-blueprints]]).

## Stats
- Blueprint `BATTLE` (`<droneBlueprint>`), `<type>BATTLE</type>`, [[source-blueprints]].
- Power **2**. Cost **35** scrap (`<!--was 60-->`), `bp` 3, `rarity` 2.
- No `weaponBlueprint`: like the repair drones it is a walking shipboard unit.

## How To Get It
- **Stores**, and as `autoReward` `drone` payouts. Generic pools (`RANDOM`, `DLC_DRONES`) name no specific blueprint, so most drone-giving events cannot be attributed to one schematic.
- Requires [[item-drone-control]] powered, and one [[item-drone-parts]] per deployment.
- No event in `raw/gamedata/` awards `BATTLE` by name.

## Blue Options It Unlocks
- [[event-giant-alien-spiders]] — `DISTRESS_INFESTATION` — send the drone down instead of crew
- [[event-research-station-with-no-response]] — `STATION_SICK`
- [[event-merchant-deliver]] — `MERCHANT_DELIVER_LIST`

## Strategy Notes
- Its blue options are the "do not send a person" answers: infestations and contaminated
  stations. It shares [[event-giant-alien-spiders]] with [[item-anti-bio-beam]] and
  [[item-boarding-drone]].
- At 35 scrap it is the joint second-cheapest drone in the file, behind
  [[item-repair-drone]] at 30 and level with the AE `ANTI_DRONE`.

## Related
- [[item-boarding-drone]] — offence rather than defence, shares a choice list
- [[item-anti-bio-beam]] — the weapon answer to the same beacons
- [[item-drone-control]] / [[item-drone-parts]]

## Open Questions
- [ ] Whether the drone can be deployed against boarders that are already aboard mid-fight, or only pre-emptively — the description implies the former.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
