---
id: item-emergency-respirators
type: item
item_kind: augment
rarity: 2
unlocks_blue: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [augment, advanced-edition, crew]
---

# Emergency Respirators

## Summary
The `O2_MASKS` augment, added in Advanced Edition — *"Crew take half damage from low oxygen."*
([[source-text-blueprints]]).

## Stats
- Blueprint `O2_MASKS` (`<augBlueprint>`), defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Cost: **50** scrap. `bp` 8, `rarity` 2. `<stackable>false</stackable>`.
- `<value>0.5</value>` — the "half damage" in the description.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `O2_MASKS` by name.

## Blue Options It Unlocks
- **None.** No `<choice req="O2_MASKS">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- It makes venting a room a cheaper tactic against boarders, and softens a broken
  [[item-oxygen-system]], but it opens no beacons.
- [[event-boarders-humans-abandoned]] links this augment from a Fandom claim; check that
  page's contradiction note before relying on it.

## Related
- [[item-oxygen-system]] — what it backstops
- [[item-lanius-crew]] — immune to the problem entirely
- [[item-doors]] — venting is the usual reason oxygen drops

## Open Questions
- [ ] The Fandom claim recorded on [[event-boarders-humans-abandoned]] — verify against the event XML.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
