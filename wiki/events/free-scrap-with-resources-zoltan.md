---
id: event-free-scrap-with-resources-zoltan
type: event
event_name: ZOLTAN_DISTRESS_SHELL
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, distress, scrap-reward, no-risk, free-item]
---

# Free scrap with resources (Zoltan) — `ZOLTAN_DISTRESS_SHELL`

## Summary
An abandoned Zoltan freighter with nobody aboard. No choices, no cost, no catch — a
`RANDOM` scrap-with-resources payout for answering the distress call. The best possible
result from the sector's distress pool.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: **distress** (`<distressBeacon/>`), no ship on Long-Ranged Scanners
  ([[source-events-zoltan]], [[source-fandom-free-scrap-with-resources-zoltan]]).
- Reached via the `DISTRESS_BEACON_ZOLTAN` event list, allocated `min=1 max=2` beacons in
  both Zoltan sectors ([[source-sector-data-xml]]). That list has eight members, so
  hitting this one specifically is not likely.
- `unique="true"` — at most once per sector.

## Text
> You arrive to find a lumbering Zoltan freighter with no one at the helm. It's a mystery
> what happened to the crew, but it'd be a shame to let the opportunity go to waste.

(`event_ZOLTAN_DISTRESS_SHELL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `autoReward level="RANDOM"` `standard` — **a random amount of scrap with resources**. | 100% |

`RANDOM` is the game's own reward level, not a placeholder — it selects a tier at random
rather than naming one. Fandom's *"You receive a random amount of scrap with resources"*
matches exactly ([[source-events-zoltan]],
[[source-fandom-free-scrap-with-resources-zoltan]]).

## Blue Options
None.

## Rewards & Risks
- **Reward:** scrap plus resources (fuel, missiles and/or drone parts) at a randomly
  selected tier.
- **Risk:** none. There is no combat branch, no crew risk, and no trap variant — unusual
  for a distress beacon, where [[event-pirate-ship-distress-trap]] and similar exist elsewhere in the
  same pool.

## Strategy Notes
- *Opinion:* the free-money outcome of the Zoltan distress pool. Nothing to decide.
- Worth knowing that Zoltan distress beacons are **not** uniformly safe: the same
  `DISTRESS_BEACON_ZOLTAN` list also contains [[event-zoltan-ship-follows-mantis-ship]]
  (an asteroid-field fight) and generic entries including `TRAP_BEACON`. A distress
  signal in a Zoltan sector is a gamble, and this is the good end of it.

## Related
- [[event-zoltan-ship-follows-mantis-ship]] — the other unique
  `DISTRESS_BEACON_ZOLTAN` member, and a far riskier one
- [[event-zoltan-free-augment]] — the equivalent no-risk payout in the item pool

## Open Questions
- [ ] What tiers `autoReward level="RANDOM"` selects between, and with what weights.
- [ ] Which resources `standard` includes at each tier.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-free-scrap-with-resources-zoltan]] (per raw/wiki/free-scrap-with-resources-zoltan.md)
