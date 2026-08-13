---
id: event-free-scrap-with-resources
type: event
event_name: FREE_ITEMS
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [free-item, scrap, no-choice, no-risk, repeatable, item-event]
---

# Free scrap with resources — `FREE_ITEMS`

## Summary
The plainest event in the game: arrive, take a medium payout of scrap with resources,
leave. No choices, no ship, no risk, and no variation beyond which of six intro strings
you see. It is the generic member of the `ITEMS` allocation pool.

## Trigger & Where It Appears
- Sectors: sixteen — everywhere the `ITEMS` pool reaches except
  [[sector-hidden-crystal-worlds]], which draws from `ITEMS_CRYSTAL` and does not include
  this event. See frontmatter for the full list.
- Pooled in `ITEMS` and `ITEM_ZOLTAN`, plus the Advanced Edition `OVERRIDE_ITEMS`
  replacement. Present in **both editions** ([[source-newevents]],
  [[source-events-zoltan]], [[source-dlceventsoverwrite]]).
- **Not `unique`** — it can occur more than once in a run
  ([[source-events-xml]], [[source-fandom-free-scrap-with-resources]]).
- Also reachable at an exit beacon, since `ITEMS` is a member of `EXIT_LIST`
  ([[source-newevents]]).
- No ship at the beacon; Long-Range Scanners show nothing.

## Text
Drawn from the `FREE_ITEMS` textList — `[varies: textList FREE_ITEMS]`. **Six strings in
Advanced Edition, four in vanilla** ([[source-text-events-xml]]):

1. *"You arrive in a system and immediately discover a pirate ship nearby. Strangely, scans indicate there are no lifeforms aboard. You salvage anything useful, but find no clue as to the whereabouts of the former crew."*
2. *"Not much remains in this abandoned system; however, scans reveal a nearby mining platform with some salvageable materials."*
3. *"As you arrive in the system you are hailed by a loyalist settlement. Upon learning of your quest, they offer you supplies."*
4. *"Debris from a forgotten battle still orbits the gas giant in this system. Some of it still might be usable."*
5. *"You receive a message from a nearby station, 'A Federation cruiser jumping into Rebel territory? Quite the bold move.' You quickly move to arm the weapons but he continues, 'Lucky for you we're not all in support of the Rebellion. Perhaps these supplies will help you get to friendlier space alive.'"* — **Advanced Edition only.**
6. *"You happen upon the remains of a space station. It has been mostly picked clean but there appears to be a few materials that will aid you in your mission."* — **Advanced Edition only.**

> **Version difference.** `text_FREE_ITEMS_5` and `text_FREE_ITEMS_6` sit under a
> `<!--DLC! added texts-->` marker in `events.xml`, so vanilla draws from strings 1–4 and
> Advanced Edition from 1–6 ([[source-events-xml]]). Assuming uniform selection across list
> entries, each string is 1/4 in vanilla and 1/6 in AE. Cosmetic only — the reward is
> unchanged. [[source-fandom-free-scrap-with-resources]] lists all six with no version note.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event body is a text load and a reward)_ | — | `<autoReward level="MED">standard</autoReward>` — **medium scrap with resources.** | 100% |

`MED` and `standard` are the game's own words; no source here converts them to numbers
([[source-events-xml]], [[source-fandom-free-scrap-with-resources]]).

## Blue Options
None.

## Rewards & Risks
- **Reward:** a medium `standard` payout — scrap with some resources mixed in. It is a
  higher tier than the `LOW` on its two siblings, which is the trade for not handing you a
  weapon or drone.
- **Risk:** none whatsoever.

## Strategy Notes
- Nothing to decide. Note only that it is the **most broadly available** of the three
  `ITEMS` freebies: it is in the Zoltan pool (unlike [[event-free-weapon]]) but not the
  Crystal pool (unlike [[event-free-drone-schematic]]).

## Related
- [[event-free-drone-schematic]], [[event-free-weapon]] — the other two freebies in `ITEMS`
- [[event-free-scrap-with-resources-engi]], [[event-free-scrap-with-resources-lanius]],
  [[event-free-scrap-with-resources-zoltan]] — **different events** with similar Fandom
  titles and different in-game ids; do not conflate them with this one
- [[concept-autoreward-tiers]], [[concept-scrap-economy]]

## Open Questions
- [ ] What `autoReward level="MED"` of type `standard` pays in absolute scrap and
      resources.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `ITEMS` and `EXIT_LIST` pools)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml — the `ITEM_ZOLTAN` pool)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-free-scrap-with-resources]] (per raw/wiki/free-scrap-with-resources.md)
