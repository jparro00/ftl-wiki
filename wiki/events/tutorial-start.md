---
id: event-tutorial-start
type: event
event_name: TUTORIAL_START
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: [[[chain-tutorial]]]
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [orphan, tutorial, engine-invoked, no-reward, framing]
---

# Tutorial start — `TUTORIAL_START`

## Summary
The opening beat of FTL's scripted tutorial: three screens of "welcome, here's the war,
here's your job", ending on a **Start Tutorial** button. Pure framing — no rewards, no
risk, no mechanics.

## Trigger & Where It Appears
- **Not in any sector event list.** Nothing in `raw/gamedata/` loads `TUTORIAL_START`; the
  id appears only in its own definition, its text entries, and the structure comment at the
  top of `events.xml` ([[source-events-xml]], [[source-text-events-xml]]). It must be
  invoked by the engine by name when the tutorial runs.
- It is the first of a three-event tutorial set — `TUTORIAL_START`,
  [[event-tutorial-enemy]], [[event-tutorial-missile]] — which the file's own summary
  comment lists together under *Structure* ([[source-events-xml]]). The tutorial also has a
  dedicated player ship blueprint, `PLAYER_SHIP_TUTORIAL` ([[source-blueprints]]).
- `version: unknown` deliberately. Nothing in the data files says whether the Advanced
  Edition build still plays this scripted sequence or replaces it — and this wiki does not
  fill that in from recollection. See Open Questions.
- No Fandom page joins this event.

## Text
Three nested screens, each a `continue` choice into the next
([[source-text-events-xml]]):

> Welcome to FTL! You are the captain of a Federation starship on a very important mission.

> The Federation is currently being torn apart by vicious Rebels. Your ship is carrying data
> vital to the defense of the Federation.

> You will be traveling through dangerous sectors of the galaxy with the Rebel fleet in hot
> pursuit. Make it to the exit beacon of each sector before the Rebels can catch you.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | Screen 2 (the Rebel war), which itself offers two choices | 100% |
| 1.1 | *Continue…* | — | Screen 3 (the exit-beacon rule). Terminal — no further tags. | 100% |
| 1.2 | Start Tutorial. | — | `<event/>` — an **empty** event. The engine takes over from here. | 100% |

Note the shape: choice 1.2 is a sibling of the nested continue, not a successor, so the
player can read the third screen *or* skip straight into the tutorial
([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
Neither. No `autoReward`, no `item_modify`, no ship.

## Version differences
No `<!--DLC-->` markers ([[source-events-xml]]). The XML is identical in both editions'
data files; whether the *engine* still uses it is the open question below, and is why
`version` is `unknown` rather than `both`.

## Related
- [[event-tutorial-enemy]] — the next beat, the practice pirate fight
- [[event-tutorial-missile]] — the hand-out that follows it
- [[chain-tutorial]] — the three-event sequence
- [[event-start-game]] — the equivalent framing text for a real run

## Open Questions
- [ ] Does the Advanced Edition build still play this scripted tutorial, or does it use a
      different (hangar-based) one? No file in `raw/` answers this.
- [ ] What does the engine do after the empty `<event/>` on "Start Tutorial."?
- [ ] Is `PLAYER_SHIP_TUTORIAL` (a Kestrel layout with pilot/doors/sensors/medbay/oxygen
      pre-started, [[source-blueprints]]) the ship used here?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
</content>
