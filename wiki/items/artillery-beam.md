---
id: item-artillery-beam
type: item
item_kind: weapon
rarity: 0
unlocks_blue: [[[event-crushed-pirate]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [weapon, beam, artillery, federation]
---

# Artillery Beam

## Summary
The `ARTILLERY_FED` weapon — *"Powers a slow, high-powered beam that pierces all shields and
does one damage per room hit. More power means faster cooldown."* ([[source-text-blueprints]]).
Fired by the `artillery` system rather than from a weapon slot.

## Stats
- Blueprint `ARTILLERY_FED` (`<weaponBlueprint>`), `<type>BEAM</type>`, [[source-blueprints]].
- Damage **1** per room, `sp` **5** (pierces all shields), `length` **500** — by far the longest beam in the file.
- `fireChance` 1, `breachChance` 0, `speed` 13, cooldown **40**, `power` 1, `cost` 0, `bp` 5, `rarity` 0.
- The `artillery` `<systemBlueprint>` that fires it: `startPower` 2, `maxPower` 4, purchase cost **150** scrap,
  upgrades 30 / 50 / 80, `rarity` 0. Its `<title>`/`<desc>` are marked in-file as *"dummy text.
  will steal from whatever weapon blueprint it uses"*.

## How To Get It
- Starting system on the Federation Cruiser layouts. Not sold or awarded anywhere in `raw/gamedata/`.

## Blue Options It Unlocks
- [[event-crushed-pirate]] — `DISTRESS_TRAPPED_MINER` via `req="WEAPONS_BEAM_DAMAGE"` — `ARTILLERY_FED` is a member of that blueprint list ([[source-autoblueprints]])

## Strategy Notes
- The only beam in the game with `sp` 5: shields do not stop it, which is why the Federation
  Cruiser can win a fight it cannot out-shoot.
- A Weapons-system hack does not affect artillery — recorded on [[event-slug-hacker-choice]].
- Because it is in `WEAPONS_BEAM_DAMAGE`, a Federation Cruiser satisfies the
  [[event-crushed-pirate]] gate with no beam in its weapon slots at all.

## Related
- [[item-flak-artillery]] — the AE Type-C replacement fired by the same system
- [[item-beam-weapons]] — the category list it belongs to
- [[item-hacking]] — cannot disable it via the Weapons system

## Open Questions
- [ ] How the artillery system's `maxPower` 4 maps onto cooldown — "more power means faster cooldown" is stated but not quantified.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
