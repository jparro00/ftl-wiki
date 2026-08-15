---
id: entity-zoltan-cruiser
type: entity
entity_kind: ship
hostility: friendly
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [player-ship, ship-unlock, zoltan, super-shield, low-reactor, diplomacy]
---

# Zoltan Cruiser — *The Adjudicator* (`PLAYER_SHIP_ENERGY`)

## Summary
The player ship awarded by [[chain-zoltan-cruiser-unlock]]. In-game description:

> *"The Zoltan's advanced shields technology gives this ship an edge during each battle."*
> ([[source-text-blueprints]], `ship_PLAYER_SHIP_ENERGY_desc`)

Its defining feature is the **Zoltan super-shield**, a free absorbing layer at the start of
every fight, paid for with the **lowest reactor in the game** — 5 power, against 7–8 for the
others. Its internal id is `ENERGY`, not `ZOLTAN`, which is worth knowing when grepping the
files.

## Stats

From `<shipBlueprint name="PLAYER_SHIP_ENERGY">` ([[source-blueprints]]):

| Field | Value |
|---|---|
| Ship id | `5` (`<unlockShip id="5"/>`) |
| Hull | 30 |
| Reactor | **5** — the lowest of any player ship |
| Crew | **3 Zoltan** |
| Starting systems | Piloting 1, **Doors 2**, Sensors 1, Oxygen 1, **Engines 1**, **Shields 2**, **Weapons 3**, Medbay 1 |
| Starting weapons | `BEAM_2` (Halberd Beam), `MISSILES_1` (Leto) |
| Starting augment | [[item-zoltan-shield]] (`ENERGY_SHIELD`) |

**Reactor 5 with Weapons 3 and Engines 1** is the whole design in three numbers: the ship can
fire a Halberd Beam from turn one and can barely dodge anything. The Zoltan crew partially
compensate — each Zoltan supplies **1 power to the room they occupy** ([[entity-zoltan]]), so
the crew are themselves part of the reactor.

## Where They Appear
A player ship. Zoltan warships met as enemies are a different blueprint family; the
[[entity-zoltan]] page covers those.

## How To Get It
- [[chain-zoltan-cruiser-unlock]] — [[event-unarmed-zoltan-transport]] →
  [[event-zoltan-peace-quest2]], in [[sector-zoltan-homeworlds]], where the opening beacon is
  guaranteed.
- The in-game hint: *"Learn from the Zoltan that sometimes diplomacy works."*
  (`ship_PLAYER_SHIP_ENERGY_unlock`, [[source-text-blueprints]]) — a direct statement of the
  chain's win condition. Step 2 looks like a Rebel ambush and is a **test**: exactly one
  choice passes it, and shooting is not it.

## Traits
- **The Zoltan super-shield** absorbs a fixed number of hits at the start of every engagement,
  before regular shields, and does not regenerate within the fight. It makes the first seconds
  of every fight free and the rest of it ordinary.
- **Reactor 5** forces hard power triage from the first jump — the tightest opening economy of
  any layout.
- **Zoltan crew are fragile** and die to boarders quickly, but each one powers the room it
  stands in.
- **Doors 2 at the start** is unusual and pairs with the fragile crew: venting is a better
  answer to boarders than fighting them.

## Related
- [[chain-zoltan-cruiser-unlock]] — how it is earned
- [[entity-zoltan]] — the crew, the power trait, and the super-shield in enemy hands
- [[item-zoltan-shield]] — the starting augment
- [[chain-zoltan-primitives]] — the other Zoltan quest line, also about non-interference
- [[sector-zoltan-homeworlds]]
- [[entity-rock-cruiser]], [[entity-stealth-cruiser]], [[entity-mantis-cruiser]],
  [[entity-federation-cruiser]] — the other event-unlocked player ships

## Open Questions
- [ ] Layout B (`PLAYER_SHIP_ENERGY_2`) is defined in `blueprints.xml`; its unlock condition
      is not in this raw set.
- [ ] How many layers the starting Zoltan super-shield provides — the augment is named in
      `blueprints.xml` but its magnitude is not recorded on this page's sources.
- [ ] Whether Fandom's alternative unlock routes for this ship exist — as with the others,
      `achievements.xml` holds no unlock conditions.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
