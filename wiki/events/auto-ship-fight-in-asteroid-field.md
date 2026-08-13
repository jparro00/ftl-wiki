---
id: event-auto-ship-fight-in-asteroid-field
type: event
event_name: AUTO_ASTEROID
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
tags: [rebel, auto-ship, no-choice, no-crew, combat, asteroid-field]
---

# Auto-ship fight in asteroid field — `AUTO_ASTEROID`

## Summary
[[event-auto-ship-fight]] with rocks. A crewless Rebel scout engages on arrival inside an
asteroid field; there are no choices and no way out but the fight. The asteroid environment
cuts both ways — it batters the auto-ship as well as you — and because the target has no
crew there is no surrender, no escape and no boarding. **Not `unique`**, so it can recur.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]]
- Event lists: `HOSTILE_REBEL` ([[source-events-rebel]]), `HOSTILE_MANTIS`
  ([[source-events-mantis]]), `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE1`
  ([[source-newevents]]), plus the AE replacements `OVERRIDE_HOSTILE1`,
  `OVERRIDE_HOSTILE_MANTIS`, `OVERRIDE_HOSTILE_PIRATE`, `OVERRIDE_HOSTILE_REBEL`
  ([[source-dlceventsoverwrite]])
- Allocation: `HOSTILE_REBEL` 6–8 in both Rebel sectors, `HOSTILE_MANTIS` 6–7 in both Mantis
  sectors, `HOSTILE_PIRATE` 6–8 in Pirate space, `HOSTILE1` 2–2 in both `STANDARD_SPACE` and
  `CIVILIAN_SECTOR` ([[source-sector-data-xml]])
- **It is commented out of `HOSTILE_CIVILIAN`** — `<!-- <event load="AUTO_ASTEROID"/> -->`
  in `newEvents.xml`, so the 4–6 civilian hostile beacons never draw it; the civilian route
  is `HOSTILE1` only ([[source-newevents]])
- Beacon: hostile — `<ship load="REBEL_AUTO" hostile="true"/>` plus
  `<environment type="asteroid"/>` fire on arrival
- Background is forced: `<img back="BG_DARK" planet="NONE"/>` ([[source-events-xml]])
- Long-range scanners show a ship **and** the asteroid field
  ([[source-fandom-auto-ship-fight-in-asteroid-field]], `LRSmap=ship+asteroidfield`)

## Text
> You arrive in an asteroid belt to discover that a Rebel automated-scout has been stationed
> here. Prepare for a fight!

(`event_AUTO_ASTEROID_text`, per [[source-text-events-xml]]. Fandom transcribes it
identically.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `REBEL_AUTO` inside `<environment type="asteroid"/>`. On destruction: *"The ship explodes, leaving behind a substantial collection of useful scrap material."* → `autoReward level="MED"` `standard`. | 100% |

### The `REBEL_AUTO` ship
`<ship name="REBEL_AUTO" auto_blueprint="SHIPS_AUTO">` — `destroyed` and `deadCrew` load
`DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`, and there is **no `<surrender>` and no
`<escape>`** ([[source-events-ships]]). Auto-ships carry no crew, so the `deadCrew` branch
and its better payout are unreachable in practice.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` `standard` — scrap with resources. Fandom reads it the same way
  ([[source-fandom-auto-ship-fight-in-asteroid-field]]).
- Risk: continuous asteroid impacts on **both** hulls for the length of the fight, on top of
  whatever `SHIPS_AUTO` rolls for the sector depth. No boarders, no surrender to negotiate,
  no escape to chase.

## Strategy Notes
- *(Opinion.)* The asteroid field is close to neutral here: it damages the auto-ship as much
  as you, and a Defense Drone turns it strongly in your favour. Against an auto-ship, which
  cannot be boarded or mind-controlled, the drone is one of the few tools that helps.
- Anti-personnel weapons, boarding parties and mind control are all dead weight — same as
  [[event-auto-ship-fight]].

## Version Differences
Base-`events.xml` event with no DLC-marked tags, so the encounter is identical in both
editions ([[source-events-xml]]). What differs is the **pool**: `OVERRIDE_HOSTILE1`,
`OVERRIDE_HOSTILE_MANTIS`, `OVERRIDE_HOSTILE_PIRATE` and `OVERRIDE_HOSTILE_REBEL` replace
the vanilla lists under AE and each adds pulsar events, so the odds of drawing this
particular beacon differ ([[source-dlceventsoverwrite]]).

## Related
- [[event-auto-ship-fight]] — the plain version, same ship
- [[event-auto-ship-fight-near-sun]] — the sun-hazard sibling, `AUTO_SUN`
- [[event-auto-ship-fight-in-nebula]], [[event-auto-ship-fight-in-plasma-storm]] — the other
  environment variants
- [[event-pirate-fight-in-asteroid-field]] — the crewed asteroid-field fight
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Numeric value of `MED` `standard` at a given sector depth.
- [ ] Composition of the `SHIPS_AUTO` auto-blueprint pool.
- [ ] Why `AUTO_ASTEROID` was commented out of `HOSTILE_CIVILIAN` while `AUTO_SUN` was left
      in. Nothing in the files says.

> ⚠️ **CONTRADICTION (sector list):** [[sector-federation-space]].
> - Game files: `HOSTILE1`, which contains `AUTO_ASTEROID`, is allocated `min=2 max=2` in
>   `STANDARD_SPACE` = *Federation Space* ([[source-newevents]], [[source-sector-data-xml]],
>   [[source-text-sectorname-xml]]).
> - Fandom: its location list gives Civilian, Mantis ×2, Pirate and Rebel ×2 — no Federation
>   Space ([[source-fandom-auto-ship-fight-in-asteroid-field]]).
>
> Trusting the game files. The same omission appears on Fandom's pages for other generic
> hostile events, so it looks like a wiki convention rather than a claim about this event.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml` — `HOSTILE_REBEL`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml` — `HOSTILE_MANTIS`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml` — `HOSTILE_PIRATE`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `HOSTILE1`, `HOSTILE_CIVILIAN`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-auto-ship-fight-in-asteroid-field]] (per `raw/wiki/auto-ship-fight-in-asteroid-field.md`)
