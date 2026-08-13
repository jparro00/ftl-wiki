---
id: source-fandom-free-weapon
type: source
source_kind: wiki
raw: raw/wiki/free-weapon.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [free-item, weapon, no-choice]
---

# Fandom — "Free weapon"

## Summary
The community wiki page for the event the game files call `FIND_WEAPON`. Retrieved via the
MediaWiki API at revision 74071. A pure reward event with no choices.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FIND_WEAPON' in the
  datafiles."* This is the join key.
- Lists all six intro variants, matching the six entries of the `FIND_WEAPON` textList in
  the files exactly — and unlike its `FIND_DRONE` and `FREE_ITEMS` siblings, **none of
  these six is marked as a DLC addition** in `events.xml`, so the pool is the same in both
  editions.
- Reads `<autoReward level="LOW">weapon</autoReward>` as *"a weapon with low scrap"*.
- Confirms availability in fifteen sectors including **Hidden Crystal Worlds** but
  **excluding the Zoltan sectors** — a real difference from its `FIND_DRONE` sibling,
  which the files bear out (`FIND_WEAPON` is absent from `ITEM_ZOLTAN`).
- `alsooccur=exit`, `LRSmap=noship`, `unique=false`.
- Categorised `Random_Events`, `Weapon reward`.

## Events Covered
- [[event-free-weapon]]

## Other Pages Touched
- [[event-free-drone-schematic]], [[event-free-scrap-with-resources]],
  [[concept-autoreward-tiers]]

## Reliability Notes
`medium`. No game version stated, but nothing on this page is version-sensitive.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Free_weapon
- [[source-events-xml]], [[source-text-events-xml]]
