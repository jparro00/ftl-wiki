---
id: event-rock-live-mine
type: event
event_name: ROCK_STARSHIP_MINE
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-engines]], [[item-missile-weapon]], [[item-beam-drone]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rock, crew-risk, hull-damage, breach, blue-option, clone-bay, unique, known-bug]
---

# Rock live mine — `ROCK_STARSHIP_MINE`

## Summary
A drilling mine latches onto your hull and you have to get it off. Without a blue option
this is one of the more punishing coin flips in the game: a crew member goes outside, and
a 50/50 decides between free scrap and *losing that crew member* plus 6 hull and a
breach. Engines 5 skips the whole thing; a missile or a beam drone caps the damage.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `NEUTRAL_ROCK`, allocated `min="7" max="8"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: no ship present ([[source-fandom-rock-live-mine]], `LRSmap=noship`); the event
  contains no `<ship>` element at any depth ([[source-events-rock]])
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
> The burnt out hull of a Rock mine layer drifts by. Behind the wreck drifts a live mine;
> an automated drone that drills into ships' hulls before exploding. It locks onto your
> ship's signature and heads your way!

(`event_ROCK_STARSHIP_MINE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

### Top level

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt evasive maneuvers. | — | *"The ship's turning circle proves too wide and the mine bites down onto the hull…"* → opens the three sub-choices below. **The evasion always fails** — this choice has no success branch. | 100% |
| 2 | **(Improved Engines)** Reverse thrusters! | `req="engines" lvl="5"` | *"It stresses the inertial dampeners, but you reverse course and outrun the mine."* Nothing happens — no damage, no reward. | 100% |

### After choice 1 — dealing with the attached mine

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Send someone out there to defuse it. | — | Loads `eventList ROCK_STARSHIP_MINE_DEFUSE` (2 entries) — see below. | 1/2 safe |
| 1b | **(Missile Weapon)** Attempt a controlled detonation using a missile. | `req="WEAPONS_MISSILES"` | `<damage amount="3"/>` + `<damage amount="1" system="random"/>` + `<autoReward level="LOW">scrap_only</autoReward>` + an `item_modify` intended to spend 1 missile (**bugged — see below**). | 100% |
| 1c | **(Beam Drone)** Use a drone to cut away the mine with a precision beam. | `req="COMBAT_BEAM_DRONE_LIST"` | *"…your beam drone removes the mine's grappling arms…"* → `item_modify` −1 drone part + `<autoReward level="LOW">scrap_only</autoReward>`. **No damage, no crew risk.** | 100% |

### Sub-event — `ROCK_STARSHIP_MINE_DEFUSE` (choice 1a)
| Entry | Text | Effect |
|---|---|---|
| 1 | *"…They make quick work of the basic device and return inside to relief all round. The mine makes good scrap pickings too."* | `<autoReward level="MED">scrap_only</autoReward>` |
| 2 | *"…When they open up the mine housing, though, they panic. The red wire or the blue?! 3... 2... 1..."* | offers two choices, **Red!** and **Blue!** — **both load the same `eventList ROCK_STARSHIP_MINE_DEFUSE2`** |

The red/blue choice is a **pure fake**. Both `<choice>` elements point at
`ROCK_STARSHIP_MINE_DEFUSE2`; the wire you pick has no effect whatsoever
([[source-events-rock]]).

### Sub-event — `ROCK_STARSHIP_MINE_DEFUSE2` (the wire cut)
| Entry | Text | Effect |
|---|---|---|
| 1 | *"You open your eyes and everything is still where it was a moment ago. You did it!"* | `<autoReward level="MED">scrap_only</autoReward>` |
| 2 | *"The weapon detonates… your bomb disposal volunteer spinning off toward a nearby sun."* | `<removeCrew>` — **lose the crew member** — plus `<damage amount="5"/>` and `<damage amount="1" system="room" effect="breach"/>` |

The `<removeCrew>` carries `<clone>true</clone>`: with a **Clone Bay** installed the lost
crew member is revived — *"Fortunately, your crewmember was close enough to the ship for
the Clone Bay to revive them. Sheepish and apologetic, they rejoin the crew."*
([[source-text-events-xml]], and [[source-fandom-rock-live-mine]] under
`Category:Clone Bay revival`).

## Blue Options
- **Engines level 5+** (`req="engines" lvl="5"`) — the only option that avoids the mine
  entirely. It also forfeits all scrap. Note the gate is the *system level*, not the
  Engines system itself.
- **Missile weapon** (`req="WEAPONS_MISSILES"`) — a weapon that fires missiles must be
  installed. [[source-fandom-rock-live-mine]] adds that the **Hull Missile does not
  satisfy it**; the game files give only the list name, not its contents.
- **Beam drone** (`req="COMBAT_BEAM_DRONE_LIST"`) — the best of the three risk-capping
  options: `LOW` scrap for one drone part and **zero** damage.
  [[source-fandom-rock-live-mine]] adds that the **Anti-Ship Fire Drone does not count**.

## Rewards & Risks
- Best realistic outcome: `MED` **scrap only** (no resources) from a successful defuse.
- Guaranteed-safe outcomes pay `LOW` scrap only (1b, 1c) or nothing (choice 2).
- Worst outcome: crew member dead, 6 hull damage total, and a breach.

> ⚠️ **CONTRADICTION (hull damage totals):**
> - Game files, missile option: two separate tags, `<damage amount="3"/>` **and**
>   `<damage amount="1" system="random"/>` ([[source-events-rock]]).
> - [[source-fandom-rock-live-mine]]: *"Your ship takes 4 hull damage, 1 damage to a
>   random system"*.
>
> Almost certainly not a real disagreement — a `<damage>` targeting a system also costs
> hull, so 3 + 1 = the 4 Fandom reports. The same pattern holds on the wire-cut failure:
> files say `amount="5"` + `amount="1" system="room" effect="breach"`, Fandom says
> *"6 hull damage, 1 damage with a breach to a random room"*. Recording both readings;
> Fandom's aggregate is the more useful number at the table, the files are the more
> precise description of the mechanism.

> ⚠️ **VERSION NOTE (`ae` vs `vanilla`):** both of the "extra" damage tags are marked
> `<!--DLC-->` inline in `raw/gamedata/events_rock.xml` ([[source-events-rock]]) — the
> random-system damage on the missile branch and the breach on the wire-cut failure. That
> comment marks them as **Advanced Edition additions**, so in vanilla this event was
> milder: 3 hull on the missile branch and 5 hull with no breach on the failure. Recorded
> as a version difference, not a contradiction. `version: ae` on this page describes the
> extracted 1.6.x build.

> ⚠️ **Suspected bug (missile not consumed):** the missile branch contains
> `<item type="missile" min="-1" max="-1"/>` — **singular** `missile`, where every other
> item_modify in the file uses the plural resource names (`missiles`, `drones`)
> ([[source-events-rock]]). [[source-fandom-rock-live-mine]] states the consequence
> outright: *"Due to a code error in the line … the missile weapon blue option does not
> waste a missile ammo."* The typo is confirmed in the game files; the *behaviour* is
> Fandom's claim and is untested here. Fandom further implies the option is selectable at
> 0 missiles, which is flagged as unconfirmed on its own page.

## Strategy Notes
- Priority: **Engines 5 > Beam Drone > Missile > defuse by hand.** Engines takes no
  damage; the beam drone takes none either but costs a part; the missile costs 4 hull and
  (per the bug) possibly nothing else; defusing by hand is a 50/50 on a crew member.
  *(Opinion, but it follows from the tables.)*
- Do not agonise over Red vs Blue — they are the same branch.
- With a Clone Bay the hand-defuse gamble changes character: the downside becomes 6 hull
  and a breach rather than a permanent crew loss.

## Related
- [[event-disabled-rock-ship]] — the other `NEUTRAL_ROCK` salvage-vs-risk beacon
- [[item-engines]], [[item-beam-drone]], [[item-missile-weapon]], [[item-clone-bay]]
- [[concept-crew-loss-risk]], [[concept-autoreward-tiers]]

## Open Questions
- [ ] Which weapons are in the `WEAPONS_MISSILES` list and which drones are in
      `COMBAT_BEAM_DRONE_LIST` — neither list is defined in `events_rock.xml`.
- [ ] Whether the missile blue option is selectable at 0 missiles (Fandom flags this as
      unresolved on its own page).
- [ ] Whether `eventList` selection is uniform (the two 1/2 splits depend on it).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-live-mine]] (per raw/wiki/rock-live-mine.md)
