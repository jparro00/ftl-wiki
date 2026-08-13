---
id: event-finish-beacon-nebula
type: event
event_name: FINISH_BEACON_NEBULA
sectors: []
beacon_type: exit
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [exit-beacon, nebula, structural, engine-event, orphan, no-choice, cut-content]
---

# Long-Range Beacon in a nebula (sector exit) — `FINISH_BEACON_NEBULA`

## Summary
The exit-beacon event used when the sector's Long-Range Beacon sits inside a nebula. Unlike
its non-nebula twin [[event-finish-beacon]], it does **nothing but print a message** — the
chained bonus-encounter roll was deliberately disabled by the developers, and the XML
comment says why.

## Trigger & Where It Appears
**Not in any sector event list**, and not a random encounter. `FINISH_BEACON_NEBULA` is
named in the *Fleet Progression* section of the summary comment at the top of `events.xml`
alongside `START_BEACON`, `FINISH_BEACON`, `FLEET_EASY_BEACON` and `FLEET_HARD` — the
structural events the engine invokes by name ([[source-events-xml]]).

It fires on arrival at a nebula sector's exit beacon.

### The disabled branch

The event's only `<choice>` is commented out in the shipped file, with a developer note
inside the comment ([[source-events-xml]]):

```xml
<!--	<choice hidden="true">
    <text id="continue"/>   There has been two sightings of odd events at the end of the
                            nebula sectors. Simplifying just as a random precaution.
    <event load="NEBULA"/>
</choice>-->
```

So the intended behaviour was to chain into the `NEBULA` event list, mirroring how
[[event-finish-beacon]] chains into `EXIT_LIST`. It was pulled in response to two
bug reports and never restored. Tagged `cut-content` on that basis: this is not an
oversight, it is a documented removal.

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> This Long-Range Beacon is almost hidden within a nebula. When the FTL Drive is charged
> you can jump to the next Sector.

(`event_FINISH_BEACON_NEBULA_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none in the shipped file)_ | — | Message only. No chained event. | 100% |
| — | ~~`continue` → `<event load="NEBULA"/>`~~ | — | **Commented out.** Would have rolled a nebula event at the exit beacon. | n/a |

## Blue Options
None.

## Rewards & Risks
Neither — which is precisely the difference from [[event-finish-beacon]]. A nebula sector's
exit beacon gives you no bonus encounter, good or bad. The nebula's own hazards (sensors
down, possible ion storm) still apply, since those are beacon properties rather than event
effects.

## Strategy Notes
- A nebula sector's exit is **safer and poorer** than an ordinary sector's exit: no roll on
  `EXIT_LIST` means no free weapon and no ambush. That asymmetry is not documented anywhere
  in-game.
- If the Rebel fleet claims the beacon first you still get the fleet event rather than
  this one.

## Related
- [[event-finish-beacon]] — the non-nebula twin, which does chain into `EXIT_LIST`
- [[event-fleet-easy-beacon]] — what fires when the fleet reaches the exit first
- [[event-fleet-easy-nebula]] — the other nebula fleet event, itself unreachable
- [[sector-uncharted-nebula]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]] — the sectors this applies to
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What the "odd events at the end of the nebula sectors" actually were — the comment
      records the symptom, not the bug.
- [ ] Whether any FTL build shipped with the branch enabled.
- [ ] Whether the engine really uses this event for every nebula-sector exit, or only when
      the exit beacon itself has the nebula flag.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — where the `NEBULA` list the
  disabled branch would have loaded is defined)
