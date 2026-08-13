---
id: event-start-demo
type: event
event_name: START_DEMO
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [flavour, no-choice, orphan, unreachable, demo-content, engine-invoked]
---

# Start demo — `START_DEMO`

## Summary
The opening briefing for FTL's **demo build**, which reframes the run as a Federation
training simulation. It ships in the retail data files but nothing in those files can reach
it — it is a leftover from the demo, preserved verbatim.

## Trigger & Where It Appears
- **Not in any sector event list**, and never referenced by any `load=` anywhere in
  `raw/gamedata/` — the only occurrences of the id are its own definition and its text
  entry ([[source-events-xml]], [[source-text-events-xml]]).
- It sits directly above `START_GAME`, the retail equivalent, and immediately above the
  `GAMEOVER` text list, which carries the explicit dev comment `<!-- demo gameover text-->`
  ([[source-events-xml]]). That comment is the file's own confirmation that this block is
  demo-build content.
- Tagged `unreachable` here: it is fully authored shipped content with no live reference in
  the retail data. It is *not* tagged `cut-content` — nothing says it was pulled from the
  retail game as opposed to simply belonging to a different build.
- No Fandom page joins this event.

## Text
> Welcome to the Federation training simulation! You're about to be sent on a very dangerous
> mission carrying data vital to the Federation fleet. We've put this simulator together to
> give you an idea of what to expect on the actual journey. Explore the sector, gather
> supplies, but get to the exit before the simulated Rebel fleet catches up!

(`event_START_DEMO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | Nothing happens. The event body is a single `<text>` tag. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Version differences
No `<!--DLC-->` marker ([[source-events-xml]]) — the block is present in the same form in
both editions' data. The version axis that matters for this event is demo-vs-retail, not
vanilla-vs-Advanced Edition.

## Related
- [[event-start-game]] — the retail briefing this mirrors
- [[event-tutorial-start]] — the other framing text aimed at new players

## Open Questions
- [ ] Is `START_DEMO` reachable in any shipped build (e.g. by launching the demo
      executable against these data files)?
- [ ] Does the demo's `GAMEOVER` text list have any live use in the retail game?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
</content>
