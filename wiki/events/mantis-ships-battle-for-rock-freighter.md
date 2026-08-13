---
id: event-mantis-ships-battle-for-rock-freighter
type: event
event_name: ROCK_MANTIS_FREIGHTER
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-repair-drone]], [[item-hull-repair-drone]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rock, mantis, blue-option, drone-parts, scrap-reward, unique, known-bug]
---

# Mantis ships battle for Rock freighter — `ROCK_MANTIS_FREIGHTER`

## Summary
Two Mantis ships are fighting over a crippled Rock freighter. You can wait and take on
the winner, walk away, or intervene with a drone. The **Repair Drone** blue option is the
standout: it pays `HIGH` scrap with **no fight at all**, making this one of the best
returns on a single drone part in the game — and per Fandom the part is not even
consumed under common conditions.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `NEUTRAL_ROCK`, allocated `min="7" max="8"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: **no ship marker on arrival** ([[source-fandom-mantis-ships-battle-for-rock-freighter]],
  `LRSmap=noship`) — the event has no top-level `<ship>` element ([[source-events-rock]])
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
> A curious sight greets you at this beacon: a disabled Rock freighter drifts in space
> while two Mantis craft battle it out - presumably over who deserves the spoils.

(`event_ROCK_MANTIS_FREIGHTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Wait, then attack the surviving Mantis. | — | Loads `eventList ROCK_MANTIS_FREIGHTER_LIST` (2 entries) — a fight with `MANTIS_ROCK_MANTIS_FREIGHTER` either way, but one entry cripples its weapons first. | 1/2 crippled |
| 2 | Ignore them. | — | *"There's quite enough action here already - prepare for light speed."* Nothing happens. | 100% |
| 3 | **(Repair Drone)** Repair the Rock ship. | `req="REPAIR"` | The Rock ship kamikazes both Mantis. `<autoReward level="HIGH">standard</autoReward>`; `<item_modify>` removes 1 drone part. **No fight.** | 100% |
| 4 | **(Hull Repair Drone)** Repair their hull. | `req="SHIP_REPAIR"` | The Rock ship chases one Mantis; the other turns on you. `<item_modify>` removes 1 drone part, then `<ship load="MANTIS_ROCK_MANTIS_FREIGHTER" hostile="true"/>`. | 100% fight |

### Choice 1 — `ROCK_MANTIS_FREIGHTER_LIST`
| Entry | Text | Effect |
|---|---|---|
| 1 | *"…the smaller ship gets the upper hand, but they must have blown a fuse… their weapons system is inoperable. Now is the time to attack!"* | `<ship load="MANTIS_ROCK_MANTIS_FREIGHTER" hostile="true"/>` **plus** `<status type="loss" target="enemy" system="weapons" amount="2"/>` — the enemy's Weapon Control is **down 2 power** |
| 2 | *"…when it comes to you they are of one mind… the larger one lets off a volley of fire and moves in to attack!"* | the same ship, at **full** weapons |

So choice 1 is a coin flip between a soft fight and a normal one.

### The enemy ship — `MANTIS_ROCK_MANTIS_FREIGHTER`
Defined inside `events_rock.xml` itself, not `events_ships.xml`
([[source-events-rock]]):
- `auto_blueprint="SHIPS_MANTIS"`
- Crew: 80% Mantis, 20% Engi (`<crewMember type="mantis" prop="0.80"/>`,
  `<crewMember type="engi" prop="0.20"/>`)
- **No `<surrender>` and no `<escape>` element** — it fights to the end.
  [[source-fandom-mantis-ships-battle-for-rock-freighter]] agrees, passing `|no|` to its
  surrender/escape template.
- `destroyed` and `deadCrew` both give
  `<autoReward level="MED">standard</autoReward>` and the same text: *"In the time it took
  you to eliminate the Mantis ship the Rock must have repaired their FTL drive and jumped
  away. You pick the bones of both Mantis vessels."*

## Blue Options
- **Repair Drone** (`req="REPAIR"`) — the best branch on the page: `HIGH` scrap with
  resources and no combat whatsoever. Requires owning a Repair drone *and* at least one
  drone part.
- **Hull Repair Drone** (`req="SHIP_REPAIR"`) — a strictly worse deal than choice 1 in
  isolation: it costs a drone part **and** gives you the same `MANTIS_ROCK_MANTIS_FREIGHTER`
  fight at full strength, with no weapons debuff and no extra reward. It exists as
  flavour, not as an upgrade.
- Both are gated on the *drone blueprint*, and both spend a drone part via `item_modify`
  ([[source-events-rock]]).

> ⚠️ **CONTRADICTION / suspected bug (drone part cost):**
> - Game files: choice 3 unconditionally contains
>   `<item_modify><item type="drones" min="-1" max="-1"/></item_modify>`, i.e. −1 drone
>   part ([[source-events-rock]]).
> - [[source-fandom-mantis-ships-battle-for-rock-freighter]]: *"Bugged: no drone part is
>   lost if the reward includes drone parts, though you still need at least 1 drone part
>   to choose this blue option."*
>
> These are not actually incompatible — Fandom is describing an interaction between
> `item_modify` and the `autoReward` payout, which the XML alone cannot show. Trusting the
> game files for what the event *declares* (−1 part) and recording Fandom's runtime claim
> alongside it. Untested here.

## Rewards & Risks
- Choice 3: **`HIGH`** scrap with resources, minus (nominally) 1 drone part, no risk.
- Choices 1 and 4: **`MED`** scrap with resources on winning the fight.
- Choice 2: nothing.
- Risk: only choices 1 and 4 fight, and the enemy is a stock `SHIPS_MANTIS` hull with a
  mostly-Mantis crew — dangerous to board, unremarkable to shoot.

## Strategy Notes
- Priority: **choice 3 > choice 1 > choice 2 > choice 4.** Choice 3 skips the fight for a
  bigger reward; choice 4 pays a drone part for nothing. *(Opinion, but it follows
  directly from the tables above.)*
- [[source-fandom-mantis-ships-battle-for-rock-freighter]] adds a combat note worth
  keeping: on the crippled-weapons branch, *"the disabled system levels serve as damage
  buffer, and the initially offline weapon can potentially be swapped to"* — i.e. the
  −2 weapons debuff degrades as the fight goes on rather than being permanent.

## Related
- [[event-mantis-ship-with-rock-body-parts]] — the other Mantis-in-Rock-space beacon
- [[item-repair-drone]], [[item-hull-repair-drone]], [[item-drone-parts]]
- [[entity-mantis]], [[entity-rock-men]]

## Open Questions
- [ ] Does the drone part actually get consumed on choice 3, and does it depend on whether
      the `HIGH` reward rolls drone parts?
- [ ] How long the `status type="loss"` weapons debuff persists once the enemy repairs.
- [ ] Whether `eventList` selection is uniform (the 1/2 figure depends on it).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-ships-battle-for-rock-freighter]] (per raw/wiki/mantis-ships-battle-for-rock-freighter.md)
