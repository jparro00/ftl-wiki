---
id: item-sensors
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-refueling-platform-garbled-broadcast]], [[event-ghost-ship]], [[event-engi-monster]], [[event-engi-research-station]], [[event-no-fuel-prepare-to-dock]], [[event-legendary-thief-kazaaakplethkilik]], [[event-rebel-fight-chance-in-nebula]], [[event-destroyed-cargo-ship]], [[event-auto-ship-near-sensor-station]], [[event-deactivated-auto-ship]], [[event-rock-atheists]], [[event-slug-unlock-1]], [[event-battlefield-wreckage]], [[event-terraforming-scan]], [[event-rebel-fight-chance]], [[event-tutorial-enemy]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 13
tags: [system, subsystem, information]
---

# Sensors

## Summary
The `sensors` subsystem — *"Reveals the interior of your ship and gives information about enemy
ships."* ([[source-text-blueprints]]). In the event data it is the most frequently required
system in the game: 25 `req="sensors"` choices spread across 17 named events and lists.

## Stats
- Blueprint `sensors` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **40** scrap. Upgrade costs: level 2 = 25 scrap, level 3 = 40 scrap.
- `rarity` 1.

## How To Get It
- **Stores** — 40 scrap, upgrades 25 and 40 ([[source-blueprints]]).
- Present on most player layouts; the Slug cruisers deliberately lack it ([[source-text-blueprints]], ship description).
- `TRADER_UPGRADES_LIST` sells a Sensors level-up — [[event-trade-scrap-for-upgrades]] ([[source-newevents]]).

## Blue Options It Unlocks
- [[event-refueling-platform-garbled-broadcast]] — `LANIUS_FUELING_STATION_LIST`, `lvl="2"` and `lvl="3"`
- [[event-ghost-ship]] — `GHOST_DOCK`, `lvl="3"`
- [[event-engi-monster]] — `ENGI_MONSTER`, `lvl="3"`
- [[event-engi-research-station]] — `DISTRESS_ENGI_REACTOR`, `lvl="2"`
- [[event-no-fuel-prepare-to-dock]] — `FUEL_APPROACH`, `lvl="3"`
- [[event-legendary-thief-kazaaakplethkilik]] — `MANTIS_NAMED_THIEF_DEFEAT`, `lvl="3"`
- [[event-rebel-fight-chance-in-nebula]] — `NEBULA_REBEL_CHASE`, `lvl="3"`
- [[event-destroyed-cargo-ship]] — `FLOATING_CARGO`, `lvl="2"`
- [[event-auto-ship-near-sensor-station]] — `AUTO_DEFENSE_MAP`, `lvl="3"`
- [[event-deactivated-auto-ship]] — `BROKEN_REBEL_DRONE`, `lvl="3"`
- [[event-rock-atheists]] — `ROCK_ATHIEST`, `lvl="2"`
- [[event-slug-unlock-1]] — the `SLUG_UNLOCK_2` sub-event, `lvl="2"`
- [[event-battlefield-wreckage]] — `WRECKAGE_EVENT`, `lvl="2"` and `lvl="3"`
- [[event-terraforming-scan]] — `TERRAFORMING_SCAN`, `lvl="2"`
- [[event-rebel-fight-chance]] — `ROGUE_REBEL`, `lvl="2"` and `lvl="3"`
- [[event-tutorial-enemy]] — `TUTORIAL_ENEMY`, `lvl="1"` — the tutorial's demonstration gate
- `HIDDEN_FEDERATION_BASE_LIST` — `lvl="2"` and `lvl="3"` gates, tagged `<!--DLC!-->`.
  The list has no page of its own; its members are written up on
  [[event-encrypted-federation-signal]] and [[event-asteroid-belt-distress]].
- `TRADER_UPGRADES_LIST` also uses `req="sensors"`, but with `max_lvl` and `blue="false"` —
  an *inverse* gate that hides the "buy an upgrade" choice once Sensors is already at that
  level. **Not** a blue option. ([[event-trade-scrap-for-upgrades]], [[source-newevents]])

## Strategy Notes
- Almost every Sensors gate wants level 2 or 3. Buying Sensors and leaving it at level 1
  unlocks essentially nothing — the opposite of [[item-teleporter]], whose gates mostly
  fire at level 1. The 25-scrap first upgrade is the one that matters.
- [[item-long-ranged-scanners]] satisfies a *different* `req` (`ADV_SCANNERS`), but six
  events carry both gates on the same choice list, so the augment substitutes for the
  subsystem at those beacons.
- [[item-slug-crew]] and [[item-lifeform-scanner]] cover the "see lifeforms without
  sensors" case in play, but they do **not** satisfy `req="sensors"` in events.

## Related
- [[item-long-ranged-scanners]] — the augment that overlaps six of the same beacons
- [[item-lifeform-scanner]] / [[item-slug-crew]] — in-play substitutes, not event substitutes

## Open Questions
- [ ] Whether the vanilla build drops the `HIDDEN_FEDERATION_BASE_LIST` sensors ladder entirely (its tag is `<!--DLC!-->`) or replaces it.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
