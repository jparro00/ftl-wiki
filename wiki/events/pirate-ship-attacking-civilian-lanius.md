---
id: event-pirate-ship-attacking-civilian-lanius
type: event
event_name: LANIUS_PIRATE_CIVILIAN
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, pirate, civilian-rescue, optional-fight, crew-reward-chance, advanced-edition]
---

# Pirate ship attacking civilian (Lanius) — `LANIUS_PIRATE_CIVILIAN`

## Summary
The Abandoned Sector's re-skin of the classic pirate-attacking-civilian encounter: same
two choices, same rescue list, Lanius-flavoured intro text. Attack the pirate and win, and
you roll the shared "save the civilian" table; walk away and nothing happens.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- No `unique` attribute → repeats freely.
- The pirate spawns as `<ship load="PIRATE_CIVILIAN_LANIUS" hostile="false"/>` — present
  but not shooting at you until you choose to attack.
- Long-range scanners show a ship
  ([[source-fandom-pirate-ship-attacking-civilian-lanius]]).

> **AE-only** as an event. The enemy is a sector-local ship definition,
> `PIRATE_CIVILIAN_LANIUS`, built on the vanilla `SHIPS_PIRATE` blueprint pool.

## Text
`[varies: textList LANIUS_PIRATE_CIVILIAN_TEXT]` — three strings, none duplicated →
**1/3** each *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]], [[source-text-events-xml]]). All three are transcribed on
[[source-fandom-pirate-ship-attacking-civilian-lanius]]. For example:

> You discover an abandoned mining facility in the process of being 'acquired' by the
> Lanius. However, you immediately receive a call from a civilian transport vessel, "Help!
> We were trying to escape before the Lanius came only to be caught by pirates!" You see a
> lone pirate ship boarding the civilian craft.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the pirate. | — | *"You charge your weapons, which quickly gets the pirate ship's attention."* → combat with `PIRATE_CIVILIAN_LANIUS`. Destroyed → `MED standard`; dead crew → `HIGH standard`; either then offers **Contact the civilian ship** (`SAVE_CIVILIAN_LIST`). | 100% |
| 2 | Avoid the conflict. | — | *"Unfortunately it is not your mission to save every person affected by this war or the Lanius invasion."* → nothing happens. | 100% |

### Contact the civilian ship (`SAVE_CIVILIAN_LIST`)
Six members, **1/6** each *assuming uniform selection across list entries*
([[source-events-pirate]]): a survivor who can **join your crew**; `MED standard`;
`LOW standard`; `LOW weapon`; **5 hull repaired**; or nothing. Full table on
[[event-lanius-ship-attacking-civilian-distress]].

## Blue Options
None.

## Rewards & Risks
- `PIRATE_CIVILIAN_LANIUS` defines only `destroyed` and `deadCrew` — **no surrender, no
  escape** ([[source-dlcevents-anaerobic]]). Unlike the plain `PIRATE` ship in
  [[event-pirate-fight-lanius]], this pirate will not offer terms.
- Dead-crew wins pay `HIGH` where hull kills pay `MED`.
- Risk: entirely optional; choice 2 is free.

## Strategy Notes
- Same calculus as [[event-lanius-ship-attacking-civilian]]: one no-surrender warship
  fight for one roll on the rescue list. The pirate here is generally the easier of the
  two, being built on `SHIPS_PIRATE` rather than `SHIPS_LANIUS`.

## Related
- [[event-lanius-ship-attacking-civilian]] — the Lanius-attacker version of the same
  structure
- [[event-lanius-ship-attacking-civilian-distress]] — the rescue list in full
- [[event-pirate-ship-attacking-civilian]] — the generic version elsewhere in the game
- [[entity-pirates]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `LOW` / `MED` / `HIGH`.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml — `SAVE_CIVILIAN_LIST`)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-ship-attacking-civilian-lanius]] (per raw/wiki/pirate-ship-attacking-civilian-lanius.md)
