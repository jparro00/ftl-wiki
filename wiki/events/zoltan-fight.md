---
id: event-zoltan-fight
type: event
event_name: ZOLTAN_FIGHT
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [filler-fight, default-rewards, varies-text, repeatable]
---

# Zoltan fight — `ZOLTAN_FIGHT`

## Summary
The baseline hostile encounter of Zoltan space: a Zoltan warship, no choices, default
rewards. It is **repeatable** (not `unique`) and shares the largest event allocation in
the sector, so it is the fight you will see most often here.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-zoltan-fight]]).
- Reached via `HOSTILE_ZOLTAN` (vanilla) / `OVERRIDE_HOSTILE_ZOLTAN` (AE), allocated
  `min=6 max=8` beacons in both Zoltan sectors ([[source-sector-data-xml]]).
- **Not** `unique="true"` — it can and does repeat within a sector.

## Text
`[varies: textList ZOLTAN_FIGHT]` — the intro is drawn from a seven-entry text list
(`text_ZOLTAN_FIGHT_1` … `_7`), with no repeated entries, so each is equally likely
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml). The file carries the
developer note `<!-- Add more! -->`.

The seven variants, per [[source-fandom-zoltan-fight]]:

1. *A Zoltan ship makes contact. "The nature of the day is rotational. The fever is emaciated. The reason is-" They've caught some nasty deep space dementia. Before you can consider finding help for them, they open fire.*
2. *You're surprised when a stationary Zoltan ship opens fire. It appears there are aggressive pugilists even among the 'enlightened'.*
3. *You receive a message, "This area is off limits. Submit your ship to processing." It's only one guard ship in a lonely beacon. You decide to fight your way out.*
4. *You discover a number of Zoltan civilian ships fighting off pirates. Unfortunately one ship mistakes your purpose and moves in to attack! They are refusing all communication; you have no choice but to fight.*
5. *Like many areas in Zoltan space, the residents of this sector prepared well for Galactic war. The military here seem to have given up reasoning with foreigners, preferring instead to attack on sight!*
6. *A Zoltan ship is waiting at this beacon. They request your identification, but radiation from the sun in this system is disrupting your communications. They take your silence for aggression and move in to attack.*
7. *The Zoltan ship patrolling this area hails you: "This area is off limits. Secrecy is vital." They power their weapons.*

Fandom's list of seven matches the seven text ids the game file references, so the two
sources agree on the count here.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="ZOLTAN_SHIP" hostile="true"/>` — immediate fight with a Zoltan ship ([[entity-zoltan]]), **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Default rewards for a Zoltan ship at the current sector depth.
- Risk is the fight itself. Zoltan ships carry the **Zoltan Super Shield**, an extra
  layer that must be stripped before normal shields even begin to matter — the defining
  difficulty of the sector. `NOTHING_ZOLTAN` flavour text spells out the counter in-game:
  *"Their Energy Shields are impressive, but you note how quickly beam and ion weaponry
  take them down"* ([[source-text-events-xml]], via
  [[event-empty-beacon-zoltan]]).
- No environment hazard, boarders, or scripted system damage.

## Strategy Notes
- *Opinion:* the recurring nature of this event is the real reason Zoltan sectors punish
  laser-only builds — you will fight Super Shields six to eight times per sector, not
  once. Ion and beam weapons, or a boarding party, change the sector's difficulty
  substantially.
- `ZOLTAN_SHIP` is the same ship blueprint used by
  [[event-zoltan-fight-in-asteroid-field]], [[event-zoltan-security-checkpoint]]
  (choice 1) and [[event-zoltan-great-eye]] (fight outcome), so experience here
  transfers directly.

> ⚠️ **CONTRADICTION (version):** which event list supplies this event.
> - `HOSTILE_ZOLTAN` in raw/gamedata/events_zoltan.xml — 7 entries.
> - `OVERRIDE_HOSTILE_ZOLTAN` in raw/gamedata/dlcEventsOverwrite.xml — the same 5 Zoltan
>   events plus `REBEL`, `REBEL_AUTO` and an added `REBEL_PULSAR`, 8 entries — replaces
>   `HOSTILE_ZOLTAN` when AE content is enabled ([[source-events-zoltan]]).
>
> A genuine **vanilla-vs-AE difference, not an error**. `ZOLTAN_FIGHT`'s share of the
> hostile pool drops from 1-in-7 to 1-in-8 in AE.

## Related
- [[event-pirate-fight-zoltan]] — the other repeatable filler fight in the same pool
- [[event-zoltan-fight-in-asteroid-field]] — the same ship, plus an asteroid hazard
- [[event-mantis-fight-zoltan]], [[event-engi-fight]] — the other unique fights in the pool
- [[entity-zoltan]], [[item-zoltan-shield]] — the opponent and its signature defence
- [[event-zoltan-surrender]] — the authored-but-unloaded `ZOLTAN_SURRENDER` aftermath; no Zoltan hull references it

## Open Questions
- [ ] Which `ZOLTAN_SHIP` blueprints spawn at each sector depth.
- [ ] Confirm the seven Fandom text variants map one-to-one onto
      `text_ZOLTAN_FIGHT_1`…`_7` in order (they were not individually grepped).

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-fight]] (per raw/wiki/zoltan-fight.md)
