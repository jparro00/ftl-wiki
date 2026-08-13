---
id: event-auto-ship-fight-near-sun
type: event
event_name: AUTO_SUN
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, auto-ship, no-choice, no-crew, combat, sun-hazard, unique]
---

# Auto-ship fight near sun — `AUTO_SUN`

## Summary
The sun-hazard twin of [[event-auto-ship-fight-in-asteroid-field]], and the more dangerous
of the two: a crewless Rebel scout that is explicitly *"impervious to the heat"* fights you
next to a star, where solar flares set **your** rooms on fire and not its. No choices, no
surrender, no escape. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]]
- Event lists: `HOSTILE_CIVILIAN` ([[source-newevents]]), allocated `min=4 max=6` in both
  `STANDARD_SPACE` and `CIVILIAN_SECTOR` ([[source-sector-data-xml]]); also listed in the AE
  pool `OVERRIDE_HOSTILE2` ([[source-dlceventsoverwrite]])
- **The `OVERRIDE_HOSTILE2` route looks dead.** There is no `HOSTILE2` `<eventList>`
  anywhere in `raw/gamedata/`, and `HOSTILE2` is allocated only inside the
  `<eventCounts sector="N">` blocks of `newEvents.xml` — which have no counterpart in
  `sector_data.xml` and one of which is headed *"PLANNING FOR the 3rd Sector"*
  ([[source-newevents]], [[source-sector-data-xml]]). Whether the engine reads those blocks
  is not established here. The live route is `HOSTILE_CIVILIAN`.
- Beacon: hostile — `<ship load="REBEL_AUTO" hostile="true"/>` plus
  `<environment type="sun"/>` on arrival
- Long-range scanners show a ship and the red giant
  ([[source-fandom-auto-ship-fight-near-sun]], `LRSmap=ship+redgiant`)
- `unique="true"` — once per run, unlike its asteroid sibling ([[source-events-xml]])

## Text
> You arrive at the beacon to find yourself dangerously close to a star. An automated Rebel
> ship, impervious to the heat, moves in to engage.

(`event_AUTO_SUN_text`, per [[source-text-events-xml]]. Fandom transcribes it identically.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `REBEL_AUTO` inside `<environment type="sun"/>`. On destruction: *"The ship explodes, leaving behind a substantial collection of useful scrap material."* → `autoReward level="MED"` `standard`. | 100% |

### The `REBEL_AUTO` ship
`auto_blueprint="SHIPS_AUTO"`; `destroyed` and `deadCrew` load the shared defaults; **no
`<surrender>`, no `<escape>`** ([[source-events-ships]]). No crew means the `deadCrew`
payout is unreachable.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` `standard` — scrap with resources.
- Risk: the sun hazard. The flavour text says the auto-ship is *impervious to the heat*, and
  the event models the hazard with a single `<environment type="sun"/>` tag with no
  compensating effect on the enemy — so, unlike the asteroid variant, the environment here
  is a **one-sided** penalty against you. Nothing in the files states an asymmetric damage
  rule, so treat the "one-sided" reading as flavour-supported, not file-proven.

## Strategy Notes
- *(Opinion.)* This is the auto-ship fight you most want to end fast. Fires spread while you
  are shooting at a target that cannot be boarded, mind-controlled or persuaded to
  surrender, and every second of the fight costs oxygen and crew health.
- Same dead-weight caveat as every auto-ship: anti-personnel weapons and boarding parties do
  nothing.

## Version Differences
Base-`events.xml` event, no DLC-marked tags — identical in both editions
([[source-events-xml]]). Its `HOSTILE_CIVILIAN` list is not redefined by
`dlcEventsOverwrite.xml`, so the pool is the same too; only the (apparently unused)
`OVERRIDE_HOSTILE2` membership is AE-side ([[source-dlceventsoverwrite]]).

## Related
- [[event-auto-ship-fight-in-asteroid-field]] — the asteroid-hazard twin, `AUTO_ASTEROID`
- [[event-auto-ship-fight]] — the plain version
- [[event-pirate-fight-near-sun]], [[event-mantis-fight-near-sun]] — crewed fights at the
  same hazard
- [[event-boarders-humans-near-sun]] — the sun hazard with boarders instead of a ship
- [[concept-rebel-fleet-advance]], [[sector-civilian-sector]], [[sector-federation-space]]

## Open Questions
- [ ] Numeric value of `MED` `standard` at a given sector depth.
- [ ] Does the engine read `<eventCounts sector="N">` in `newEvents.xml`? If not,
      `OVERRIDE_HOSTILE2` is an orphan list.
- [ ] Is the auto-ship mechanically immune to solar flares, or only narratively? No tag in
      the files distinguishes it.

> ⚠️ **CONTRADICTION (sector list):** [[sector-federation-space]].
> - Game files: `HOSTILE_CIVILIAN` is allocated `min=4 max=6` in `STANDARD_SPACE` =
>   *Federation Space* ([[source-sector-data-xml]], [[source-text-sectorname-xml]]).
> - Fandom: Civilian Sector only ([[source-fandom-auto-ship-fight-near-sun]]).
>
> Trusting the game files; the same omission recurs across Fandom's generic-hostile pages
> and reads as a wiki convention.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `HOSTILE_CIVILIAN`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml` — `OVERRIDE_HOSTILE2`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-text-sectorname-xml]] (per `raw/gamedata/text_sectorname.xml`)
- [[source-fandom-auto-ship-fight-near-sun]] (per `raw/wiki/auto-ship-fight-near-sun.md`)
