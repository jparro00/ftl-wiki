---
id: event-unlock-stealth
type: event
event_name: UNLOCK_STEALTH
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unreachable, cut-content, orphan, ship-unlock, stealth-cruiser]
---

# Unlock Stealth (unused) — `UNLOCK_STEALTH`

## Summary
A shipped, fully-written one-line event announcing that you have found a hidden Federation
research lab and downloaded its ship blueprints — an earlier, simpler way to unlock the
Stealth Cruiser. **Nothing in the 1.6.x game data references it.** The live unlock runs
through the Engi Homeworlds quest chain instead. Documented here because it is authored
content that shipped, not because it can be played.

## Trigger & Where It Appears
- **No trigger.** A grep of every file in `raw/gamedata/` for `UNLOCK_STEALTH` returns
  exactly one hit: the definition itself, at `newEvents.xml` line 430
  ([[source-newevents]]). It is in no event list, no `sector_data.xml` allocation, no
  `<quest>` target, and no ship block. That is positive evidence of unreachability, not
  merely a missing sector allocation ([[concept-sector-event-allocation]]).
- It sits in `newEvents.xml` under the header *"SYSTEM — Some test/system events"*,
  between `ASTEROID_TEST` and `CASH_IN_DRONE` ([[source-newevents]]). Its neighbours are
  developer scaffolding; unlike them, this one carries in-world prose and reads as a real
  beacon narration, which is why it gets a page rather than being dropped as a system
  message.
- No Fandom page joins this event; the community wiki does not document it.

## Text
> You stumble across a hidden Federation research laboratory! They have been experimenting
> with some unique ship designs. You download their blueprints for future use.

The string is written **inline** in `newEvents.xml` rather than referenced from
`text_events.xml` — the same pattern as the other events in the SYSTEM block, and unlike
almost every live event ([[source-newevents]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | Nothing. The event body is a single `<text>` element — **no `<unlockShip>`, no reward, no ship, no choice**. | — |

This matters: even if the engine could reach it, the event as written would *not* unlock
anything. Whatever mechanism it belonged to must have applied the unlock elsewhere.

## Blue Options
None.

## How the Stealth Cruiser is actually unlocked
- `blueprints.xml` gives the ship's own unlock hint:
  *"This ship is being built near the Engi homeworlds. To unlock it you'll need to help
  them, but they only trust their own kind."*
  (`ship_PLAYER_SHIP_STEALTH_unlock`, per [[source-text-blueprints]])
- That points at [[chain-stealth-cruiser-unlock]], whose payoff event
  [[event-engi-unlock-4]] carries the actual `<unlockShip id="1"/>`
  ([[source-events-engi]]).
- The `PLAYER_SHIP_STEALTH_2` layout is instead gated on achievements
  (*"Complete 2/3 of the Stealth Cruiser Achievements to unlock this ship."*,
  [[source-text-blueprints]]), and `PLAYER_SHIP_STEALTH_3` is an Advanced Edition addition
  in `dlcBlueprintsOverwrite.xml`.

So the unlock this event was presumably written for exists and is live — it just does not
run through here.

## Rewards & Risks
Neither. The event has no mechanical payload of any kind.

## Strategy Notes
Nothing to play. The practical value of this page is negative: if you are hunting for a
"hidden Federation research laboratory" beacon to unlock the Stealth Cruiser, **it does not
exist in the shipped game** — go to the Engi Homeworlds and run
[[chain-stealth-cruiser-unlock]].

## Related
- [[chain-stealth-cruiser-unlock]] — the live route to this ship
- [[event-engi-unlock-4]] — where `<unlockShip id="1"/>` actually fires
- [[concept-sector-event-allocation]] — the standard for calling something unreachable

## Open Questions
- [ ] Was this ever live in a pre-1.0 or demo build? The neighbouring `STEALTH_1`–
      `STEALTH_7` events are explicitly labelled "Old events for the Original Demo", which
      suggests the whole block is legacy.
- [ ] Is there an engine-side call by name (the way `NEUTRAL` and `NEUTRAL_EXIT` are
      called) that could still reach it? Nothing in the data suggests one, but the
      possibility cannot be closed from files alone.
- [ ] Did the unlock originally fire from a wrapper event that loaded this one for text?

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
