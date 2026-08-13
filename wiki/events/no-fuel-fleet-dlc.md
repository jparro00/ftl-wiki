---
id: event-no-fuel-fleet-dlc
type: event
event_name: NO_FUEL_FLEET_DLC
sectors: []
beacon_type: unknown
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rebel-fleet, hostile, orphan, engine-event, no-choice, advanced-edition, pds]
---

# No fuel: the fleet arrives (AE) — `NO_FUEL_FLEET_DLC`

## Summary
The Advanced Edition version of [[event-no-fuel-fleet]]. Same predicament, same elite Rebel
fuel carrier, same 2–4 fuel payout — but AE adds a **Planetary Defense System firing on
your ship** for the duration of the fight. It is the harshest form of the out-of-fuel
failure state in the game.

## Trigger & Where It Appears
**Not in any sector event list, and not in either out-of-fuel pool.** Like its base-game
counterpart, `NO_FUEL_FLEET_DLC` appears in `raw/gamedata/` only in its own definition
([[source-events-fuel]]). It carries `<fleet>rebel</fleet>`, which switches the beacon to
the Rebel-fleet state — consistent with being loaded by the engine when the fleet overtakes
a stranded ship rather than drawn from a list. **No source states the trigger explicitly.**

**Version.** `ae`. Two independent signals: the `_DLC` suffix, and
`<environment type="PDS" target="player"/>` — the Planetary Defense System is an Advanced
Edition hazard ([[source-events-fuel]]). It sits directly beneath `NO_FUEL_FLEET` in the
base file rather than in `dlcEvents.xml`, so it is an AE-only event defined in a shared
file, not an override.

## Text
> Your pilot deftly avoids incoming artillery fire from the surrounding fleet while you try
> to sort out exactly what your plan is... One of the many approaching fighters gets into
> weapon range and your scanners detect it has surplus fuel. Maybe you can still pull this
> off.

(`event_NO_FUEL_FLEET_DLC_text`, per [[source-text-events-xml]])

The prose is a near-twin of the unreferenced [[event-fuel-escape-fleet]], whose text reads
"Your pilot deftly avoids the artillery fire from the surrounding fleet while you try to
sort out exactly what your plan is....". This one continues into the fight; that one stops
at the first sentence.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — straight into combat)* | — | Hostile `REBEL_FLEET_FUEL`, **plus `<environment type="PDS" target="player"/>` — a Planetary Defense System firing at your ship throughout.** | 100% |

### Ship: `REBEL_FLEET_FUEL` ([[source-events-ships]])

Identical to [[event-no-fuel-fleet]]: auto-blueprint `SHIPS_REBEL_ELITE`, 80-second escape
timer with a 30-second charge.

| Result | Effect |
|---|---|
| Escapes | "The ship jumps away without a word. You assume they just went to get reinforcements..." Nothing gained. |
| Destroyed | "You manage to retrieve a few precious fuel capsules. You hurry to jump away from the cruiser fire!" → `item_modify` **+2–4 fuel**. |
| Crew killed | Same text, same **+2–4 fuel**. |

A flat `item_modify`, not an `autoReward` — no scrap, no reward tiering.

## Blue Options
None.

## Rewards & Risks
- Reward: 2–4 fuel. Unchanged from vanilla.
- Risk: an elite Rebel fighter *and* incoming PDS fire, with no fuel to disengage and an
  80-second window before the target jumps away.
- The PDS is the whole difference between editions, and it is a pure downside — AE made
  this event strictly harder for the same payout.

## Strategy Notes
- *Opinion:* the PDS makes shields and evasion matter more than damage race here, but the
  escape timer punishes stalling. Nothing in the event can be played around; the only real
  mitigation is not reaching this state.
- Because the reward is a flat `item_modify`, a crew kill is worth no more than a hull kill
  — take whichever is faster and get out from under the PDS.

## Related
- [[event-no-fuel-fleet]] — the base-game version, identical minus the PDS
- [[event-fuel-escape-fleet]] — an unreferenced AE event with near-identical prose
- [[event-no-fuel-rebel-fleet-delay]] — the mechanic that postpones ever reaching this event
- [[concept-rebel-fleet-advance]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine picks this over `NO_FUEL_FLEET` when AE is enabled, and that the
      two never both fire.
- [ ] Whether the PDS here uses the standard AE PDS damage profile.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `REBEL_FLEET_FUEL`)
