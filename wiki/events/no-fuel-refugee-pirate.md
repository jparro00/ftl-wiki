---
id: event-no-fuel-refugee-pirate
type: event
event_name: NO_FUEL_REFUGEE_PIRATE
sectors: []
beacon_type: distress
hostile: unknown
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, distress-beacon, refugee, pirate, trading, advanced-edition, derived-odds]
---

# No fuel: refugee wanting armaments — `NO_FUEL_REFUGEE_PIRATE`

## Summary
A refugee ship answers your distress call wanting weapons, not scrap. The name gives away
the twist: half of each branch is a pirate ambush. Trading is nonetheless the better line —
you keep the fuel even when they turn on you, whereas refusing is a coin flip between a
free fight and nothing much.

## Trigger & Where It Appears
- **Not a sector event, and not directly in a pool.** Member of the `NO_FUEL_REFUGEE` event
  list, which is one entry in `NO_FUEL_DISTRESS` — the distress-beacon-**on** out-of-fuel
  pool ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Version: `ae`.** The `NO_FUEL_REFUGEE` entry carries `<!-- DLC - below -->` and the block
sits under the file's `DLC!!!` header ([[source-events-fuel]]). Not present in vanilla.

**Derived odds.** 1 of 3 members of `NO_FUEL_REFUGEE`, which is 1 of 12 entries in the AE
`NO_FUEL_DISTRESS` list → **1/36 (~2.8%)** per wait. *Assumes uniform selection across list
entries.*

## Text
> A refugee ship fleeing the Rebel advance enters the system, having picked up your distress
> beacon. While it doesn't have much fuel to spare, it is bad need of armaments and is
> willing to trade for them.

(`event_NO_FUEL_REFUGEE_PIRATE_text`, per [[source-text-events-xml]] — the missing "in" is
in the game file.)

No `<ship>` tag until a branch produces one.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Offer some missiles for fuel. | — | Loads `NO_FUEL_REFUGEE_PIRATE_ACCEPT` (2 entries) — see below. | — |
| 2 | Refuse their offer. | — | Loads `NO_FUEL_REFUGEE_PIRATE_REJECT` (4 entries) — see below. | — |

### Choice 1 — `NO_FUEL_REFUGEE_PIRATE_ACCEPT` (2 entries, 1/2 each)

| Outcome | Result | Odds |
|---|---|---|
| "The refugee ship makes the exchange, and wishes you well on your mission." | **−1 missile, +5–7 fuel.** | 1/2 |
| "Having traded supplies, the ship suddenly powers up and attacks - it's a pirate ship!" | **−1 missile, +5–7 fuel**, *then* a hostile `PIRATE` (default rewards). You keep the fuel. | 1/2 |

### Choice 2 — `NO_FUEL_REFUGEE_PIRATE_REJECT` (4 entries)

The fourth entry is a **duplicate** of the third, so the pirate ambush is weighted double:

| Outcome | Result | Odds |
|---|---|---|
| "The refugee ship apologizes, but they need their fuel." | Nothing happens. | 1/4 |
| "Sensing your reluctance, the refugee ship nevertheless parts with a small amount of fuel." | `autoReward level="LOW"` **fuel_only**. | 1/4 |
| "Taking your reluctance as weakness, the refugee ship suddenly bristles with weapons - it's a pirate ship, and it believes it's found easy prey!" | Hostile `PIRATE` (default rewards). **Listed twice in the 4-entry list → 2/4.** | 2/4 (1/2) |

All the fractions above are derived from `<eventList>` entry counts and **assume uniform
selection across list entries** ([[source-events-fuel]]). Fandom independently flags the
duplicate with its `{{DuplicateEvent|2}}` marker, agreeing on the doubled weight
([[source-fandom-no-fuel-refugee-trading]]).

### Ship: `PIRATE` ([[source-events-ships]])
Auto-blueprint `SHIPS_PIRATE`, default rewards. 50% surrender chance (3–4 charge) and a 50%
escape chance (2–4 charge).

## Blue Options
None. Notably, the Engi blue option that helps on [[event-no-fuel-refugee-damaged]] does
**not** appear here.

## Rewards & Risks
- Trading always pays: **1 missile buys 5–7 fuel**, one of the best fuel rates anywhere in
  the out-of-fuel family, and you keep it even in the ambush branch.
- Refusing is worse on every axis: 1/2 a pirate fight for default rewards, 1/4 a small
  `LOW` fuel handout, 1/4 nothing.
- Overall a 50% chance of a pirate fight either way — with the fuel already banked if you
  traded.

## Strategy Notes
- *Opinion:* trade. The fuel is unconditional, the missile cost is trivial next to being
  stranded, and the ambush risk is identical to the risk you take by refusing. There is no
  branch where refusing beats trading.
- The fight is a standard `PIRATE` and can surrender, so it is not necessarily a bad
  outcome — but with zero fuel you cannot disengage if it goes badly.

## Related
- [[event-no-fuel-refugee-damaged]] — the sibling refugee event in the same list
- [[event-no-fuel-friendly-refugee]] — the distress-off refugee, free and safe
- [[event-no-fuel-prepare-to-dock]] — the other out-of-fuel event with pirate-ambush branches
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact fuel value of `autoReward level="LOW"` fuel_only (Fandom reads it as 1–3).
- [ ] Whether the duplicated reject entry is deliberate weighting or a copy-paste artefact,
      as with the `FUEL_ON_MANTIS_ATTACK` text list.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-refugee-trading]] (per raw/wiki/no-fuel-refugee-trading.md — the
  Fandom page covers the whole `NO_FUEL_REFUGEE` list, including this event)
