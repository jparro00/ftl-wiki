---
id: item-shields
type: item
item_kind: system
rarity: 1
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [system, defence]
---

# Shields

## Summary
The `shields` system — *"Powers your shields. Each additional barrier can block one shot."*
([[source-text-blueprints]]).

## Stats
- Blueprint `shields` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 2, `maxPower` 8 — i.e. four shield bubbles at full power.
- Purchase cost: **125** scrap.
- Upgrade costs, levels 2→9: 100, 20, 30, 40, 60, 80, 100, 120 scrap. The level-2 entry
  costing 100 while level 3 costs 20 is what the file says; barriers come in pairs of power bars.
- `rarity` 1.

## How To Get It
- **Stores** — 125 scrap ([[source-blueprints]]).
- Present on almost every player layout from the start.
- No event in `raw/gamedata/` grants Shields or shield levels.

## Blue Options It Unlocks
- **None.** There is no `<choice req="shields">` anywhere in `raw/gamedata/`.
  Shields is the most important system in the game and gates nothing.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Worth recording precisely because of the absence: shields buy survival, never options.
- [[item-zoltan-shield]] is a separate augment layer that also gates nothing.

## Related
- [[item-zoltan-shield]] — the Super Shield augment
- [[item-cloaking]] / [[item-engines]] — the defences that *do* gate events

## Open Questions
- [ ] Why the level-2 shield upgrade costs 100 scrap against level 3's 20 — likely a pair-of-bars artefact, but no source states it.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
