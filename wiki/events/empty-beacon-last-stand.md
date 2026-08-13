---
id: event-empty-beacon-last-stand
type: event
event_name: BOSS_FLEETS_FED
sectors: [[[sector-the-last-stand]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, no-choice, federation, endgame, last-stand, fleet]
---

# Empty beacon (Last Stand) — `BOSS_FLEETS_FED`

## Summary
The safe draw in [[sector-the-last-stand]]: a beacon the Rebel fleet has not reached yet,
still held by Federation warships. Flavour text and nothing else — no choices, no ship, no
rewards. Its only mechanical effect is `<fleet>fed</fleet>`, which puts the Federation
fleet in the background art.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`).
- Beacon: empty. Long-range scanners show **no** ship
  ([[source-fandom-empty-beacon-last-stand]]).
- Event list: `BOSS_NEUTRAL` — five distinct entries → **1/5**, assuming uniform selection
  across list entries ([[source-events-boss]]). `FINAL` allocates `BOSS_NEUTRAL`
  `min=7 max=10` and starts you on one ([[source-sector-data-xml]]).
- The XML comment describes these as *"empty nodes that the Rebels have not reached yet."*

## Text
Drawn from the `BOSS_FLEETS_FED` text list: five distinct strings, each listed twice, so
1/5 apiece assuming uniform selection across list entries ([[source-events-boss]],
[[source-text-events-xml]]). The XML annotates each with the fleet size it is meant to
describe (large fed fleet / small fleet + debris / small fleet + populated planet / large
fleet / small fleet + planet).

> You arrive to see a number of Federation forward-carriers and dreadnoughts. This must be
> a system of high importance to warrant such a fleet.

> A few scattered heavy vessels are left to defend the nearby Federation settlement. They
> seem to be in the process of evacuation.

> A large host of Federation heavy vessels are in formation around the beacon. Sensors run
> hot with missile locks, but once you transmit your ship signature they leave you alone.

All five are transcribed on [[source-fandom-empty-beacon-last-stand]] and match verbatim.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements and no `<ship>`)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. This is the one Last Stand beacon type that costs nothing and gives nothing
([[source-events-boss]], [[source-fandom-empty-beacon-last-stand]]).

## Strategy Notes
- Worth noting only as the denominator: with 7–10 `BOSS_NEUTRAL` beacons and five equal
  list members, most of a Last Stand run's "quiet" beacons are actually one of the four
  other outcomes. *(Derived from list membership, not a sourced strategy claim.)*

## Related
- [[event-rebel-fight-among-federation-and-rebel-fleets]] — the hostile draw from the same list
- [[event-rebel-ship-attacking-civilians-in-last-stand]] — the choice-bearing draw
- [[event-rebel-fight]] (`REBEL`) and [[event-rebel-ship-attacking-refueling-outpost]]
  (`SQUAT_REFUEL_STATION`) — the remaining `BOSS_NEUTRAL` members
- [[sector-the-last-stand]]
- [[entity-federation]]
- [[event-boss-fleets-both]] (`BOSS_FLEETS_BOTH`) — the other peaceful battle-background beacon

## Open Questions
- [ ] None outstanding — the event is three lines of XML.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-last-stand]] (per raw/wiki/empty-beacon-last-stand.md)
