---
id: item-mantis-pheromones
type: item
item_kind: augment
rarity: 0
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, crew, mantis]
---

# Mantis Pheromones

## Summary
The `CREW_STIMS` augment — *"Your crew's movement speed is increased by 25 percent."*
([[source-text-blueprints]]).

## Stats
- Blueprint `CREW_STIMS` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **50** scrap. `bp` 9, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.25</value>` — the 25 percent in the description.

## How To Get It
- **[[event-legendary-thief-kazaaakplethkilik]]** — `MANTIS_NAMED_THIEF_DEFEAT` awards `<augment name="CREW_STIMS"/>` ([[source-events-mantis]]). The only named grant in the event data.
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- **None.** No `<choice req="CREW_STIMS">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- Pure boarding/firefighting support: it makes the [[item-teleporter]] cycle faster and
  crew reach breaches sooner, but it gates nothing.
- Exactly mirrors [[item-drone-reactor-booster]] (`DRONE_SPEED`) — same 50 scrap, same
  `bp` 9, same `<value>0.25</value>`, applied to drones instead of crew ([[source-blueprints]]).

## Related
- [[item-drone-reactor-booster]] — the identical augment for shipboard drones
- [[item-teleporter]] — what it most improves
- [[chain-mantis-cruiser-unlock]] — the quest line the grant sits on

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
