---
id: item-engines
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-boarders-asteroid-ghost]], [[event-crystalline-cache]], [[event-mantis-gamble]], [[event-rebel-fight-choice-in-nebula]], [[event-auto-ship-fight-in-plasma-storm]], [[event-slaver-hostile]], [[event-rock-live-mine]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [system, evasion]
---

# Engines

## Summary
The `engines` system — *"Powers the FTL drive and allows the ship to dodge. Upgrading improves
dodge chance and the rate that your FTL drive charges."* ([[source-text-blueprints]]).

## Stats
- Blueprint `engines` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 2, `maxPower` 8.
- Purchase cost: **1** scrap — nominal; every ship starts with the system.
- Upgrade costs, levels 2→9: 10, 15, 30, 40, 60, 80, 120, 150 scrap. The file labels level 9 *"Imaginary"*.
- `rarity` 1.

## How To Get It
- Present on every ship from the start; upgraded at stores.
- `CONFUSED_MANTIS_HOME` grants `<upgrade system="engines" amount="1"/>` — [[event-confused-mantis]] ([[source-newevents]]).

## Blue Options It Unlocks
- [[event-boarders-asteroid-ghost]] — `BOARDERS_ASTEROID_GHOST`, `lvl="5"`
- [[event-crystalline-cache]] — `CRYSTAL_CACHE_LIST`, `lvl="7"` — the highest system-level gate found anywhere in the event data
- [[event-mantis-gamble]] — `MANTIS_GAMBLE_BLUE` and `MANTIS_GAMBLE_RED`, both `lvl="4"`
- [[event-rebel-fight-choice-in-nebula]] — `NEBULA_REBEL_UNDETECTED_LIST`, `lvl="4"`
- [[event-auto-ship-fight-in-plasma-storm]] — `STORM_AUTO`, `lvl="3"` and `lvl="6"`
- [[event-slaver-hostile]] — `PIRATE_SLAVER`, `lvl="6"`
- [[event-rock-live-mine]] — `ROCK_STARSHIP_MINE`, `lvl="5"`

## Strategy Notes
- Every engines gate in the data is a high one: the lowest is `lvl="3"`, the median is 5.
  Engines is the one system whose blue options only start paying out well past the level
  you would buy for dodge alone.
- `CRYSTAL_CACHE_LIST` at `lvl="7"` is the single highest system-level requirement of any
  choice in `raw/gamedata/`.

## Related
- [[item-cloaking]] — the other evasion lever
- [[item-piloting]] — dodge needs a manned helm
- [[item-reactor]] — what has to grow to power 8 bars of engines

## Open Questions
- [ ] Whether any event grants engine upgrades other than `CONFUSED_MANTIS_HOME`.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
