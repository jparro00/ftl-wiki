---
id: item-doors
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-refueling-platform-garbled-broadcast]], [[event-refueling-platform]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [system, subsystem]
---

# Door System

## Summary
The `doors` subsystem, displayed as **Door System** — *"Allows remote opening and closing of
doors. Upgrades to Blast Doors that impede fire spread and intruder movement."*
([[source-text-blueprints]]).

## Stats
- Blueprint `doors` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **60** scrap. Upgrade costs: level 2 = 35 scrap, level 3 = 50 scrap.
- `rarity` 1.

## How To Get It
- **Stores** — 60 scrap ([[source-blueprints]]).
- `TRADER_UPGRADES_LIST` sells a Door System level-up — [[event-trade-scrap-for-upgrades]] ([[source-newevents]]).
- Present on most player layouts.

## Blue Options It Unlocks
- [[event-refueling-platform-garbled-broadcast]] — `LANIUS_FUELING_STATION`, `lvl="2"` — the only genuine `req="doors"` blue option in the game
- [[event-refueling-platform]] — `FUELING_STATION_PIRATE_LIST`, `lvl="2"`
- `TRADER_UPGRADES_LIST` also uses `req="doors"`, but with `max_lvl` and `blue="false"` —
  an inverse gate that hides the "buy an upgrade" choice once the Door System is already at
  that level. **Not** a blue option. ([[event-trade-scrap-for-upgrades]], [[source-newevents]])

## Strategy Notes
- The Door System is one of the weakest blue-option keys in the game: two gates, both
  `lvl="2"`, both on refuelling-platform beacons, and both AE-era content.
- Its case is entirely in play — venting fires and slowing boarders — not at beacons.

## Related
- [[item-door-system]] — alias page for the same subsystem
- [[item-hacking]] — a hack locks the target system's doors ([[source-text-blueprints]])
- [[item-oxygen-system]] — the other half of venting

## Open Questions
- [ ] Whether the two `lvl="2"` door gates differ in payout.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
