---
id: event-free-weapon
type: event
event_name: FIND_WEAPON
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-hidden-crystal-worlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [free-item, weapon, no-choice, no-risk, repeatable, item-event]
---

# Free weapon — `FIND_WEAPON`

## Summary
A pure gift beacon that hands you a weapon and a little scrap. No choices, no ship, no
risk. Structurally identical to [[event-free-drone-schematic]] but with a `weapon` payload
— and, unlike its two siblings, its text pool is the same in both editions.

## Trigger & Where It Appears
- Sectors: fifteen — everywhere except the **Zoltan** sectors, which draw from
  `ITEM_ZOLTAN` and do not include this event. See frontmatter for the full list.
- Pooled in the item lists `ITEMS`, `ITEMS_CRYSTAL` and `ITEMS_ENGI`, plus the Advanced
  Edition `OVERRIDE_ITEMS` replacement. Present in **both editions**
  ([[source-newevents]], [[source-events-crystal]], [[source-events-engi]],
  [[source-dlceventsoverwrite]]).
- **Not `unique`** — it can occur more than once in a run
  ([[source-events-xml]], [[source-fandom-free-weapon]]).
- Also reachable at an exit beacon, since `ITEMS` is a member of `EXIT_LIST`
  ([[source-newevents]], [[source-fandom-free-weapon]]).
- No ship at the beacon; Long-Range Scanners show nothing.

## Text
The intro prose is drawn from the `FIND_WEAPON` textList — `[varies: textList FIND_WEAPON]`
— six strings, **none of them DLC-marked**, so the pool is identical in vanilla and
Advanced Edition ([[source-events-xml]], [[source-text-events-xml]]):

1. *"Holy crap! A weapon is just floating in space!"*
2. *"You inform a nearby station of your flight from the Rebels. They offer to outfit your ship with a weapon and wish you well."*
3. *"A settlement still loyal to the Federation hails your ship. They have prepared a weapon to aid your escape from the Rebels."*
4. *"As soon as you arrive a small Mantis ship detaches from a wreck and jumps away. You must have interrupted their salvage operation because you find a weapon ready to be installed!"*
5. *"A small merchant ship messages you, 'Underground Federation comm channels are all talking about your "secret" mission. Let us install a weapon to help. Good luck!'"*
6. *"Debris from a battle is scattered around this system. A few pieces bounce against your ship. You passively scan them and discover there is a functioning weapon among them!"*

Assuming uniform selection across list entries, each is 1/6. Several strings carry
background art hints in the file (`planet="NONE"`, `back="BG_NEBULA"`, and so on) that do
not affect the outcome.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event body is a text load and a reward)_ | — | `<autoReward level="LOW">weapon</autoReward>` — **a weapon with low scrap.** | 100% |

`weapon` is the `autoReward` payload type and `LOW` is the game's own tier word. Fandom's
gloss is *"a weapon with low scrap"* ([[source-fandom-free-weapon]]).

## Blue Options
None.

## Rewards & Risks
- **Reward:** one weapon plus a low tier of scrap. Which weapon is not stated by any source
  here — the engine draws it.
- **Risk:** none.
- Caveat: with no free weapon slot the weapon is broken down for scrap instead; that is
  what the `EQUIP_FULL` system message covers ([[source-events-xml]]).

## Strategy Notes
- Nothing to decide. Its weight is in the sector pools: this is one of the ways a run picks
  up a second or third weapon without paying a store price.
- Worth noting for routing that the **Zoltan sectors cannot roll it** — `ITEM_ZOLTAN`
  contains `FIND_DRONE`, `FREE_ITEMS` and `FUEL_FOR_DRONE` but not `FIND_WEAPON`
  ([[source-events-zoltan]]). If you are hunting weapons, Zoltan space is the wrong place.

## Related
- [[event-free-drone-schematic]] — the drone-flavoured twin, same shape
- [[event-free-scrap-with-resources]] — the scrap-flavoured twin
- [[concept-autoreward-tiers]]

## Open Questions
- [ ] What `autoReward level="LOW"` of type `weapon` pays in scrap, and how the weapon
      blueprint is drawn.
- [ ] Whether the weapon pool is rarity-weighted or sector-scaled.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `ITEMS` and `EXIT_LIST` pools)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml — the `ITEMS_CRYSTAL` pool)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — the `ITEMS_ENGI` pool)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml — the `ITEM_ZOLTAN` pool it is *absent* from)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml — the `OVERRIDE_ITEMS` pool)
- [[source-fandom-free-weapon]] (per raw/wiki/free-weapon.md)
