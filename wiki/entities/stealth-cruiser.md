---
id: entity-stealth-cruiser
type: entity
entity_kind: ship
hostility: friendly
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [player-ship, ship-unlock, cloaking, no-shields, engi-built, glass-cannon]
---

# Stealth Cruiser — *The Nesasio* (`PLAYER_SHIP_STEALTH`)

## Summary
The player ship awarded by [[chain-stealth-cruiser-unlock]]. In-game description:

> *"Constructed for the Federation by the Engi, this ship is designed to use cloaking
> technology and speed to get behind enemy lines."* ([[source-text-blueprints]],
> `ship_PLAYER_SHIP_STEALTH_desc`)

It is the game's glass cannon and the only unlockable layout that **starts with no shields at
all**. In exchange it begins with Cloaking installed, Engines 4, Sensors 2 and two augments.

## Stats

From `<shipBlueprint name="PLAYER_SHIP_STEALTH">` ([[source-blueprints]]):

| Field | Value |
|---|---|
| Ship id | `1` (`<unlockShip id="1"/>`) |
| Hull | 30 |
| Reactor | 8 |
| Crew | **3 human** |
| Starting systems | Piloting 1, Doors 1, **Sensors 2**, Oxygen 1, **Engines 4**, **Weapons 2**, Medbay 1, **Cloaking 1** |
| **Shields** | **`start="false"` — the room exists, the system does not** |
| Starting weapons | `BEAM_1` (Mini Beam), `LASER_BURST_2` |
| Starting augments | [[item-titanium-system-casing]] (`SYSTEM_CASING`), [[item-long-ranged-scanners]] (`ADV_SCANNERS`) |

**Engines 4 at the start is the highest of any unlockable layout**, and with no shields it is
the ship's entire defence: evasion plus cloak uptime.

## Where They Appear
A player ship only. It is built by the Engi ([[entity-engi]]) for the Federation
([[entity-federation]]), and the unlock chain is the story of that construction — but the hull
never appears as an enemy.

## How To Get It
- [[chain-stealth-cruiser-unlock]] — `ENGI_UNLOCK_1` → `2REAL`/`2FAKE` → `3` → `4`, beginning
  at [[event-engi-fleet-discussion]] in [[sector-engi-homeworlds]].
- The in-game hint: *"This ship is being built near the Engi homeworlds. To unlock it you'll
  need to help them, but they only trust their own kind."* (`ship_PLAYER_SHIP_STEALTH_unlock`,
  [[source-text-blueprints]]) — *"they only trust their own kind"* is the **Engi crew
  requirement** on the opening beacon.

**This hint is what settled a naming confusion in this wiki.** `ENGI_UNLOCK_1→4` awards
`<unlockShip id="1"/>`, and id 1 is the *Stealth* Cruiser, not the Engi Cruiser — the Engi
Cruiser is an achievement unlock (*"get to the 5th sector with any layout of the Kestrel"*)
with no event chain at all. See [[chain-stealth-cruiser-unlock]].

## Traits
- **No shields at start.** Every hit that connects is a hull hit until you buy and power a
  shield system.
- **Cloaking from the first beacon** — the only layout that begins with it, and the reason the
  ship can win fights it could not survive otherwise.
- **Sensors 2 plus [[item-long-ranged-scanners]]** makes it the best-informed starting ship in
  the game, which matters for the several events gated on Sensors level — see
  [[chain-hidden-federation-base]].
- [[item-titanium-system-casing]] mitigates the fragility slightly by deflecting system damage.

## Related
- [[chain-stealth-cruiser-unlock]] — how it is earned
- [[entity-engi]] — its builders, and the crew requirement on the chain
- [[item-long-ranged-scanners]], [[item-titanium-system-casing]] — its augments
- [[item-cloaking]] — its defining system
- [[entity-rock-cruiser]], [[entity-mantis-cruiser]], [[entity-zoltan-cruiser]],
  [[entity-federation-cruiser]] — the other event-unlocked player ships

## Open Questions
- [ ] Layout B (`PLAYER_SHIP_STEALTH_2`) is defined in `blueprints.xml`; its unlock condition
      is not in this raw set.
- [ ] Whether the shields room can be fitted at a store on the same terms as any other system.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
