---
id: item-damaged-stasis-pod
type: item
item_kind: augment
rarity: 0
unlocks_blue: [[[event-zoltan-research-facility]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, quest, crystal-route]
---

# Damaged Stasis Pod

## Summary
The `STASIS_POD` augment — *"This bizarre alien artifact appears to be barely operational. It
has no practical function but perhaps someone can repair it."* ([[source-text-blueprints]]).
A quest token rather than an upgrade: the first step of the Crystal Cruiser route.

## Stats
- Blueprint `STASIS_POD` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **30** scrap. `bp` 15, `rarity` **0**.
- `<stackable>true</stackable>` and `<value>0.15</value>` — both meaningless for an item the
  description says has "no practical function". The file gives no explanation.

## How To Get It
- **[[event-dense-asteroid-field-distress]]** — both `ASTEROID_DERELICT_SHIP_ROCK` and
  `ASTEROID_DERELICT_SHIP_SEARCH` award `<augment name="STASIS_POD"/>` ([[source-events-xml]]).
- Not obtainable from stores in the way ordinary augments are — `rarity` 0.

## Blue Options It Unlocks
- [[event-zoltan-research-facility]] — `ZOLTAN_CREW_STUDY` — the Zoltan scientists recognise the pod, the next step toward [[chain-crystal-cruiser-unlock]]

## Strategy Notes
- It is the key to a chain, not a combat upgrade: carry it to [[event-zoltan-research-facility]].
- Its `<value>` and `stackable` flags look like boilerplate copied from another augment;
  treat them as meaningless unless a source says otherwise.

## Related
- [[chain-crystal-cruiser-unlock]] — the chain it opens
- [[item-crystal-vengeance]] — the augment at the far end of that chain
- [[event-dense-asteroid-field-distress]] — where the pod is found

## Open Questions
- [ ] Why a "no practical function" augment carries `stackable="true"` and `<value>0.15</value>`.
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
