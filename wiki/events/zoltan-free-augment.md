---
id: event-zoltan-free-augment
type: event
event_name: ZOLTAN_FREE_AUGMENT
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, augment-reward, no-risk, free-item]
---

# Zoltan free augment — `ZOLTAN_FREE_AUGMENT`

## Summary
A free augment with low scrap, no choices and no cost. One of the purest positive
beacons in the game — the developers' own source comment on it reads
`<!-- this is pretty sweet :/  -->`.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary, no ship on Long-Ranged Scanners
  ([[source-fandom-zoltan-free-augment]]).
- Reached via the `ITEM_ZOLTAN` event list, allocated `min=1 max=2` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]). That list has nine members, so this
  specific event is far from guaranteed.
- `unique="true"` — at most once per sector.

## Text
> A Zoltan academy sits docked just outside the beacon perimeter. They're happy to show
> you the fruits of their labor, and offer something to take home with you.

(`event_ZOLTAN_FREE_AUGMENT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `autoReward level="LOW"` `augment` — **you receive an augmentation plus low scrap**. | 100% |

Both sources agree: the game file says `<autoReward level="LOW">augment</autoReward>` and
Fandom says *"You receive an augmentation with low scrap"*
([[source-events-zoltan]], [[source-fandom-zoltan-free-augment]]).

## Blue Options
None, and none are needed.

## Rewards & Risks
- **Reward:** one augment from the random augment pool, plus `LOW` scrap.
- **Risk:** none. There is no combat, no cost, no choice, and no negative branch.
- The only failure mode is an **augment slot being full** — in which case the game's
  `AUGMENT_FULL` sell-or-discard prompt fires. That is a system message rather than part
  of this event.

## Strategy Notes
- *Opinion:* always route through this beacon if Long-Ranged Scanners let you identify
  the `ITEM_ZOLTAN` pool. There is no downside case.
- The augment is drawn at random, so the value swings widely — a Pre-Igniter is
  run-defining, a Slug Repair Gel is nearly worthless. No source ingested here states the
  pool or its weights.

## Related
- [[event-zoltan-free-map]], [[event-zoltan-odd-moon]] — the other Zoltan members of the
  `ITEM_ZOLTAN` pool
- [[concept-augmentations]] — the reward pool

## Open Questions
- [ ] Which augments the `autoReward` `augment` pool can draw, and their weights.
- [ ] Scrap value of `LOW` at each sector depth.
- [ ] Does it exclude augments you already own?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-free-augment]] (per raw/wiki/zoltan-free-augment.md)
