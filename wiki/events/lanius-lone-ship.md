---
id: event-lanius-lone-ship
type: event
event_name: LANIUS_SCARED_CIVILIAN
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, neutral, blue-option, store-opportunity, optional-fight, unique, advanced-edition]
---

# Lanius lone ship — `LANIUS_SCARED_CIVILIAN`

## Summary
A civilian screams that the "metal monsters" are about to melt their ship — but the event
text itself tells you no weapons are powered. They are not a threat. Attacking gets you an
ordinary Lanius fight; talking to them is a 1/3 store, 1/3 nothing, 1/3 fight; and a Lanius
crew member converts the whole thing into a **guaranteed store** with no risk at all. One of
the clearest blue-option payoffs in the [[sector-abandoned-sector]].

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `NEUTRAL_LANIUS`, allocated `min="5" max="6"` beacons per sector
  ([[source-sector-data-xml]]) — the largest allocation in the sector.
- `NEUTRAL_LANIUS` has **13** members — `LANIUS_CIVILIAN`, `LANIUS_PIRATE_CIVILIAN`,
  `LANIUS_SOLO_SALVAGE`, `LANIUS_SCARED_CIVILIAN`, `LANIUS_AUTO_REBEL`,
  `LANIUS_GROUP_AUTO`, `LANIUS_BEACON_EATER`, `LANIUS_DORMANT_EVENT`,
  `LANIUS_FUELING_STATION`, `FRIENDLY_SLAVER`, `PIRATE_BRIBER`, `ASTEROID_EXPLORE`,
  `BROKEN_REBEL_DRONE` — none duplicated, so this is **1/13** of any neutral beacon
  *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- The event loads `<ship load="LANIUS_SHIP" hostile="false"/>` at the top level, so a ship
  is present but not hostile; long-range scanners show a ship
  ([[source-fandom-lanius-lone-ship]] renders `LRSmap=ship`).

> **AE-only.** AE data file, AE sector, no `OVERRIDE_NEUTRAL_LANIUS` in
> `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]). Fandom files it under
> *Advanced Edition Content Events*.

## Text
> You arrive at the beacon to discover a civilian ship fleeing from a lone Lanius craft.
> The civilian messages you, "Help! The metal monsters are coming to melt down our ship!"
> Strangely, no active weapon signatures are detected.

(`event_LANIUS_SCARED_CIVILIAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Lanius ship. | — | "The civilian ship hastily retreats while you intercept the path of the ship and lock on weapons." → the already-loaded `LANIUS_SHIP` flips hostile; default Lanius rewards. | 100% |
| 2 | Stay out of it. | — | "You ignore the ship's pleas and watch as it hastily escapes. Oddly, the Lanius ship makes no move to chase it. You wonder if they were ever a threat at all." Nothing happens. | 100% |
| 3 | Try to contact the Lanius ship. | — | Flavour, then a single hidden follow-up choice loading `LANIUS_SCARED_CIVILIAN_LIST` — see below. | 100% |
| 4 | **(Lanius Crew)** Try to contact the ship. | `req="anaerobic"` | "…they are scouting for a merchant's guild…" → a **store** opens. | 100% |

### Choice 3 → `LANIUS_SCARED_CIVILIAN_LIST`
The follow-up choice is labelled *"Ignore them and continue."* (i.e. ignore the panicking
civilian, not the Lanius). It loads a three-entry list, none duplicated → **1/3 each**
*assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| "Explore. Assess trade potential." — a merchant ship after all. | a **store** opens |
| "Expunge... Floral... Proposition..." — the translator fails. | nothing |
| "The Lanius seem enraged for an indiscernible reason. They cut transmission and power their weapons." | `<ship hostile="true"/>` — fight the `LANIUS_SHIP` |

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — turns a 1/3-store, 1/3-nothing,
  1/3-forced-fight gamble into a guaranteed store, and skips the intermediate screen
  entirely. Strictly better than choice 3 in every branch
  ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- **The Lanius are not actually attacking anyone.** Choice 2's text says so outright, and
  choice 4 confirms they are a merchant scout. The civilian's distress call is wrong.
- Choice 1 or the bad third of choice 3: a fight with `LANIUS_SHIP` — surrender
  `chance="0.2"`, escape `chance="0.2"`, "default Lanius rewards"; the full outcome tables
  live on [[event-lanius-fight]] ([[source-dlcevents-anaerobic]],
  [[source-fandom-lanius-lone-ship]]).
- Choice 3 or 4: a store, which is the real prize — Abandoned sectors guarantee only 2
  ([[source-sector-data-xml]]).
- No resource cost on any branch.

## Strategy Notes
- *Opinion, derived from the tables above:* with Lanius crew, choice 4 is free. Without it,
  choice 3 is a 1/3 chance of a bonus store against a 1/3 chance of a fight you did not
  need — reasonable early, poor when your hull is low.
- Attacking outright is the worst option: the same fight as choice 3's bad branch, with the
  store possibility thrown away.
- This is one of two events in the sector where Lanius crew buys a store outright; the other
  is the `LANIUS_SOLO_SALVAGE` line's scrap grant ([[event-lanius-ship-salvager]]).

## Related
- [[event-lanius-ship-salvager]] — the other `NEUTRAL_LANIUS` "attack it or talk to it"
  Lanius beacon with a Lanius-crew blue option
- [[event-lanius-fight]] — documents the shared `LANIUS_SHIP` enemy block
- [[event-lanius-ship-attacking-civilian]] — the version where the Lanius really are hostile
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-blue-options]]

## Open Questions
- [ ] Whether the store opened by choice 3/4 has any Lanius-specific stock bias — nothing
      in the event constrains it.
- [ ] Whether the `LANIUS_SHIP` loaded non-hostile at event level uses the same hull roll
      once flipped hostile.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-lone-ship]] (per raw/wiki/lanius-lone-ship.md)
