---
id: event-no-fuel-auto-ship-warning
type: event
event_name: FUEL_ON_REBEL_WARNING
sectors: []
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, rebel, auto-ship, hostile, rebel-fleet, no-choice, derived-odds]
---

# No fuel: Auto-ship warning — `FUEL_ON_REBEL_WARNING`

## Summary
The worst draw in the distress-on pool. A Rebel automated scout answers your beacon,
identifies you, and immediately starts charging its FTL to report your position. It is the
only out-of-fuel fight on a **40-second** timer instead of the usual 80 — and the only one
that makes the Rebel fleet close faster if you fail to kill it in time.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-auto-ship-warning]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries* ([[source-events-fuel]]).

## Text
> A ship responding to your distress moves in. Unfortunately it turns out to be an
> automated Rebel scout. It immediately reverses thrust after scanning your ship.

(`event_FUEL_ON_REBEL_WARNING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event fires straight into combat)* | — | Hostile `REBEL_AUTO_WARNING` (auto-blueprint `SHIPS_AUTO`), already fleeing. | 100% |

### Ship: `REBEL_AUTO_WARNING` ([[source-events-ships]])

| Result | Effect |
|---|---|
| Escape sequence (starts **immediately**, `timer="40"`, charge `min/max=22`) | "The ship starts to power up its FTL Drive. If it gets away, it will no doubt warn the fleet of your position!" |
| Gets away | "The scout jumps away. It will certainly have informed the fleet of your position." → **`<modifyPursuit amount="1"/>` — the Rebel fleet advances an extra step.** |
| Destroyed | "The ship breaks apart and you feel relief…" → `autoReward level="LOW"` **standard** (scrap with resources). |

There is no `deadCrew` block — it is an auto-ship with no crew to kill.

> ⚠️ **CONTRADICTION:** what "gets away" costs.
> - Game files: `<modifyPursuit amount="1"/>` — one extra fleet advance
>   ([[source-events-fuel]], per raw/gamedata/events_ships.xml).
> - Fandom: *"Rebel Fleet pursuit is **doubled**"*
>   ([[source-fandom-no-fuel-auto-ship-warning]]).
>
> Trusting the game files (`high` vs `medium`). The two may be describing the same thing —
> one extra advance on top of the one the wait already costs *is* double for that turn —
> but Fandom's phrasing is not what the tag says, and no source confirms the reading.

## Blue Options
None.

## Rewards & Risks
- Reward if killed in time: `LOW` standard rewards — scrap with resources. This is the
  **only** forced out-of-fuel fight that does not pay fuel; you get scrap, not a way out.
- Risk: 40 seconds to kill an auto-ship, or the Rebel fleet closes on you while you are
  already unable to jump.

## Strategy Notes
- *Opinion:* this is the draw that argues for turning the distress beacon back **off** once
  you have banked a couple of good rolls — it is the only out-of-fuel event that actively
  worsens the fleet timer, and the reward for winning does not solve the fuel problem.
- Fandom notes the 40-second timer is shared with the ordinary *Auto-ship warning*,
  *Auto-ship warning in nebula* and *Rebel ship warning* events, and is half the 80-second
  timer used by every other out-of-fuel ship
  ([[source-fandom-no-fuel-auto-ship-warning]]) — corroborated by the `timer="40"` value in
  the ship block ([[source-events-ships]]).

## Related
- [[event-auto-ship-warning]] / [[event-auto-ship-warning-in-nebula]] — the same scout on the
  same 40s timer outside the out-of-fuel pool
- [[event-no-fuel-rebel-fight]], [[event-no-fuel-mantis-fight]] — the other two forced
  fights in this pool
- [[event-no-fuel-rebel-fleet-delay]] — the mirror image, in the distress-off pool
- [[concept-rebel-fleet-advance]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Whether `modifyPursuit amount="1"` here stacks with the advance the wait itself costs.
- [ ] Exact scrap value of `autoReward level="LOW"` standard.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `REBEL_AUTO_WARNING`)
- [[source-fandom-no-fuel-auto-ship-warning]] (per raw/wiki/no-fuel-auto-ship-warning.md)
