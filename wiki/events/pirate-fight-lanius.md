---
id: event-pirate-fight-lanius
type: event
event_name: LANIUS_PIRATE_FIGHT
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, pirate, combat, no-choice, default-rewards, advanced-edition]
---

# Pirate fight (Lanius) — `LANIUS_PIRATE_FIGHT`

## Summary
An ordinary pirate fight wearing Abandoned Sector clothes. Mechanically it is three lines
— a text list and `<ship load="PIRATE" hostile="true"/>` — and the enemy is the standard
`PIRATE` ship definition from `events_ships.xml`, not a Lanius one. All that is
sector-specific is the flavour: pirates picking through Lanius leftovers, or baiting the
Lanius with scrap metal.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); six members, none duplicated → **1/6** *assuming uniform
  selection across list entries* ([[source-dlcevents-anaerobic]]).
- No `unique` attribute → repeats freely.
- Long-range scanners show a ship ([[source-fandom-pirate-fight-lanius]]).

> **AE-only** as an event: the file and the sector are Advanced Edition. The *enemy* is
> the same `PIRATE` ship the vanilla game uses everywhere.

## Text
`[varies: textList LANIUS_PIRATE_FIGHT_TEXT]` — five strings,
`text_LANIUS_PIRATE_FIGHT_TEXT_1` through `_5`, none duplicated → **1/5** each *assuming
uniform selection across list entries* ([[source-dlcevents-anaerobic]],
[[source-text-events-xml]]). All five are transcribed on
[[source-fandom-pirate-fight-lanius]]. For example:

> An upgraded pirate ship sits among the remains of a number of Lanius ships. It hails
> you, "These punks think they can jus' waltz in here into our sector? Obnoxious, right?
> Well, I'm sure you know the routine, let's do this."

> Debris from a number of battleships are scattered around the beacon. As you approach the
> area a pirate ship thrusts itself through the hulks to attack. It must be using the
> metal to lure the Lanius into a trap.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with the standard `PIRATE` ship; **default rewards**. | 100% |

The `PIRATE` definition ([[source-events-ships]]): surrender `chance="0.5" min="3"
max="4"` → `PIRATE_SURRENDER`; escape `chance="0.5" min="2" max="4"` → `PIRATE_ESCAPE`;
destroyed → `DESTROYED_DEFAULT`; dead crew → `DEAD_CREW_DEFAULT`. Note both chances are
**0.5 against the Lanius ships' 0.2** — pirates here are far more likely to offer terms or
run than the Lanius are ([[source-dlcevents-anaerobic]]).

## Blue Options
None.

## Rewards & Risks
- Reward: default rewards; a surrender offer is comparatively likely.
- Risk: an ordinary pirate warship, sector-scaled. No avoid option.

## Strategy Notes
- The soft option among the sector's hostile beacons: pirates surrender and flee far more
  readily than the Lanius, and their loot table is the generic one rather than the
  Lanius-specific tables on [[event-lanius-fight]].

## Related
- [[event-lanius-fight]], [[event-rebel-fight-lanius]] — the other flavoured fights in
  `HOSTILE_LANIUS`
- [[event-pirate-ship-attacking-civilian-lanius]] — the optional-fight pirate event in
  this sector
- [[event-pirate-fight]] — the generic pirate encounter elsewhere in the game
- [[entity-pirates]], [[sector-abandoned-sector]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind "default rewards" (`DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `PIRATE` ship)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-fight-lanius]] (per raw/wiki/pirate-fight-lanius.md)
