---
id: event-rebel-ship-warning
type: event
event_name: SQUAT_WARNING
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, unique, no-choice, timed-escape, fleet-advance-risk]
---

# Rebel ship warning — `SQUAT_WARNING`

## Summary
The crewed twin of [[event-auto-ship-warning]]: a Rebel forward scout that is already
charging its FTL when you arrive. Kill it inside the window for a `MED` payout, or let it
jump and pay a fleet-pursuit advance. Unlike the auto-ship version, this one has a crew —
so a boarding kill is on the table and pays the same as a hull kill.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]].
- Beacon: hostile.
- Event lists: `HOSTILE_REBEL` ([[source-events-rebel]]), `HOSTILE_ENGI`
  ([[source-events-engi]]), `HOSTILE1` and `HOSTILE_CIVILIAN` ([[source-newevents]]), plus
  the AE lists `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`,
  `OVERRIDE_HOSTILE_REBEL` ([[source-dlceventsoverwrite]]).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-rebel-ship-warning]]).

## Text
> You stumble across a forward scout of the Rebel fleet.

(`event_SQUAT_WARNING_text`, per [[source-text-events-xml]]) — a single fixed string, in
contrast to the nine-variant list used by [[event-auto-ship-warning]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Combat with `<ship load="SQUAT_WARNING" hostile="true"/>`, already escaping. Destroy it or kill the crew → `autoReward level="MED"` `standard`. It gets away → `modifyPursuit amount="1"`. | 100% |

### The `SQUAT_WARNING` ship
`auto_blueprint="SHIPS_REBEL"`, `<escape timer="40" min="22" max="22">`
([[source-events-ships]]):

- **Escape text:** *"They are powering up their FTL! If they get away, they will no doubt
  warn the fleet of your position!"*
- **`gotaway`:** *"The scout jumps away. They are sure to have informed the fleet of your
  position. You must get to the next Sector as soon as possible!"* →
  `<modifyPursuit amount="1"/>`.
- **`destroyed`:** *"Their ship breaks apart and you are relieved to know that you are
  still one step ahead of the fleet."* → `autoReward level="MED"` `standard`.
- **`deadCrew`:** *"Their ship goes silent and you are relieved to know that you are still
  one step ahead of the fleet."* → `autoReward level="MED"` `standard` — the same payout,
  unusually; most ships pay more for a crew kill.
- **No surrender branch** — confirmed by both the file and
  [[source-fandom-rebel-ship-warning]].

> ⚠️ **CONTRADICTION:** as on [[event-auto-ship-warning]],
> [[source-fandom-rebel-ship-warning]] renders the `gotaway` penalty as *"Rebel Fleet
> pursuit is **doubled**"* while the file states `<modifyPursuit amount="1"/>`
> ([[source-events-ships]]). Trusting the game files for the raw value; what one
> `modifyPursuit` step means in play is an open question.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` `standard` on either kill path — better than [[event-auto-ship-warning]]'s
  `LOW`, presumably because a crewed Rebel warship is a harder target than an auto-scout.
- Risk: fleet advance if it escapes. No hull-damage twist beyond the fight itself.

## Strategy Notes
- *(Opinion.)* Because `deadCrew` pays the same as `destroyed`, there is no reward
  incentive to board — take whichever kill is fastest, since the clock, not the payout, is
  the binding constraint.
- Same 40-unit timer as [[event-auto-ship-warning]] but a longer `min`/`max` escape window
  is not granted — this is a burst-damage check.

## Related
- [[event-auto-ship-warning]] — the unmanned equivalent, `LOW` reward
- [[event-rebel-fight]] — the untimed Rebel fight
- [[event-rebel-transport-ship]] — the other `SQUAT_*` runner, with far better loot
- [[concept-rebel-fleet-advance]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What one `modifyPursuit amount="1"` step costs in play.
- [ ] Numeric value of `MED` `standard` at a given sector depth.
- [ ] Why `deadCrew` and `destroyed` pay identically here when most Rebel ships differ.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-rebel-ship-warning]] (per `raw/wiki/rebel-ship-warning.md`)
