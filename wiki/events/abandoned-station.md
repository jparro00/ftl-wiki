---
id: event-abandoned-station
type: event
event_name: EMPTY_STATION2
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [[[item-clone-bay]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-16
sources: 6
tags: [filler, unique, boarding-risk, pds, clone-bay, blue-option, crew-reward, pirate, ae]
---

# Abandoned station — `EMPTY_STATION2`

## Summary
A filler beacon with an abandoned station you may examine. Six equally-likely outcomes:
three are harmless (nothing, or a little scrap), one is a Clone Bay puzzle that can hand
you a free crew member, and two are ambushes — pirate boarders plus either a pirate ship
or a planetary defence battery. Examining is a 1/3 chance of walking into a fight for a
`LOW` scrap-only payout, which makes it one of the worse examine-or-leave gambles in the
Advanced Edition filler pool.

## Trigger & Where It Appears
- **Advanced Edition only.** `EMPTY_STATION2` appears in exactly two lists, both of them
  in `dlcEventsOverwrite.xml`: `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]). It is in **neither** of the base `NEUTRAL` /
  `NEUTRAL_EXIT` lists in `newEvents.xml`, so with the DLC off the event never fires.
  [[source-fandom-abandoned-station]] independently categorises it *Advanced Edition
  Content Events*.
- `OVERRIDE_NEUTRAL` is the hardcoded fill-in list — the XML comment on it reads *"This
  event list is hardcoded to fill out a sector if it ran out of all other calls for that
  sector"* — so this event can surface in **any** sector, not only those that name
  `NEUTRAL` explicitly. `sector_data.xml` names `NEUTRAL` explicitly only in the two Slug
  sectors ([[source-sector-data-xml]]), which is why Fandom's location list is
  [[sector-slug-controlled-nebula]] and [[sector-slug-home-nebula]] plus
  *exit and filler*.
- `OVERRIDE_NEUTRAL_EXIT` puts it on exit beacons as well.
- Beacon: ordinary/filler; no ship staged, so it starts non-hostile.
- `unique="true"` — at most once per run.
- **Also reused as a sub-event:** `QUEST_CONSTRUCTIONYARD` loads `EMPTY_STATION2_LIST`
  directly for its "cargo ship docked to an empty space station" branch
  ([[source-newevents]]). Fandom uses this to explain the `2` in the id — there is no
  `EMPTY_STATION` or `EMPTY_STATION1` anywhere in the datafiles
  ([[source-fandom-abandoned-station]]).

## Text
The intro prose is drawn from `textList EMPTY_STATION2_TEXT`, so it **varies** across
three variants ([[source-text-events-xml]]):

> You find a small space station that appears to be abandoned.

> You arrive to find what appears to be a colonized moon, however scans show it has been
> abandoned. You also detect an abandoned space station near the Beacon.

> This area shows signs of a battle some time ago. There are scattered remains of ships
> but one station appears to be intact.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Move in to examine the station. | — | Loads `eventList EMPTY_STATION2_LIST` (6 entries) — see below. | see below |
| 2 | Stay near the Beacon. | — | *"You decide it's not worth the time to examine."* Nothing happens. | 100% |

`EMPTY_STATION2_LIST` — 6 entries, no duplicates:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"…the station is simply an empty shell. It has been stripped of useful materials long ago."* | Nothing. |
| 2 | *"…a small rest stop that was abandoned a while ago. You take what few supplies you can find."* | `autoReward level="LOW">scrap_only` |
| 3 | *"…a large portion of its hull destroyed. You take what few supplies you can find."* | `autoReward level="LOW">scrap_only` |
| 4 | *"The station is in disarray. You find a cloning bay partially intact…"* | Opens a two-option sub-menu (see below). |
| 5 | *"…pirates burst in. Meanwhile scanners pick up a previously undetected pirate ship moving in to attack!"* | `boarders min="2" max="2"` **and** `ship load="PIRATE" hostile="true"`. |
| 6 | *"…pirates burst in. Meanwhile multiple warning signals go off on the bridge. The pirates have activated a remote planetary defense system…"* | `boarders min="2" max="4"` **and** `environment type="PDS" target="player"` — an Anti-Ship Battery fires at you for the duration. No enemy ship. |

**Assuming uniform selection across the six list entries:** 1/6 nothing, 2/6 low scrap,
1/6 the Clone Bay branch, 2/6 an ambush. The game files state no percentages; these
fractions are derived from list membership only ([[source-newevents]]).

Entry 4 sub-menu — both options are `hidden="true"`, so neither previews its result:

| # | Choice | Requirement | Outcome(s) |
|---|--------|-------------|-----------|
| 4a | **(Clonebay)** Search for a surviving DNA bank. | `req="clonebay"` | *"…you find someone was in queue to be cloned…"* → "continue" → loads `eventList EMPTY_STATION2_CLONE` (3 entries). |
| 4b | Scrap the machinery. | — | *"You take what you can and prepare to move on."* → `autoReward level="LOW">scrap_only` |

`EMPTY_STATION2_CLONE` — 3 entries:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"The clone is extremely confused but calms down after you try to explain the situation…"* | `crewMember amount="1"` — a free crew member. |
| 2 | *"The clone is extremely confused but seems to accept their new situation…"* | `crewMember amount="1"` — a free crew member. |
| 3 | *"The clone emerges in a crazed frenzy and refuses to calm down. You have no choice but to fight."* | `boarders min="1" max="1"` — one boarder, no ship. |

Two of the three entries give a crew member, so **assuming uniform selection, 2/3 crew
member and 1/3 a single boarder**. Fandom marks the two crew outcomes with its
`{{DuplicateEvent|2}}` template, an independent observation of the same duplication
([[source-fandom-abandoned-station]]).

## Blue Options
- **[[item-clone-bay]]** (`req="clonebay"`) — the only gate in the event, and it only
  appears on 1/6 of examines. It converts a `LOW` scrap payout into a 2/3 chance of a free
  crew member (1/3 one boarder). The crew member's species is not specified, so it is a
  random draw. Worth taking whenever offered: a single boarder is a much smaller cost than
  a crew slot is worth.

## Rewards & Risks
- **Rewards:** `LOW` `scrap_only` on 2/6 examines (3/6 if you scrap the cloning
  machinery), or a free crew member from the Clone Bay branch. `LOW`/`scrap_only` are the
  game's own reward tier words — no numeric value is stated in any source here.
- **Risks:**
  - 1/6 — 2 boarders **and** a `PIRATE` ship fight. Per `events_ships.xml` the `PIRATE`
    ship has `surrender chance="0.5" min="3" max="4"` and `escape chance="0.5" min="2"
    max="4"`, and default destroyed/deadCrew rewards ([[source-events-ships]]).
  - 1/6 — 2–4 boarders while a planet-side Anti-Ship Battery shoots at you. This is the
    nastier of the two: no enemy ship to destroy means the PDS keeps firing until you
    jump.
  - 1/3 of the Clone Bay branch — 1 boarder.
- Choice 2 is completely free and completely safe.

## Strategy Notes
- Examining costs nothing but risks a lot: two of six outcomes are ambushes and the best
  ordinary payout is `LOW` scrap. On a healthy hull with a boarding-capable crew it is
  worth the roll; on a damaged hull, late in a sector, or with the Rebel fleet close, the
  expected value does not justify a PDS beacon. (Opinion, reasoned from the outcome table;
  no source ranks this event.)
- The PDS outcome is the one to fear — there is no ship to kill to end it, so the battery
  fires for as long as you stay.
- With a Clone Bay installed, the examine gamble improves slightly: the 1/6 cloning branch
  becomes a crew-member lottery rather than a small scrap payout.
- As a filler event it can fill out beacons in sectors that allocate few named events —
  the Abandoned Sector allocates only `STORE`, so its beacons fall through to this list.

## Related
- [[event-space-station-under-construction]] — `QUEST_CONSTRUCTIONYARD`, which reuses
  `EMPTY_STATION2_LIST` as one of its own outcomes
- [[event-refueling-platform]] — the other AE filler station event from the same file
- [[event-confused-mantis]] — same file, same AE neutral pool
- [[item-clone-bay]], [[entity-pirates]]
- [[concept-anti-ship-battery]], [[concept-blue-options]]
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- [[concept-sector-event-allocation]] — the leftover-beacon fallback that puts this event in
  any sector, and the `NEUTRAL` → `OVERRIDE_NEUTRAL` delta, of which this event *is* the
  whole delta
- [[sector-the-last-stand]] — the one sector whose table always leaves beacons for the
  fallback, so a sighting here would prove AE substitutes `OVERRIDE_NEUTRAL` at that call
  site

## Open Questions
- [ ] Whether `eventList` selection is uniform (the 1/6 and 2/3 figures depend on it).
- [ ] Numeric value of `LOW` `scrap_only`.
- [ ] Species distribution of the `crewMember amount="1"` clone reward.
- [ ] Whether the PDS on outcome 6 stops if you destroy nothing, i.e. how long it fires.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-abandoned-station]] (per raw/wiki/abandoned-station.md)
