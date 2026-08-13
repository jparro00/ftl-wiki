---
id: item-distraction-buoys
type: item
item_kind: augment
rarity: 3
unlocks_blue: [[[event-crystalline-ship-messaging-about-rebels]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, advanced-edition, rebel-fleet]
---

# Distraction Buoys

## Summary
The `FLEET_DISTRACTION` augment, added in Advanced Edition — *"Leaves a false signal at sector
start to delay Rebels 1 jump."* ([[source-text-blueprints]]).

## Stats
- Blueprint `FLEET_DISTRACTION` (`<augBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Cost: **55** scrap. `bp` 8, `rarity` 3. `<stackable>false</stackable>`.
- `<value>1.f</value>` — a malformed float literal in the source file, presumably meaning 1.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `FLEET_DISTRACTION` by name.

## Blue Options It Unlocks
- [[event-crystalline-ship-messaging-about-rebels]] — `CRYSTAL_REQUEST`, tagged `<!--DLC-->` — the only `req="FLEET_DISTRACTION"` choice in the game

## Strategy Notes
- One extra jump of slack per sector is worth most in [[sector-the-last-stand]] and on the
  detour-heavy [[chain-crystal-cruiser-unlock]] route — which is also where its single blue
  option lives.

## Related
- [[event-crystalline-ship-messaging-about-rebels]] — its only gate
- [[item-ftl-jumper]] — the other map-level augment

## Open Questions
- [ ] What `<value>1.f</value>` was meant to be — the literal is not valid XML-numeric and no source explains it.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
