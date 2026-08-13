---
id: event-tutorial-missile
type: event
event_name: TUTORIAL_MISSILE
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: [[[chain-tutorial]]]
version: unknown
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [orphan, tutorial, engine-invoked, weapon-reward, no-choice, teaching-example]
---

# Tutorial missile — `TUTORIAL_MISSILE`

## Summary
The tutorial's hand-out: a free **Artemis Missiles** launcher, given so the player can get
through the practice pirate's shields. The event exists to teach one thing — that events
can give you items — and says so in its own text.

## Trigger & Where It Appears
- **Not in any sector event list.** Nothing in `raw/gamedata/` loads `TUTORIAL_MISSILE`;
  the id appears only in its own definition and its text entry
  ([[source-events-xml]], [[source-text-events-xml]]). The engine invokes it during the
  tutorial.
- Third beat of the tutorial set, following [[event-tutorial-start]] and
  [[event-tutorial-enemy]]. Its text (*"Looks like you need some more help to get through
  his shields!"*) places it **after** the fight has started, not before it.
- `version: unknown` — the data is unchanged across editions, but no source here says
  whether the Advanced Edition build still runs this sequence.
- No Fandom page joins this event.

## Text
> Looks like you need some more help to get through his shields! Some events can provide
> items. This one is providing you with an Artemis Missile Launcher.

(`event_TUTORIAL_MISSILE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | `<weapon name="MISSILES_2_PLAYER"/>` — you are given the weapon outright. No choices, no other tags. | 100% |

### The weapon — `MISSILES_2_PLAYER`

Titled **Artemis Missiles** ([[source-text-blueprints]]). It is one of *two* Artemis
blueprints: `blueprints.xml` also defines a plain `MISSILES_2` with the same title,
description, damage, cost and rarity, but different handling ([[source-blueprints]]):

| | `MISSILES_2_PLAYER` (this event) | `MISSILES_2` (the normal Artemis) |
|---|---|---|
| Damage | 2 | 2 |
| Missiles per shot | 1 | 1 |
| Cooldown | **11** | **10** |
| Power | **1** | **2** |
| System points | 5 | 5 |
| Cost / rarity | 38 / 0 | 38 / 0 |

The tutorial version costs **half the power** in exchange for one second of cooldown —
generous, on a ship that has almost no reactor yet.

Despite the `_PLAYER` suffix this is **not** a tutorial-exclusive weapon. It is in the
`STARTING_WEAPONS` blueprint list and on the starting loadout of four player ship
blueprints, including `PLAYER_SHIP_EASY` (the Kestrel), and it is a member of the
`WEAPONS_MISSILES` and `WEAPONS_MISSILES_EVENTS` reward pools that events draw from
([[source-blueprints]], [[source-autoblueprints]], [[source-dlcblueprintsoverwrite]]). Both
Artemis variants are also listed at `rarity="0"` in `sector_data.xml`'s blueprint table
([[source-sector-data-xml]]).

The event text calls it an *"Artemis Missile Launcher"* while the blueprint title is
*"Artemis Missiles"* — a wording difference inside the game files, not a source conflict.

## Blue Options
None.

## Rewards & Risks
- Reward: the weapon, guaranteed. No scrap, no resources.
- No risk. The event has no ship, no damage and no crew tags.

## Version differences
No `<!--DLC-->` markers on the event or either blueprint
([[source-events-xml]], [[source-blueprints]]). Identical data in both editions; whether
the tutorial sequence still runs is the open question.

## Related
- [[event-tutorial-start]], [[event-tutorial-enemy]] — the rest of the sequence
- [[chain-tutorial]]
- [[item-artemis-missiles]] — the weapon

## Open Questions
- [ ] Does the Advanced Edition build still play this tutorial?
- [ ] What actually distinguishes `MISSILES_2_PLAYER` from `MISSILES_2` in the shop/reward
      UI, given identical titles and descriptions? A player receiving one from an event
      pool cannot tell which they got except by its power cost.
- [ ] Does the tutorial's inventory carry into a real run?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
- [[source-text-blueprints]] (per `raw/gamedata/text_blueprints.xml`)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml`)
- [[source-dlcblueprintsoverwrite]] (per `raw/gamedata/dlcBlueprintsOverwrite.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
</content>
