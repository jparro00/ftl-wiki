---
id: event-fleet-easy-dlc
type: event
event_name: FLEET_EASY_DLC
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rebel-fleet, structural, engine-event, orphan, no-choice, combat, pds, advanced-edition]
---

# Rebel fleet takeover (AE id) — `FLEET_EASY_DLC`

## Summary
The Advanced Edition-suffixed duplicate of [[event-fleet-easy]]. Its definition, its ship,
its environment and even its prose are identical to the base id — the only difference is
the name and a separately-stored copy of the same string. Recorded separately because it
carries its own `event_name` join key.

## Trigger & Where It Appears
**Not in any sector event list.** Like its base twin it is a structural event the engine
calls by name when the Rebel fleet claims the beacon you are sitting on. It carries the
`<fleet>rebel</fleet>` marker ([[source-events-xml]]).

The `_DLC` suffix marks it as the Advanced Edition variant — the same convention as
`FLEET_EASY_BEACON_DLC` and `NO_FUEL_FLEET_DLC`. **How the engine picks between the two ids
is not stated anywhere in `raw/gamedata/`**; that it is an edition switch is inference from
the naming convention alone.

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> The Rebel fleet has found you, and a nearby scout turns to engage. The cruisers in the
> distance are firing on you!

(`event_FLEET_EASY_DLC_text`, per [[source-text-events-xml]] — a **separate string entry
with identical wording** to `event_FLEET_EASY_text`. Contrast
[[event-fleet-easy-nebula]], whose string is genuinely unique.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with `LONG_FLEET` inside `<environment type="PDS" target="player"/>`. | 100% |

`LONG_FLEET` pays **+1 fuel** on destroyed or dead crew, with no surrender and no escape
block ([[source-events-ships]]). Full breakdown on [[event-fleet-easy]].

## Blue Options
None.

## Rewards & Risks
Identical to [[event-fleet-easy]]: +1 fuel for a kill, against an elite Rebel ship and a
hostile PDS barrage. Leave.

## Strategy Notes
Nothing distinguishes it in play from [[event-fleet-easy]]. Its only interest is
bookkeeping: if you are matching observed events to ids, both ids produce the same screen.

## Related
- [[event-fleet-easy]] — the base id, identical content, fuller write-up
- [[event-fleet-easy-beacon-dlc]] — the exit-beacon AE variant
- [[event-fleet-hard]], [[event-fleet-easy-nebula]]
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Why the duplicate exists at all, given the definitions are identical — no AE-only
      element appears in it.
- [ ] The engine's selection rule between `FLEET_EASY` and `FLEET_EASY_DLC`.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `LONG_FLEET` block)
