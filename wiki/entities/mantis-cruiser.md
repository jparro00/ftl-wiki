---
id: entity-mantis-cruiser
type: entity
entity_kind: ship
hostility: friendly
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [player-ship, ship-unlock, mantis, boarding, teleporter, crew-kill]
---

# Mantis Cruiser — *The Gila Monster* (`PLAYER_SHIP_MANTIS`)

## Summary
The player ship awarded by [[chain-mantis-cruiser-unlock]]. In-game description:

> *"This warship is designed to enhance its crew for close combat missions."*
> ([[source-text-blueprints]], `ship_PLAYER_SHIP_MANTIS_desc`)

It is the boarding ship: it starts with a **Teleporter**, three Mantis, and only **Weapons 1**
— the lowest starting weapons power of any unlockable layout. The design intent is that you
win fights by killing crews, not hulls.

## Stats

From `<shipBlueprint name="PLAYER_SHIP_MANTIS">` ([[source-blueprints]]):

| Field | Value |
|---|---|
| Ship id | `2` (`<unlockShip id="2"/>`) |
| Hull | 30 |
| Reactor | **7** — the lowest of the five |
| Crew | **3 Mantis + 1 Engi** |
| Starting systems | Piloting 1, Doors 1, Oxygen 1, **Shields 2**, Engines 2, **Weapons 1**, Medbay 1, **Teleporter 1** |
| Starting weapons | `BOMB_1` (Small Bomb), `LASER_BURST_1` |
| Starting augment | [[item-mantis-pheromones]] (`CREW_STIMS`) |

**No Sensors at start** — the systemList gives it no `sensors` entry with `start="true"`,
which is worth knowing given how many blue options gate on Sensors level.

The crew composition is deliberate: 3 Mantis to board with, and 1 Engi to repair while they
are away. Mantis are the fastest and deadliest boarders and the **worst repairers** in the
game ([[entity-mantis]], [[entity-engi]]).

## Where They Appear
A player ship. In-fiction it belongs to the Mantis thief **KazaaakplethKilik** until you take
it from him; the ship you fight at that beacon is a separate blueprint.

## How To Get It
- [[chain-mantis-cruiser-unlock]] — [[event-legendary-thief-kazaaakplethkilik]] →
  [[event-mantis-named-thief-defeat]] → [[event-mantis-named-thief-stash]], in
  [[sector-mantis-homeworlds]], where `sectordata.xml` allocates the opening beacon at
  `min=1 max=1` — a guaranteed encounter.
- The in-game hint: *"The famous Mantis thief, KazaaakplethKilik, owns this ship. You'll have
  to 'convince' him to help you."* (`ship_PLAYER_SHIP_MANTIS_unlock`,
  [[source-text-blueprints]]).
- **The quotation marks are load-bearing.** The unlock fires from
  `MANTIS_NAMED_THIEF_DEFEAT`, which triggers only when you **kill the crew** rather than
  destroy the ship — destroying it ends the chain silently. This is the same inversion
  [[chain-rock-cruiser-unlock]] and [[chain-capture-the-ship]] use.

> ⚠️ **CONTRADICTION:** Fandom asserts an alternative unlock by winning a run with the Zoltan
> Cruiser. As with the other cruisers, `achievements.xml` records no unlock conditions
> ([[source-achievements]]), so this raw set cannot verify it. Recorded as Fandom-only — see
> [[event-legendary-thief-kazaaakplethkilik]].

## Traits
- **Boarding-first.** Weapons 1 cannot meaningfully damage a hull; the Teleporter is the
  primary weapon and the Small Bomb exists to soften a room before the Mantis arrive.
- **Reactor 7** means power is tight from the first jump — one of the sharper early
  constraints in the game.
- [[item-mantis-pheromones]] is a boarding augment, not a general one.
- Boarding is also how the ship *earns* rewards: `deadCrew` branches routinely pay a tier
  higher than `destroyed` ones across the event pool.

## Related
- [[chain-mantis-cruiser-unlock]] — how it is earned
- [[entity-mantis]] — the crew, and why they board well and repair badly
- [[entity-engi]] — the fourth crew member, and why they are aboard
- [[item-teleporter]], [[item-mantis-pheromones]]
- [[sector-mantis-homeworlds]]
- [[entity-rock-cruiser]], [[entity-stealth-cruiser]], [[entity-zoltan-cruiser]],
  [[entity-federation-cruiser]] — the other event-unlocked player ships

## Open Questions
- [ ] Layout B (`PLAYER_SHIP_MANTIS_2`) is defined in `blueprints.xml`; its unlock condition
      is not in this raw set.
- [ ] Whether Fandom's Zoltan-Cruiser-victory route exists — unverifiable from the game data.
- [ ] Whether the missing Sensors system is intentional or an artifact of the layout.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
