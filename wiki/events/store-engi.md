---
id: event-store-engi
type: event
event_name: STORE_ENGI
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, no-choice, varies-text]
---

# Store (Engi) — `STORE_ENGI`

## Summary
The Engi store beacon. Three flavour texts, then a store opens. Notable mainly for its
allocation: **two to three per Engi sector**, more than most sectors get, which makes Engi
space a reliable place to plan purchases around.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: **store** — the event body is `<text load="STORE_ENGI"/>` plus `<store/>`
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Allocated directly by sector, not through a list: `STORE_ENGI min=2 max=3` in both Engi
  sectors ([[source-sector-data-xml]])
- Not unique

## Text
The prose **varies**: `textList STORE_ENGI` holds three entries ([[source-events-xml]]).
All three, per [[source-fandom-store-engi]]:

> The Engi can do remarkable things with just a pile of scrap. The Engi hive at this beacon
> are selling equipment for just that.

> A message arrives: "Your scrap, ours. Our weapons for you." You're about to raise the
> shields when you realize it's just an Engi trader looking for a trade.

> An Engi ship hails: "Engine upgrade necessary for travel home. Sale of equipment
> necessary for engine upgrade."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | `<store/>` — a store opens. | 100% |

## Blue Options
None.

## Rewards & Risks
- Whatever the store stocks. **No source here states any Engi-specific stock weighting** —
  neither the event definition nor the Fandom page says the inventory differs from a
  generic store ([[source-events-xml]], [[source-fandom-store-engi]]).
- No risk.

## Strategy Notes
- The `min=2 max=3` allocation is the fact worth carrying: both Engi sectors guarantee at
  least two stores, against a single guaranteed `QUESTS_ENGI` beacon and one to three
  distress beacons ([[source-sector-data-xml]]). *(Opinion: that makes Engi space a good
  place to arrive with banked scrap.)*

## Related
- [[concept-stores]]
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] Does the Engi sector bias store stock toward drones or Engi-flavoured gear? No source
      here says.
- [ ] Are the three text variants weighted equally?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-store-engi]] (per `raw/wiki/store-engi.md`)
