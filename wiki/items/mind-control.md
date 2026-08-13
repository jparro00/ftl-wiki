---
id: item-mind-control
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-large-trade-station]], [[event-merchant-deliver]], [[event-mantis-capture-commando]], [[event-pirate-ship-selling-weapon]], [[event-zoltan-security-checkpoint]], [[event-confused-mantis]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [system, advanced-edition, crew]
---

# Mind Control

## Summary
The `mind` system, added in Advanced Edition. *"Temporarily turn enemies into allies."*
([[source-text-blueprints]]).

## Stats
- Blueprint `mind` (`<systemBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **75** scrap. Upgrade costs: level 2 = 30, level 3 = 60.
- `rarity` 1. Carries `<locked>1</locked>`.

## How To Get It
- **Stores** — 75 scrap ([[source-dlcblueprints]]).
- Starting system on several AE layouts.
- No event in `raw/gamedata/` grants Mind Control as a reward.

## Blue Options It Unlocks
- [[event-large-trade-station]] — `STORE_REBELSIDE`, separate gates at `lvl="1"`, `2` and `3`
- [[event-merchant-deliver]] — `MERCHANT_DELIVER_LIST`
- [[event-mantis-capture-commando]] — `MANTIS_CAPTURE_COMMANDO`, tagged `<!--DLC-->`
- [[event-pirate-ship-selling-weapon]] — `NEBULA_WEAPONS_TRADER`, tagged `<!--DLC-->`
- [[event-zoltan-security-checkpoint]] — `ZOLTAN_CREW_SCAN`
- [[event-confused-mantis]] — `CONFUSED_MANTIS`, `lvl="1"`

## Strategy Notes
- Mind Control's gates are social rather than tactical: three of the six are negotiation
  beacons (`STORE_REBELSIDE`, `NEBULA_WEAPONS_TRADER`, `ZOLTAN_CREW_SCAN`) where the blue
  option is coercion instead of combat.
- `STORE_REBELSIDE` is the only event that ladders Mind Control across three levels.
- Because the blueprint is `dlcBlueprints.xml`-only, none of these beacons behave this way
  in vanilla; two of the six are additionally tagged `<!--DLC-->` inside base-file events.

## Related
- [[item-slug-crew]] — immune to mind control ([[source-text-blueprints]])
- [[item-zoltan-shield]] — a Super Shield blocks mind control unless the Zoltan Shield Bypass augment is fitted

## Open Questions
- [ ] What `<locked>1</locked>` controls.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
