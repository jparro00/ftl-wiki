---
id: item-engi-med-bot-dispersal
type: item
item_kind: augment
rarity: 0
unlocks_blue: [[[event-rebel-ship-attacking-federation-loyalists]], [[event-unknown-disease-on-mining-colony]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, crew, engi]
---

# Engi Med-bot Dispersal

## Summary
The `NANO_MEDBAY` augment — *"Engi nano med-bots heal the crew outside of the med-bay (at a
reduced speed)."* ([[source-text-blueprints]]). Also linked from event pages as
[[item-nano-med-bot-dispersal]] after its blueprint id.

## Stats
- Blueprint `NANO_MEDBAY` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **60** scrap. `bp` 12, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.25</value>` — presumably the reduced heal rate, but the file does not say.

## How To Get It
- **[[event-distress-engi-rebel-result]]** — the `DISTRESS_ENGI_REBEL_LIST2` pool awards `<augment name="NANO_MEDBAY"/>` ([[source-events-engi]]).
- `FREE_NANO` in [[source-events-xml]] also awards it. That event has **no wiki page** and no
  reference anywhere else in `raw/gamedata/` — flagged below.
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- [[event-rebel-ship-attacking-federation-loyalists]] — `REBEL_VS_FEDERATION_SAVED_LIST`
- [[event-unknown-disease-on-mining-colony]] — `DISTRESS_STATION_DISEASE`

## Strategy Notes
- Both gates are "keep people alive away from the Medbay" beacons, which is exactly what
  the augment does in play.
- On a [[item-clone-bay]] ship there is no Medbay to walk back to, which is the case where
  passive healing matters most — but no source in `raw/` states an interaction.

## Related
- [[item-nano-med-bot-dispersal]] — alias page under the blueprint id
- [[item-medbay]] / [[item-clone-bay]] — what it supplements
- [[item-healing-burst]] — the weapon that does the same job on demand

## Open Questions
- [ ] `FREE_NANO` (`events.xml`) is a complete event that awards this augment but has no page and no inbound reference in `raw/gamedata/` — needs a reachability check.
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
