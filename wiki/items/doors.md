---
id: item-doors
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-refueling-platform-garbled-broadcast]], [[event-refueling-platform]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 6
tags: [system, subsystem, oxygen, venting]
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

## The venting model

The numbers behind "its case is entirely in play", from
[[source-xftl-oxygen-mechanics]] via [[concept-oxygen-and-suffocation]]:

- **Each open airlock door vents 16% O₂/sec** — twice a hull breach's 8%.
- Loss reaches connected rooms scaled by **`0.75^distance`**, so airlocks anywhere on the ship
  contribute to venting anywhere else.
- Air *redistribution* between open-door rooms is **distance-independent** (8% of the gap to the
  chunk average, per second).

That asymmetry — loss decays with distance, spread does not — is the whole of door tactics:

| Goal | Do this |
|---|---|
| **Vent a room** (fire, boarders) | Open **every** airlock on the ship, not just nearby ones. On the Kestrel, venting the teleporter through two airlocks takes **3.5s vs 5.2s** through one. |
| **Save a breached room** | Close the doors *around* it; leave one long snaking path of open rooms feeding it from far away. Opening nearby doors loses more air than it delivers. |

## Strategy Notes
- The Door System is one of the weakest blue-option keys in the game: two gates, both
  `lvl="2"`, both on refuelling-platform beacons, and both AE-era content.
- Its case is entirely in play — venting fires and slowing boarders — not at beacons.
- **Venting kills less than it evicts.** Boarders path away from rooms below 10% O₂, while crew
  only start taking damage at 5% ([[source-fandom-oxygen]]) — so venting reliably *moves*
  boarders and only kills the ones that cannot leave.

## Related
- [[item-door-system]] — alias page for the same subsystem
- [[item-hacking]] — a hack locks the target system's doors ([[source-text-blueprints]])
- [[item-oxygen-system]] — the other half of venting
- [[concept-oxygen-and-suffocation]] — the full rate table and the propagation rule
- [[concept-solar-flares]] — venting as the general fire answer

## Open Questions
- [ ] Whether the two `lvl="2"` door gates differ in payout.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-xftl-oxygen-mechanics]] (per raw/modding/2026-08-14-xftl-oxygen-mechanics.txt)
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
