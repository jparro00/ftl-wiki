---
id: event-auto-ship-warning-in-nebula
type: event
event_name: NEBULA_AUTO_WARNING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [nebula, rebel, auto-ship, no-choice, combat, fleet-advance, escape, unique]
---

# Auto-ship warning in nebula — `NEBULA_AUTO_WARNING`

## Summary
A timed kill. A Rebel drone is already charging its FTL when you arrive; you have 40
seconds to destroy it or the Rebel fleet advances. There are no choices — the entire
event is the fight, and everything interesting lives in the ship definition rather than
the event.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA`, `NEBULA_HOSTILE`, `NEBULA_REBEL` ([[source-newevents]],
  [[source-events-nebula]], [[source-events-rebel]]), reaching Federation Space and
  Civilian via `NEBULA`, both Rebel sectors via `NEBULA_REBEL`, Pirate and Zoltan sectors
  through the nested `NEBULA_REBEL` entry, and [[sector-uncharted-nebula]] via
  `NEBULA_HOSTILE` (5–6 beacons per sector, [[source-sector-data-xml]]).
- Long-range scanners show a ship ([[source-fandom-auto-ship-warning-in-nebula]]).

## Text
> It appears that an automated Rebel scout was positioned within the nebula to warn of
> your passing.

(`event_NEBULA_AUTO_WARNING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `REBEL_AUTO_WARNING`, which is **already trying to escape**. | 100% |

The whole event is `<text>` + `<ship load="REBEL_AUTO_WARNING" hostile="true"/>` +
`<environment type="nebula"/>` ([[source-events-nebula]]). The `REBEL_AUTO_WARNING`
definition in `events_ships.xml` ([[source-events-ships]]) supplies the rest:

| Ship outcome | XML | Effect |
|---|---|---|
| Escape attempt | `<escape timer="40" min="22" max="22">` | *"The ship starts to power up its FTL Drive. If it gets away, it will no doubt warn the fleet of your position!"* — Fandom reads this as the escape starting **immediately** on a **40-second timer** ([[source-fandom-auto-ship-warning-in-nebula]]). |
| Got away | `<gotaway>` + `<modifyPursuit amount="1"/>` | *"The scout jumps away… You must get to the next sector as soon as possible!"* The Rebel fleet advances. |
| Destroyed | `<destroyed>` + `autoReward level="LOW">standard` | *"The ship breaks apart and you feel relief in the knowledge that you will hopefully still be one step ahead of the fleet."* — **low** scrap with resources. |

> ⚠️ **CONTRADICTION (framing, not fact):** Fandom renders `<modifyPursuit amount="1"/>`
> as *"Rebel Fleet pursuit is doubled"* ([[source-fandom-auto-ship-warning-in-nebula]]),
> while the game files state only the raw amount, with no unit or multiplier
> ([[source-events-ships]]). The sibling page for `NEBULA_REBEL_UNDETECTED` glosses the
> *same* element as *"doubled for 1 jump"*
> ([[source-fandom-rebel-fight-choice-in-nebula]]) — so Fandom is not self-consistent
> either. Trusting the game files for what is recorded (`+1`) and treating the "doubled"
> reading as an unverified interpretation.

## Blue Options
None. There is no engines/cloaking out — unusually for a nebula escape event, the game
gives you no lever at all.

## Rewards & Risks
- Reward: `LOW` / `standard` — a deliberately poor payout for a fight you are forced into.
- Risk: **fleet advance**. Failing to kill it in 40 seconds is a strategic loss, not a
  material one; nothing is damaged, but the map gets worse.
- Fought in a nebula, so your sensors are down for the duration — you are shooting blind
  against a clock.

## Strategy Notes
- Everything must be pointed at the drone from the first second. This is one of the few
  FTL fights where a slow, high-damage weapon loadout is actively bad.
- 22 is the hull threshold on the `escape` element, not a percentage — the source does not
  state how it converts to the auto-ship's actual hull pool.
- Categorised by Fandom as a `Rebel Fleet advancement hazard` (as opposed to a *risk*):
  the advance is the default outcome unless you actively prevent it
  ([[source-fandom-auto-ship-warning-in-nebula]]).

## Related
- [[event-auto-ship-fight-in-nebula]] — the same drone with no timer
- [[event-auto-ship-fight-in-plasma-storm]] — storm variant, with escape options
- [[event-auto-ship-near-storage-station-in-nebula]]
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] What `min="22" max="22"` means in absolute hull terms for `SHIPS_AUTO`.
- [ ] Whether `modifyPursuit amount="1"` doubles pursuit, adds one jump of advance, or
      something else — no source read here states the mechanic.
- [ ] Numeric values behind `autoReward level="LOW">standard`.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-auto-ship-warning-in-nebula]] (per raw/wiki/auto-ship-warning-in-nebula.md)
