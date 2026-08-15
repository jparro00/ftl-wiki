---
id: event-large-asteroid-field
type: event
event_name: ASTEROID_EXPLORE
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-scrap-recovery-arm]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 13
tags: [unique, filler, blue-option, asteroid-field, fuel-reward-chance, missiles-reward-chance, drone-parts-reward-chance, hull-damage-risk]
---

# Large asteroid field — `ASTEROID_EXPLORE`

## Summary
The game's most widely-distributed filler event: it sits in nearly every neutral pool, in
both hardcoded fallback lists, and doubles as an outcome of the out-of-fuel
[[event-no-fuel-explore-the-system]]. Exploring rolls a six-entry table that is mostly
resources, once nothing, once a hull hit and once a pirate ambush. It is also **the only
event in the game that uses the Scrap Recovery Arm as a blue option**
([[source-fandom-large-asteroid-field]]).

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]], [[sector-abandoned-sector]]
- Event lists — the widest membership in this batch:
  `NEUTRAL_CIVILIAN`, `NEUTRAL`, `NEUTRAL_EXIT` ([[source-newevents]]); `NEUTRAL_ENGI`
  ([[source-events-engi]]); `NEUTRAL_PIRATE` ([[source-events-pirate]]); `NEUTRAL_ZOLTAN`
  ([[source-events-zoltan]]); `NEUTRAL_LANIUS` ([[source-dlcevents-anaerobic]]); and the AE
  fallbacks `OVERRIDE_NEUTRAL` / `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]])
- The two `OVERRIDE_NEUTRAL*` lists are annotated in the file as *"hardcoded to fill out a
  sector if it ran out of all other calls for that sector"* — so this event is also part of
  the generator's last-resort padding ([[source-dlceventsoverwrite]])
- **Also reachable while out of fuel:** `events_fuel.xml` loads
  `ASTEROID_EXPLORE_RESULTS` directly from `FUEL_EXPLORE_LIST`, i.e. from
  [[event-no-fuel-explore-the-system]] — with the same six outcomes but **without** the
  Scrap Recovery Arm blue option, since that lives on the parent event
  ([[source-events-fuel]]; Fandom notes the same difference)
- `unique="true"` — once per run ([[source-events-xml]])

## Text
> Scans reveal a large asteroid field nearby. Short-range scanners may discover useful
> materials while we wait for the FTL to recharge.

(`event_ASTEROID_EXPLORE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Explore the asteroid field. | — | Rolls `ASTEROID_EXPLORE_RESULTS` (6 entries) — see below | 1/6 each |
| 2 | Too dangerous. We'll just wait for the FTL to charge. | — | `<event/>` — literally nothing | 100% |
| 3 | **(Scrap Recovery Arm)** Attempt to mine the asteroids. | `req="SCRAP_COLLECTOR"` | *"You carefully extract as much usable material as possible…"* → `autoReward level="HIGH"` `scrap_only` | 100% |

### Choice 1 → `ASTEROID_EXPLORE_RESULTS`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"A brief exploration yields nothing of interest."* → nothing | 1/6 |
| 2 | *"…You extract some fuel."* → `autoReward level="HIGH"` `fuel_only` | 1/6 |
| 3 | *"…It still has some functional missiles."* → `autoReward level="MED"` `missiles` | 1/6 |
| 4 | *"…A few mining drones were left behind and could be repurposed."* → `autoReward level="MED"` `droneparts` | 1/6 |
| 5 | *"The asteroid field proved more dangerous than expected…"* → `damage 3` + `damage 1 random system` (AE only) + `damage 1 room effect="fire"` | 1/6 |
| 6 | *"A pirate ship hiding behind one of the larger asteroids attacks you!"* → `<ship load="PIRATE" hostile="true"/>` + `<environment type="asteroid"/>` | 1/6 |

Six entries, none duplicated → **1/6 each**, assuming uniform selection across list entries
([[source-events-xml]]).

### The ambush (entry 6)
`<ship name="PIRATE" auto_blueprint="SHIPS_PIRATE">` with `<surrender chance="0.5" min="3"
max="4" load="PIRATE_SURRENDER"/>`, `<escape chance="0.5" min="2" max="4"
load="PIRATE_ESCAPE"/>`, a `<gotaway>` line, and the shared `DESTROYED_DEFAULT` /
`DEAD_CREW_DEFAULT` rewards ([[source-events-ships]]). Per [[concept-surrender-offers]],
`chance="0.5"` is a **50%** surrender offer. The fight is fought inside an asteroid field,
so both ships take rock hits.

## Blue Options
- **[[item-scrap-recovery-arm]]** (`req="SCRAP_COLLECTOR"`, an augment) — replaces the whole
  gamble with a guaranteed `HIGH` `scrap_only`. Fandom notes this is the **only** event in
  the game that uses the Scrap Recovery Arm as a blue-option gate
  ([[source-fandom-large-asteroid-field]]).

## Rewards & Risks
- **Rewards:** `HIGH` fuel, `MED` missiles, or `MED` drone parts — 3 of 6 entries pay
  something, 1 pays nothing.
- **Risks:** 5 hull, a random system down and a fire (entry 5, AE reading); or a Pirate
  fight in an asteroid field (entry 6). Combined that is a **1/3 chance of a bad outcome**.
- Choice 2 is a guaranteed clean skip — rare, and worth remembering when you are low on hull.

## Version Differences
Base-`events.xml` event, present in both editions. One `<!--DLC-->`-marked tag:
`<damage amount="1" system="random"/>` in entry 5 ([[source-events-xml]]). Vanilla therefore
takes **4 hull and a fire**; AE takes 5 hull, a fire, and a random system knocked out.
Fandom's "5 hull, 1 random system, 1 fire" is the AE reading.

The AE fallback lists `OVERRIDE_NEUTRAL` / `OVERRIDE_NEUTRAL_EXIT` redefine the vanilla
`NEUTRAL` / `NEUTRAL_EXIT` pools this event belongs to, so the **surrounding pool** differs
between editions even though the event itself does not ([[source-dlceventsoverwrite]]).

## Strategy Notes
- *(Opinion.)* Without the Scrap Recovery Arm this is a coin-flip-ish gamble that is usually
  worth taking early (fuel and missiles matter most in sectors 1–3) and usually not worth
  taking on a damaged hull late.
- With the Arm equipped there is never a reason to pick choice 1.

## Related
- [[event-no-fuel-explore-the-system]] — loads the same `ASTEROID_EXPLORE_RESULTS` list
- [[event-pirate-fight-in-asteroid-field]] — the same asteroid-field Pirate fight as a
  standalone event
- [[event-asteroid-belt-distress]], [[event-dense-asteroid-field-distress]] — the other
  asteroid-field events in this batch
- [[item-scrap-recovery-arm]]
- [[concept-surrender-offers]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? Every 1/6 above assumes it.
- [ ] Numeric ranges behind `HIGH fuel_only`, `MED missiles`, `MED droneparts`. Fandom gives
      3–6 fuel, 2–4 missiles and 1 drone part, but the game files state only the level.

> ⚠️ **CONTRADICTION (sector list):** [[sector-federation-space]].
> - Game files: `NEUTRAL_CIVILIAN` (which contains `ASTEROID_EXPLORE`) is allocated
>   `min=2 max=4` in `STANDARD_SPACE`, whose display name is *Federation Space*
>   ([[source-newevents]], [[source-sector-data-xml]], [[source-text-sectorname-xml]]).
> - Fandom: its location list omits Federation Space entirely
>   ([[source-fandom-large-asteroid-field]]).
>
> Trusting the game files. This omission is **systematic** across Fandom's `{{Locations}}`
> templates for generic events, not specific to this page, so it reads as a wiki convention
> (treating sector 1 separately) rather than a factual claim that the event cannot occur
> there.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `NEUTRAL`, `NEUTRAL_CIVILIAN`, `NEUTRAL_EXIT`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-dlcevents-anaerobic]] (per `raw/gamedata/dlcEvents_anaerobic.xml` — `NEUTRAL_LANIUS`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-events-fuel]] (per `raw/gamedata/events_fuel.xml` — `FUEL_EXPLORE_LIST`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml` — the `PIRATE` ship)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-large-asteroid-field]] (per `raw/wiki/large-asteroid-field.md`)
