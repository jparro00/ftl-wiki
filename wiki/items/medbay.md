---
id: item-medbay
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-single-life-form-on-moon]], [[event-unknown-disease-on-mining-colony]], [[event-research-station-with-no-response]], [[event-zoltan-research-facility]], [[event-plagued-station]], [[event-legendary-thief-kazaaakplethkilik]], [[event-slug-hacker-medical]], [[event-nebula-wreckage]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [system, crew]
---

# Medbay

## Summary
The `medbay` system — *"Heals all crew-members within the Medbay room. Upgrading increases
healing speed."* ([[source-text-blueprints]]). Occupies the same slot as the AE-only
[[item-clone-bay]].

## Stats
- Blueprint `medbay` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **50** scrap. Upgrade costs: level 2 = 35, level 3 = 45.
- `rarity` 1.

## How To Get It
- **Stores** — 50 scrap ([[source-blueprints]]).
- Starting system on most player layouts.
- No event in `raw/gamedata/` grants a Medbay as a reward.

## Blue Options It Unlocks
- [[event-single-life-form-on-moon]] — the `STRANDED` list at `lvl="2"` and `lvl="3"` (the level-3 branch tagged `<!--DLC!-->`), plus the `MADMAN` list at `lvl="2"`
- [[event-unknown-disease-on-mining-colony]] — `DISTRESS_STATION_DISEASE`, `lvl="2"`
- [[event-research-station-with-no-response]] — `STATION_SICK_LIST`, `lvl="2"` and `lvl="3"`
- [[event-zoltan-research-facility]] — `ZOLTAN_CREW_STUDY`, `lvl="3"`
- [[event-plagued-station]] — `DONOR_PLAGUE_LIST`, `lvl="2"`
- [[event-legendary-thief-kazaaakplethkilik]] — `MANTIS_NAMED_THIEF_DEFEAT`, `lvl="2"`
- [[event-slug-hacker-medical]] — `NEBULA_SLUG_MEDBAY`, `lvl="2"`
- [[event-nebula-wreckage]] — the `BATTLEFIELD_SURVIVOR` sub-event, `lvl="2"`

## Strategy Notes
- Every Medbay gate in the data is `lvl="2"` or higher — a bare level-1 Medbay unlocks
  nothing at all. The 35-scrap first upgrade is what buys the blue options.
- The gates are overwhelmingly *rescue* beacons: sick colonists, plague victims, survivors.
  Medbay is the game's "help people" key the way Teleporter is its "go and take it" key.
- The AE-only `lvl="3"` branch in `STRANDED` yields a better version of the same rescue
  (a crew member with `all_skills="1"`) — see [[event-single-life-form-on-moon]].

## Related
- [[item-clone-bay]] — the AE alternative in the same slot
- [[item-engi-med-bot-dispersal]] / [[item-healing-burst]] — healing outside the Medbay room

## Open Questions
- [ ] Whether the vanilla `STRANDED` list drops the level-3 branch entirely.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
