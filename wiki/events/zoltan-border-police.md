---
id: event-zoltan-border-police
type: event
event_name: ZOLTAN_BOARDERS
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, boarding-hazard, default-rewards, forced-fight]
---

# Zoltan border police — `ZOLTAN_BOARDERS`

## Summary
An unavoidable boarding action: **3–4 Zoltan boarders** appear aboard your ship at the
same moment a Zoltan warship engages. No choices, no warning text, default rewards. The
larger of the sector's two boarding events.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-zoltan-border-police]]). The boarders are **not** signalled in advance.
- Reached via the `BOARDERS_ZOLTAN` event list, allocated `min=1 max=2` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]). That list has only three members —
  this event, [[event-mantis-outcasts]], and `BOARDERS_HACKING` — so a boarding beacon in
  a Zoltan sector is roughly a one-in-three shot at this specific event.
- `unique="true"` — at most once per sector.

## Text
> There are few more zealous in their customs checks than the Zoltan. A team of border
> police beam on board. There's just a little confusion over your weapons licences, but
> things escalate rapidly from heated discussion to gunfire!

(`event_ZOLTAN_BOARDERS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="ZOLTAN_SHIP" hostile="true"/>` + `<boarders min="3" max="4" class="energy"/>` — **3–4 Zoltan boarders aboard your ship** and a simultaneous fight with a Zoltan ship ([[entity-zoltan]]), **default rewards**. | 100% |

Both sources agree exactly on the boarder count: the game file says `min="3" max="4"`
and Fandom says *"3-4 zoltan boarders"*
([[source-events-zoltan]], [[source-fandom-zoltan-border-police]]).

## Blue Options
None. There is no dialogue, licence check, or bribe option — the event resolves straight
to combat.

## Rewards & Risks
- **Rewards:** default rewards for a Zoltan ship at the current sector depth. Nothing
  extra is granted for surviving the boarding.
- **Risks:**
  - 3–4 boarders is a large party — enough to take and hold a system room against a
    small crew. [[entity-zoltan]] boarders die in an explosion that damages the room
    they are in, so killing them near your own systems has a cost.
  - Because it fires with no preceding choice, there is no opportunity to vent rooms or
    reposition crew before the boarders land.
  - Fighting the ship and repelling boarders happen simultaneously, splitting your
    attention and your crew.

## Strategy Notes
- *Opinion:* this is the single most dangerous filler beacon in Zoltan space for a small
  or unarmoured crew. Unlike [[event-zoltan-security-checkpoint]], there is no dialogue
  branch that avoids it.
- Venting the boarded rooms to space is the standard answer and costs nothing but time;
  Zoltan boarders are individually weak in melee.
- A [[item-medbay]] chokepoint or [[item-mind-control]] on one boarder swings the fight
  quickly given the party size.

## Related
- [[event-mantis-outcasts]] — the other unique member of the `BOARDERS_ZOLTAN` pool,
  with a smaller but far deadlier boarding party
- [[event-zoltan-security-checkpoint]] — a Zoltan boarding fight you *can* talk your way
  out of
- [[entity-zoltan]] — the boarders and their death explosion
- [[entity-zoltan]] — the ship

## Open Questions
- [ ] Which `ZOLTAN_SHIP` blueprints spawn here at each sector depth.
- [ ] Whether the boarders arrive immediately or on a delay after the fight starts.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-border-police]] (per raw/wiki/zoltan-border-police.md)
