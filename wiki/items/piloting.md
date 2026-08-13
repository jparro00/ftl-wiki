---
id: item-piloting
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-lanius-ship-in-rich-debris-field]], [[event-lanius-powered-down-ship]], [[event-boarders-asteroid-ghost]], [[event-plasma-storm-incapacitated-ships]], [[event-slug-distress-piloting]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [system, subsystem]
---

# Piloting

## Summary
The `pilot` subsystem — *"Allows the ship to make FTL jumps and dodge when piloted. Upgrading
adds auto-pilot that allows some evasion even without a pilot."* ([[source-text-blueprints]]).

## Stats
- Blueprint `pilot` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **1** scrap (nominal — every ship starts with it).
- Upgrade costs: level 2 = 20 scrap, level 3 = 50 scrap.
- `rarity` 1.

## How To Get It
- Present on every ship; upgraded at stores.
- `TRADER_UPGRADES_LIST` sells a Piloting level-up — [[event-trade-scrap-for-upgrades]] ([[source-newevents]]).

## Blue Options It Unlocks
- [[event-lanius-ship-in-rich-debris-field]] — `LANIUS_HARVESTER`, `lvl="2"` and `lvl="3"`
- [[event-lanius-powered-down-ship]] — the `LANIUS_DORMANT_INVESTIGATE` sub-event, `lvl="2"`
- [[event-boarders-asteroid-ghost]] — `BOARDERS_ASTEROID_GHOST`, `lvl="2"`
- [[event-plasma-storm-incapacitated-ships]] — `STORM_ITEMS`, `lvl="2"`
- [[event-slug-distress-piloting]] — `SLUG_DISTRESS_PILOTING`, `lvl="2"`
- `TRADER_UPGRADES_LIST` also uses `req="pilot"`, but with `max_lvl` and `blue="false"` —
  an inverse gate that hides the "buy an upgrade" choice once Piloting is already at that
  level. **Not** a blue option. ([[event-trade-scrap-for-upgrades]], [[source-newevents]])

## Strategy Notes
- Every genuine Piloting gate wants `lvl="2"`; only `LANIUS_HARVESTER` goes to 3. At 20
  scrap the first upgrade is the cheapest blue-option key in the game.
- Three of the five gates are debris/derelict manoeuvring beacons, two of them in the
  Lanius (AE) event set.

## Related
- [[item-engines]] — dodge is the product of both
- [[item-sensors]] / [[item-doors]] / [[item-oxygen-system]] — the other cheap subsystems `TRADER_UPGRADES_LIST` sells

## Open Questions
- [ ] Whether Piloting level 3's auto-pilot has any event effect, or only combat effect.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
