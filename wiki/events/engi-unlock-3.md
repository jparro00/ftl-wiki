---
id: event-engi-unlock-3
type: event
event_name: ENGI_UNLOCK_3
sectors: []
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, chain, quest-marker, forced-fight]
---

# Engi unlock — the cargo escort — `ENGI_UNLOCK_3`

## Summary
Step 3 of [[chain-stealth-cruiser-unlock]]: you catch the stolen-technology convoy, an Engi
pirate squadron jumps in to help, and you fight one Mantis-hulled ship that turns out to be
crewed by Rebels. Unlike step 2, nothing here can fail the chain — every victory outcome
leads to [[event-engi-unlock-4]].

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via the final quest marker, placed either by
  [[event-engi-unlock-2real-surrender]] or by killing the crew at
  [[event-engi-unlock-2real]] — both carry `<quest event="ENGI_UNLOCK_3"/>`
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml` and
  `raw/gamedata/events_ships.xml`).
- Beacon: **quest**.

## Text
> You have finally caught up with the ships you've been hunting. A hangar-sized cargo ship is
> being escorted by a number of Mantis ships. As you reconsider the assault, a squadron of
> Engi ships with pirate emblems jump in and assist you. You prepare to fight the Mantis but
> scans indicate they are manned by Rebels!

(`event_ENGI_UNLOCK_3_text`, per [[source-text-events-xml]])

## Choices & Outcomes

No choices — the event loads `<ship load="MANTIS_ENGI_UNLOCK_3" hostile="true"/>` immediately.

| Ship outcome | Definition | Result |
|---|---|---|
| **Destroyed** | `<destroyed load="ENGI_UNLOCK_4"/>` | Straight to [[event-engi-unlock-4]]. **No `autoReward`** — no scrap for this outcome. |
| **Dead crew** | `<autoReward level="MED">standard</autoReward>`, then continue → `ENGI_UNLOCK_4` | `MED` scrap with resources, *then* [[event-engi-unlock-4]]. |

The enemy is a Mantis hull (`auto_blueprint="SHIPS_MANTIS"`) with `<crewMember type="human"/>` —
matching the intro text's "scans indicate they are manned by Rebels". It has no `<surrender>`
and no `<escape>` block ([[source-events-xml]], per `raw/gamedata/events_ships.xml`;
corroborated by [[source-fandom-engi-fleet-discussion]]).

Despite the prose describing "a number of Mantis ships" and an allied Engi squadron, only
**one** enemy ship is loaded. The fleet action is narrative, resolved off-screen at
[[event-engi-unlock-4]].

## Blue Options
None.

## Rewards & Risks
- `MED` scrap with resources **only** on the dead-crew outcome; destroying the hull pays
  nothing at this step.
- No way to fail the chain here — both victory outcomes route to
  [[event-engi-unlock-4]]. The only failure mode is losing the fight.

## Strategy Notes
- Killing the crew rather than the hull is worth `MED` scrap that is otherwise simply not
  awarded. Against a human crew on a Mantis hull, that is a realistic target for boarders or
  an anti-personnel weapon. *(Opinion, derived from the two outcome blocks.)*
- Arrive with hull to spare: the payoff at [[event-engi-unlock-4]] includes 20 repairs, so
  taking damage here is partly refunded. *(Opinion.)*

## Related
- [[chain-stealth-cruiser-unlock]] — this is step 3 of 4
- [[event-engi-unlock-2real]], [[event-engi-unlock-2real-surrender]] — the two routes that place this marker
- [[event-engi-unlock-4]] — the payoff, reached from either outcome
- [[entity-mantis]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Is the enemy ship's difficulty scaled by sector, or fixed?
- [ ] Does the allied Engi squadron have any mechanical effect during the fight?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
