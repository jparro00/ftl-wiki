---
id: item-halberd-beam
type: item
item_kind: weapon
rarity: 2
unlocks_blue: [[[event-crushed-pirate]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, beam]
---

# Halberd Beam

## Summary
The `BEAM_2` weapon — *"Slow but reliably powerful standard beam weapon."* Tooltip: *"Beam
weapon, 2 damage per room."* ([[source-text-blueprints]]).

## Stats
- Blueprint `BEAM_2` (`<weaponBlueprint>`), `<type>BEAM</type>`, [[source-blueprints]].
- Damage **2** per room, `length` 80, `sp` 0, `fireChance` 0, `breachChance` 0.
- Power **3**, cooldown **17**. Cost **65** scrap (`<!--was 70-->`), `bp` 7, `rarity` 2.

## How To Get It
- **[[event-tutorial-enemy]]** — `TUTORIAL_PIRATE` hands the player a `<weapon name="BEAM_2"/>` ([[source-events-xml]]).
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.

## Blue Options It Unlocks
- [[event-crushed-pirate]] — `DISTRESS_TRAPPED_MINER` via `req="WEAPONS_BEAM_DAMAGE"` — the Halberd is a member of that blueprint list ([[source-autoblueprints]])

## Strategy Notes
- Its blue option is inherited from the category, not from the blueprint: see
  [[item-beam-weapons]] for the full `WEAPONS_BEAM_DAMAGE` membership.
- `sp` 0 — like every beam except the artillery, it is stopped cold by shields.

## Related
- [[item-beam-weapons]] — the category list that carries its blue option
- [[item-artillery-beam]] — the one shield-piercing beam in the same list
- [[event-tutorial-enemy]] — where the tutorial hands it over

## Open Questions
- [ ] Whether the tutorial grant persists into a real run.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
