---
id: event-federation-base
type: event
event_name: FEDERATION_BASE
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [endgame, last-stand, orphan, scripted, text-only, federation]
---

# Federation Base — `FEDERATION_BASE`

## Summary
The arrival text at the Federation Base beacon in [[sector-the-last-stand]] — the beacon
you are defending, and where the Flagship must be stopped. Mechanically it is a single
line of prose: one `<text>` tag and nothing else. No choices, no ship, no rewards, no
status effects.

## Trigger & Where It Appears
- **Orphan in the data.** `FEDERATION_BASE` is in **no `eventList` and no
  `sectorDescription`**; the only reference in `raw/gamedata/` is its own definition
  ([[source-events-boss]], [[source-sector-data-xml]]). (The similarly-named
  `FEDERATION_BASE_ASSIST` and `HIDDEN_FEDERATION_BASE_LIST` in `events.xml` are unrelated
  mid-game quest content, not this event.)
- It is fired by the endgame scripting when you jump to the base beacon, which is also the
  Flagship's destination.
- Sector: [[sector-the-last-stand]] (`FINAL`).

## Text
> You arrive near the Federation Base to find the bulk of their fleet skirmishing with
> Rebel forces. You hang back near the far side of the moon to avoid the conflict. There's
> not much you can do to help in that battle, and your mission holds the key to turn the
> tide of the war. You prepare to face the Flagship.

(`event_FEDERATION_BASE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a single `<text>` tag)* | — | Text only. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The event carries no `autoReward`, `item_modify`, `damage`, `ship` or `status`
tag ([[source-events-boss]]).

## Strategy Notes
None — there is nothing to decide. The interest here is narrative: the base is the thing
the Flagship is destroying while you fight it, and this is the only text that describes it.

## Related
- [[event-last-stand-start]] — the outpost briefing that precedes it
- [[event-boss-text-1]], [[event-boss-text-2]], [[event-boss-text-3]] — the Flagship phases
- [[event-boss-destroyed]] — the ending
- [[sector-the-last-stand]]
- [[chain-the-flagship]]
- [[entity-federation]]

## Open Questions
- [ ] Whether this text plays on every arrival at the base beacon or only the first.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
