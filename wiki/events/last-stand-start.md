---
id: event-last-stand-start
type: event
event_name: LAST_STAND_START
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [endgame, last-stand, orphan, scripted, hull-repair, free-resources, federation]
---

# Last Stand start — `LAST_STAND_START`

## Summary
The scripted arrival event of [[sector-the-last-stand]]: you dock at a Federation outpost,
brief Admiral Tully's war room, and are sent off with a full tank and a patched hull. It is
the only place in the game where the Federation acknowledges your mission, and it hands
over **+10 fuel and +10 hull** for free before the Flagship sequence begins.

## Trigger & Where It Appears
- **Orphan in the data.** `LAST_STAND_START` appears in **no `eventList` and no
  `sectorDescription`** — the only reference to the name anywhere in `raw/gamedata/` is its
  own definition ([[source-events-boss]], [[source-sector-data-xml]]). It is invoked by the
  game's endgame scripting, not by the beacon-allocation system.
- The XML comment states the trigger explicitly: *"the first time you arrive at the base,
  before the rebel fleet arrives."*
- `<fleet>fed</fleet>` — the Federation fleet fills the background.
- The `FINAL` sector's own `startEvent` is `BOSS_NEUTRAL`, which the file itself annotates
  *"STUPID, since it's starting you at the 'exit'"* ([[source-sector-data-xml]]) — so this
  event is not the sector's start beacon in the allocation sense.

## Text
> You arrive at an outpost close to the Federation Base. Your access codes get you past
> initial security and an officer sets up a direct feed to the Federation Base's war room.
> Admiral Tully speaks first saying, "What is the meaning of this?! Who are you?"

(`event_LAST_STAND_START_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Explain your mission. | — | *"Your explanation is met with murmurs of cynicism and disbelief among the officers. General Turzil of the Engi Brigade speaks up, 'Intel suggests potential counter to Rebel technology. Risk all or save none.'"* → leads to the single follow-up below. | 100% (only choice) |
| 1.1 | Explain the weakness of the enemy fleet, the Rebel flagship. | `hidden="true"` | Tully's reply (below) → `<item_modify><item type="fuel" min="10" max="10"/></item_modify>` = **+10 fuel**, and `<damage amount="-10"/>` = **+10 hull**. | 100% (only continuation) |

> Tully responds, "It's settled. The Rebels will be here in a matter of moments. We will do
> what we can to hold off their warships but you must succeed in destroying this flagship.
> Your current outpost can provide some repairs and fuel, and the other repair stations can
> provide aid as well. Good luck."

(`event_LAST_STAND_START_c1_c1_text`, per [[source-text-events-xml]])

There is no branch and no failure state: the event is a two-step corridor to a fixed
reward.

## Blue Options
None.

## Rewards & Risks
- **+10 fuel**, **+10 hull**. Unconditional ([[source-events-boss]]).
- No risk — no ship, no negative branch.
- Tully's line is also the in-fiction pointer to
  [[event-repair-station-in-last-stand]]: *"the other repair stations can provide aid as
  well."*

## Strategy Notes
- The +10 fuel matters: the Last Stand has no fuel pressure of its own, but arriving with a
  near-empty tank from the previous sector is survivable because of this event.
  *(Reading of the reward, not a sourced strategy claim.)*

## Related
- [[sector-the-last-stand]] — the sector this opens
- [[event-federation-base]] — the arrival text at the base itself
- [[event-repair-station-in-last-stand]] — the "other repair stations" Tully mentions
- [[event-boss-text-1]] — the next scripted beat, the Flagship's first phase
- [[chain-the-flagship]]
- [[entity-federation]], [[entity-engi]]

## Open Questions
- [ ] What exactly fires this event — arrival at the sector, or arrival at a specific
      beacon. The data files only carry the developer comment.
- [ ] What `START_BEACON_BOSS` (listed in the file's header comment but never defined) was
      meant to be; it may be this event's original name.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
