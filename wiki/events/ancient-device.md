---
id: event-ancient-device
type: event
event_name: ROCK_CRYSTAL_BEACON
sectors: [[[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [crystal crew]
chain: [[[chain-crystal-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [crystal-route, ship-unlock, unique, blue-option]
---

# Ancient device — `ROCK_CRYSTAL_BEACON`

## Summary
A guaranteed beacon in the [[sector-rock-homeworlds]] and the third step of
[[chain-crystal-cruiser-unlock]]. Without a Crystal crew member it is an ordinary
scrap-or-leave choice; with one it opens the wormhole to
[[sector-hidden-crystal-worlds]].

## Trigger & Where It Appears
- Sector: [[sector-rock-homeworlds]] only
- Guaranteed: `sector_data.xml` allocates `ROCK_CRYSTAL_BEACON` at `min=1 max=1`
  ([[source-sector-data-xml]])
- Beacon: normally an ordinary beacon; becomes a **quest beacon** if you carry the
  Crystal crew member from the Stasis Pod (Ruwen) ([[source-fandom-ancient-device]])

## Text
> An ancient device is orbiting within the crystal rings of a nearby gas giant. You
> can't discern its nature or function, but it seems to have been deactivated for a
> very long time. Perhaps you can get some scrap from it.

(`event_ROCK_CRYSTAL_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Scrap it. | — | (a) "You break it apart and take it for scrap." → high scrap. (b) A Rock military ship jumps in → fight a Rock ship, default rewards. | unknown |
| 2 | Leave it alone. | — | "Better not risk it." → nothing happens. | 100% |
| 3 | **(Crystal Crew)** Reactivate it. | `req="crystal"` | Device powers on, +1 fuel, a wormhole forms → you jump to [[sector-hidden-crystal-worlds]] (−1 fuel). | 100% |

Choice 1 branches through a sub-event list, `ROCK_CRYSTAL_BEACON_LIST`; the split
between the two outcomes is **not stated in the game files as a percentage** and no
source here gives odds. ([[source-events-xml]])

## Blue Options
- **Crystal crew member** (`req="crystal"`) — the only way to reach
  [[sector-hidden-crystal-worlds]] through this event. *Any* Crystal crew member
  satisfies the requirement, but only Ruwen (from the Stasis Pod) also converts the
  beacon into a marked quest beacon. ([[source-fandom-ancient-device]])

## Rewards & Risks
- Choice 1: high scrap, or a Rock ship fight with default rewards.
- Choice 3: +1 fuel, then −1 fuel for the wormhole jump; net zero, and it consumes the
  jump. ([[source-fandom-ancient-device]])
- Risk: choice 1 can start a fight. Choice 3 leaves the normal sector map behind — on
  exiting the Crystal sector you do not get to pick your next sector.

## Strategy Notes
- If the Crystal chain is live, this is the payoff beacon and the Rock Homeworlds are
  worth routing into. If it is not, this is an ordinary scrap event.
- Taking choice 1 does not appear to break the chain — but that is untested here.

> ⚠️ **CONTRADICTION:** the wording of the choice-3 outcome differs between sources.
> - Game files: *"It looks like we have found the abandoned link to **the Crystal home
>   worlds**. I can reactivate it."* ([[source-text-events-xml]], per
>   raw/gamedata/text_events.xml)
> - Fandom: *"It looks like we have found the abandoned link to **my home worlds**. I
>   can reactivate it."* ([[source-fandom-ancient-device]])
>
> Trusting the game files — reliability `high` vs `medium`, and they are the exact 1.6.x
> build being played. Most likely the wiki transcribes pre-AE wording. Not yet
> confirmed as a version difference.

## Related
- [[chain-crystal-cruiser-unlock]] — this is step 3 of 4
- [[event-crystal-unlock]] — step 4, the payoff
- [[sector-hidden-crystal-worlds]] — where choice 3 sends you
- [[item-crystal-vengeance]] — awarded at the end of the chain

## Open Questions
- [ ] Odds of the fight-vs-scrap split on choice 1.
- [ ] Exact scrap value of "high scrap".
- [ ] Does taking choice 1 (or fighting) lock you out of choice 3 on a revisit?
- [ ] Is the text discrepancy above a vanilla/AE difference or a wiki error?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md)
