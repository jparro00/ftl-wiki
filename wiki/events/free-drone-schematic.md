---
id: event-free-drone-schematic
type: event
event_name: FIND_DRONE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-hidden-crystal-worlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [free-item, drone, no-choice, no-risk, repeatable, item-event]
---

# Free drone schematic — `FIND_DRONE`

## Summary
A pure gift beacon: you arrive, you are handed a drone schematic and a little scrap, and
that is the whole event. No choices, no ship, no risk. It is one of the four members of
the `ITEMS` allocation pool that every sector draws from, so it is one of the most common
things that can happen in a run.

## Trigger & Where It Appears
- Sectors: seventeen, effectively everywhere including
  [[sector-hidden-crystal-worlds]] — see frontmatter for the full list.
- Pooled in the item lists `ITEMS`, `ITEMS_CRYSTAL`, `ITEMS_ENGI` and `ITEM_ZOLTAN`, plus
  the Advanced Edition `OVERRIDE_ITEMS` replacement. Present in **both editions**
  ([[source-newevents]], [[source-events-crystal]], [[source-events-engi]],
  [[source-events-zoltan]], [[source-dlceventsoverwrite]]).
- **Not `unique`** — it can occur more than once in a run
  ([[source-events-xml]], [[source-fandom-free-drone-schematic]]).
- Also reachable at an exit beacon (`alsooccur=exit`, and `ITEMS` is a member of
  `EXIT_LIST`) ([[source-newevents]], [[source-fandom-free-drone-schematic]]).
- No ship at the beacon; Long-Range Scanners show nothing.

## Text
The intro prose is drawn from the `FIND_DRONE` textList — `[varies: textList FIND_DRONE]`.
Six strings in Advanced Edition, five in vanilla ([[source-text-events-xml]]):

1. *"When you ask a nearby station for aid, a friendly programmer gives you the schematics for a drone!"*
2. *"An abandoned space station circles a lonely planet. A quick check yields schematics for a drone. You bring it aboard the ship."*
3. *"Federation sympathizers contact you as you arrive. 'We know your mission should be secret, so don't ask how we know about it. Take this schematic, it's all we can do to help.'"*
4. *"A small Engi research vessel is trying to fend off a Mantis ship. You move in to engage, but after a quick scan of your ship the Mantis ship retreats. The Engi offer you a drone schematic as thanks for your timely arrival."*
5. *"You find an abandoned mining station on a nearby moon. A quick scan shows no life forms; however, you discover a usable drone schematic!"*
6. *"You receive a wide-band message, 'Free schematic samples! Be sure to visit our new military-grade drone store opening in sector XR1-45!'"* — **Advanced Edition only.**

> **Version difference.** `text_FIND_DRONE_6` is wrapped with `<!--DLC! Added text-->` in
> `events.xml`, so the vanilla pool is strings 1–5 and the AE pool is 1–6
> ([[source-events-xml]]). Assuming uniform selection across list entries, each string is
> 1/5 in vanilla and 1/6 in Advanced Edition. Purely cosmetic — the reward does not change.
> [[source-fandom-free-drone-schematic]] lists all six with no version note.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event body is a text load and a reward)_ | — | `<autoReward level="LOW">drone</autoReward>` — **a drone schematic with low scrap.** | 100% |

`drone` is the `autoReward` payload type, and `LOW` is the game's own word for the tier;
neither is converted to a number by any source here. Fandom's gloss is *"a drone schematic
with low scrap"* ([[source-fandom-free-drone-schematic]]).

## Blue Options
None.

## Rewards & Risks
- **Reward:** one drone schematic plus a low tier of scrap. Which drone is not stated —
  the reward is drawn by the engine, not named in the event.
- **Risk:** none. No ship, no combat, no hull damage, no crew exposure.
- Caveat: if your drone slots are full the schematic is broken down for scrap — that is
  what the separate `EQUIP_FULL` system message exists to say ([[source-events-xml]]).

## Strategy Notes
- Nothing to decide. Its only strategic weight is that it occupies a slot in the `ITEMS`
  pool, so sectors that allocate more `ITEMS` beacons are richer in free gear.
- Compare its two siblings in the same pool: [[event-free-weapon]] gives a weapon,
  [[event-free-scrap-with-resources]] gives medium scrap with resources. `FIND_DRONE` is
  the only one of the three that appears in the Zoltan item pool **and** in the Crystal
  and Engi pools.

## Related
- [[event-free-weapon]] — the weapon-flavoured twin, same shape
- [[event-free-scrap-with-resources]] — the scrap-flavoured twin
- [[event-trade-fuel-for-drone-parts]] — the other drone-flavoured member of `ITEMS`
- [[item-drone-control]]
- [[concept-autoreward-tiers]]

## Open Questions
- [ ] What `autoReward level="LOW"` of type `drone` actually pays in scrap, and how the
      drone blueprint is picked.
- [ ] Whether the drone can be one your ship cannot install.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `ITEMS` and `EXIT_LIST` pools)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml — the `ITEMS_CRYSTAL` pool)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — the `ITEMS_ENGI` pool)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml — the `ITEM_ZOLTAN` pool)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-free-drone-schematic]] (per raw/wiki/free-drone-schematic.md)
