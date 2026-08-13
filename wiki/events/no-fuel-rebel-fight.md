---
id: event-no-fuel-rebel-fight
type: event
event_name: FUEL_ON_REBEL_ATTACK
sectors: []
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, rebel, hostile, no-choice, derived-odds]
---

# No fuel: Rebel fight — `FUEL_ON_REBEL_ATTACK`

## Summary
Your distress call is answered by a Rebel fighter that recognises you. No choices; the
fight starts immediately. Mechanically identical to [[event-no-fuel-mantis-fight]] — a
fuel-carrying enemy that pays `MED` fuel when destroyed and `HIGH` when its crew is killed.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-rebel-fight]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries* ([[source-events-fuel]]).

## Text
Prose is drawn from the `FUEL_ON_REBEL_ATTACK` `textList`, **4 variants**, each listed once
([[source-text-events-xml]]). For example:

> A Rebel ship hails you, "Hello citizen. We are responding to your distress call and can
> assist... Wait a second... You're that ship! Prepare to die!"

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event fires straight into combat)* | — | Hostile `REBEL_FUEL` (auto-blueprint `SHIPS_REBEL`). | 100% |

### Ship: `REBEL_FUEL` ([[source-events-ships]])

| Result | Effect |
|---|---|
| Escapes (80s timer, 30s charge) | "The ship jumps away without a word. You hope they didn't leave to get reinforcements." Nothing gained. |
| Destroyed | `autoReward level="MED"` **fuel** (fuel + scrap). |
| Crew killed | `autoReward level="HIGH"` **fuel** (fuel + scrap). |

No `<surrender>` block.

Note this is a plain Rebel fighter, **not** a fleet ship — it does not advance Rebel
pursuit on escape, unlike [[event-no-fuel-auto-ship-warning]].

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` fuel destroyed, `HIGH` fuel on a crew kill.
- Risk: an ordinary Rebel fighter fight, unavoidable, with no fuel to disengage. Losing is
  a run-ender; the ship escaping after 80 seconds costs you the reward but nothing else.

## Strategy Notes
- *Opinion:* prefer the crew kill for the `HIGH` reward tier if you have the tools, but do
  not stall past the 80-second escape timer chasing it — an escaped ship pays nothing.
- One of three forced fights in the distress-on pool (with
  [[event-no-fuel-mantis-fight]] and [[event-no-fuel-auto-ship-warning]]), roughly 3/12 of
  that pool.

## Related
- [[event-no-fuel-mantis-fight]] — same structure, Mantis hull
- [[event-no-fuel-auto-ship-warning]] — the third forced fight, and the only one with a
  fleet-advance penalty
- [[entity-rebels]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact fuel/scrap values behind `autoReward` `MED` / `HIGH` fuel.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `REBEL_FUEL`)
- [[source-fandom-no-fuel-rebel-fight]] (per raw/wiki/no-fuel-rebel-fight.md)
