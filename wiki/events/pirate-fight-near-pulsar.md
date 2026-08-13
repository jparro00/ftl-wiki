---
id: event-pirate-fight-near-pulsar
type: event
event_name: PIRATE_PULSAR
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [pirate, combat, pulsar, hazard, no-choice, default-rewards, unique, advanced-edition]
---

# Pirate fight near pulsar — `PIRATE_PULSAR`

## Summary
An ordinary pirate ambush with a pulsar on the board. Three lines of XML — a text list, a
`PIRATE` ship, and `<environment type="pulsar"/>` — and no choices at all. The pulsar is the
whole event: it periodically knocks out systems and drains shields on **both** ships, which
turns a routine fight into a scramble.

## Trigger & Where It Appears
- Sectors, per [[source-fandom-pirate-fight-near-pulsar]]: [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]].
- Lists: it is a member of four Advanced Edition override lists in
  `dlcEventsOverwrite.xml` — `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`,
  `OVERRIDE_HOSTILE_ENGI` and `OVERRIDE_HOSTILE_PIRATE`
  ([[source-dlceventsoverwrite]]). Those lists replace the vanilla `HOSTILE1`, `HOSTILE2`,
  `HOSTILE_ENGI` and `HOSTILE_PIRATE` lists when the DLC is active; the file's own header
  says so: *"Events and Event lists that will be overwritten if the DLC is turned on"*, with
  an explicit note *"Adding pulsar to normal hostile lists"*.
- Share of a hostile beacon *assuming uniform selection across list entries*:
  **1/12** in `OVERRIDE_HOSTILE1`, **1/15** in `OVERRIDE_HOSTILE2`, **1/10** in
  `OVERRIDE_HOSTILE_ENGI`, **1/8** in `OVERRIDE_HOSTILE_PIRATE` — no entry is duplicated in
  any of the four ([[source-dlceventsoverwrite]]).
- Allocation of those lists: `HOSTILE_ENGI` is allocated `min="5" max="7"` in both Engi
  sector definitions and `HOSTILE_PIRATE` `min="6" max="8"` in the Pirate sector
  ([[source-sector-data-xml]]). `HOSTILE1` is allocated `min="2" max="2"` by
  `CIVILIAN_SECTOR` and `STANDARD_SPACE`, and `HOSTILE1`/`HOSTILE2` are also allocated by
  the depth-based `<eventCounts sector="0">` … `sector="3"` blocks in
  `raw/gamedata/newEvents.xml` ([[source-newevents]]) — see *Open Questions*.
- `unique="true"` — at most once per run ([[source-dlcevents]]).
- Long-range scanners show a **ship and a pulsar**
  ([[source-fandom-pirate-fight-near-pulsar]], `LRSmap=ship+pulsar`).

> **AE-only.** `PIRATE_PULSAR` is defined in `dlcEvents.xml` (an Advanced Edition data file)
> and every list containing it is an `OVERRIDE_` list that only takes effect with the DLC
> on ([[source-dlcevents]], [[source-dlceventsoverwrite]]). **Vanilla behaviour is this
> event not existing**: the vanilla `HOSTILE1` in `newEvents.xml` contains no pulsar entry
> ([[source-newevents]]). Fandom independently categorises it as
> *Advanced Edition Content Events*.

## Text
`[varies: textList PIRATE_PULSAR_TEXT]` — six `<text>` entries drawing on **three** distinct
strings, each listed twice. The second block is preceded by a `<!-- NEEDS MORE-->` comment,
so the duplication is stated padding, not weighting; effectively **1/3 each** *assuming
uniform selection across list entries* ([[source-dlcevents]]). All three, per
[[source-text-events-xml]]:

> Sensors go wild as a nearby pulsar is detected. While you are attempting to recalibrate
> the FTL drive, a pirate sneaks up on your ship, weapons charging. Prepare for a fight!

> You arrive to find a pulsar dominating the view screen. You see a small silhouette pass in
> front of the star. Before you can ponder what it is, warning signals go off. It appears to
> be a ship in a firing trajectory!

> A small research station orbits a nearby pulsar. It appears largely abandoned, but you
> detect power signatures flaring up as soon as you're in scanning distance. A small combat
> ship launches from the station. Pirates!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `PIRATE` under a pulsar. **Default rewards.** | 100% |

### The `PIRATE` enemy
`auto_blueprint="SHIPS_PIRATE"`, defined in `raw/gamedata/events_ships.xml`
([[source-events-ships]]):

| Outcome | Definition | Payout |
|---|---|---|
| Surrender | `chance="0.5" min="3" max="4"` → `PIRATE_SURRENDER` | the standard pirate surrender offer |
| Escape | `chance="0.5" min="2" max="4"` → `PIRATE_ESCAPE` | they jump out; you get nothing |
| Destroyed | `DESTROYED_DEFAULT` (2 identical entries) | `MED standard`, always |
| Dead crew | `DEAD_CREW_DEFAULT` (9 entries) | **3/9** `MED standard`; **2/9** `HIGH standard`; **2/9** `HIGH fuel`; **1/9** a **free crew member** + `LOW scrap_only`; **1/9** `LOW weapon` |

The dead-crew fractions assume uniform selection across list entries; the list states no
weights, only repeated members ([[source-events-xml]], per `raw/gamedata/events.xml`).
Fandom calls the whole table "default rewards"
([[source-fandom-pirate-fight-near-pulsar]]).

## Blue Options
None. Unlike its ASB counterparts [[event-rebel-pds]] and [[event-rebel-auto-pds]], this
event offers **no way to manipulate the hazard** — no Hacking option, nothing
([[source-dlcevents]]).

## Rewards & Risks
- Reward: default rewards only. The pulsar adds no bonus.
- Risk: the pulsar hazard applies to both ships — it periodically disables systems and
  drops shields fleet-wide. Ships that rely on a single strong shield layer or on a
  precisely timed weapon volley suffer most.
- The `PIRATE` block has a 50% escape roll, so a slow kill can end with nothing at all.

## Strategy Notes
- *Opinion, derived from the tables:* boarding is disproportionately good here — 4/9 of the
  dead-crew table beats the flat `MED standard` you get for destroying the hull, and it is
  the only route to the free crew member or the `LOW weapon`. The pulsar's system knockouts
  hurt a boarder less than a weapons-based ship.
- With no choices and no blue options, the only lever is not being at low hull when you
  arrive — and there is no warning: long-range scanners show a ship and a pulsar but not
  which pulsar event you will get.
- The pirate's 50% escape chance argues for burst damage over attrition.

## Related
- [[event-rebel-fight-near-pulsar]] — the identical event with a Rebel ship, in the same
  four override lists plus three more
- [[event-lanius-fight-near-pulsar]] — the Abandoned Sector's pulsar fight
- [[event-fuel-escape-pulsar]] — what happens when you flee a pulsar beacon out of fuel
- [[event-rebel-pds]], [[event-rebel-auto-pds]] — the ASB-hazard siblings from the same
  file, which *do* give you a hazard-manipulation option
- [[entity-pirates]], [[concept-hazards]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] How `<eventCounts sector="N">` in `newEvents.xml` interacts with per-sector-type
      allocation. Read naively it would place `HOSTILE1`/`HOSTILE2` beacons in every sector
      at depths 0–3, which would put this event in more sectors than Fandom lists. Fandom's
      four-sector list matches only the `HOSTILE_ENGI` / `HOSTILE_PIRATE` / `HOSTILE1`
      (Civilian) allocations. Unresolved from the files alone.
- [ ] Numeric scrap values behind `LOW` / `MED` / `HIGH`.
- [ ] How `chance="0.5"` converts to an in-game surrender/escape probability.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `DESTROYED_DEFAULT`, `DEAD_CREW_DEFAULT`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-fight-near-pulsar]] (per raw/wiki/pirate-fight-near-pulsar.md)
