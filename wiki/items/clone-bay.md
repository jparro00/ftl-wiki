---
id: item-clone-bay
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-single-life-form-on-moon]], [[event-legendary-thief-kazaaakplethkilik]], [[event-nebula-wreckage]], [[event-abandoned-station]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [system, advanced-edition, crew]
---

# Clone Bay

## Summary
The `clonebay` system, added in Advanced Edition. *"Automatically clones dead crew with skill
penalty. Taking advantage of micro-cloning, crew heals partially every jump. Jump heal is
passive and requires no power."* ([[source-text-blueprints]]). It occupies the Medbay slot — a
ship has one or the other.

## Stats
- Blueprint `clonebay` (`<systemBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **50** scrap. Upgrade costs: level 2 = 35, level 3 = 45.
- `rarity` 1.

## How To Get It
- **Stores** — 50 scrap ([[source-dlcblueprints]]).
- Starting system on several AE layouts.
- No event in `raw/gamedata/` grants a Clone Bay as a reward.

## Blue Options It Unlocks
- [[event-single-life-form-on-moon]] — the `MADMAN` sub-list, `req="clonebay" lvl="2"`, tagged `<!--DLC!-->` — recovers Charlie where a level-2 Medbay does the same job in vanilla
- [[event-legendary-thief-kazaaakplethkilik]] — `MANTIS_NAMED_THIEF_DEFEAT`, `lvl="2"`
- [[event-nebula-wreckage]] — the `BATTLEFIELD_SURVIVOR` sub-event
- [[event-abandoned-station]] — `EMPTY_STATION2_LIST`

## Strategy Notes
- Every Clone Bay gate in the data sits on the same choice list as an equivalent Medbay
  gate (`MADMAN`, `MANTIS_NAMED_THIEF_DEFEAT`, `BATTLEFIELD_SURVIVOR`), so trading Medbay
  for Clone Bay costs nothing in blue options at those beacons — it only changes which
  `req` fires. ([[source-events-xml]], [[source-events-mantis]], [[source-events-slug]])
- Four gates against Medbay's eight, so on raw event count the Medbay is still the better
  key. The Clone Bay's argument is in combat, not at beacons.

## Related
- [[item-medbay]] — the mutually exclusive alternative
- [[item-backup-dna-bank]] — keeps clone storage working with the system off or broken
- [[item-teleporter]] — the system whose risk maths the Clone Bay most changes

## Open Questions
- [ ] Whether the vanilla build offers any substitute for the AE-only `MADMAN` clonebay branch beyond the level-2 Medbay choice.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
