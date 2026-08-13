---
id: event-start-beacon-crystal
type: event
event_name: START_BEACON_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-crystal-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [crystal-route, start-beacon, quest-marker, no-choices]
---

# Start beacon (Crystal) — `START_BEACON_CRYSTAL`

## Summary
The arrival beacon of [[sector-hidden-crystal-worlds]] and the hinge between steps 3 and 4
of [[chain-crystal-cruiser-unlock]]. It is pure plumbing: your Crystalline companion keeps
his side of the bargain and forwards the coordinates of his old ship, which plants the
quest marker for [[event-crystal-unlock]] on the sector map.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] — it is that sector's `<startEvent>`, so it
  fires automatically at the first beacon on arrival, every time
  ([[source-sector-data-xml]]).
- Not in any event list and not pool-allocated; it cannot be rolled at a random beacon
  ([[source-events-xml]]).
- Prerequisite: being in the sector at all, which means the Crystal-crew blue option at
  [[event-ancient-device]] ([[source-fandom-ancient-device]]).
- It has no Fandom page of its own — the community wiki documents it as the "Hidden Crystal
  Worlds" section of the *Ancient device* page ([[source-fandom-ancient-device]]).

## Text
> You arrive in a sector not listed in any star charts. Strange crystalline ships dot the
> horizon. Your companion speaks, "Here we are, my home sector. It has been a long time
> since others have set foot here, I wonder how you will be received."

(`event_START_BEACON_CRYSTAL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Continue. | — | *"You have done as you promised and so shall I. The coordinates of my old ship have been forwarded to your navigation system."* → `<quest event="CRYSTAL_UNLOCK"/>` — **a quest marker for [[event-crystal-unlock]] is added to your map.** | 100% |

The only choice node uses the shared `continue` string, so it is a single unavoidable
click. ([[source-events-xml]])

## Blue Options
- None.

## Rewards & Risks
- No scrap, fuel, damage or crew effects — the entire mechanical payload is the `quest`
  tag.
- No risk. There is no ship at this beacon and no hostile branch.

## Strategy Notes
- The marker is what makes the sector navigable with a purpose: without it you would be
  searching 20-odd beacons blind. Getting the map revealed early — for instance via
  [[event-federation-deserters]] — pairs well with it. *(Opinion.)*
- Note that the `quest` tag fires unconditionally in the file, with no `req` on Ruwen or on
  Crystal crew. That matters for the Rock Cruiser Layout C / already-unlocked Crystal
  Cruiser shortcut described on [[chain-crystal-cruiser-unlock]]: those routes enter the
  sector without completing steps 1–2, and nothing in this event appears to gate the
  marker. **Unconfirmed** — no source states the outcome for that route.

## Related
- [[chain-crystal-cruiser-unlock]] — this sits between step 3 and step 4
- [[event-ancient-device]] — step 3, the wormhole that brings you here
- [[event-crystal-unlock]] — step 4, the marker this event plants
- [[sector-hidden-crystal-worlds]] — the sector whose `startEvent` this is

## Open Questions
- [ ] Whether the quest marker is placed on a random beacon or a deterministic one.
- [ ] Whether entering the sector via the shortcut routes still yields the marker (see
      Strategy Notes).
- [ ] Whether the marker can be lost to Rebel fleet advance before you reach it.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md)
