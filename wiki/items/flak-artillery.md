---
id: item-flak-artillery
type: item
item_kind: weapon
rarity: 0
unlocks_blue: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [weapon, artillery, federation, advanced-edition]
---

# Flak Artillery

## Summary
The `ARTILLERY_FED_C` weapon, added in Advanced Edition — *"Powers a slow, high-powered flak gun
that fires seven projectiles. More power means faster cooldown."* ([[source-text-blueprints]]).
The Federation Cruiser Type C's artillery.

## Stats
- Blueprint `ARTILLERY_FED_C` (`<weaponBlueprint>`), `<type>BURST</type>`, defined **only** in [[source-dlcblueprints]] — Advanced Edition content.
- Damage **1** per projectile, `radius` 35, `spin` 720, `speed` 26, `sp` **0**.
- `<projectiles>`: 3 × `debris_large`, 4 × `debris_med` (real), plus 7 × `debris_small` marked `fake="true"`.
  The tooltip's *"7 projectiles"* corresponds to the 3 + 4 real ones plus the visual-only shower.
- Power **3**, cooldown **40**. Cost 75, `bp` 10, `rarity` 0. `drone_targetable` 1.

## How To Get It
- Starting artillery on the Federation Cruiser Type C (*The Fregatidae*), whose description
  names it directly ([[source-text-blueprints]]). Not sold or awarded anywhere in `raw/gamedata/`.

## Blue Options It Unlocks
- **None.** `ARTILLERY_FED_C` appears in no `req` and in no event blueprint list.
  Unlike [[item-artillery-beam]], it is **not** a member of `WEAPONS_BEAM_DAMAGE`
  ([[source-autoblueprints]]) — a Type C Federation Cruiser therefore does *not* satisfy the
  [[event-crushed-pirate]] beam gate.

## Strategy Notes
- `drone_targetable="1"` means enemy defence drones can shoot its projectiles down, which
  [[item-artillery-beam]] (a beam) is immune to.
- `sp` 0: unlike the Artillery Beam it does not pierce shields — it is a shield-stripper,
  not a shield-ignorer.
- A Weapons hack does not affect artillery — recorded on [[event-slug-hacker-choice]].

## Related
- [[item-artillery-beam]] — the base-game artillery, and the one with a blue option
- [[item-defense-drone]] — what shoots flak projectiles down
- [[item-hacking]]

## Open Questions
- [ ] Whether the 7 `fake="true"` small projectiles do damage — the flag suggests not, but no source says.

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
