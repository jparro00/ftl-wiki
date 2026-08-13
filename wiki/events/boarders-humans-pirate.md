---
id: event-boarders-humans-pirate
type: event
event_name: BOARDERS
sectors: [[[sector-pirate-controlled-sector]], [[sector-federation-space]]]
beacon_type: any
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [pirate, boarding-hazard, no-enemy-ship, no-choice, unique, varies-text]
---

# Boarders: Humans (Pirate) — `BOARDERS`

## Summary
The plainest boarding event in the game and the archetype the others are variations on:
3–5 human boarders appear in your ship, there is **no enemy vessel to shoot**, no choice,
no reward and no hazard. Only the intro prose varies. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-pirate-controlled-sector]] (live), [[sector-federation-space]] (nominal
  — see below)
- Event lists: `BOARDERS_PIRATE` ([[source-events-pirate]]) and `HOSTILE_BOARDING`
  ([[source-newevents]])
- Allocation: `BOARDERS_PIRATE` `min=1 max=1` in `PIRATE_SECTOR` — a **guaranteed** beacon
  in Pirate space, though which of the list's five members it draws is a five-way roll
  ([[source-sector-data-xml]])
- **`HOSTILE_BOARDING` is dead in `sector_data.xml`**: `min="0" max="0"` in `STANDARD_SPACE`
  and commented out in `CIVILIAN_SECTOR` ([[source-sector-data-xml]]). That is why Fandom
  lists Pirate Controlled Sector only. The same finding is recorded on
  [[event-boarders-asteroid]] and [[event-boarders-humans-near-sun]].
- Beacon: any — the event has no `<distressBeacon/>`, no `<ship>` and no `<environment>`
- Long-range scanners show **no ship** ([[source-fandom-boarders-humans-pirate]])
- `unique="true"` — once per run

## Text
`<text load="BOARDERS_TEXT"/>` — the prose is drawn from a **five-entry `<textList>`**
(`text_BOARDERS_TEXT_1` … `_5`), so the intro varies between playthroughs
([[source-events-xml]], [[source-text-events-xml]]). The list is declared
`unique="false"`, so entries can repeat across the events that share it. All five are
transcribed on [[source-fandom-boarders-humans-pirate]]; representative examples:

> What appears to be a civilian ship sends a friendly hail. As you approach the vessel, you
> detect a teleporter signal but it's too late... intruders have beamed aboard!

> You detect life-signs actually on the beacon itself! A teleporter signal warns you but
> it's too late, they've beamed from the beacon onto your ship and seem intent on taking it
> over.

> As you arrive, you become aware of a small Rebel outpost near the beacon. You are hardly
> able to bark an order before a small team is beamed aboard your ship. They must have been
> expecting you...

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(no choices)* | — | `<boarders min="3" max="5" class="human"/>` — **3–5 human boarders** aboard. Nothing else. | 100% |

The entire event body is a `<text load>` and a `<boarders>` tag. There is no `<ship>`, no
`<autoReward>`, no `<environment>` and no outcome branch ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- **Reward: none.** The event defines no `autoReward` and no items. Killing the boarders
  simply ends it.
- **Risk:** 3–5 human boarders — the largest plain boarding party in the game (its siblings
  `BOARDERS_SUN` and `BOARDERS_ASTEROID` send 2–4). With no enemy ship, weapons are useless
  and the fight is entirely crew-vs-crew, or airlock-vs-boarders.

## Strategy Notes
- *(Opinion.)* 3–5 humans is a real threat to a small or injured crew, and there is nothing
  to gain by winning — the correct play is whatever ends it cheapest. Venting is free here
  because, unlike [[event-boarders-humans-near-sun]], there is no fire hazard fighting you
  for the same rooms.
- Human boarders are the weakest boarder class, which is the only mercy in a 5-strong party.

## Version Differences
Base-`events.xml` event with no DLC-marked tags — identical in both editions
([[source-events-xml]]). `BOARDERS_PIRATE` is not redefined by `dlcEventsOverwrite.xml`, so
the pool is unchanged too.

## Related
- [[event-boarders-humans-jammed-sensors]] — `BOARDERS_HACKING`, the same 3–5 humans plus a
  sensors blackout; shares the `BOARDERS_PIRATE` list
- [[event-boarders-humans-near-sun]] — 2–4 humans, sun hazard
- [[event-boarders-asteroid]] — 2–4 humans, asteroid hazard, unreachable list
- [[event-boarders-asteroid-ghost]] — the ghost-boarder variant
- [[event-destroyed-cargo-ship]], [[event-ghost-ship]] — the other `HOSTILE_BOARDING` members
- [[entity-pirates]], [[sector-pirate-controlled-sector]]

## Open Questions
- [ ] Is the boarder count uniform over 3–5? The file gives `min`/`max` only.
- [ ] Are the five `BOARDERS_TEXT` variants equally weighted?
- [ ] Can this event actually appear in [[sector-federation-space]]? Its only route there is
      `HOSTILE_BOARDING`, allocated `min=0 max=0`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml` — the event and the `BOARDERS_TEXT` list)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml` — `BOARDERS_PIRATE`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `HOSTILE_BOARDING`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-boarders-humans-pirate]] (per `raw/wiki/boarders-humans-pirate.md`)
