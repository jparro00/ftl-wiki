---
id: chain-tutorial
type: chain
trigger_event: [[[event-tutorial-start]]]
steps: [[[event-tutorial-start]], [[event-tutorial-enemy]], [[event-tutorial-missile]]]
sectors: []
reward: ""
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 3
tags: [tutorial, scripted, no-beacon, engine-invoked, onboarding]
---

# The tutorial

## Summary
Not a quest. The three `TUTORIAL_*` events are a **scripted onboarding sequence** the engine
runs outside the beacon system entirely — no `<quest>` markers, no `eventList` membership, no
`sector_data.xml` allocation. They are filed as a chain because they are an ordered sequence
that the wiki's event pages kept linking to as one, and because leaving three dangling
`[[chain-tutorial]]` links pointing at nothing was worse than saying plainly what they are.

Their real interest is documentary: **the tutorial is where the game states its own design
rules in its own words**, including the only in-game definition of a blue option.

## How It Starts
Engine-invoked when the player selects the tutorial. There is no beacon and no trigger event in
the ordinary sense — see the `beacon_type: unknown` convention in CLAUDE.md §2.1.

## Steps

1. **[[event-tutorial-start]]** (`TUTORIAL_START`) — the premise, delivered as three nested
   forced continues ([[source-events-xml]]):
   > *"Welcome to FTL! You are the captain of a Federation starship on a very important
   > mission."* → *"The Federation is currently being torn apart by vicious Rebels. Your ship
   > is carrying data vital to the defense of the Federation."* → *"You will be traveling
   > through dangerous sectors of the galaxy with the Rebel fleet in hot pursuit. Make it to
   > the exit beacon of each sector before the Rebels can catch you."*

   The last line is the game's own statement of its core loop, and the closest thing the data
   holds to a design brief.

2. **[[event-tutorial-enemy]]** (`TUTORIAL_ENEMY`) — a staged fight against `TUTORIAL_PIRATE`,
   used to explain the event interface: *"Every new location will have an event like this. You
   might have multiple choices available to you at an event."*

   It carries a `<choice req="sensors" lvl="1">` whose **label is the explanation itself**:

   > *"Special BLUE choices like these are unlocked by having certain upgrades or equipment.
   > They are nearly always a good choice."*

   This is the game's only in-fiction definition of the mechanic documented at
   [[concept-blue-options]] — and note it makes a claim the wiki has found to be false in at
   least one place: blue options are *not* nearly always a good choice. See
   [[chain-mantis-war-camp]], whose missile-weapon blue option is strictly worse than leaving.

3. **[[event-tutorial-missile]]** (`TUTORIAL_MISSILE`) — the missile-weapon lesson.

## Requirements
None. The `req="sensors" lvl="1"` gate on step 2 is satisfied by the tutorial ship's own
loadout, so the blue option always displays — it has to, since its purpose is to show the
player what one looks like.

## Reward
None. No `autoReward`, no items, no scrap anywhere in the sequence.

## Failure Modes
Not applicable. The sequence is scripted and the pirate is a set-piece.

## Strategy Notes
Nothing to play around. Recorded here so the three event pages have a parent, and so the
tutorial's own claims about blue options are on the record where they can be compared against
what the event pool actually does.

## Related
- [[concept-blue-options]] — the mechanic the tutorial defines, and overstates
- [[concept-rebel-fleet-advance]] — the pursuit the opening text describes
- [[event-start-beacon]] — the equivalent orientation text for an ordinary sector entry

## Open Questions
- [ ] Whether the tutorial is reachable at all in 1.6.x, or superseded by the AE hangar
      tutorial — no source here establishes which is used.
- [ ] What `TUTORIAL_PIRATE` is, mechanically, compared with an ordinary `SHIPS_PIRATE` draw.
- [ ] Whether `TUTORIAL_MISSILE` fires in sequence or is triggered by the player's actions.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
