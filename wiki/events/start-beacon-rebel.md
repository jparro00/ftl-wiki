---
id: event-start-beacon-rebel
type: event
event_name: START_BEACON_REBEL
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rebel, structural, start-beacon, no-choice, flavour-only, no-fandom-page]
---

# Start beacon (Rebel) — `START_BEACON_REBEL`

## Summary
The text you get on arriving in a Rebel sector. Five variants, all saying the same thing in
different words: the Rebels own this space, they are looking for you, be careful. Purely
structural — no choices, no mechanics.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- **Not in any event list.** It is named as the `<startEvent>` of both `REBEL_SECTOR` and
  `REBEL_SECTOR_MINIBOSS` in `raw/gamedata/sector_data.xml`
  ([[source-sector-data-xml]]), so it fires exactly once, on the first beacon of the
  sector, and cannot be avoided or repeated.
- Filed under the `STRUCTURE!!! / Required structural` header in `events_rebel.xml`
  ([[source-events-rebel]]).
- **No Fandom page joins this event** — the community wiki does not document start-beacon
  texts as events.

## Text
Drawn from the `START_BEACON_REBEL` text list — **five variants**
([[source-events-rebel]], [[source-text-events-xml]]):

> This sector was bustling with activity just a few years ago. Now, more than half of the
> jump beacons have been destroyed, many settlements have been abandoned and the Rebels
> patrol constantly.

> This sector was hit hard by the rebellion. The many alien settlements and stations located
> here are now watched over by almost an equal number of Rebel bases, heavy-handedly
> 'keeping the peace'.

> Once the Federation forces were scattered, the Rebels came down hard on the locals here.
> Between the 'tax collectors' and military bases, the Rebel presence in this sector is
> high.

> At one point this was one of the most commonly traveled sectors. Knowing that, the Rebels
> have stationed a number of fleets here. Be careful.

> You will have to be very cautious in this sector. The Rebels have full control and are no
> doubt looking for you.

(`text_START_BEACON_REBEL_1` … `_5`, per [[source-text-events-xml]])

Note that the same `START_BEACON_REBEL` event serves both the ordinary Rebel Controlled
Sector and the Rebel Stronghold — the prose gives no hint that the latter contains the
[[event-rebel-shipyard]] miniboss ([[source-sector-data-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event body is a single `<text load="START_BEACON_REBEL"/>`)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The event has no mechanical payload of any kind.

## Strategy Notes
Nothing to decide. Recorded for completeness and because it is the game's own framing of
what a Rebel sector is.

## Related
- [[event-empty-beacon-rebel]], [[event-store-rebel]] — the other two structural entries
- [[event-start-beacon-engi]], [[event-start-beacon-mantis]], [[event-start-beacon-rock]],
  [[event-start-beacon-zoltan]], [[event-start-beacon-crystal]] — the sibling start events
- [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether the five variants are equally weighted (the list states no weights and no
      `planet=` gates, unlike `NOTHING_REBEL`).

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
