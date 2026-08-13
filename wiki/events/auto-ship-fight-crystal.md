---
id: event-auto-ship-fight-crystal
type: event
event_name: CRYSTAL_AUTO
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, auto-ship, no-choices]
---

# Auto-ship fight (Crystal) — `CRYSTAL_AUTO`

## Summary
The one Rebel *automated* ship in [[sector-hidden-crystal-worlds]]. It is a plain forced
fight with no choices and no surrender, and because the enemy is an auto-ship it has no
crew — boarding and anti-personnel weapons do nothing, and mind control/hacking targets
are limited.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **7** entries in the `HOSTILE_CRYSTAL` event list, which the sector
  allocates `min=6 max=10` times ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — once it has fired it is removed from the pool for the rest of the run
  ([[source-events-xml]])
- Beacon: shows a **ship** on Long-Range Scanners ([[source-fandom-auto-ship-fight-crystal]])

## Text
> The Rebels must have sent their automated scouts to find you. One jumps in and
> immediately moves to attack.

(`event_CRYSTAL_AUTO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<ship load="REBEL_AUTO" hostile="true"/>` → immediate combat against a Rebel auto-ship | 100% |

On victory the Fandom page reports *"The ship explodes, leaving behind a substantial
collection of useful scrap material."* and **medium scrap with resources**
([[source-fandom-auto-ship-fight-crystal]]). The reward is defined on the shared
`REBEL_AUTO` ship entry in `events_ships.xml`, not on this event
([[source-events-xml]]).

## Blue Options
- None.

## Rewards & Risks
- **Reward:** medium scrap with resources on destruction
  ([[source-fandom-auto-ship-fight-crystal]]).
- **Risk:** an unavoidable fight. There is no "leave" choice and no surrender branch on
  `REBEL_AUTO`, so the only exits are destroying it or jumping away.
- Auto-ships have no crew, so a boarding-based ship (Mantis-style) has to win this one
  with guns.

## Strategy Notes
- Flagged as one of the more forgiving beacons in a sector whose hostile pool is otherwise
  Crystal warships: an auto-ship's crew count is zero, so nothing can board *you* back.
  *(Opinion, inferred — no source states it.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-rebel-fight-crystal]] — the crewed Rebel equivalent in the same pool
- [[event-crystal-fight]] — the Crystal warship that dominates the same pool
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] The exact `REBEL_AUTO` ship blueprint list and its difficulty scaling in this sector
      (`events_ships.xml` line 355 defines it as `auto_blueprint="SHIPS_AUTO"`, not yet
      ingested in detail).
- [ ] Whether enemy strength here follows the Rock Homeworlds sector number as the rest of
      the sector does ([[source-fandom-ancient-device]] states that for the sector, not
      for this event specifically).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-auto-ship-fight-crystal]] (per raw/wiki/auto-ship-fight-crystal.md)
