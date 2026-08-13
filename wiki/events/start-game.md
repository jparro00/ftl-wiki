---
id: event-start-game
type: event
event_name: START_GAME
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [flavour, no-choice, orphan, engine-invoked, framing]
---

# Start game — `START_GAME`

## Summary
The briefing you get when a run begins: carry the data, loot every sector, stay ahead of
the fleet. It is a one-line event with no choices and no mechanics — the game's opening
framing rather than an encounter.

## Trigger & Where It Appears
- **Not in any sector event list.** Nothing in `raw/gamedata/` loads `START_GAME`: the only
  occurrences of the id are its own `<event name="START_GAME">` definition and its text
  entry ([[source-events-xml]], [[source-text-events-xml]]).
- An event that is defined but never referenced by any list, ship block or `load=` must be
  invoked by the engine directly, by name. Its neighbours in the file are the same kind of
  thing — `AUGMENT_FULL`, `EQUIP_FULL`, `START_DEMO`, `DUMMY` (which carries the comment
  *"Dummy event, please leave in"*).
- The prose is a new-run briefing, and it sits immediately beside `START_DEMO`, the demo
  build's equivalent. Exactly when the engine fires it — at the hangar, on the first jump,
  or not at all in the current build — is **not** determinable from the data files.
- No Fandom page joins this event.

## Text
> The data you carry is vital to the remaining Federation fleet. You'll need supplies for
> the journey, so make sure to explore each sector before moving on to the next. But get to
> the exit before the pursuing Rebel fleet can catch up!

(`event_START_GAME_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | Nothing happens. The event body is a single `<text>` tag. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Version differences
No `<!--DLC-->` marker ([[source-events-xml]]). Present unchanged in both editions of the
data files.

## Related
- [[event-start-demo]] — the demo build's version of the same briefing
- [[event-start-beacon]] — the per-sector reminder that repeats the same instruction
- [[event-tutorial-start]] — the tutorial's opening text

## Open Questions
- [ ] When exactly does the engine show this? No data file says.
- [ ] Is it still shown in the Advanced Edition build, or superseded by the hangar
      briefing?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
</content>
