---
id: item-fire-bomb
type: item
item_kind: weapon
rarity: 2
unlocks_blue: [[[event-remote-settlement]], [[event-quest-mantis-invasion]], [[event-capture-the-ship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [weapon, bomb, fire]
---

# Fire Bomb

## Summary
The `BOMB_FIRE` weapon — *"Self-teleporting explosive designed to damage crew-members and light
fires. Can target your own ship."* ([[source-text-blueprints]]).

## Stats
- Blueprint `BOMB_FIRE` (`<weaponBlueprint>`), `<type>BOMB</type>`, [[source-blueprints]].
- Hull damage 0, `sysDamage` 0, crew damage (`persDamage`) **2**, `fireChance` **10**.
- Power **2**, cooldown **15**, 1 shot, consumes **1 missile** per shot.
- Cost **50** scrap (`<!--was 55-->`), `bp` 5, `rarity` 2.

## How To Get It
- **Stores**, and as `autoReward` `weapon` payouts. Generic reward pools (`RANDOM`, `WEAPONS_*` lists) name no specific blueprint, so most events cannot be attributed to one weapon.
- No event in `raw/gamedata/` awards `BOMB_FIRE` by name.

## Blue Options It Unlocks
- [[event-remote-settlement]] — `PIRATE_STATION_CROPS` — burn the crops; the same list also takes [[item-fire-beam]]
- [[event-quest-mantis-invasion]] — `QUEST_MANTIS_INVASION`
- [[event-capture-the-ship]] — the `QUEST_CREWDEAD_START_2` sub-event

## Strategy Notes
- `fireChance` 10 is the maximum value seen on any weapon in [[source-blueprints]] — it is
  the most reliable fire-starter in the file, ahead of [[item-fire-beam]] at 8.
- Because bombs teleport, they ignore shields entirely; the trade is one missile per shot.
- Its three gates are all "set something on fire deliberately" beacons.

## Related
- [[item-fire-beam]] — shares the `PIRATE_STATION_CROPS` choice list
- [[item-missile-weapon]] — the `WEAPONS_MISSILES` category, which does **not** include bombs
- [[item-healing-burst]] / [[item-crystal-lockdown-bomb]] — the other utility bombs

## Open Questions
- [ ] Whether `fireChance` is a percentage, a weight, or a 0–10 scale — no source defines the units.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
