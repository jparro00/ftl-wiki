---
id: event-rebel-auto-pds
type: event
event_name: REBEL_AUTO_PDS
sectors: []
beacon_type: unknown
hostile: true
blue_options: [hacking]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [rebel, auto-ship, combat, asb, pds, hazard, blue-option, hacking, unique, unreachable, orphan, no-fandom-page, advanced-edition]
---

# Rebel auto-ship fight with hostile ASB — `REBEL_AUTO_PDS`

## Summary
A complete, fully authored event that **nothing in the shipped data ever loads**. It is the
auto-ship version of [[event-rebel-pds]]: hostile Anti-Ship Battery, a `REBEL_AUTO` drone
ship, and two Hacking options to redirect the battery. Every part of it exists — event
block, choices, effects, flavour text, its own `textList` — but no `eventList` anywhere in
`raw/gamedata/` references it.

## Trigger & Where It Appears
**None. This event is unreachable in normal play.**

- A grep of every file in `raw/gamedata/` finds `REBEL_AUTO_PDS` only in its own definition
  in `dlcEvents.xml` and in its `text_events.xml` strings. It is a member of no `eventList`,
  is named by no `sectorDescription`, and is not a `startEvent`
  ([[source-dlcevents]], [[source-dlceventsoverwrite]], [[source-sector-data-xml]],
  [[source-newevents]]).
- There is **no commented-out reference** either, so there is no evidence it was ever wired
  up and later pulled — unlike, say, `LANIUS_BOARDERS`, whose list entry is explicitly
  commented out in `dlcEvents_anaerobic.xml`. It reads as content that was written and
  simply never hooked in. Tagged `unreachable`; **not** tagged `cut-content`, because no dev
  note supports that reading.
- Its live sibling [[event-rebel-pds]] *is* wired up, through `OVERRIDE_HOSTILE2`
  ([[source-dlceventsoverwrite]]) — which is the strongest hint about where this one was
  meant to go.
- `unique="true"` is declared, which would matter if it were reachable
  ([[source-dlcevents]]).
- **No Fandom page** covers this event, consistent with it never appearing in play.

> **AE-only** by construction — `dlcEvents.xml` is an Advanced Edition file, and both the
> ASB hazard and the Hacking system are AE features. There is no vanilla form to record.

## Text
`[varies: textList REBEL_AUTO_PDS_TEXT]` — nominally a list, but all **four** entries point
at the same string `text_REBEL_AUTO_PDS_TEXT_1`, with a `<!-- NEEDS MORE-->` comment marking
the padding. The text would never actually vary ([[source-dlcevents]]):

> As soon as you arrive multiple warnings go off. A hostile automated ship is detected and
> an Anti-Ship Battery begins firing. This doesn't look good!

(`text_REBEL_AUTO_PDS_TEXT_1`, per [[source-text-events-xml]])

## Choices & Outcomes

The event body applies `<environment type="PDS" target="player"/>` and loads
`<ship load="REBEL_AUTO" hostile="true"/>` before the choice screen
([[source-dlcevents]]).

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-------------|------|
| 1 | Prepare to fight. | — | Empty `<event/>`. Fight the auto-ship with the ASB firing **on you**. | 100% |
| 2 | **(Simple Hacking)** Confuse the Anti-Ship Battery's targets. | `req="hacking" lvl="1"` | −1 drone part; `<environment type="PDS" target="all"/>` — the ASB fires on **both** ships. | 100% |
| 3 | **(Advanced Hacking)** Override the ASB's target. | `req="hacking" lvl="3"` | −1 drone part; `<environment type="PDS" target="enemy"/>` — the ASB fires on the **Rebel ship only**. | 100% |

The flavour differs slightly from [[event-rebel-pds]]: choice 2 here says the drone will
*"periodically confuse the ASB's lock signal. It should sometimes fire on the Rebel ship
now"*, where the crewed version says *"It should also fire on the Rebel ship now"*. The
mechanical payload (`target="all"`) is identical, so the wording difference is cosmetic
([[source-text-events-xml]]).

### The `REBEL_AUTO` enemy
`auto_blueprint="SHIPS_AUTO"` ([[source-events-ships]]). An auto-ship: **no crew**, and the
block declares only:

| Outcome | Definition | Payout |
|---|---|---|
| Destroyed | `DESTROYED_DEFAULT` (2 identical entries) | `MED standard`, always |
| Dead crew | `DEAD_CREW_DEFAULT` | declared but unreachable in practice — an auto-ship has no crew to kill |

No `<surrender>`, no `<escape>`, no `<gotaway>` — the ship fights to destruction
([[source-events-ships]], [[source-events-xml]]).

## Blue Options
- **Hacking, level 1** (`req="hacking" lvl="1"`) — 1 drone part; ASB → `target="all"`.
- **Hacking, level 3** (`req="hacking" lvl="3"`) — 1 drone part; ASB → `target="enemy"`.

Same gates and same cost as [[event-rebel-pds]] ([[source-dlcevents]]).

## Rewards & Risks
- Reward if it were reachable: `MED standard` for destroying the auto-ship, nothing more.
  No bonus attaches to either Hacking option.
- Auto-ships cannot surrender or flee, so the fight always runs to a kill — which makes the
  ASB damage you take a function of how fast you can break the hull.
- Cost: 1 drone part for either Hacking option.

## Strategy Notes
- Academic — you will never see this beacon. Recorded so the shipped content is not silently
  dropped, and so that anyone comparing [[event-rebel-pds]] against a mod or a datamined
  list knows this second definition exists.
- If it were live it would be the harsher of the two ASB fights: an auto-ship with no
  surrender and no escape roll, under sustained battery fire, for a flat `MED standard`.
- Modders wiring this back in would add `<event load="REBEL_AUTO_PDS"/>` to
  `OVERRIDE_HOSTILE2` alongside `REBEL_PDS`, which is where its sibling sits.

## Related
- [[event-rebel-pds]] — the live crewed version; identical structure and Hacking gates
- [[event-pirate-fight-near-pulsar]], [[event-rebel-fight-near-pulsar]] — the reachable
  hazard fights from the same file
- [[event-fuel-escape-pds]] — the out-of-fuel escape from an ASB beacon
- [[item-hacking]], [[entity-rebels]], [[concept-hazards]]
- [[event-lanius-boarders]] — the contrasting case: a list entry explicitly commented out

## Open Questions
- [ ] Whether any list in a build not represented in `raw/gamedata/` (a console or mobile
      port, or a patch revision) loads this event.
- [ ] Whether it was written as an alternative to `REBEL_PDS` and dropped, or intended to
      sit alongside it.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `DESTROYED_DEFAULT`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
