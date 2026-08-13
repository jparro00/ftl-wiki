---
id: item-missile-weapon
type: item
item_kind: weapon
rarity: unknown
unlocks_blue: [[[event-quest-mantis-invasion]], [[event-rock-live-mine]], [[event-asteroid-mining-colony]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [weapon, category, missile]
---

# Missile Weapon (category)

## Summary
Not a single item: `WEAPONS_MISSILES` and `WEAPONS_MISSILES_EVENTS` are `<blueprintList>`
entries that events use to ask *"do you own any missile launcher?"*. Both lists are annotated
in the source as *"for events"* / *"for an event that asks for missiles"*.

## Stats
- **`WEAPONS_MISSILES`** ([[source-autoblueprints]]) — members: `MISSILES_1` (Leto),
  `MISSILES_2` and `MISSILES_2_PLAYER` ([[item-artemis-missiles]]), `MISSILES_3` (Hermes),
  `MISSILES_BURST` (Pegasus), `MISSILES_BREACH` ([[item-breach-missiles]]),
  `MISSILE_CHARGEGUN` (Swarm).
- **`WEAPONS_MISSILES_EVENTS`** ([[source-dlcblueprintsoverwrite]]) — identical membership,
  same seven blueprints.
- Note what is **absent**: bombs. [[item-fire-bomb]] and the other `<type>BOMB</type>`
  weapons consume missiles but are not members of either list.
- `MISSILES_HULL` (Hull Missile) is also absent from both lists despite being a missile.

## How To Get It
- Own any one of the seven listed launchers. See [[item-artemis-missiles]] and
  [[item-breach-missiles]] for the two with their own pages.

## Blue Options It Unlocks
- [[event-quest-mantis-invasion]] — `QUEST_MANTIS_INVASION`, `req="WEAPONS_MISSILES"`
- [[event-rock-live-mine]] — `ROCK_STARSHIP_MINE`, `req="WEAPONS_MISSILES"`
- [[event-asteroid-mining-colony]] — `HELP_MINERS`, `req="WEAPONS_MISSILES_EVENTS"` — the only use of the second list

## Strategy Notes
- Carrying a Leto (the weakest launcher in the game) satisfies these gates exactly as well
  as carrying a Breach Missile. For blue-option purposes any missile is any other missile.
- Two lists with identical membership, one in the base data and one in the DLC overwrite
  file, is the sort of duplication worth flagging rather than resolving — see below.

## Related
- [[item-artemis-missiles]] / [[item-breach-missiles]] — members with their own pages
- [[item-ion-weapons]] / [[item-beam-weapons]] — the sibling category gates
- [[item-fire-bomb]] — consumes missiles but is **not** a member

## Open Questions
- [ ] Why `WEAPONS_MISSILES_EVENTS` exists as a duplicate of `WEAPONS_MISSILES` with identical membership, and whether the AE overwrite changes either list's behaviour.
- [ ] Why `MISSILES_HULL` is excluded from both lists.

## Sources
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
