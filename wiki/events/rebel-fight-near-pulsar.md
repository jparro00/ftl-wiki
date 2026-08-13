---
id: event-rebel-fight-near-pulsar
type: event
event_name: REBEL_PULSAR
sectors: [[[sector-civilian-sector]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, combat, pulsar, hazard, no-choice, default-rewards, unique, advanced-edition]
---

# Rebel fight near pulsar — `REBEL_PULSAR`

## Summary
The Rebel twin of [[event-pirate-fight-near-pulsar]] and structurally identical to it: a
text list, a `REBEL` ship, `<environment type="pulsar"/>`, no choices. It appears in more
override lists than any other pulsar event — five of them — which makes it the pulsar fight
you are most likely to meet across a run.

## Trigger & Where It Appears
- Sectors, per [[source-fandom-rebel-fight-near-pulsar]]: [[sector-civilian-sector]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]].
- Lists: five Advanced Edition override lists in `dlcEventsOverwrite.xml` —
  `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_MANTIS`,
  `OVERRIDE_HOSTILE_REBEL` and `OVERRIDE_HOSTILE_ZOLTAN` ([[source-dlceventsoverwrite]]).
  These replace the vanilla `HOSTILE1`, `HOSTILE2`, `HOSTILE_MANTIS`, `HOSTILE_REBEL` and
  `HOSTILE_ZOLTAN` lists when the DLC is on.
- Share of a hostile beacon *assuming uniform selection across list entries*: **1/12** in
  `OVERRIDE_HOSTILE1`, **1/15** in `OVERRIDE_HOSTILE2`, **1/8** in
  `OVERRIDE_HOSTILE_MANTIS` (note `MANTIS_FIGHT` is listed twice there, so that list is not
  flat overall — `REBEL_PULSAR` itself appears once), **1/6** in `OVERRIDE_HOSTILE_REBEL`,
  **1/8** in `OVERRIDE_HOSTILE_ZOLTAN` ([[source-dlceventsoverwrite]]).
- Allocation: `HOSTILE_MANTIS` `min="6" max="7"` in both Mantis sectors, `HOSTILE_REBEL`
  `min="6" max="8"` in both Rebel sectors, `HOSTILE_ZOLTAN` `min="6" max="8"` in both Zoltan
  sectors, `HOSTILE1` `min="2" max="2"` in `CIVILIAN_SECTOR` and `STANDARD_SPACE`
  ([[source-sector-data-xml]]). `HOSTILE1` and `HOSTILE2` are also allocated by the
  depth-based `<eventCounts sector="0">` … `sector="3"` blocks in `newEvents.xml`
  ([[source-newevents]]) — see *Open Questions*.
- `unique="true"` — at most once per run ([[source-dlcevents]]).
- Long-range scanners show a **ship and a pulsar**
  ([[source-fandom-rebel-fight-near-pulsar]], `LRSmap=ship+pulsar`).
- `OVERRIDE_HOSTILE_REBEL` is the smallest list it belongs to (6 members), so a Rebel sector
  is where it is most likely to come up.

> **AE-only.** Defined in `dlcEvents.xml` and reachable only through `OVERRIDE_` lists that
> take effect with the DLC on ([[source-dlcevents]], [[source-dlceventsoverwrite]]).
> **Vanilla behaviour is this event not existing** — the vanilla `HOSTILE1` in
> `newEvents.xml` has no pulsar entry ([[source-newevents]]). Fandom categorises it as
> *Advanced Edition Content Events*.

## Text
`[varies: textList REBEL_PULSAR_TEXT]` — the list is itself tagged `<!--DLC2-->` and holds
six `<text>` entries drawing on **three** distinct strings, each listed twice with a
`<!-- NEEDS MORE-->` comment between the blocks. The duplication is stated padding, so
effectively **1/3 each** *assuming uniform selection across list entries*
([[source-dlcevents]]). All three, per [[source-text-events-xml]]:

> A Rebel captain appears on the screen. "I thought we had been doomed to backwater
> assignments. This is my chance to get back in Command's good graces! Charge the weapons!"

> A small rebel research station overlooks a pulsating star. Before you can react a Rebel
> ship spots you and moves in to attack.

> You arrive at an infrequently used beacon close to a pulsar. Before long a Rebel ship
> happens to jump nearby. Looks like you'll have to fight.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `REBEL` under a pulsar. **Default rewards.** | 100% |

### The `REBEL` enemy
`auto_blueprint="SHIPS_REBEL"`, defined in `raw/gamedata/events_ships.xml`
([[source-events-ships]]):

| Outcome | Definition | Payout |
|---|---|---|
| Surrender | `chance="0.5" min="2" max="3"` → `PIRATE_SURRENDER` | the standard surrender offer |
| Escape | `chance="0.5" min="3" max="4"` → `PIRATE_ESCAPE` | they jump out; you get nothing |
| Destroyed | `DESTROYED_DEFAULT` (2 identical entries) | `MED standard`, always |
| Dead crew | `DEAD_CREW_DEFAULT` (9 entries) | **3/9** `MED standard`; **2/9** `HIGH standard`; **2/9** `HIGH fuel`; **1/9** a **free crew member** + `LOW scrap_only`; **1/9** `LOW weapon` |

Fractions assume uniform selection across list entries; the list states no weights, only
repeated members ([[source-events-xml]], per `raw/gamedata/events.xml`). Fandom calls this
"default rewards" ([[source-fandom-rebel-fight-near-pulsar]]). Note the `REBEL` block
declares **no `<gotaway>`** text, unlike `PIRATE`.

## Blue Options
None — no choices exist at all ([[source-dlcevents]]).

## Rewards & Risks
- Reward: default rewards. The pulsar adds nothing.
- Risk: the pulsar disables systems and drops shields on **both** ships periodically. Rebel
  ships are ordinary crewed warships, so the hazard is symmetric — it is the more fragile
  ship that suffers.
- 50% escape roll means a slow fight can pay nothing.

## Strategy Notes
- *Opinion, derived from the tables:* kill the crew rather than the hull where you can —
  4/9 of `DEAD_CREW_DEFAULT` beats the flat `MED standard` from destruction, and it is the
  only path to a free crew member.
- The pulsar's shield drops are an opportunity for a boarding party and a problem for a
  missile-and-ion build that needs reliable timing.
- Nothing about this event can be avoided, deferred or negotiated once you jump in.

## Related
- [[event-pirate-fight-near-pulsar]] — the identical event with a Pirate ship
- [[event-lanius-fight-near-pulsar]] — the Abandoned Sector's pulsar fight
- [[event-fuel-escape-pulsar]] — the out-of-fuel escape from a pulsar beacon
- [[event-rebel-pds]] — the ASB-hazard Rebel fight from the same file, which *does* offer
  Hacking options
- [[entity-rebels]], [[concept-hazards]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] How `<eventCounts sector="N">` in `newEvents.xml` interacts with per-sector-type
      allocation — a naive reading would place `HOSTILE1`/`HOSTILE2` beacons in every sector
      at depths 0–3, which is broader than Fandom's seven-sector list.
- [ ] Numeric scrap values behind `LOW` / `MED` / `HIGH`.
- [ ] Whether the `<!--DLC2-->` tag on `REBEL_PULSAR_TEXT` marks a later AE content pass
      (the reading here) or something else.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `DESTROYED_DEFAULT`, `DEAD_CREW_DEFAULT`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-near-pulsar]] (per raw/wiki/rebel-fight-near-pulsar.md)
