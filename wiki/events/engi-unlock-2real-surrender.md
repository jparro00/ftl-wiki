---
id: event-engi-unlock-2real-surrender
type: event
event_name: ENGI_UNLOCK_2REAL_SURRENDER
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [orphan, chain, quest-marker, surrender]
---

# Engi unlock — real base surrender — `ENGI_UNLOCK_2REAL_SURRENDER`

## Summary
The surrender dialogue at the real Rebel base in [[chain-stealth-cruiser-unlock]]. Short and
entirely positive: the Rebel scout gives up the coordinates and the final quest marker is
placed. There is no choice to make — the single option advances the chain.

## Trigger & Where It Appears
- **Not in any sector event list.** It is loaded by the Rebel scout's surrender block at
  [[event-engi-unlock-2real]]: `<surrender min="5" max="5" load="ENGI_UNLOCK_2REAL_SURRENDER"/>`
  ([[source-events-xml]], per `raw/gamedata/events_ships.xml`).
- Beacon: **quest** — it happens in combat at the real quest-marker beacon.
- Fandom folds it into the "First Quest Marker (Real)" section of the chain walkthrough
  rather than treating it as its own event ([[source-fandom-engi-fleet-discussion]]).

## Text
> "Stop! This isn't worth dying for..."

(`event_ENGI_UNLOCK_2REAL_SURRENDER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Demand information on the stolen technology. | — | *"Of course, that's why you're here. Yes, they passed by here but I had nothing to do with it, I don't know what they were carrying. I'll transmit coordinates. Now just let us go..."* → `<quest event="ENGI_UNLOCK_3"/>` — the **final quest marker** is added to your map. | 100% |
| 1a | *(then)* Let them go. | — | *"You prepare an FTL message containing the coordinates to send to the Engi and get ready to jump."* → `<ship hostile="false"/>`; the fight ends. | 100% |

There is no "attack anyway" branch. The game file carries the removed alternative in a
comment, annotated *"REMOVED THIS TO PREVENT DOUBLE QUESTS"* — the cut choice would have let
you keep fighting after taking the coordinates ([[source-events-xml]], per
`raw/gamedata/events_engi.xml`). The decoy's surrender event
([[event-engi-unlock-2fake-surrender]]) still has both branches.

## Blue Options
None.

## Rewards & Risks
- The `ENGI_UNLOCK_3` quest marker. **No scrap** — the surrender route pays nothing, unlike
  the dead-crew route at [[event-engi-unlock-2real]], which grants `HIGH` scrap *and* the
  same marker ([[source-events-xml]]).
- No risk: the ship turns non-hostile and the encounter ends.

## Strategy Notes
- Reaching this event at all means the chain is safe. But note it is the *worse* of the two
  passing outcomes — forcing a surrender costs you the `HIGH` scrap that killing the crew
  would have paid. *(Opinion, derived from the two reward lines.)*
- Since the removed branch means you cannot resume the fight, there is no way to take the
  coordinates and then finish the ship for scrap.

## Related
- [[chain-stealth-cruiser-unlock]]
- [[event-engi-unlock-2real]] — the fight this resolves
- [[event-engi-unlock-2fake-surrender]] — the decoy's equivalent, which keeps both branches
- [[event-engi-unlock-3]] — the marker this places

## Open Questions
- [ ] Confirmed in play that the surrender route grants no scrap at all?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
