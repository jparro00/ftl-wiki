---
id: event-dock-bomb-salesman
type: event
event_name: DOCK_BOMB_SALESMAN
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unreachable, cut-content, weapons, missiles, trading, pirate, ambush-risk, ae]
---

# Pirate bomb salesman — `DOCK_BOMB_SALESMAN`

## Summary
A fully authored weapons shop — missiles, a cheap bomb launcher, an expensive missile
launcher — that **cannot be reached in normal play**. It is the twin of
[[event-dock-drone-salesman]] and was written to share the same pool, but its only list
entry is commented out, leaving the drone shop as the pirate salesman's sole outcome. Two
blueprint lists exist in the game files for the express purpose of stocking it, and both
are now dead weight.

## Trigger & Where It Appears
- **Unreachable.** `DOCK_BOMB_SALESMAN` appears exactly twice in `raw/gamedata/`: its own
  definition, and one list entry that is **commented out**
  ([[source-newevents]]):
  ```
  <eventList name="DOCK_PIRATE_SALESMAN">
      <!--<event load="DOCK_BOMB_SALESMAN"/>-->
      <event load="DOCK_DRONE_SALESMAN"/>
  </eventList>
  ```
- With that line disabled, `DOCK_PIRATE_SALESMAN` has one live member and
  [[event-dock-drone-salesman]] fires 100% of the time you dock with the pirate salesman.
  Had the line been live, the two shops would presumably split the pool.
- **This is cut content, not merely orphaned.** The comment-out is a deliberate edit in a
  live list, and the two weapon pools it draws from are annotated in `autoBlueprints.xml`
  with `<!-- USED IN EVENT DOCK_BOMB_SALESMAN -->` above each — the blueprint lists survive
  in the shipped data even though nothing can now call them
  ([[source-autoblueprints]]).
- No Fandom page exists for it, consistent with it never firing in play.
- Sectors, beacon type, and long-range-scanner appearance: **unknown** — it never appears.
- Would have been Advanced Edition content: it sits in the `DLC!!!` block of
  `newEvents.xml`, immediately after the drone salesman.

## Text
> A human in an exquisite suit meets you on board. "Welcome to my ship! We specialize in
> explosives of all kinds, can I interest you in any?"

(`event_DOCK_BOMB_SALESMAN_text`, per [[source-text-events-xml]] — the string is present
in the shipped string table despite the event being unreachable.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Buy some missiles. | — | −10 scrap, **+5 missiles**. Fixed price. | 100% |
| 2 | Buy a bomb launcher. | — | −40 to −60 scrap, `weapon name="WEAPONS_BOMBS_CHEAP"` — a random draw from `BOMB_ION`, `BOMB_1`, `BOMB_BREACH_1`. | 100% |
| 3 | Buy a rocket weapon. | — | −50 to −60 scrap, `weapon name="WEAPONS_MISSILES_EXPENSIVE"` — a random draw from `MISSILES_3`, `MISSILES_BURST`, `MISSILES_BREACH`. | 100% |
| 4 | Buy nothing. | — | *"Ah, I'm sorry to hear that! Pleasant journeys." Once back to the helm, a series of explosions rocks your ship. The pirate ship has powered its weapons!* → **`ship load="PIRATE" hostile="true"`**, plus `damage amount="1" system="engines" effect="random"` and two × `damage amount="1" system="room" effect="random"`. | 100% |

Choices 2 and 3 draw from `blueprintList`s, so the specific weapon **varies**; the three
members of each list are given above from `autoBlueprints.xml`
([[source-autoblueprints]]). Which member is selected, and whether the draw is uniform, is
not stated.

The "buy nothing" punishment is byte-for-byte the same construction as the drone
salesman's, minus one line of taunt text — the two events were clearly written together.

## Blue Options
None. Unlike the drone shop, this event has no `req` on any choice at all.

## Rewards & Risks
- **Missiles:** +5 for a flat 10 scrap — half what the drone shop charges for 5 drone
  parts.
- **Bomb launcher:** 40–60 scrap for one of `BOMB_ION` (**Ion Bomb**), `BOMB_1` (**Small
  Bomb**) or `BOMB_BREACH_1` (**Breach Bomb Mark I**) ([[source-text-blueprints]]).
- **Rocket weapon:** 50–60 scrap for one of `MISSILES_3` (**Hermes Missile**),
  `MISSILES_BURST` (**Pegasus Missile**) or `MISSILES_BREACH` (**Breach Missiles**)
  ([[source-text-blueprints]]).
- **Risk:** the "buy nothing" exit, identical to the drone shop's — 3 points of system
  damage across engines and two random rooms with random secondary effects, then a
  `PIRATE` fight (`surrender chance="0.5" min="3" max="4"`, `escape chance="0.5" min="2"
  max="4"`, default rewards, per [[source-events-ships]]).
- **Actual risk in play: none.** You cannot reach this screen.

## Strategy Notes
- Nothing actionable. Recorded so the shipped content is visible rather than silently
  dropped, and so the `DOCK_PIRATE_SALESMAN` pool is documented as single-membered rather
  than assumed to be a coin flip.
- The practical consequence for play is on the *other* page: because this entry is
  disabled, docking with the pirate salesman is a guaranteed drone shop. A player looking
  for weapons there will never find them.
- `WEAPONS_BOMBS_CHEAP` and `WEAPONS_MISSILES_EXPENSIVE` are referenced by no other event
  in `raw/gamedata/`, so both blueprint lists are effectively dead data.

## Related
- [[event-dock-drone-salesman]] — the surviving twin, and the sole live member of the pool
- [[event-pirate-ship-selling-drones]] — `PIRATE_SALESMAN`, the beacon that would have led here
- [[event-pirate-ship-selling-drones]] — `CONTACT_PIRATE_SALESMAN`, the docking step
- [[event-asteroid-mining-colony]] — the AE event that *takes* missiles, where this one
  would have sold them
- [[entity-pirates]]

## Open Questions
- [ ] Why the entry was disabled — no dev note explains it. Balance, bugs, or an
      unfinished shop UI are all consistent with the evidence, and none is stated.
- [ ] Whether it was ever live in a shipped build. The AE `<!--DLC-->` annotations do not
      cover this line, and no pre-AE copy of `newEvents.xml` is available here.
- [ ] Whether `weapon name="<blueprintList>"` selection is uniform across the three
      members.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
