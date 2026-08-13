---
id: item-lanius-crew
type: item
item_kind: crew
rarity: 0
unlocks_blue: [[[event-lanius-ship-attacking-civilian-distress]], [[event-lanius-with-federation-science-craft]], [[event-lanius-craftsmen]], [[event-lanius-trader]], [[event-lanius-ship-salvager]], [[event-lanius-lone-ship]], [[event-lanius-ship-absorbing-rebel-base]], [[event-lanius-ship-absorbing-jump-beacon]], [[event-lanius-powered-down-ship]], [[event-the-engi-virus]], [[event-space-station-under-construction]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [crew, lanius, advanced-edition]
---

# Lanius (crew)

## Summary
The `anaerobic` crew blueprint, added in Advanced Edition — *"These anaerobic beings seem
friendly enough."* ([[source-text-blueprints]]). The blueprint id is `anaerobic`; the display
name is Lanius.

## Stats
- Blueprint `anaerobic` (`<crewBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Powers, verbatim: *"Drains oxygen from rooms."* and *"Slow movement but no damage from
  lack of oxygen."*
- Hire cost **50** scrap, `bp` 2, `rarity` **0**.

## How To Get It
- Hired at stores, most often in [[sector-abandoned-sector]].
- No event in `raw/gamedata/` grants a Lanius via a named `<crewMember class="anaerobic">`;
  the Lanius event set grants them through `autoReward` and unnamed crew tags instead.

## Blue Options It Unlocks
- [[event-lanius-ship-attacking-civilian-distress]] — `LANIUS_DISTRESS_FIGHT`
- [[event-lanius-with-federation-science-craft]] — `LANIUS_RESEARCHER_CONTACT`
- [[event-lanius-craftsmen]] — `LANIUS_RESEARCHER_CRAFT`
- [[event-lanius-trader]] — `LANIUS_TRADER`
- [[event-lanius-ship-salvager]] — `LANIUS_SOLO_SALVAGE`
- [[event-lanius-lone-ship]] — `LANIUS_SCARED_CIVILIAN`
- [[event-lanius-ship-absorbing-rebel-base]] — `LANIUS_GROUP_AUTO`
- [[event-lanius-ship-absorbing-jump-beacon]] — `LANIUS_BEACON_EATER`
- [[event-lanius-powered-down-ship]] — the `LANIUS_DORMANT_INVESTIGATE` sub-event
- [[event-the-engi-virus]] — `ENGI_VIRUS` — the one non-Lanius beacon that takes the gate
- [[event-space-station-under-construction]] — `QUEST_CONSTRUCTIONYARD`

## Strategy Notes
- Eleven gates, essentially all of them inside the Lanius event set in
  [[source-dlcevents-anaerobic]] — the species is its own self-contained blue-option economy.
  Outside [[sector-abandoned-sector]] it opens almost nothing.
- Oxygen drain is a liability on a crewed ship and an asset when boarding; the gates are
  diplomatic ("we have one of you aboard") rather than mechanical.

## Related
- [[item-oxygen-system]] / [[item-emergency-respirators]] — the systems its drain fights
- [[sector-abandoned-sector]] — where the whole event set lives

## Open Questions
- [ ] How Lanius crew are actually acquired in events — no named `<crewMember class="anaerobic">` grant exists in `raw/gamedata/`.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
