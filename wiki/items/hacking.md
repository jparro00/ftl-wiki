---
id: item-hacking
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-rebel-pds]], [[event-rebel-auto-pds]], [[event-boarders-humans-jammed-sensors]], [[event-the-engi-virus]], [[event-auto-ship-near-storage-station-in-nebula]], [[event-pirate-engine-hacker]], [[event-auto-ship-carrying-shield-virus]], [[event-auto-ship-near-radar-station]], [[event-slug-hacker-choice]], [[event-slug-hacker-doors]], [[event-slug-hacker-oxygen]], [[event-slug-hacker-medical]], [[event-slug-distress-piloting]], [[event-pirate-ship-selling-drones]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 12
tags: [system, advanced-edition]
---

# Hacking

## Summary
The `hacking` system, added in Advanced Edition. *"Targets a single system, locking its doors
and granting the ability to temporarily disable or disrupt it. Requires drone part to launch."*
([[source-text-blueprints]]).

## Stats
- Blueprint `hacking` (`<systemBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **80** scrap. Upgrade costs: level 2 = 35, level 3 = 60.
- `rarity` 1. Launching a hack consumes a [[item-drone-parts]] ([[source-text-blueprints]]).

## How To Get It
- **Stores** — 80 scrap ([[source-dlcblueprints]]).
- Starting system on the AE hacker layouts (see the `shipBlueprint` entries in [[source-dlcblueprintsoverwrite]]).
- No event in `raw/gamedata/` grants the Hacking system as a reward.

## Blue Options It Unlocks
- [[event-rebel-pds]] — `REBEL_PDS`, separate gates at `lvl="1"` and `lvl="3"`
- [[event-rebel-auto-pds]] — `REBEL_AUTO_PDS`, separate gates at `lvl="1"` and `lvl="3"`
- [[event-boarders-humans-jammed-sensors]] — `BOARDERS_HACKING`, tagged `<!--DLC - added -->` inside the base file
- [[event-the-engi-virus]] — `ENGI_VIRUS`, gates at `lvl="1"`, `2` and `3`
- [[event-auto-ship-near-storage-station-in-nebula]] — `NEBULA_AUTO_DEFENSE_ITEM`, `lvl="1"` and `lvl="2"`, tagged `<!--DLC-->`
- [[event-pirate-engine-hacker]] — `PIRATE_NO_ESCAPE`
- [[event-auto-ship-carrying-shield-virus]] — `AUTO_HACKER`
- [[event-auto-ship-near-radar-station]] — the `REBEL_AUTO_RADAR` ship block in `events_ships.xml`
- [[event-slug-hacker-choice]] — `NEBULA_SLUG_CHOOSE_DEATH`
- [[event-slug-hacker-doors]] — `NEBULA_SLUG_DOORS`
- [[event-slug-hacker-oxygen]] — `NEBULA_SLUG_OXYGEN`
- [[event-slug-hacker-medical]] — `NEBULA_SLUG_MEDBAY`
- [[event-slug-distress-piloting]] — `SLUG_DISTRESS_PILOTING`
- [[event-pirate-ship-selling-drones]] — the `CONTACT_PIRATE_SALESMAN` hail step

## Strategy Notes
- Fourteen events carry a `req="hacking"` choice, second only to [[item-sensors]]. Four of
  them (`REBEL_PDS`, `REBEL_AUTO_PDS`, `ENGI_VIRUS`, `NEBULA_AUTO_DEFENSE_ITEM`) ladder the
  payoff across system levels, so upgrading has beacon value on top of combat value.
- The whole Slug-hacker cluster (`NEBULA_SLUG_DOORS` / `_MEDBAY` / `_OXYGEN` /
  `_CHOOSE_DEATH`) is gated on Hacking, concentrating its event value in
  [[sector-slug-controlled-nebula]] and [[sector-slug-home-nebula]].

## Related
- [[item-drone-parts]] — consumed on every hack launch
- [[item-sensors]] — the system that most often opens the same beacons
- [[item-artillery-beam]] / [[item-flak-artillery]] — artillery is not affected by a Weapons hack ([[event-slug-hacker-choice]])

## Open Questions
- [ ] Whether any vanilla-only alternative choice exists at the beacons whose hacking gate is tagged `<!--DLC-->` inside base event files.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
