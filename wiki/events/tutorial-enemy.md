---
id: event-tutorial-enemy
type: event
event_name: TUTORIAL_ENEMY
sectors: []
beacon_type: hostile
hostile: true
blue_options: [sensors 1]
chain: [[[chain-tutorial]]]
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, tutorial, engine-invoked, combat, blue-option, teaching-example]
---

# Tutorial enemy — `TUTORIAL_ENEMY`

## Summary
The tutorial's practice fight, and the game's only self-referential event: its second
choice is a blue option whose text *explains what blue options are*. The enemy is a
deliberately feeble 5-hull pirate, and the kill pays 100 scrap, 1 fuel, 3 missiles and a
**Halberd Beam** — the most generous single fight in the data files, because it is teaching
you what a reward screen looks like.

## Trigger & Where It Appears
- **Not in any sector event list.** Nothing in `raw/gamedata/` loads `TUTORIAL_ENEMY`; the
  id appears only in its own definition, its text entries, and the structure comment at the
  top of `events.xml` ([[source-events-xml]], [[source-text-events-xml]]). The engine
  invokes it as part of the tutorial.
- Second beat of the three-event tutorial set, after [[event-tutorial-start]].
- `version: unknown` — the data is unchanged across editions, but no source here says
  whether the Advanced Edition build still runs this sequence.
- No Fandom page joins this event.

## Text
> Every new location will have an event like this. You might have multiple choices available
> to you at an event. In this example, a weak pirate ship is trying to destroy you.

(`event_TUTORIAL_ENEMY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *Continue…* | — | `<event/>` — empty. You are dropped into the fight. | 100% |
| 2 | *"Special BLUE choices like these are unlocked by having certain upgrades or equipment. They are nearly always a good choice."* | `req="sensors" lvl="1"`, `hidden="true"` | `<event/>` — also empty. The choice exists purely to demonstrate the blue-option UI. | 100% |

Both choices lead to the same place: `<ship load="TUTORIAL_PIRATE" hostile="true"/>` on the
event body ([[source-events-xml]]).

### The enemy — `TUTORIAL_PIRATE`

Unusually, the `<ship>` block is defined **inline in `events.xml`** rather than in
`events_ships.xml`, and it uses a **fixed** `blueprint="TUTORIAL_PIRATE"` rather than an
`auto_blueprint` pool — so it is the same ship every time
([[source-events-xml]], [[source-blueprints]]):

| Stat | Value |
|------|-------|
| Class | Pirate |
| Hull | **5** |
| Max power | 11 |
| Crew | 1 human |
| Weapons | 1 × `LASER_BURST_1` |
| Systems | pilot 1, shields 4, engines 1, weapons 3, oxygen 2 |

It has no `<surrender>`, no `<escape>` and no `gotaway` — it cannot give up, flee, or be
avoided.

**Both** `destroyed` and `deadCrew` pay identically ([[source-events-xml]]):

> You destroyed the pirate ship. As salvage, you gain (from left to right) some Fuel,
> Missiles, Scrap and another weapon! Note the reward resource icons correspond to your
> reserves along the top of the screen.

- **1 fuel** (`min="1" max="1"`)
- **3 missiles** (`min="3" max="3"`)
- **100 scrap** (`min="100" max="100"`)
- **`BEAM_2`** — the **Halberd Beam** ([[source-text-blueprints]])

Every figure is a flat min=max, not a range — nothing is randomised.

## Blue Options
- **Sensors, level 1** (`req="sensors" lvl="1"`) — the only blue option in the game that
  does nothing mechanically. Its outcome is an empty `<event/>`; its purpose is to make the
  blue button appear so the tutorial can point at it. The requirement is level 1 Sensors,
  which the tutorial ship starts with (`PLAYER_SHIP_TUTORIAL` has
  `<sensors power="2" room="3" start="true"/>`, [[source-blueprints]]), so it is always
  visible.

## Rewards & Risks
- Reward: 100 scrap, 1 fuel, 3 missiles, Halberd Beam — flat, guaranteed, on either win
  condition.
- Risk: a 5-hull pirate with one Burst Laser I and 4 power in shields. It is armed enough to
  make the fight legible, not enough to be dangerous.

## Version differences
No `<!--DLC-->` markers on the event, the ship block, or the blueprint
([[source-events-xml]], [[source-blueprints]]). Identical data in
both editions; whether the sequence still runs is the open question.

## Related
- [[event-tutorial-start]] — the beat before
- [[event-tutorial-missile]] — the beat after, if you cannot get through the shields
- [[chain-tutorial]]
- [[concept-blue-options]] — the mechanic this event exists to teach
- [[item-halberd-beam]] — the reward

## Open Questions
- [ ] Does the Advanced Edition build still play this tutorial?
- [ ] Is `TUTORIAL_PIRATE`'s 4-power shield system actually powered during the fight? The
      blueprint allots it but the tutorial is scripted.
- [ ] Does the 100-scrap reward carry into a real run, or is the tutorial sandboxed?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
- [[source-text-blueprints]] (per `raw/gamedata/text_blueprints.xml`)
</content>
