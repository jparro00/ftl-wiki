---
id: event-no-fuel-mantis-fight
type: event
event_name: FUEL_ON_MANTIS_ATTACK
sectors: []
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, mantis, hostile, no-choice, derived-odds]
---

# No fuel: Mantis fight — `FUEL_ON_MANTIS_ATTACK`

## Summary
One of two "your distress call was answered by the wrong people" draws. A Mantis ship
answers your beacon and attacks immediately — no choices, no way out. The consolation is
that the ship is a fuel carrier: killing it is one of the more reliable ways to actually
end the fuel crisis.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-mantis-fight]]).
- The developer comment block above it in the file is a copy-paste of the ENGI header
  ("Specific no fuel events that should eventually be tied to the engi sector") — it is
  **not** sector-gated ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla (the list loses its
`<!-- DLC -->` `NO_FUEL_REFUGEE` entry). *Assumes uniform selection across list entries*
([[source-events-fuel]]).

## Text
Prose is drawn from the `FUEL_ON_MANTIS_ATTACK` `textList`, which contains **8 entries that
are 4 distinct texts each listed twice** — so the four variants are equally likely at 1/4
whichever way the engine samples ([[source-text-events-xml]]). For example:

> A Mantis ship hails you, "Looks like we found the poor fools that need some help. Come
> brothers, let's 'help' them!" They move in to attack.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event fires straight into combat)* | — | Hostile `MANTIS_FUEL` (auto-blueprint `SHIPS_MANTIS`). | 100% |

### Ship: `MANTIS_FUEL` ([[source-events-ships]])

| Result | Effect |
|---|---|
| Escapes (80s timer, 30s charge) | "The ship jumps away without a word. You hope they didn't leave to get reinforcements." Nothing gained. |
| Destroyed | `autoReward level="MED"` **fuel** (fuel + scrap). |
| Crew killed | `autoReward level="HIGH"` **fuel** (fuel + scrap). |

No `<surrender>` block — this ship cannot be talked down.

## Blue Options
None.

## Rewards & Risks
- Reward: `MED` fuel on destruction, `HIGH` fuel if you kill the crew instead (boarding or
  suffocation pays more here).
- Risk: a full Mantis-ship fight while you cannot jump away. Mantis crews board; with zero
  fuel you have no escape option at all.
- The 80-second escape timer means a slow kill loses the reward entirely.

## Strategy Notes
- *Opinion:* if you have boarders or can vent the ship, go for the crew kill — the reward
  step from `MED` to `HIGH` is the difference between one jump and several.
- This draw is the main downside of switching the distress beacon on: together with
  [[event-no-fuel-rebel-fight]] and [[event-no-fuel-auto-ship-warning]], roughly 3/12 of
  the distress-on pool is an unavoidable fight.

## Related
- [[event-no-fuel-rebel-fight]] — the identical-shape Rebel version (`FUEL_ON_REBEL_ATTACK`)
- [[event-no-fuel-auto-ship-warning]] — the third forced fight in the same pool
- [[entity-mantis]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Why the `textList` duplicates all four entries — deliberate weighting that cancels
      out, or a copy-paste artefact.
- [ ] Exact fuel/scrap values behind `autoReward` `MED` / `HIGH` fuel.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `MANTIS_FUEL`)
- [[source-fandom-no-fuel-mantis-fight]] (per raw/wiki/no-fuel-mantis-fight.md)
