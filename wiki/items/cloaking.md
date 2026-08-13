---
id: item-cloaking
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-malfunctioning-defense-system]], [[event-no-fuel-prepare-to-dock]], [[event-mantis-fight-choice]], [[event-rebel-fight-choice-in-nebula]], [[event-auto-ship-near-storage-station-in-nebula]], [[event-auto-ship-fight-in-plasma-storm]], [[event-auto-ship-near-storage-station]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [system, evasion]
---

# Cloaking

## Summary
The `cloaking` system — *"Cloaks the ship, adding 60 to your evasion and preventing the enemy
ship from locking on with their weapons."* ([[source-text-blueprints]]).

## Stats
- Blueprint `cloaking` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **150** scrap — tied with Artillery for the most expensive system in the file.
- Upgrade costs: level 2 = 30 scrap, level 3 = 50 scrap.
- `rarity` 1. Carries `<locked>1</locked>`.

## How To Get It
- **Stores** — 150 scrap ([[source-blueprints]]).
- Starting system on the Stealth Cruiser layouts.
- No event in `raw/gamedata/` grants the Cloaking system as a reward.

## Blue Options It Unlocks
- [[event-malfunctioning-defense-system]] — `DISTRESS_SATELLITE_DEFENSE` — three separate choices at `lvl="1"`, `2` and `3`, the ladder tagged `<!--DLC!-->`
- [[event-no-fuel-prepare-to-dock]] — the `FUEL_APPROACH_SCAN_LIST` sub-list
- [[event-mantis-fight-choice]] — `MANTIS_FIGHT_CHOICE`, `lvl="1"`
- [[event-rebel-fight-choice-in-nebula]] — `NEBULA_REBEL_UNDETECTED`
- [[event-auto-ship-near-storage-station-in-nebula]] — `NEBULA_AUTO_DEFENSE_ITEM`, `lvl="1"` and `lvl="2"`
- [[event-auto-ship-fight-in-plasma-storm]] — `STORM_AUTO`
- [[event-auto-ship-near-storage-station]] — `AUTO_DEFENSE_ITEM`

## Strategy Notes
- Cloaking's gates cluster on *avoidance* beacons — automated defence platforms and Rebel
  patrols — where the blue option is "slip past without a fight". Four of the seven are
  auto-ship encounters.
- `DISTRESS_SATELLITE_DEFENSE` is the only event that ladders Cloaking across three `lvl`
  gates, and the whole ladder is marked `<!--DLC!-->`: in vanilla those choices are absent.
  ([[source-events-xml]])
- At 150 scrap it is never an early buy on event value alone.

## Related
- [[item-engines]] — the other evasion lever
- [[item-sensors]] — the other common "avoid the fight" gate

## Open Questions
- [ ] What `<locked>1</locked>` controls.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
