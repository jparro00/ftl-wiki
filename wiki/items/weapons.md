---
id: item-weapons
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-pirate-ship-attacking-civilian-distress]], [[event-merchant-deliver]], [[event-pirate-smuggler]], [[event-rock-nursery]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [system]
---

# Weapon Control

## Summary
The `weapons` system, displayed in game as **Weapon Control** — *"Powers all of the ship's
weapons. Upgrading lets you power more weapons."* ([[source-text-blueprints]]). Also the page
for the `req="weapons"` blue-option gate, which every instance of sets at `lvl="6"`.

## Stats
- Blueprint `weapons` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 4, `maxPower` 8.
- Purchase cost: **20** scrap (nominal — every ship starts with it).
- Upgrade costs, levels 2→9: 40 (`<!--CHANGED was 60-->`), 25, 35, 50, 75, 90, 100, 120 scrap. Level 9 is labelled *"Imaginary"*.
- `rarity` 1.

## How To Get It
- Present on every ship; upgraded at stores.
- No event in `raw/gamedata/` grants Weapon Control levels directly.

## Blue Options It Unlocks
- [[event-pirate-ship-attacking-civilian-distress]] — `PIRATE_CIVILIAN_BEACON`, `lvl="6"`
- [[event-merchant-deliver]] — `MERCHANT_DELIVER_LIST`, `lvl="6"`
- [[event-pirate-smuggler]] — `NEBULA_PIRATE_SMUGGLE`, `lvl="6"`
- [[event-rock-nursery]] — `ROCK_NURSERY`, `lvl="6"`

## Strategy Notes
- All four `req="weapons"` gates in the game demand `lvl="6"`, and nothing lower ever
  appears. It is the most uniform gate in the data: you either have six bars of weapons or
  none of these choices exist for you.
- Six bars costs 40+25+35+50+75 = 225 scrap of upgrades above the starting level 4 on a
  typical hull, so these are late-run options by construction.

## Related
- [[item-weapon-control]] — alias page for the same system
- [[item-reactor]] — six bars of weapons has to be powered from somewhere
- [[item-missile-weapon]] / [[item-ion-weapons]] / [[item-beam-weapons]] — the weapon-*category* gates, which are separate `req` values

## Open Questions
- [ ] Whether any store event sells Weapon Control levels the way `TRADER_UPGRADES_LIST` sells subsystem levels.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
