---
id: event-start-beacon-pirate
type: event
event_name: START_BEACON_PIRATE
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [structural, flavor-only, pirate, no-fandom-page]
---

# Start beacon (Pirate) — `START_BEACON_PIRATE`

## Summary
The beacon you arrive on when you jump into a [[sector-pirate-controlled-sector]]. It is
a structural event, not an encounter: it prints one of four "this place is lawless"
blurbs and does nothing else.

## Trigger & Where It Appears
- Sector: [[sector-pirate-controlled-sector]] (`PIRATE_SECTOR`) only
- Allocation: `<startEvent>START_BEACON_PIRATE</startEvent>`
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`)
- Beacon: the sector entry beacon — always the first beacon of the sector, never random
- **No Fandom page** covers this event; everything here is from the game files.

## Text
Varies — `<text load="START_BEACON_PIRATE"/>` over a four-entry `textList`
([[source-events-pirate]]). All four, per [[source-text-events-xml]]:

> A few years ago this region was bustling with trade activity. Now it is overrun with
> bandits and marauders. You should tread lightly here.

> This somewhat isolated region was thrown into chaos at the start of the rebellion. Even
> in peacetime it was always beset by pirates but now it houses a center of operations for
> countless pirate fleets.

> If the reports are true, this area has been under the control of pirates for quite some
> time. Some traders still attempt to trade with the few settlements that remain, but they
> do so at great risk.

> A few Federation-friendly planets still exist in this sector, but they are constantly
> under attack by pirate raids. This is a dangerous sector, so be careful.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The `<event name="START_BEACON_PIRATE">` element contains a single `<text>` child and
nothing else ([[source-events-pirate]]).

## Rewards & Risks
None. It is a signpost.

## Strategy Notes
- All four variants are pure flavour; none of them signals anything about the sector's
  actual roll. The real warning is in `sector_data.xml`: a Pirate sector allocates 6–8
  `HOSTILE_PIRATE` beacons and a guaranteed `BOARDERS_PIRATE` one
  ([[source-sector-data-xml]]).

## Related
- [[sector-pirate-controlled-sector]]
- [[event-empty-beacon-pirate]] — the other no-op Pirate beacon
- [[event-store-pirate]]
- [[entity-pirates]]

## Open Questions
- [ ] None outstanding — the event has no mechanical content to confirm.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
