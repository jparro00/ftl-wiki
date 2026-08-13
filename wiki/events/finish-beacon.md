---
id: event-finish-beacon
type: event
event_name: FINISH_BEACON
sectors: []
beacon_type: exit
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [exit-beacon, structural, engine-event, orphan, no-choice]
---

# Long-Range Beacon (sector exit) — `FINISH_BEACON`

## Summary
The event that fires when you arrive at a sector's exit beacon. It is a structural
event — the engine calls it by name rather than drawing it from a pool — and its one
mechanical job is to roll a **bonus encounter** from `EXIT_LIST` on top of the exit
message. This is the machinery behind the "can also occur at an exit beacon" note that
Fandom puts on so many event pages.

## Trigger & Where It Appears
**Not in any sector event list**, and not a random encounter. `FINISH_BEACON` is named in
the *Fleet Progression* section of the summary comment at the top of `events.xml`,
alongside `START_BEACON`, `FINISH_BEACON_NEBULA`, `FLEET_EASY_BEACON` and `FLEET_HARD` —
the structural events the engine invokes directly ([[source-events-xml]]).

It fires on arrival at the sector's exit (Long-Range) beacon. Compare
[[event-finish-beacon-nebula]], the variant used when the exit beacon is inside a nebula.

## Text
> You've arrived at the Long-Range Beacon. When the FTL Drive is charged you can jump to
> the next Sector.

(`event_FINISH_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | `<choice hidden="true">` labelled `continue` | — | Loads `EXIT_LIST` — a bonus encounter fires at the exit beacon. | 100% |

The choice is `hidden="true"`, meaning it is not a decision — it chains automatically.

### `EXIT_LIST`

Two members, each of which is itself a list ([[source-newevents]]):

```xml
<eventList name="EXIT_LIST">
    <event load="NEUTRAL_EXIT"/>
    <event load="ITEMS"/>
</eventList>
```

**Assuming uniform selection across list entries, that is a 1/2 chance of a `NEUTRAL_EXIT`
event and a 1/2 chance of an `ITEMS` event.** The game files state no percentage; this is
derived from list membership only.

- `NEUTRAL_EXIT` is the filler pool — `PIRATE_CIVILIAN`, `REBEL_TRANSPORT`,
  `AUTO_REFUEL_STATION`, `ASTEROID_EXPLORE`, `FRIENDLY_SLAVER`, `PIRATE_BRIBER`,
  `AUTO_DEFENSE_ITEM`, [[event-intelligent-ponies]], [[event-plagued-station]], plus AE
  additions. Its own XML comment reads *"This event list is hardcoded to fill out a sector
  if it ran out of all other calls for that sector … TECHNICALLY it uses the EXIT_LIST
  above us now"* ([[source-newevents]]).
- `ITEMS` is the freebie pool — [[event-free-drone-schematic]], [[event-free-weapon]],
  [[event-free-scrap-with-resources]], [[event-trade-fuel-for-drone-parts]], plus stores
  and stations ([[source-newevents]]).

In Advanced Edition the `OVERRIDE_NEUTRAL_EXIT` and `OVERRIDE_ITEMS` lists replace their
base counterparts, so the AE exit-beacon pool is substantially larger
([[source-dlceventsoverwrite]]).

## Blue Options
None.

## Rewards & Risks
Nothing directly. Everything you get here comes from whichever `EXIT_LIST` member fires —
which can be a free weapon, a store, a trade, or a fight (`PIRATE_CIVILIAN`,
`REBEL_TRANSPORT`).

## Strategy Notes
- The exit beacon is not a dead end: it always rolls a second event. Budget for the
  possibility of a fight there, not just a jump.
- If the Rebel fleet reaches the exit beacon first you get
  [[event-fleet-easy-beacon]] instead of this.

## Related
- [[event-finish-beacon-nebula]] — the nebula variant, whose equivalent chained choice is
  **commented out**
- [[event-fleet-easy-beacon]], [[event-fleet-easy-beacon-dlc]] — what replaces this when
  the fleet gets there first
- [[event-free-drone-schematic]], [[event-free-weapon]],
  [[event-free-scrap-with-resources]], [[event-trade-fuel-for-drone-parts]] — the `ITEMS`
  half of `EXIT_LIST`
- [[event-intelligent-ponies]], [[event-plagued-station]] — two of the `NEUTRAL_EXIT` half
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether `EXIT_LIST` selection is genuinely uniform between its two members, which
      would make an `ITEMS` freebie a coin flip at every sector exit.
- [ ] Whether the engine skips `EXIT_LIST` in some conditions (e.g. the final sector).
- [ ] Whether a store rolled from `ITEMS` at the exit beacon behaves like a normal store.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `EXIT_LIST`, `NEUTRAL_EXIT`, `ITEMS`)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
