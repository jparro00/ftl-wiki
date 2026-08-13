---
id: event-zoltan-free-map
type: event
event_name: ZOLTAN_FREE_MAP
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, map-reveal, no-risk, free-item]
---

# Zoltan free map — `ZOLTAN_FREE_MAP`

## Summary
A free reveal of the entire current sector map, with no choices and no cost. Functionally
a one-shot [[item-long-ranged-scanners]] for the sector — most valuable early, when it
can reshape your whole route.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary, but **a friendly Zoltan ship is present** —
  `<ship load="ZOLTAN_SHIP" hostile="false"/>` — so Long-Ranged Scanners report a ship at
  this beacon even though nothing hostile happens
  ([[source-events-zoltan]], [[source-fandom-zoltan-free-map]]).
- Reached via the `ITEM_ZOLTAN` event list, allocated `min=1 max=2` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> The Zoltan stationed near this beacon are happy to receive you. As they give you the
> formal tour of their ship you spy some local star charts and mentally log the details.

(`event_ZOLTAN_FREE_MAP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<reveal_map/>` — **the current sector map is revealed**. A non-hostile Zoltan ship sits at the beacon and does nothing. | 100% |

## Blue Options
None.

## Rewards & Risks
- **Reward:** full sector map reveal. No scrap, fuel, or items.
- **Risk:** none. The Zoltan ship is loaded `hostile="false"` and no branch turns it
  hostile.

## Strategy Notes
- *Opinion:* value is highly position-dependent. Hit early in a sector, the reveal lets
  you plan around [[event-zoltan-fight-in-asteroid-field]] and the boarding beacons and
  route toward stores. Hit on your second-to-last jump, it is worth almost nothing.
- Redundant if you already carry [[item-long-ranged-scanners]] — though this reveals the
  whole map at once rather than adjacent beacons, so it is still strictly more
  information.
- The friendly ship makes this beacon indistinguishable from a hostile one on Long-Ranged
  Scanners, so a "ship detected" reading in a Zoltan sector is not automatically a fight.

## Related
- [[event-zoltan-free-augment]], [[event-zoltan-odd-moon]] — the other Zoltan members of
  the `ITEM_ZOLTAN` pool
- [[item-long-ranged-scanners]] — the persistent equivalent
- [[entity-zoltan]] — the (friendly) ship at the beacon

## Open Questions
- [ ] Does `<reveal_map/>` also reveal beacon *types*, or only the beacon layout?
- [ ] Why is a `ZOLTAN_SHIP` loaded at all when no branch uses it — purely for the
      Long-Ranged Scanners reading?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-free-map]] (per raw/wiki/zoltan-free-map.md)
