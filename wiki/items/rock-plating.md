---
id: item-rock-plating
type: item
item_kind: augment
rarity: 0
unlocks_blue: [[[event-asteroid-belt-distress]], [[event-dense-asteroid-field-distress]], [[event-mantis-ship-with-rock-body-parts]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [augment, defence, rock]
---

# Rock Plating

## Summary
The `ROCK_ARMOR` augment — *"Superior hull armor provides a 15 percent chance to negate incoming
hull damage (hit systems will still be damaged)."* ([[source-text-blueprints]]).

## Stats
- Blueprint `ROCK_ARMOR` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **80** scrap. `bp` 8, `rarity` **0**. `<stackable>false</stackable>`.
- `<value>0.15</value>` — matches the 15 percent in the description.

## How To Get It
- **[[event-rock-unlock3]]** — `ROCK_UNLOCK3` awards `<augment name="ROCK_ARMOR"/>` ([[source-events-rock]]), the final step of [[chain-rock-cruiser-unlock]].
- Starting augment on the Rock Cruiser layouts.
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).

## Blue Options It Unlocks
- [[event-asteroid-belt-distress]] — `CIVILIAN_ASTEROIDS_BEACON_2` — push through the belt without taking the hull hit
- [[event-dense-asteroid-field-distress]] — `ASTEROID_DERELICT_SHIP`
- [[event-mantis-ship-with-rock-body-parts]] — `ROCK_MANTIS_HUNTER`

## Strategy Notes
- Two of its three gates are asteroid-field beacons, which is thematically exact: the
  augment's blue option is "the rocks don't hurt us".
- The third, `ROCK_MANTIS_HUNTER`, sits on a list that also accepts [[item-rock-crew]] —
  the augment stands in for having a Rockman aboard.

## Related
- [[item-rock-crew]] — accepted on the same choice list at `ROCK_MANTIS_HUNTER`
- [[item-titanium-system-casing]] — the same 15 percent trick applied to systems instead of hull
- [[chain-rock-cruiser-unlock]] — where it is awarded

## Open Questions
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
