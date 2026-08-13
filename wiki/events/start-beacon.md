---
id: event-start-beacon
type: event
event_name: START_BEACON
sectors: [[[sector-federation-space]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [flavour, no-choice, sector-entry]
---

# Start beacon — `START_BEACON`

## Summary
The generic sector-entry text: the reminder to explore and then run for the exit before the
Rebel fleet arrives. It is the `<startEvent>` for `STANDARD_SPACE`
([[sector-federation-space]]) only — every other sector type declares a faction-specific
variant. No choices, no effects.

## Trigger & Where It Appears
- Sector: [[sector-federation-space]] (`STANDARD_SPACE`) declares
  `<startEvent>START_BEACON</startEvent>` ([[source-sector-data-xml]]).
- Beacon: the sector entry beacon. It is in **no** event list — it is placed by the
  `<startEvent>` mechanism, not allocated from a pool ([[source-events-xml]]). See
  [[concept-sector-event-allocation]].
- Guaranteed exactly once, at the start of every run, since Federation Space is the
  starting sector.
- No Fandom page joins this event, so everything here comes from the game files.

## Text
> Welcome to a new sector! Get to the exit beacon and jump to the next sector before the
> pursuing Rebels catch you!

(`event_START_BEACON_text`, per [[source-text-events-xml]])

Unlike most of the faction variants, this one is a single fixed `<text id="..."/>` — there
is no `textList` behind it ([[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | Nothing happens. The event body is one `<text>` tag: no `autoReward`, no ship, no choices. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Version differences
No `<!--DLC-->` marker on the event or on the `STANDARD_SPACE` `<startEvent>` line
([[source-events-xml]], [[source-sector-data-xml]]). Identical in both editions.

## Related
- [[event-start-beacon-engi]], [[event-start-beacon-mantis]], [[event-start-beacon-pirate]],
  [[event-start-beacon-rebel]], [[event-start-beacon-rock]], [[event-start-beacon-slug]],
  [[event-start-beacon-zoltan]], [[event-start-beacon-nebula]],
  [[event-start-beacon-crystal]], [[event-start-beacon-lanius]] — the faction variants
- [[event-start-game]] — the run-opening text that precedes it
- [[sector-federation-space]]
- [[concept-sector-event-allocation]]

## Open Questions
- [ ] `sector_data.xml` has a commented-out `<startEvent>START_BEACON_CIVILIAN</startEvent>`
      marked "JUSTIN TO DO" on the Civilian Sector, which therefore falls back to something
      else. What does the Civilian Sector actually show on entry?
- [ ] Does any Fandom page document the start-beacon texts? None joined this batch.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
</content>
