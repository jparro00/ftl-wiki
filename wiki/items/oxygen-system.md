---
id: item-oxygen-system
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-slug-hacker-oxygen]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [system, subsystem]
---

# Oxygen

## Summary
The `oxygen` subsystem — *"Refills the oxygen in the ship. Upgrading increases the rate of
refill."* ([[source-text-blueprints]]).

## Stats
- Blueprint `oxygen` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **0** scrap — the only system in the file priced at zero.
- Upgrade costs: level 2 = 25, level 3 = 50, plus a 75-scrap entry the file annotates as an *"imaginary level 4"*.
- `rarity` 1.

## How To Get It
- Present on every ship. Upgrades bought at stores.
- `TRADER_UPGRADES_LIST` and `HIGH_SCAN_TERRAFORMING` both grant `<upgrade system="oxygen" amount="1"/>` — [[event-trade-scrap-for-upgrades]] and [[event-terraforming-scan]] ([[source-newevents]]).

## Blue Options It Unlocks
- [[event-slug-hacker-oxygen]] — `NEBULA_SLUG_OXYGEN`, `lvl="2"` — the only genuine `req="oxygen"` blue option in the game
- `TRADER_UPGRADES_LIST` also uses `req="oxygen"`, but with `max_lvl` and `blue="false"` —
  an inverse gate hiding the "buy an upgrade" choice once Oxygen is already at that level.
  **Not** a blue option. ([[event-trade-scrap-for-upgrades]], [[source-newevents]])

## Strategy Notes
- One blue option in the entire game. Oxygen upgrades are bought for survivability, never
  for event access.
- [[item-emergency-respirators]] and [[item-lanius-crew]] both interact with low oxygen but
  satisfy different `req` values.

## Related
- [[item-emergency-respirators]] — halves suffocation damage
- [[item-lanius-crew]] — drains oxygen from rooms, immune to suffocation
- [[item-doors]] — venting is the usual reason oxygen matters

## Open Questions
- [ ] What the "imaginary level 4" upgrade entry is for.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
