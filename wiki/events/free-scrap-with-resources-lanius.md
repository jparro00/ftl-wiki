---
id: event-free-scrap-with-resources-lanius
type: event
event_name: LANIUS_FREE_STUFF
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, free-reward, no-choice, unique, advanced-edition]
---

# Free scrap with resources (Lanius) — `LANIUS_FREE_STUFF`

## Summary
The Abandoned Sector's free lunch: a battered Lanius ship flees at the sight of you,
leaving a field of destroyed Rebel automated ships to scrap. One text tag, one
`autoReward`, no choices, no risk. The single highest-value guaranteed payout in the
sector's item pool.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `ITEM_LANIUS`, allocated `min=2 max=4` beacons per sector — the heaviest item
  allocation of any sector in the game ([[source-sector-data-xml]]). That list has five
  members — `LANIUS_FREE_STUFF`, `LANIUS_TRADER_TRANSLATOR`, `LANIUS_TRADER`,
  `LANIUS_RESEARCHER_CRAFT`, `LANIUS_RESEARCHER_CONTACT` — none duplicated → **1/5**
  *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- Long-range scanners show **no** ship
  ([[source-fandom-free-scrap-with-resources-lanius]]).

> **AE-only** — Advanced Edition file and sector.

## Text
> You stumble across a badly damaged Lanius craft. It jumps away as soon as it sees you.
> Looking around the area, you discover a number of destroyed Rebel automated ships. It
> must have been quite the fight. You scrap what remains.

(`event_LANIUS_FREE_STUFF_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event is a text tag plus one reward tag)_ | — | `<autoReward level="HIGH">standard</autoReward>` — **high** scrap with resources. | 100% |

`HIGH` and `standard` are the game's own words: the highest tier of the mixed
scrap-plus-resources payout ([[source-dlcevents-anaerobic]]). No source read here converts
that to numbers.

## Blue Options
None — and none are needed.

## Rewards & Risks
- Reward: guaranteed `HIGH standard`.
- Risk: none. There is no ship, no choice and no failure branch.

## Strategy Notes
- Nothing to decide. Worth knowing as one of five equally likely results when the sector
  rolls an item beacon, and the only one that costs nothing and demands nothing.

## Related
- [[event-lanius-fight]] — where a `HIGH standard` payout otherwise requires killing a
  crew
- [[event-lanius-ship-in-rich-debris-field]] — the other route to `HIGH standard` in this
  sector, gated behind level-3 Piloting
- [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `HIGH standard`.
- [ ] The other four `ITEM_LANIUS` members are not yet paged.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-free-scrap-with-resources-lanius]] (per raw/wiki/free-scrap-with-resources-lanius.md)
