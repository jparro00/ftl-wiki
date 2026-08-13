---
id: event-engi-surrender
type: event
event_name: ENGI_SURRENDER
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, free-loot, moral-choice]
---

# Engi surrender — `ENGI_SURRENDER`

## Summary
An Engi ship surrenders its cargo before you have done anything. Taking the loot is a
guaranteed payout; telling them you are friendly is the same payout on a coin flip. The
event is unusual in that the "nice" option is strictly a gamble on the same reward, with no
compensating upside recorded in any source.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: ordinary — no `<distressBeacon/>` or `<store/>` tag ([[source-events-xml]], per
  `raw/gamedata/events_engi.xml`)
- Event list: `ITEMS_ENGI`, allocated `min=3 max=3` per Engi sector
  ([[source-sector-data-xml]])
- `unique="true"` — at most once per run

## Text
> An Engi ship in the vicinity, seeing you jump in armed to the teeth, immediately
> broadcasts its surrender: "Subject goal: wealth. Engi motivation: survival. Transfer of
> goods acceptable?"

(`event_ENGI_SURRENDER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Explain that you're friendly. | — | Loads `ENGI_SURRENDER_LIST`, two entries: (a) *"The Engi seem relieved, and eager to get underway. They set off without saying goodbye."* → **nothing**; (b) *"The Engi are satisfied with your explanation… They send over the gear willingly, and you feel better for it."* → `<autoReward level="RANDOM">standard</autoReward>`. | unknown |
| 2 | Accept their offer of surrender. | — | *"The Engi obediently transfer over the goods and get on their way. Money for nothing."* → `<autoReward level="RANDOM">standard</autoReward>`. | 100% |

Both branches award the *same* reward line. The only difference is that choice 1 routes
through a two-entry list, one entry of which pays nothing
([[source-events-xml]]; corroborated by [[source-fandom-engi-surrender]]).

## Blue Options
None — notably, there is no `req="engi"` option here despite the event being an Engi
encounter.

## Rewards & Risks
- `RANDOM` `standard` — scrap with resources, tier rolled. No source converts `RANDOM` to
  numbers.
- No risk in either branch: no fight, no crew loss, no hull damage
  ([[source-events-xml]]).

## Strategy Notes
- Choice 2 is a guaranteed payout; choice 1 is the same payout on one of two list entries.
  The two entries' weighting is not stated anywhere, but even at an even split choice 1 is
  worse in expectation. *(Opinion, derived directly from the two branches above.)*
- There is no recorded downstream consequence to accepting the surrender — no reputation
  system, no follow-up event. If one exists, no source here mentions it.

## Related
- [[event-engi-cache]], [[event-free-scrap-with-resources-engi]] — the other `ITEMS_ENGI` Engi entries
- [[event-engi-smashed-ships]] — the other "leave them alone" Engi judgement call
- [[entity-engi]]

## Open Questions
- [ ] Relative weighting of the two `ENGI_SURRENDER_LIST` entries.
- [ ] Does accepting the surrender have any recorded downstream effect? No source says.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-surrender]] (per `raw/wiki/engi-surrender.md`)
