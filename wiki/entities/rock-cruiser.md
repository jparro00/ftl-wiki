---
id: entity-rock-cruiser
type: entity
entity_kind: ship
hostility: friendly
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [player-ship, ship-unlock, rock, missiles, fire-immune]
---

# Rock Cruiser — *Bulwark* (`PLAYER_SHIP_ROCK`)

## Summary
The player ship awarded by [[chain-rock-cruiser-unlock]]. In-game description:

> *"Similar to its designers, this super-dense behemoth uses brute force to overwhelm its
> foes."* ([[source-text-blueprints]], `ship_PLAYER_SHIP_ROCK_desc`)

It is the missile ship: it starts with **two missile launchers and no beam or laser**, and its
all-Rock crew cannot be burned. It is also the only starting layout that begins with
**Rock Plating** already installed.

## Stats

From `<shipBlueprint name="PLAYER_SHIP_ROCK">` ([[source-blueprints]]):

| Field | Value |
|---|---|
| Ship id | `6` (`<unlockShip id="6"/>`) |
| Hull | 30 |
| Reactor | 8 |
| Crew | **3 Rock** |
| Starting systems | Piloting 1, Doors 1, Sensors 1, Oxygen 1, **Engines 2**, **Shields 2**, **Weapons 3**, Medbay 1 |
| Starting weapons | `MISSILES_2_PLAYER`, `MISSILES_HULL` |
| Starting augment | [[item-rock-plating]] (`ROCK_ARMOR`) |
| Starting drones | none |

**Weapons 3 with two missile launchers** is an unusually front-loaded weapons system, and the
reason the ship plays as a burst-damage platform that runs out of ammunition rather than a
sustained-fire one.

> ⚠️ **`MISSILES_2_PLAYER` vs `MISSILES_2`.** The two share a display name but have different
> stats — one of the shipped data quirks recorded in `overview.md`'s known-bugs list. The
> player variant is the one installed here.

## Where They Appear
Not an encounter — this is a **player ship**, and it appears in the game data only as a
blueprint and an `<unlockShip>` target. The Rockmen who field it in-fiction are
[[entity-rock-men]], whose warships are a different blueprint family (`SHIPS_ROCK`).

## How To Get It
- [[chain-rock-cruiser-unlock]] — [[event-rock-unlock1]] → [[event-rock-unlock2]] →
  [[event-rock-unlock3]], in [[sector-rock-homeworlds]]. The step-2 duel must be **survived,
  not won**.
- The in-game hint reads *"Prove yourself to the Rockmen to earn this powerful cruiser."*
  (`ship_PLAYER_SHIP_ROCK_unlock`, [[source-text-blueprints]]) — describing this chain and no
  other route.

> ⚠️ **CONTRADICTION:** Fandom states the Rock Cruiser is *also* unlocked by winning a run
> with the Slug Cruiser. `achievements.xml` records **no unlock conditions at all**
> ([[source-achievements]]), and `text_achievements.xml` carries only prose descriptions, so
> this raw set cannot check the claim. Recorded as Fandom-only — see
> [[chain-rock-cruiser-unlock]].

## Traits That Follow From The Crew
Its crew are [[entity-rock-men]]: **immune to fire**, high health, slow movement. Practical
consequences —

- Fires are a repair job rather than an emergency; the crew can stand in a burning room.
- Boarding actions are strong on offence and slow to redeploy on defence.
- The sun and solar-flare hazards that make [[event-rock-unlock2]] dangerous are much less
  dangerous *in* this ship than in the one that earns it.

## Related
- [[chain-rock-cruiser-unlock]] — how it is earned
- [[entity-rock-men]] — the crew and the faction
- [[item-rock-plating]] — its starting augment
- [[sector-rock-homeworlds]] — where the chain runs
- [[entity-stealth-cruiser]], [[entity-mantis-cruiser]], [[entity-zoltan-cruiser]],
  [[entity-federation-cruiser]] — the other event-unlocked player ships

## Open Questions
- [ ] Layout B (`PLAYER_SHIP_ROCK_2`, *Shivan*) is defined in `blueprints.xml` but its unlock
      condition is not in this raw set.
- [ ] Whether Fandom's Slug-Cruiser-victory route exists — unverifiable from the game data.
- [ ] The exact stats of `MISSILES_2_PLAYER` versus `MISSILES_2`.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
