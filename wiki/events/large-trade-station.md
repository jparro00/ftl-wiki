---
id: event-large-trade-station
type: event
event_name: STORE_REBELSIDE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: store
hostile: false
blue_options: [mind control]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [store, rebel, blue-option, mind-control, optional-fight, unique, advanced-edition]
---

# Large trade station — `STORE_REBELSIDE`

## Summary
A store you have to work for. The Rebels broadcast a warning not to trade with you, and
searching for a seller anyway is a **50% chance of an auto-ship fight**. Mind Control skips
the gamble entirely — and at level 2 or 3 the announcer apologises with free supplies on top
of opening the store. It is one of the strongest arguments in the game for the Mind Control
system outside of combat.

## Trigger & Where It Appears
- Sectors, per [[source-fandom-large-trade-station]]: [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]], [[sector-uncharted-nebula]] — and it can also occur on an
  **exit beacon**.
- List: `OVERRIDE_ITEMS` in `dlcEventsOverwrite.xml`, which replaces the vanilla `ITEMS`
  list when the DLC is on. It is one of **14** members, none duplicated → **1/14** of any
  item beacon *assuming uniform selection across list entries*
  ([[source-dlceventsoverwrite]]). The file annotates it `<!-- dlcEvents-->`, marking it as
  one of the four AE additions to that list.
- Allocation: `ITEMS` is allocated by most `sectorDescription` blocks — 1–3 beacons
  depending on sector, e.g. `min="2" max="3"` in `CIVILIAN_SECTOR`, `min="1" max="2"` in the
  Rock and Rebel sectors, `min="0" max="2"` in the Slug sectors
  ([[source-sector-data-xml]]). Notably the Zoltan sectors allocate no `ITEMS` at all, and
  the Abandoned Sector uses `ITEM_LANIUS` instead — which matches Fandom's sector list
  omitting both.
- `unique="true"` — at most once per run ([[source-dlcevents]]).
- Long-range scanners show **no ship** ([[source-fandom-large-trade-station]]).

> **AE-only.** Defined in `dlcEvents.xml`, reachable only through `OVERRIDE_ITEMS`, and its
> two best branches are gated on Mind Control — an Advanced Edition system. **Vanilla
> behaviour is this event not existing**: the vanilla `ITEMS` list in `newEvents.xml`
> contains no `STORE_REBELSIDE` entry ([[source-newevents]],
> [[source-dlceventsoverwrite]]).

## Text
> You come across a large trade station. However, as soon as you approach a warning goes out
> to all ships in the region: "Do not associate with the Federation sympathizer. All who
> oppose the Rebels will be punished."

(`event_STORE_REBELSIDE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-------------|------|
| 1 | Search among the stores to see if someone will sell to you. | — | Loads `STORE_REBELSIDE_SEARCH` — see below. | 100% |
| 2 | Leave. | — | "You decide it's better to not push your luck and move on." Nothing happens. | 100% |
| 3 | **(Mind Control)** Alter the announcer's opinions. | `req="mind" lvl="1"` | A **store** opens. | 100% |
| 4 | **(Improved Mind Control)** Alter the announcer's opinions. | `req="mind" lvl="2"` | `autoReward level="MED">standard` **and** a store opens. | 100% |
| 5 | **(Advanced Mind Control)** Alter the announcer's opinions. | `req="mind" lvl="3"` | `autoReward level="HIGH">standard` **and** a store opens. | 100% |

All three Mind Control choices carry `max_group="0"`, and choices 1–5 are all
`hidden="true"` ([[source-dlcevents]]).

### `STORE_REBELSIDE_SEARCH` (choice 1)
Four entries, and the auto-ship entry is **listed twice** — so, *assuming uniform selection
across list entries* ([[source-dlcevents]]):

| Outcome | Payload | Share |
|---|---|---|
| "You find a single store that responds to your hails: 'Don't open any wide band channels. We'll sell to you but we don't want to draw attention to ourselves.'" | a **store** opens | **1/4** |
| "Your search for a friendly marketplace yields no results but after a time a small shuttle approaches. They release some supplies in your direction with the message, 'We are not all friends of the Rebel fleet. Stay strong.'" | `autoReward level="RANDOM">standard` | **1/4** |
| "You apparently spoke to the wrong person in your search for a store. Warnings go off and you detect an automated Rebel ship moving in to attack." | `<ship load="REBEL_AUTO" hostile="true"/>` | **2/4** |

Fandom marks the duplicated entry with its `DuplicateEvent|2` template, independently
confirming the 2-in-4 weighting ([[source-fandom-large-trade-station]]).

### The `REBEL_AUTO` enemy
`auto_blueprint="SHIPS_AUTO"` ([[source-events-ships]]). No `<surrender>`, no `<escape>`,
no `<gotaway>` — an auto-ship fights to destruction. `destroyed` loads `DESTROYED_DEFAULT`,
which is two identical entries paying `autoReward level="MED">standard`
([[source-events-xml]]).

## Blue Options
- **Mind Control, level 1** (`req="mind" lvl="1"`) — skips the search gamble; store opens,
  no fight, no reward.
- **Mind Control, level 2** (`req="mind" lvl="2"`) — store **plus** `MED standard`.
- **Mind Control, level 3** (`req="mind" lvl="3"`) — store **plus** `HIGH standard`.

The gate is on the Mind Control **system's power level**, not on an augment or crew. Nothing
is spent — no scrap, no drone parts, no cooldown modelled in the event
([[source-dlcevents]]).

## Rewards & Risks
- Without Mind Control: 1/4 store, 1/4 a random-level scrap-with-resources handout, 2/4 an
  unavoidable auto-ship fight paying `MED standard`.
- With Mind Control 3: a store **and** `HIGH standard`, for free, with zero risk. That is
  the single best outcome available at any item beacon covered so far.
- Leaving is free but throws away a store in a sector that may not have many.
- `MED` / `HIGH` / `RANDOM` are the game's own `autoReward` levels; no source read here
  converts them to numbers.

## Strategy Notes
- *Opinion, derived from the tables:* if you have Mind Control at all, always use it here —
  even level 1 converts a coin-flip fight into a guaranteed store. Powering Mind Control to
  2 or 3 before choosing is worth doing if you can spare the reactor, since the difference
  is a free `MED` or `HIGH` reward.
- Without Mind Control the search is still usually worth taking: the fight is against an
  auto-ship, which has no boarders and no surrender complications, and even the bad branch
  pays `MED standard`.
- This is a rare case where a *system level* rather than a system's mere presence changes
  the payout — the same pattern as [[event-rebel-pds]]'s Hacking gates.

> ⚠️ **CONTRADICTION (minor, wording):** Fandom renders choice 2 as *"You decide it's better
> **not to** push your luck"* and the Mind Control outcomes as *"Hopefully you **have**
> enough time to shop"*; the game files read *"it's better **to not** push your luck"* and
> *"Hopefully you **will have** enough time to shop"* ([[source-text-events-xml]] vs
> [[source-fandom-large-trade-station]]). Trusting the game files — reliability `high` vs
> `medium`. Transcription smoothing, not a version difference.

> ⚠️ **CONTRADICTION (reward wording):** Fandom labels the auto-ship destruction reward
> *"medium scrap with resources"* and quotes *"The ship explodes, leaving behind a
> **substantial** collection of useful scrap material."*
> ([[source-fandom-large-trade-station]]). The files route it through the generic
> `DESTROYED_DEFAULT` list, whose two entries both pay `MED standard`
> ([[source-events-xml]]) — so the reward level agrees; the "substantial" wording is
> Fandom's, from the shared `event_DESTROYED_DEFAULT_1_text` string rather than anything
> specific to this event.

## Related
- [[event-store-rock]], [[event-store-lanius]], [[event-store-engi]] — ordinary
  no-strings store beacons
- [[event-rebel-pds]] — the other `dlcEvents.xml` event whose blue options key off system
  *level*
- [[event-lanius-lone-ship]] — the other batch event where a blue option buys a store
  outright
- [[item-mind-control]], [[entity-rebels]], [[concept-stores]], [[concept-blue-options]]

## Open Questions
- [ ] Numeric scrap values behind `MED` / `HIGH` / `RANDOM standard`.
- [ ] Whether `max_group="0"` on the three Mind Control choices has any player-visible
      effect here, or is purely an authoring grouping flag.
- [ ] Whether the store opened by any branch differs in stock from an ordinary store.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `DESTROYED_DEFAULT`)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-large-trade-station]] (per raw/wiki/large-trade-station.md)
