---
id: item-lifeform-scanner
type: item
item_kind: augment
rarity: 3
unlocks_blue: [[[event-research-station-with-no-response]], [[event-no-fuel-drifting-debris]], [[event-rebel-fight-chance-in-nebula]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [augment, information, advanced-edition]
---

# Lifeform Scanner

## Summary
The `LIFE_SCANNER` augment, added in Advanced Edition — *"Detects the location of any life
forms, even when sensors don't function."* ([[source-text-blueprints]]).

## Stats
- Blueprint `LIFE_SCANNER` (`<augBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Cost: **40** scrap. `bp` 8, `rarity` 3. `<stackable>false</stackable>`, `<value>0.0</value>`.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `LIFE_SCANNER` by name.

## Blue Options It Unlocks
- [[event-research-station-with-no-response]] — `STATION_SICK`, tagged `<!--DLC-->` in the base file
- [[event-no-fuel-drifting-debris]] — `FUEL_OFF_ROCK_WRECK`, tagged `<!--DLC-->`
- [[event-rebel-fight-chance-in-nebula]] — `NEBULA_REBEL_CHASE`, tagged `<!--DLC-->`

## Strategy Notes
- All three gates are `<!--DLC-->` additions inside *base* event files: the beacons exist in
  vanilla, the Lifeform Scanner choice does not. Version differences here are real, not
  incidental. ([[source-events-xml]], [[source-events-fuel]], [[source-events-nebula]])
- It answers the "is anyone still alive in there?" question — all three gates are on
  derelict/quarantine beacons.
- [[item-slug-crew]] gives the same in-play information ([[source-text-blueprints]]) but
  satisfies `req="slug"`, a different gate, and the two never appear on the same list.

## Related
- [[item-slug-crew]] — the crew equivalent in play, a different `req` in events
- [[item-sensors]] — what it substitutes for when down
- [[item-long-ranged-scanners]] — the other scanning augment

## Open Questions
- [ ] Whether any of the three beacons offers a vanilla alternative to the removed choice.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
