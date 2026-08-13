---
id: event-start-beacon-engi
type: event
event_name: START_BEACON_ENGI
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [flavour, no-choice, varies-text, sector-entry]
---

# Start beacon (Engi) — `START_BEACON_ENGI`

## Summary
The text you get on arriving in an Engi sector. It is the sector's `<startEvent>`, not a
random encounter — guaranteed exactly once per Engi sector, at the beacon you jump in on,
with no choices and no effects.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]] and [[sector-engi-homeworlds]] both declare
  `<startEvent>START_BEACON_ENGI</startEvent>` ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`)
- Beacon: the sector entry beacon. It appears in **no** event list — it is allocated by the
  `<startEvent>` mechanism rather than by `ITEMS_ENGI` / `HOSTILE_ENGI` / etc.
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Guaranteed once per Engi sector visited
- No matching Fandom page was in this batch, so everything here comes from the game files.

## Text
The prose **varies**: the event body is a single `<text load="START_BEACON_ENGI"/>` drawing
one of two entries from `textList START_BEACON_ENGI` ([[source-events-xml]]). Both, per
[[source-text-events-xml]]:

> You have arrived in Engi space. The Mantis have been threatening the Engi core worlds,
> but you should be able to stock up for your journey.

(`text_START_BEACON_ENGI_1`)

> You have arrived in Engi space. The fall of the Federation has brought tough times for
> these robotic lifeforms, but they're usually willing to help.

(`text_START_BEACON_ENGI_2`)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | Nothing happens. The event has no `autoReward`, no ship and no choices. | 100% |

## Blue Options
None.

## Rewards & Risks
None of either.

## Strategy Notes
- Nothing to decide. Both texts do flag the sector's actual character honestly: the Mantis
  threat that drives [[event-mantis-fight-engi]] and
  [[event-engi-ship-attacked-by-mantis-ship]], and the unusually generous store allocation
  behind [[event-store-engi]].

## Related
- [[event-empty-beacon-engi]] — the other pure-flavour Engi event
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] Are the two text variants weighted equally?
- [ ] Does any Fandom page document this event? None was supplied in this batch.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
