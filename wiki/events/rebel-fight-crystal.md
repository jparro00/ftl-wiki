---
id: event-rebel-fight-crystal
type: event
event_name: CRYSTAL_REBEL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat, rebel, no-choices]
---

# Rebel fight (Crystal) — `CRYSTAL_REBEL`

## Summary
A standard Rebel pursuit fight, reskinned for [[sector-hidden-crystal-worlds]]. No
choices, generic `REBEL` ship, default rewards — the plainest beacon in the sector's
hostile pool.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **7** entries in the `HOSTILE_CRYSTAL` event list, which the sector
  allocates `min=6 max=10` times ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — it can recur at several beacons in the same sector
  ([[source-events-xml]])
- Beacon: shows a **ship** on Long-Range Scanners ([[source-fandom-rebel-fight-crystal]])

## Text
> As soon as you arrive, a Rebel ship jumps in after you; they must be really hot on your
> tail.

(`event_CRYSTAL_REBEL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<ship load="REBEL" hostile="true"/>` → immediate combat against a generic Rebel ship, **default rewards** | 100% |

The `REBEL` ship entry carries both a surrender and an escape branch; the Fandom
transcription of that entry elsewhere in this batch gives 50% surrender at 3–4 hull
(30–40% threshold) and a 50% escape ([[source-fandom-crystal-chat]], footnote on the
shared `REBEL` ship). Those numbers belong to the ship, not to this event.

## Blue Options
- None.

## Rewards & Risks
- **Reward:** default rewards for a `REBEL` kill ([[source-fandom-rebel-fight-crystal]]).
- **Risk:** an unavoidable fight against a crewed Rebel warship in a sector where enemy
  strength scales to the Rock Homeworlds sector number
  ([[source-fandom-ancient-device]]) — i.e. potentially a late-game-strength ship.

## Strategy Notes
- Nothing to decide. The only lever is whether you can afford the fight before jumping in,
  and Long-Range Scanners will at least warn you a ship is present
  ([[source-fandom-rebel-fight-crystal]]).

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-auto-ship-fight-crystal]] — the uncrewed Rebel equivalent in the same pool
- [[event-rebel-ship-attacking-crystal-ship]] — a Rebel fight you can opt out of
- [[event-crystal-fight-choice]] — the other Rebel-adjacent neutral encounter
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What "default rewards" resolves to numerically for the generic `REBEL` ship
      (`events_ships.xml` not yet fully ingested).
- [ ] Whether this fight can advance the Rebel fleet (no `modifyPursuit` in the file, so
      apparently not).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-crystal]] (per raw/wiki/rebel-fight-crystal.md)
