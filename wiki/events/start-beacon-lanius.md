---
id: event-start-beacon-lanius
type: event
event_name: START_BEACON_LANIUS
sectors: [[[sector-abandoned-sector]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [structural, flavor-only, lanius, no-fandom-page, advanced-edition]
---

# Start beacon (Lanius) — `START_BEACON_LANIUS`

## Summary
The beacon you arrive on when you jump into an Abandoned Sector. A structural event, not an
encounter: it prints one of four lines explaining why the sector is empty and does nothing
else.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- Allocation: `<startEvent>START_BEACON_LANIUS</startEvent>` in the `LANIUS_SECTOR`
  definition ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`).
- Beacon: the sector entry beacon — always the first beacon of the sector, never random.
- Not a member of any `eventList`, so it never appears anywhere else.
- **No Fandom page** covers this event; everything here is from the game files.

> **AE-only.** `dlcEvents_anaerobic.xml` is an Advanced Edition data file and
> `LANIUS_SECTOR` is an AE sector; there is no vanilla form. `dlcEventsOverwrite.xml`
> defines no override for it ([[source-dlceventsoverwrite]]).

## Text
`[varies: textList START_BEACON_LANIUS]` — four entries, none duplicated → **1/4 each**
*assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]). All four,
per [[source-text-events-xml]]:

> This sector has been largely abandoned since a series of battles decimated the local
> population. An unusual alien race is reportedly scavenging in the area. You'd best be on
> guard.

> This sector was the site of many major battles between the Federation and Rebel fleets.
> Strangely, there's very little evidence of those battles remaining...

> There have been a number of reports of advanced ships salvaging the wrecks and abandoned
> mining facilities in this sector. Could it be that the Lanius have resurfaced?

> The war tore through this civilian sector, and just recently even the few life signs that
> remained have begun blinking out. Rumours suggest the Lanius are responsible.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The `<event name="START_BEACON_LANIUS">` element contains a single `<text load=…/>` child
and nothing else ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
None. It is a signpost.

## Strategy Notes
- Pure flavour with no mechanical difference between the four variants — none of them
  signals anything about how the sector rolled.
- The real read on an Abandoned Sector comes from its allocation, not this beacon: 5–6
  hostile, 1–2 hazard-hostile, 1–2 boarding, 1–2 distress, 5–6 neutral, 2–4 item and
  exactly 2 store beacons ([[source-sector-data-xml]]).

## Related
- [[event-empty-beacon-lanius]] — the other no-op Lanius beacon
- [[event-store-lanius]] — the sector's guaranteed store
- [[event-start-beacon-rock]], [[event-start-beacon-mantis]] — the same slot in other
  sectors
- [[sector-abandoned-sector]], [[entity-lanius]]

## Open Questions
- [ ] None outstanding — the event has no mechanical content to confirm.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
