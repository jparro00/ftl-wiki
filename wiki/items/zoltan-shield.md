---
id: item-zoltan-shield
type: item
item_kind: augment
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, defence, zoltan]
---

# Zoltan Shield

## Summary
The `ENERGY_SHIELD` augment — *"An unexplained technology creates this nearly impenetrable
shield. Only the energy outburst from an FTL engine is powerful enough to recharge it."*
([[source-text-blueprints]]). The Super Shield layer that sits outside normal shields and
recharges only on a jump.

## Stats
- Blueprint `ENERGY_SHIELD` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **80** scrap. `bp` 8, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>2</value>` — the file gives no units for this figure.

## How To Get It
- **[[event-zoltan-peace-quest2]]** — `ZOLTAN_PEACE_QUEST_REWARD` awards `<augment name="ENERGY_SHIELD"/>` ([[source-events-zoltan]]). This is the only named grant in the event data.
- Starting augment on the Zoltan Cruiser layouts.
- `rarity` 0 — see the open question about what that means for store stock.

## Blue Options It Unlocks
- **None.** No `<choice req="ENERGY_SHIELD">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Ten event pages link this augment, but always as a *reward* or as flavour — it gates
  nothing. Its whole value is combat.
- The AE `ZOLTAN_BYPASS` augment (Zoltan Shield Bypass) exists specifically to let crew
  teleports, bombs and [[item-mind-control]] through a Super Shield ([[source-text-blueprints]]),
  which is how enemy Zoltan Shields interact with boarding runs.

## Related
- [[item-shields]] — the normal shield layer this sits outside of
- [[item-teleporter]] / [[item-mind-control]] — both blocked by an enemy Super Shield
- [[chain-zoltan-cruiser-unlock]] — the quest line that ends at [[event-zoltan-peace-quest2]]

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.
- [ ] What `<value>2</value>` counts — barriers, recharge, or something else. No source says.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
