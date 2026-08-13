---
id: item-artemis-missiles
type: item
item_kind: weapon
rarity: 0
unlocks_blue: [[[event-quest-mantis-invasion]], [[event-rock-live-mine]], [[event-asteroid-mining-colony]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [weapon, missile]
---

# Artemis Missiles

## Summary
The `MISSILES_2` weapon — *"Standard missile launcher on most Federation ships."* Tooltip:
*"Fires 1 missile; does 2 damage; pierces all shields."* ([[source-text-blueprints]]). A second
blueprint, `MISSILES_2_PLAYER`, carries identical display text but **different stats** — see
below.

## Stats
- Blueprint `MISSILES_2` (`<weaponBlueprint>`), `<type>MISSILES</type>`, [[source-blueprints]].
- Damage **2**, 1 shot, consumes 1 missile, `sp` **5** (pierces all shields).
- `fireChance` 1, `breachChance` 1, `stunChance` 1.
- Power **2**, cooldown **10**. Cost **38** scrap, `bp` 5, **`rarity` 0**.
- **`MISSILES_2_PLAYER`** — same damage, shots, `sp` and cost, but **power 1** and **cooldown
  11** ([[source-blueprints]]). It is the cheaper-to-power, marginally slower variant, and it
  is the one the tutorial hands out. The in-game text for both is byte-identical
  ([[source-text-blueprints]]), so nothing in the UI distinguishes them.
- For comparison, `MISSILES_1` (Leto) has the fastest missile cooldown in the file at 9, for
  1 damage.

## How To Get It
- **[[event-tutorial-missile]]** — `TUTORIAL_MISSILE` grants `<weapon name="MISSILES_2_PLAYER"/>` ([[source-events-xml]]).
- Starting weapon on the Kestrel and several other layouts.
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.

## Blue Options It Unlocks
- [[event-quest-mantis-invasion]] — `QUEST_MANTIS_INVASION` via `req="WEAPONS_MISSILES"`
- [[event-rock-live-mine]] — `ROCK_STARSHIP_MINE` via `req="WEAPONS_MISSILES"`
- [[event-asteroid-mining-colony]] — `HELP_MINERS` via `req="WEAPONS_MISSILES_EVENTS"`

## Strategy Notes
- All three blue options come from category membership rather than the blueprint id — see
  [[item-missile-weapon]].
- `MISSILES_2` and `MISSILES_2_PLAYER` are both members of `WEAPONS_MISSILES` and
  `WEAPONS_MISSILES_EVENTS` ([[source-autoblueprints]], [[source-dlcblueprintsoverwrite]]),
  so either satisfies all three gates.
- The `_PLAYER` variant's 1 power against the standard 2 is a real difference the game never
  surfaces: the two share a title, a short name, a description and a tooltip. Where a source
  says "Artemis Missiles" without a blueprint id, it is `unknown` which one is meant.

## Related
- [[item-missile-weapon]] — the category that carries the blue options
- [[item-breach-missiles]] — the heavy end of the same category

## Open Questions
- [ ] Which of `MISSILES_2` / `MISSILES_2_PLAYER` a store actually stocks, and whether the
      player can ever obtain the 2-power version.
- [ ] What `rarity` 0 means for store/reward generation — the blueprint files state the number but never define the scale.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
