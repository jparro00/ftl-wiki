---
id: item-teleporter
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]], [[event-research-station-with-no-response]], [[event-merchant-investigate]], [[event-capture-the-ship]], [[event-crystalline-cache]], [[event-legendary-thief-kazaaakplethkilik]], [[event-nebula-lost-ship]], [[event-slaver-friendly]], [[event-auto-ship-near-sensor-station]], [[event-zoltan-trade-hub]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
tags: [system, boarding]
---

# Crew Teleporter

## Summary
The `teleporter` system — *"Allows you to send your crew-members to board enemy vessels."*
([[source-text-blueprints]]). Mechanically it is the boarding system; in the event data it is
also one of the two most-used "reach something that is not on your ship" keys in the game.

## Stats
- Blueprint `teleporter` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **90** scrap (the file notes `<!--CHANGED was 75-->`).
- Upgrade costs: level 2 = 30 scrap, level 3 = 60 scrap.
- `rarity` 1. Carries `<locked>1</locked>`; the blueprint files never define what `locked` does.

## How To Get It
- **Stores** — 90 scrap ([[source-blueprints]]).
- Starting system on several player layouts (see the `shipBlueprint` entries in [[source-blueprints]] and [[source-dlcblueprintsoverwrite]]).
- No event in `raw/gamedata/` grants the teleporter system as a reward.

## Blue Options It Unlocks
- [[event-asteroid-belt-distress]] — `CIVILIAN_ASTEROIDS_BEACON_2`, the follow-up beacon
- [[event-rebel-ship-attacking-federation-loyalists]] — `REBEL_VS_FEDERATION_SAVED_LIST` — beam the survivors aboard; adds a crew member and the hidden-Federation-base quest marker
- [[event-research-station-with-no-response]] — `STATION_SICK_LIST`
- [[event-merchant-investigate]] — `MERCHANT_INVESTIGATE_LIST`
- [[event-capture-the-ship]] — `QUEST_CREWDEAD_START_2`, `lvl="1"` — the boarding route through the derelict
- [[event-crystalline-cache]] — `CRYSTAL_CACHE_LIST`, `lvl="2"`
- [[event-legendary-thief-kazaaakplethkilik]] — `MANTIS_NAMED_THIEF_DEFEAT`
- [[event-nebula-lost-ship]] — `NEBULA_LOST_SHIP`
- [[event-slaver-friendly]] — `FRIENDLY_SLAVER`, `lvl="2"`
- [[event-auto-ship-near-sensor-station]] — `AUTO_DEFENSE_MAP`
- [[event-zoltan-trade-hub]] — `ZOLTAN_TRADE_HUB`, `lvl="1"`

## Strategy Notes
- Eleven distinct events carry a `req="teleporter"` choice — behind only Sensors (17) and
  Hacking (14) across an exhaustive scan of the event files in `raw/gamedata/`.
- Only two of those gates ask for a level above 1 (`CRYSTAL_CACHE_LIST` and
  `FRIENDLY_SLAVER`, both `lvl="2"`), so an unupgraded 1-power teleporter satisfies nine
  of the eleven. That is the opposite of [[item-sensors]] and [[item-medbay]], whose gates
  almost all want level 2+.

## Related
- [[item-boarding-drone]] — the dronebay route to putting bodies on an enemy ship
- [[item-clone-bay]] / [[item-medbay]] — what keeps boarders alive
- [[item-mantis-pheromones]] — movement speed for boarding parties

## Open Questions
- [ ] What `<locked>1</locked>` controls — it appears on `teleporter`, `cloaking` and `mind` only.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
