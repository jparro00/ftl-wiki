---
id: event-auto-ship-fight
type: event
event_name: REBEL_AUTO
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, no-choice, no-crew, combat]
---

# Auto-ship fight — `REBEL_AUTO`

## Summary
The unmanned counterpart to [[event-rebel-fight]]: a Rebel automated scout engages on
arrival, no choices. Mechanically the cleanest fight in the game — the `REBEL_AUTO` ship
has **no crew**, so there is no surrender, no escape, and no boarding threat, but also no
crew to kill for the better `DEAD_CREW_DEFAULT` payout. The `REBEL_AUTO` ship definition
is reused as the enemy by many other events, and this event shares its entire text list
with [[event-auto-ship-warning]] and [[event-auto-bait]].

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-civilian-sector]], [[sector-federation-space]], [[sector-abandoned-sector]],
  [[sector-pirate-controlled-sector]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]].
- Beacon: hostile — a hostile ship is loaded on arrival.
- Event lists: `HOSTILE_REBEL` ([[source-events-rebel]]), `HOSTILE1`
  ([[source-newevents]]), `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_ZOLTAN`
  ([[source-events-zoltan]]), `HOSTILE_LANIUS` ([[source-dlcevents-anaerobic]]), plus the
  AE lists `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_PIRATE`,
  `OVERRIDE_HOSTILE_REBEL`, `OVERRIDE_HOSTILE_ZOLTAN` ([[source-dlceventsoverwrite]]).
- `HOSTILE_REBEL` is allocated `min=6 max=8` per Rebel sector ([[source-sector-data-xml]]).
- Not unique — recurs freely. Long-range scanners show a ship
  ([[source-fandom-auto-ship-fight]]).

## Text
Drawn from the `REBEL_AUTO` text list — **nine variants**, shared verbatim with
[[event-auto-ship-warning]] and [[event-auto-bait]]
([[source-events-rebel]], [[source-text-events-xml]]). Representative examples:

> You discover one of the Rebel's autonomous scouts. The ship's AI wastes no time in
> engaging your ship.

> Your ship is hailed: "This is an automated message. Resisting our takeover is pointless.
> Prepare to die." It appears this Rebel ship is run by an AI.

> A small shuttle appears on the local radar. Turns out it is a Rebel automated scout!

All nine are transcribed on [[source-fandom-auto-ship-fight]] and in
`raw/gamedata/text_events.xml` at `text_REBEL_AUTO_1` … `text_REBEL_AUTO_9`.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `<ship load="REBEL_AUTO" hostile="true"/>`. On destruction: *"The ship explodes, leaving behind a substantial collection of useful scrap material."* → `autoReward level="MED"` `standard`. | 100% |

### The `REBEL_AUTO` ship
`<ship name="REBEL_AUTO" auto_blueprint="SHIPS_AUTO">` — `destroyed` and `deadCrew` both
load the shared `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` lists, and **no surrender or
escape branch is defined** ([[source-events-ships]]). Auto-ships carry no crew, so the
`deadCrew` branch is unreachable in practice.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` `standard` — scrap with resources ([[source-fandom-auto-ship-fight]] gives
  the same reading).
- Risk: whatever the `SHIPS_AUTO` blueprint pool rolls for the sector depth. No boarding,
  no surrender to negotiate, no escape to chase. The fight ends only when the hull does.

## Strategy Notes
- Nothing to decide. Auto-ships are the safest forced fight of the Rebel pool — anti-personnel
  weapons, mind control and boarding are all dead weight against them, and conversely you
  cannot farm the better crew-kill reward.
- Distinguishing it from [[event-auto-ship-warning]] at the beacon is impossible: the intro
  texts are identical. The tell is the on-screen escape timer that `AUTO_WARNING` starts
  ([[source-fandom-auto-ship-warning]]).

## Related
- [[event-auto-ship-warning]] — same nine texts, but the ship runs for the fleet
- [[event-auto-bait]] — same nine texts, a trapped auto-ship (unreachable content)
- [[event-rebel-fight]] — the crewed counterpart
- [[event-deactivated-auto-ship]] — the same `REBEL_AUTO` ship, dormant
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Numeric value of `MED` `standard` at a given sector depth.
- [ ] Composition of the `SHIPS_AUTO` auto-blueprint pool.
- [ ] Whether the nine text variants are equally weighted.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-auto-ship-fight]] (per `raw/wiki/auto-ship-fight.md`)
