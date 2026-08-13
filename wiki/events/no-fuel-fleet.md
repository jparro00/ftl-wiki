---
id: event-no-fuel-fleet
type: event
event_name: NO_FUEL_FLEET
sectors: []
beacon_type: unknown
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rebel-fleet, hostile, orphan, engine-event, no-choice]
---

# No fuel: the fleet arrives — `NO_FUEL_FLEET`

## Summary
What happens when you run out of fuel and stall long enough for the Rebel fleet to reach
your beacon. There is no choice and no negotiation: an elite Rebel fighter is in range and
carrying fuel, and you attack it because it is the only way out. Killing it yields 2–4
fuel — exactly enough to jump.

## Trigger & Where It Appears
**Not in any sector event list, and not in either out-of-fuel pool.** `NO_FUEL_FLEET`
appears in `raw/gamedata/` only in its own definition ([[source-events-fuel]]). Two pieces
of evidence place it as an engine-triggered event rather than a drawn one:

1. The file's own structure comment lists it **above** the two pools as a standalone item,
   not as a member of either:
   ```
   Structure:
   	NO_FUEL_FLEET

   No Beacon:    	NO_FUEL (this is a list)
   ```
2. It carries `<fleet>rebel</fleet>`, which switches the beacon to the Rebel-fleet
   background — a state the engine sets when the fleet overtakes you, not something an
   ordinary wait produces ([[source-events-fuel]]).

**No source states the trigger explicitly**, and there is no Fandom page for it. The
reading above is inference from the file, recorded as such.

## Text
> The Rebel fleet has caught up to you. You detect significant fuel reserves in one of
> their closer fighters and move in to attack. Maybe you can still pull this off.

(`event_NO_FUEL_FLEET_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — straight into combat)* | — | Hostile `REBEL_FLEET_FUEL`. | 100% |

### Ship: `REBEL_FLEET_FUEL` ([[source-events-ships]])

Auto-blueprint `SHIPS_REBEL_ELITE` — an **elite** Rebel hull, tougher than the ordinary
`REBEL_FUEL` fought in [[event-no-fuel-rebel-fight]]. The ship block carries the developer
note `<!-- NEEDS ELITE BLUEPRINT -->`.

| Result | Effect |
|---|---|
| Escapes (80s timer, 30s charge) | "The ship jumps away without a word. You assume they just went to get reinforcements..." Nothing gained. |
| Destroyed | "You manage to retrieve a few precious fuel capsules. You hurry to jump away from the cruiser fire!" → `item_modify` **+2–4 fuel**. |
| Crew killed | Same text, same **+2–4 fuel**. |

Note this is a flat `item_modify`, **not** an `autoReward` — so the payout is exactly 2–4
fuel with no scrap and no `LOW`/`MED`/`HIGH` tiering, and killing the crew is worth no more
than destroying the hull.

## Blue Options
None.

## Rewards & Risks
- Reward: 2–4 fuel, and nothing else.
- Risk: an elite Rebel fighter, fought inside the fleet's kill zone, with no fuel to escape
  and an 80-second window before it jumps out with your only exit.
- Losing this fight ends the run.

## Strategy Notes
- *Opinion:* nothing to decide — the only lever is how fast you can kill it. Because the
  reward is a flat `item_modify` rather than a tiered `autoReward`, boarding for a crew kill
  buys you nothing over a straight hull kill; take whichever is faster.

## Related
- [[event-no-fuel-fleet-dlc]] — the Advanced Edition variant of this exact event, which adds
  a Planetary Defense System firing on you
- [[event-no-fuel-rebel-fight]] — the ordinary (non-elite) Rebel fuel carrier
- [[event-fuel-escape-fleet]] — an unreferenced AE event describing the same predicament
- [[concept-rebel-fleet-advance]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm the engine loads this by hard-coded name when the fleet reaches a stranded
      ship (data files alone cannot show it).
- [ ] Whether AE replaces this entirely with [[event-no-fuel-fleet-dlc]] or the two coexist.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `REBEL_FLEET_FUEL`)
