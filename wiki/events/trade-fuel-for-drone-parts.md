---
id: event-trade-fuel-for-drone-parts
type: event
event_name: FUEL_FOR_DRONE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, fuel, drone-parts, repeatable, no-risk, item-event]
---

# Trade fuel for drone parts — `FUEL_FOR_DRONE`

## Summary
A flat trade at an item beacon: 2–4 fuel for 1–3 drone parts, take it or leave it. No
risk, no branching, no blue options, and the actual numbers are shown before you decide —
which makes this the least interesting and most transparent event in the `ITEMS` pool.

## Trigger & Where It Appears
- Sectors: sixteen — see frontmatter for the full list.
- Pooled in `ITEMS` and `ITEM_ZOLTAN`, plus the Advanced Edition `OVERRIDE_ITEMS`
  replacement. Present in **both editions** ([[source-newevents]],
  [[source-events-zoltan]], [[source-dlceventsoverwrite]]).
- **Not `unique`** — it can recur in a run.
- Also reachable at an exit beacon, since `ITEMS` is a member of `EXIT_LIST`
  ([[source-newevents]], [[source-fandom-trade-fuel-for-drone-parts]]).
- No ship at the beacon; Long-Range Scanners show nothing.

## Text
Drawn from the `FUEL_FOR_DRONE` textList — `[varies: textList FUEL_FOR_DRONE]`. Three
strings, none DLC-marked, so the pool is identical in both editions
([[source-events-xml]], [[source-text-events-xml]]):

1. *"A nearby space station hails you. 'Greetings! Your arrival is most fortuitous. We recently came across some extra drones. If you have some fuel, perhaps we can make a deal?'"*
2. *"A strange vessel approaches. A digital message appears on your view-screen: 'This is an automated merchant. Refill this vessel with fuel and it will supply you with drones.'"*
3. *"You arrive in the sector and are greeted by a science vessel waiting by the beacon. They hail you, 'We find ourselves low on fuel and have a proposition.'"*

Assuming uniform selection across list entries, each is 1/3.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept the offer. | — | `<item type="fuel" min="-4" max="-2"/>` and `<item type="drones" min="1" max="3"/>` — **pay 2–4 fuel, receive 1–3 drone parts.** No outcome prose at all: the event body is an `<item_modify>` block with no `<text>`. | 100% |
| 2 | Reject their offer. | — | Nothing — an empty `<event/>`, no prose. | 100% |

The exact amounts are shown before you commit: *"the actual trade offer is shown prior to
making the choice"* ([[source-fandom-trade-fuel-for-drone-parts]]). So the 2–4 / 1–3 ranges
are never a gamble at the point of decision — you see the specific numbers.

## Blue Options
None.

## Rewards & Risks
- **Cost:** 2–4 fuel. **Return:** 1–3 drone parts.
- Worst visible offer is 4 fuel for 1 drone part; best is 2 fuel for 3. Since both figures
  are revealed first, you can simply decline the bad rolls.
- **Risk:** none. No ship, no combat, no crew exposure. The only downside is fuel you may
  need later.

## Strategy Notes
- Only worth taking if you are running drones at all. On a ship with no Drone Control the
  parts are dead weight you can sell, and fuel is the more urgent resource.
- Because the offer is visible before you accept, treat this as a store with one item and
  a randomised price — decline anything worse than about even. *Opinion*, from the ranges;
  no source rates it.
- Compare [[event-friendly-ship-out-of-fuel]], which charges the same 2–4 fuel for a much
  better expected return — but appears at distress beacons, not item beacons.

## Related
- [[event-friendly-ship-out-of-fuel]] — the other fuel-for-goods trade, randomised payout
- [[event-free-drone-schematic]] — the other drone-flavoured member of `ITEMS`
- [[item-drone-control]]
- [[concept-fuel]]

## Open Questions
- [ ] Whether the fuel cost and the drone-part return are rolled independently, or paired
      into a fair exchange rate.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `ITEMS` and `EXIT_LIST` pools)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml — the `ITEM_ZOLTAN` pool)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml — the `OVERRIDE_ITEMS` pool)
- [[source-fandom-trade-fuel-for-drone-parts]] (per raw/wiki/trade-fuel-for-drone-parts.md)
