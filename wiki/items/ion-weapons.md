---
id: item-ion-weapons
type: item
item_kind: weapon
rarity: unknown
unlocks_blue: [[[event-malfunctioning-defense-system]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [weapon, category, ion]
---

# Ion Weapon (category)

## Summary
Not a single item: `WEAPONS_ION` is a `<blueprintList>` annotated *"for events"* that asks
*"do you own any ion weapon?"*.

## Stats
- **`WEAPONS_ION`** ([[source-autoblueprints]]) — members: `ION_1` (Ion Blast), `ION_2`
  (Heavy Ion), `ION_4` (Ion Blast Mark II), `BOMB_ION` (Ion Bomb), `ION_STUN` (Ion Stunner,
  **listed twice**), `BOMB_STUN` (Stun Bomb), `ION_CHARGEGUN` (Ion Charger), `ION_CHAINGUN`
  (Chain Ion).
- Nine entries, eight distinct blueprints — `ION_STUN` appears at both position 5 and
  position 9. Since the list is used only as a membership test, the duplicate has no effect.
- Four of the eight (`ION_STUN`, `BOMB_STUN`, `ION_CHARGEGUN`, `ION_CHAINGUN`) are defined
  only in [[source-dlcblueprints]], so the *satisfiable* membership is smaller in vanilla.

## How To Get It
- Own any one of the eight listed weapons.

## Blue Options It Unlocks
- [[event-malfunctioning-defense-system]] — `DISTRESS_SATELLITE_DEFENSE`, `req="WEAPONS_ION"` — disable the platform without destroying it; the only `WEAPONS_ION` gate in the game

## Strategy Notes
- One blue option in the entire game, and it is on a beacon that also offers
  [[item-cloaking]] and Engi-crew routes to the same outcome.
- Bombs count here where they do not for [[item-missile-weapon]]: `BOMB_ION` and `BOMB_STUN`
  are members. The lists are curated by *effect*, not by weapon type.

## Related
- [[item-missile-weapon]] / [[item-beam-weapons]] — the sibling category gates
- [[event-malfunctioning-defense-system]] — its only gate

## Open Questions
- [ ] Whether the duplicated `ION_STUN` entry is a typo or has a purpose.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
