---
id: event-free-scrap-with-resources-engi
type: event
event_name: ENGI_GIFT
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [filler, free-loot, no-choice, varies-text]
---

# Free scrap with resources (Engi) — `ENGI_GIFT`

## Summary
Pure free loot. No choices, no risk, no fight — you arrive, the Engi hand you supplies, you
leave. The only variable is which of four flavour texts you get.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: ordinary — no `<distressBeacon/>` or `<store/>` tag
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Event list: `ITEMS_ENGI`, allocated `min=3 max=3` per Engi sector
  ([[source-sector-data-xml]])
- Not unique — it can recur within a run

## Text
The prose **varies**: the event uses `<text load="ENGI_GIFT"/>`, which draws one of four
entries from `textList ENGI_GIFT` ([[source-events-xml]]). The four variants, per
[[source-fandom-free-scrap-with-resources-engi]]:

> An Engi vessel hails you. "Identity: Federation? Outlier probability. Implies... revival.
> Implies... hope. Assistance suggested." They offer some supplies.

> You cross paths with an Engi cargo vessel hurrying home before the Mantis fleets attempt
> to take over this sector. They're happy to offload some of their cargo to get home faster.

> You make contact with an isolated Engi science station who are staying put despite the
> likelihood of Mantis invasion. They suggest you trial some experimental technology.

> This was the site of a recent battle. Either a show of Mantis force, or the Engi here
> weren't disposed to go peacefully. You pick through the pieces.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | `<autoReward level="RANDOM">standard</autoReward>` — a random amount of scrap with resources. | 100% |

`RANDOM` is the game's own `autoReward` level, meaning the tier itself is rolled; no source
here converts it to numbers ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- Scrap with resources, random tier. Nothing else happens.
- No risk of any kind — the event has no choices, no ship, and no crew or hull effects.

## Strategy Notes
- Nothing to decide. Its only strategic weight is that it occupies one of the three
  `ITEMS_ENGI` slots per Engi sector, competing with [[event-engi-cache]] and
  [[event-engi-surrender]] for the same allocation. *(Opinion.)*

## Related
- [[event-engi-cache]], [[event-engi-surrender]] — the other `ITEMS_ENGI` Engi-specific entries
- [[event-empty-beacon-engi]] — the no-reward equivalent
- [[entity-engi]]

## Open Questions
- [ ] Scrap range of a `RANDOM` `standard` reward at a given sector depth.
- [ ] Are the four text variants weighted equally?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-free-scrap-with-resources-engi]] (per `raw/wiki/free-scrap-with-resources-engi.md`)
