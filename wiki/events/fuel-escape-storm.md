---
id: event-fuel-escape-storm
type: event
event_name: FUEL_ESCAPE_STORM
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, ion-storm, nebula, orphan, engine-event, no-choice]
---

# Fuel escape (ion storm) — `FUEL_ESCAPE_STORM`

## Summary
A one-line resolution event: you were stranded without fuel in an ion storm and the storm
has now passed. No choices, no rewards, no ship. One of the three base-game members of the
`FUEL_ESCAPE_*` family.

Note the difference in framing from its siblings: the sun and asteroid versions have you
*manoeuvre out* of the hazard, whereas here the hazard simply stops on its own — *"The ion
storm died down."* An ion storm is a nebula property, not something you can drift away
from.

## Trigger & Where It Appears
**Not in any sector event list.** `FUEL_ESCAPE_STORM` appears in `raw/gamedata/` only as
its own definition in `events.xml` (line 192) and its string in `text_events.xml`
([[source-events-xml]], [[source-text-events-xml]]).

The reasoning for how it is reached is set out on [[event-fuel-escape-sun]] and
[[event-fuel-escape-pulsar]] and applies identically: it belongs to a block of one-line
events (`BOSS_STALEMATE`, `CREW_STUCK`, `AUGMENT_FULL`, `EQUIP_FULL`) that the engine calls
by hard-coded name. **No source in `raw/` states the trigger**; this is inference from
structure and from the family's internal consistency.

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> The ion storm died down, leaving your ship in peace as you wait for help.

(`event_FUEL_ESCAPE_STORM_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — a single `<text>` tag)_ | — | Message only. The ion storm ends. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither.

## Strategy Notes
Nothing to play. Its practical significance is that being fuel-stranded in an ion storm is
not necessarily terminal — the storm can lift while you wait.

## Related
- [[event-fuel-escape-sun]], [[event-fuel-escape-asteroids]] — the other two base-game
  members of the family
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]], [[event-fuel-escape-fleet]] —
  the Advanced Edition additions
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name.
- [ ] Whether it can fire at any nebula beacon with a storm, or only where the storm was
      the active hazard when you ran dry.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml — the out-of-fuel machinery that
  does *not* reference it)
