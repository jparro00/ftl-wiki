---
id: item-beam-weapons
type: item
item_kind: weapon
rarity: unknown
unlocks_blue: [[[event-crushed-pirate]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, category, beam]
---

# Beam Weapon (category)

## Summary
Not a single item: `WEAPONS_BEAM_DAMAGE` is a `<blueprintList>` annotated *"for events"*. The
name is precise — it is the list of beams that do **damage**, which is why the two 0-damage
beams are excluded.

## Stats
- **`WEAPONS_BEAM_DAMAGE`** ([[source-autoblueprints]]) — members: `BEAM_HULL` (Hull Beam),
  `BEAM_3` (Glaive Beam), `BEAM_2` ([[item-halberd-beam]]), `BEAM_1` (Mini Beam),
  `BEAM_LONG` (Pike Beam), `ARTILLERY_FED` ([[item-artillery-beam]]).
- **Excluded**: [[item-anti-bio-beam]] (`BEAM_BIO`) and [[item-fire-beam]] (`BEAM_FIRE`) —
  both have `<damage>0</damage>` in [[source-blueprints]], which the list name accounts for.
- Also excluded: [[item-flak-artillery]] (`ARTILLERY_FED_C`), which is a `BURST` weapon, not a beam.
- Including `ARTILLERY_FED` means a Federation Cruiser satisfies the gate with an empty
  weapon rack.

## How To Get It
- Own any one of the six listed beams, or fly a Federation Cruiser Type A or B.

## Blue Options It Unlocks
- [[event-crushed-pirate]] — `DISTRESS_TRAPPED_MINER`, `req="WEAPONS_BEAM_DAMAGE"` — cut the pirate free; the only `WEAPONS_BEAM_DAMAGE` gate in the game. The same event separately accepts [[item-combat-beam-drone]] via `COMBAT_BEAM_DRONE_LIST`

## Strategy Notes
- One blue option, but it is a good demonstration of how carefully these lists were built:
  a Fire Beam can cut through a bulkhead in fiction and is still excluded, because the list
  tests for damage output rather than for owning a beam.
- [[event-crushed-pirate]] is one of only two beacons gated on two different blueprint lists
  at once; the other is [[event-rock-live-mine]] (`COMBAT_BEAM_DRONE_LIST` plus
  `WEAPONS_MISSILES`).

## Related
- [[item-halberd-beam]] / [[item-artillery-beam]] — members with their own pages
- [[item-anti-bio-beam]] / [[item-fire-beam]] — beams that are **not** members
- [[item-combat-beam-drone]] — the drone-side gate on the same beacon

## Open Questions
- [ ] Whether the exclusion of `BEAM_BIO` and `BEAM_FIRE` is really about `<damage>0</damage>` — the list name implies it, but no source states the rule.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
