---
id: event-auto-ship-warning
type: event
event_name: AUTO_WARNING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, auto-ship, unique, no-choice, timed-escape, fleet-advance-risk]
---

# Auto-ship warning — `AUTO_WARNING`

## Summary
An auto-ship fight on a clock. Identical intro text to [[event-auto-ship-fight]], but the
enemy is running its FTL drive: if it escapes, the Rebel fleet pursuit is advanced. You
have a fixed window to kill it. One of the few random events that can actively cost you
map time.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]].
- Beacon: hostile.
- Event lists: `HOSTILE_REBEL` ([[source-events-rebel]]), `HOSTILE_MANTIS`
  ([[source-events-mantis]]), `HOSTILE1` ([[source-newevents]]), and the AE lists
  `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE_MANTIS`, `OVERRIDE_HOSTILE_REBEL`
  ([[source-dlceventsoverwrite]]).
- `unique="true"` — at most once per run.
- Long-range scanners show a ship ([[source-fandom-auto-ship-warning]]).

## Text
Shares the `REBEL_AUTO` text list with [[event-auto-ship-fight]] and [[event-auto-bait]] —
**nine variants**, so the prose gives you no warning that this is the timed version
([[source-events-rebel]], [[source-text-events-xml]]). Examples:

> The AI of a nearby small Rebel scout immediately identifies you as a threat and engages.

> This beacon is being patrolled by a unmanned scout. A fight is unavoidable.

All nine are listed on [[event-auto-ship-fight]] and [[source-fandom-auto-ship-warning]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Combat with `<ship load="REBEL_AUTO_WARNING" hostile="true"/>`, which is already trying to escape. Kill it → `autoReward level="LOW"` `standard`. Let it get away → `modifyPursuit amount="1"`. | 100% |

### The `REBEL_AUTO_WARNING` ship
`auto_blueprint="SHIPS_AUTO"`, with an `<escape timer="40" min="22" max="22">` branch
([[source-events-ships]]):

- **Escape starts immediately.** The escape event fires at once and the ship's FTL charges
  over the timer window: *"The ship starts to power up its FTL Drive. If it gets away, it
  will no doubt warn the fleet of your position!"*
- **`gotaway`** — *"The scout jumps away. It will certainly have informed the fleet of your
  position. You must get to the next sector as soon as possible!"* →
  `<modifyPursuit amount="1"/>`.
- **`destroyed`** — *"The ship breaks apart and you feel relief in the knowledge that you
  will hopefully still be one step ahead of the fleet."* → `autoReward level="LOW"`
  `standard`.
- No surrender branch; auto-ships have no crew, so there is no `deadCrew` payout either.

> ⚠️ **CONTRADICTION:** [[source-fandom-auto-ship-warning]] describes the `gotaway`
> penalty as *"Rebel Fleet pursuit is **doubled**"*. The game file states
> `<modifyPursuit amount="1"/>` — one extra pursuit step
> ([[source-events-ships]]). These are descriptions of the same tag at different levels
> of abstraction (the wiki is describing the in-game effect of one `modifyPursuit` tick as
> a doubled advance for that jump), not necessarily a factual disagreement — but the wiki's
> wording is not what the file says. Trusting the game files (`high` vs `medium`) for the
> raw value; the in-game magnitude of one `modifyPursuit` step is an open question.

## Blue Options
None. Unlike its nebula sibling, this event offers no `req=` choice at all.

## Rewards & Risks
- Reward: `LOW` `standard` — deliberately worse than the `MED` `standard` of the untimed
  [[event-auto-ship-fight]]. You are paid less for a harder job.
- Risk: **fleet advance**. Failing to kill it in the window is a strictly negative outcome
  with no compensation.

## Strategy Notes
- *(Opinion.)* This is the one auto-ship fight where dumping everything — missiles,
  drone parts, a hacking charge — is defensible, because the failure state costs map turns
  rather than hull. Weigh it against how many beacons you still want to visit in the sector.
- Nothing distinguishes it from [[event-auto-ship-fight]] before the fight starts, so you
  cannot pre-commit ordnance on the intro text.

## Related
- [[event-auto-ship-fight]] — same texts, untimed, better reward
- [[event-auto-bait]] — same texts, the inverse trap (destroying it is what hurts you)
- [[event-rebel-ship-warning]] — the crewed equivalent (`SQUAT_WARNING`)
- [[concept-rebel-fleet-advance]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What one `modifyPursuit amount="1"` step actually costs in beacons/jumps.
- [ ] Whether the 40-unit escape timer is seconds or an internal unit.
- [ ] Numeric value of `LOW` `standard`.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-auto-ship-warning]] (per `raw/wiki/auto-ship-warning.md`)
