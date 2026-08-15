---
id: item-emergency-respirators
type: item
item_kind: augment
rarity: 2
unlocks_blue: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 5
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

### What the 0.5 multiplies
Suffocation base rate is **6.4 HP/sec** at ≤5% room O₂ ([[source-fandom-oxygen]]), so:

| Crew | With Respirators |
|---|---|
| Standard (6.4 HP/sec) | **3.2 HP/sec** |
| [[entity-crystal-men]] (already halved, 3.2) | **1.6 HP/sec** — the two stack to 25% |
| [[entity-lanius]] | irrelevant — exempt anyway |

It **also applies while your crew are boarding an enemy ship** ([[source-fandom-oxygen]]) —
which is where it earns its keep, since you do not control the enemy's oxygen.

Caveat carried from [[concept-oxygen-and-suffocation]]: the 6.4 base is single-sourced. The
0.5 multiplier itself is from the game files and is not in doubt.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `O2_MASKS` by name.

## Blue Options It Unlocks
- **None.** No `<choice req="O2_MASKS">` exists anywhere in `raw/gamedata/`.
  ([[source-events-xml]] and the other event files, searched exhaustively)

## Strategy Notes
- It makes venting a room a cheaper tactic against boarders, and softens a broken
  [[item-oxygen-system]], but it opens no beacons.
- **A powered level-1 [[item-medbay]] beats it outright** in the one room it covers —
  suffocation damage there is not halved but *zero* ([[source-fandom-oxygen]]). The augment's
  value is everywhere the Medbay isn't: the rest of your ship, and enemy ships.
- [[event-boarders-humans-abandoned]] links this augment from a Fandom claim; check that
  page's contradiction note before relying on it.

## Related
- [[concept-oxygen-and-suffocation]] — the base rate this halves, and the full modifier table
- [[item-oxygen-system]] — what it backstops
- [[item-medbay]] — full immunity, but only in one room
- [[item-lanius-crew]] — immune to the problem entirely
- [[entity-crystal-men]] — the other 50% reduction; stacks with this one
- [[item-doors]] — venting is the usual reason oxygen drops

## Open Questions
- [ ] The Fandom claim recorded on [[event-boarders-humans-abandoned]] — verify against the event XML.
- [ ] Whether enemy **mind-controlled** crew benefit from it — [[source-fandom-oxygen]] flags
      this as untested in its own `@to-do`.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
- [[source-xftl-oxygen-mechanics]] (per raw/modding/2026-08-14-xftl-oxygen-mechanics.txt)
