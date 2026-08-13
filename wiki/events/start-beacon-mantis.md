---
id: event-start-beacon-mantis
type: event
event_name: START_BEACON_MANTIS
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [start-beacon, no-choice, flavour-only, mantis, structural]
---

# Start beacon (Mantis) — `START_BEACON_MANTIS`

## Summary
The arrival beacon for both Mantis sector types — the text you see the moment you jump in,
before anything else happens. Pure flavour with a warning attached: check your hull and
your fuel. It has no choices and no payload.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]] and [[sector-mantis-homeworlds]]
- Named as `<startEvent>START_BEACON_MANTIS</startEvent>` in **both** the `MANTIS_SECTOR`
  and `MANTIS_HOME` sector descriptions ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`) — so it fires exactly once per Mantis sector, guaranteed,
  at the entry beacon.
- Not drawn from any event list; it is structural, allocated by the sector definition
  itself.
- No Fandom page joins this event — the community wiki does not catalogue start beacons
  separately.

## Text
> You've entered a poorly charted area of space that's known to be home to the Mantis.
> Ensure your hull plating is up to scratch and that you have enough fuel in the tank to
> make it through.

(`event_START_BEACON_MANTIS_text`, per [[source-text-events-xml]]) — a single fixed
string, not a text list.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event is a single `<text id="event_START_BEACON_MANTIS_text"/>`)_ | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The event definition is two lines long and contains no effect elements at all
([[source-events-xml]], per `raw/gamedata/events_mantis.xml` lines 102–104).

## Strategy Notes
- The text's advice is accurate as a description of the sector: Mantis sectors allocate
  6–7 hostile beacons and 1–2 boarding beacons, the highest combined combat pressure of
  the faction sectors covered so far ([[source-sector-data-xml]]).
- Both Mantis sector types share this start beacon *and* share an identical event
  allocation, except that [[sector-mantis-homeworlds]] adds the guaranteed
  [[event-legendary-thief-kazaaakplethkilik]] beacon at `min=1 max=1`. Nothing in the
  arrival text distinguishes the two.

## Related
- [[event-empty-beacon-mantis]] — the other zero-payload Mantis beacon
- [[event-store-mantis]]
- [[event-legendary-thief-kazaaakplethkilik]] — the homeworlds-only set piece
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- [[concept-start-beacons]] — the per-sector `START_BEACON_*` family

## Open Questions
- [ ] Nothing outstanding — the event has no unresolved mechanics.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
