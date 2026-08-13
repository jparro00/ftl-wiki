---
id: event-start-beacon-rock
type: event
event_name: START_BEACON_ROCK
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [structural, flavor-only, rock, no-fandom-page]
---

# Start beacon (Rock) — `START_BEACON_ROCK`

## Summary
The beacon you arrive on when you jump into a Rock sector. It is a structural event, not
an encounter: it prints one of two warning blurbs about Rock xenophobia and does nothing
else. Both Rock sector definitions use it as their `startEvent`.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]] (`ROCK` sector description) and
  [[sector-rock-homeworlds]] (`ROCK_HOME`)
- Allocation: `<startEvent>START_BEACON_ROCK</startEvent>` in both
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`)
- Beacon: the sector entry beacon — always the first beacon of the sector, never random
- **No Fandom page** covers this event; everything here is from the game files.

## Text
Varies — `<text load="START_BEACON_ROCK"/>` over a two-entry `textList`
([[source-events-rock]]). Both entries, per [[source-text-events-xml]]:

> The Rock people have a particularly aggressive stance toward alien races trespassing in
> their space. You should tread carefully here.

> The Rock people are a powerful and proud race. It is not unheard of to have a peaceful
> journey through their lands, but don't count on it.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The `<event name="START_BEACON_ROCK">` element contains a single `<text>` child and
nothing else ([[source-events-rock]]).

## Rewards & Risks
None. It is a signpost.

## Strategy Notes
- The two variants are pure flavour and carry no mechanical difference — do not read the
  "peaceful journey" line as a signal about the sector's roll.

## Related
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- [[event-empty-beacon-rock]] — the other no-op Rock beacon
- [[entity-rock-men]]

## Open Questions
- [ ] None outstanding — the event has no mechanical content to confirm.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
