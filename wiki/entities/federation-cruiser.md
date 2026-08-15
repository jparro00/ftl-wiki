---
id: entity-federation-cruiser
type: entity
entity_kind: ship
hostility: friendly
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [player-ship, ship-unlock, federation, artillery, mixed-crew, miniboss]
---

# Federation Cruiser — *The Osprey* (`PLAYER_SHIP_FED`)

## Summary
The player ship awarded by [[event-rebel-shipyard]], the miniboss beacon in
[[sector-rebel-stronghold]]. In-game description:

> *"This ship features the latest in Federation technology: an advanced beam weapon that
> pierces through shields."* ([[source-text-blueprints]], `ship_PLAYER_SHIP_FED_desc`)

It is the only player ship with an **Artillery Beam** — a fixed, unaimable system weapon that
charges slowly and ignores shields entirely — and the only one that starts with **one crew
member of four different species**.

## Stats

From `<shipBlueprint name="PLAYER_SHIP_FED">` ([[source-blueprints]]):

| Field | Value |
|---|---|
| Hull | 30 |
| Reactor | 8 |
| Crew | **1 human, 1 Mantis, 1 Rock, 1 Engi** — four species, four sets of traits |
| Starting systems | Piloting 1, Doors 1, Sensors 1, Oxygen 1, Engines 2, Shields 2, Weapons 2, Medbay 1 |
| **Artillery** | `<artillery power="1" room="6" weapon="ARTILLERY_FED"/>` — a system, not a weapon slot |
| Starting weapons | `LASER_BURST_3` |
| Starting augments | **none** |

**The Artillery Beam is a system.** It occupies its own room, draws reactor power, can be
damaged and repaired like any system, and fires automatically on a long cooldown. It cannot be
sold, cannot be aimed, and does not compete for weapon slots — see [[item-artillery-beam]].

## Where They Appear
A player ship. The Federation fleet's *other* hulls (`FED_SCOUT`, `FED_BOMBER`) are separate
blueprints and are covered on [[entity-federation]] — which also carries the naming note that
event pages linking `entity-federation-cruiser` mean this hull rather than the faction.

## How To Get It
- [[event-rebel-shipyard]] (`FLAGSHIP_CONSTRUCTION`) — a **guaranteed beacon** in
  [[sector-rebel-stronghold]], where you can fight a second, unfinished Rebel Flagship.
- The in-game hint: *"There have been rumors of advanced ship construction in the Rebel
  Stronghold…"* (`ship_PLAYER_SHIP_FED_unlock`, [[source-text-blueprints]]).
- It is the only ship unlock that is not a multi-beacon quest chain — one beacon, one very
  hard fight.

## Traits
- **Four species, one of each.** The crew is a toolkit rather than a specialisation: a Rock who
  can stand in fires, an Engi who repairs fastest, a Mantis who boards, and a human who levels
  up fastest. It is also the most awkward crew to lose members from, since each loss removes a
  capability outright.
- **Artillery fires whether you do or not**, which makes the ship strong in long fights and
  against high-shield targets, and does nothing to help it win short ones.
- No starting augment — the only unlockable layout with an empty augment slate.

## Related
- [[event-rebel-shipyard]] — the miniboss that unlocks it
- [[item-artillery-beam]] — its defining system
- [[entity-federation]] — the faction, and the naming note
- [[chain-the-flagship]] — the Flagship this ship's prototype opponent is a copy of
- [[sector-rebel-stronghold]]
- [[entity-rock-cruiser]], [[entity-stealth-cruiser]], [[entity-mantis-cruiser]],
  [[entity-zoltan-cruiser]] — the other event-unlocked player ships

## Open Questions
- [ ] Layout B (`PLAYER_SHIP_FED_2`) is defined in `blueprints.xml`; its unlock condition is
      not in this raw set.
- [ ] `ARTILLERY_FED`'s charge time and damage — the weapon blueprint is not summarised here.
- [ ] Whether the unfinished Flagship at [[event-rebel-shipyard]] can be avoided while still
      unlocking the ship.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
