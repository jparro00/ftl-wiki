---
id: event-fleet-easy-beacon
type: event
event_name: FLEET_EASY_BEACON
sectors: []
beacon_type: exit
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rebel-fleet, exit-beacon, structural, engine-event, orphan, no-choice, combat]
---

# Rebels at the exit beacon — `FLEET_EASY_BEACON`

## Summary
You reach the sector's exit beacon and the Rebel fleet is already there. An elite Rebel
scout engages and you have to survive until the FTL drive charges. It replaces
[[event-finish-beacon]] at the exit, and it swaps that event's bonus-encounter roll for a
fight worth one unit of fuel.

## Trigger & Where It Appears
**Not in any sector event list.** `FLEET_EASY_BEACON` is named explicitly in the *Fleet
Progression* section of the summary comment at the top of `events.xml`, alongside
`START_BEACON`, `FINISH_BEACON`, `FINISH_BEACON_NEBULA` and `FLEET_HARD` — the structural
events the engine invokes by name rather than drawing from a pool ([[source-events-xml]]).

It carries `<fleet>rebel</fleet>`, marking the beacon as fleet-held.

**No Fandom page joins it**; the slug comes from the in-game id.

**Note the difference from its own `_DLC` twin:** this base version has **no
`<environment>` element at all**, while [[event-fleet-easy-beacon-dlc]] adds
`<environment type="PDS" target="player"/>`. That is a real mechanical difference between
the two ids, unlike the `FLEET_EASY` / `FLEET_EASY_DLC` pair, which are identical
([[source-events-xml]]).

## Text
> You've found the exit beacon but the Rebels got here first! You must survive long enough
> to be able to jump to the next sector.

(`event_FLEET_EASY_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `LONG_FLEET`. **No environment hazard.** | 100% |

`LONG_FLEET`, on the `SHIPS_REBEL_ELITE` pool ([[source-events-ships]]):

| Ship result | Outcome |
|---|---|
| Destroyed | `<item type="fuel" min="1" max="1"/>` — **+1 fuel, nothing else.** |
| Dead crew | The identical +1 fuel. |
| Surrender / escape | Neither is defined. |

## Blue Options
None.

## Rewards & Risks
- **Reward:** +1 fuel for a kill.
- **Risk:** an elite Rebel warship between you and the next sector. The prose frames it as
  survival — *"survive long enough to be able to jump"* — so the intended play is to charge
  the FTL and leave.
- Compared with the ordinary exit ([[event-finish-beacon]]), you also lose the coin-flip
  roll on `EXIT_LIST` — no free weapon, no store, no trade. The fleet costs you the bonus
  encounter as well as the safety.

## Strategy Notes
- Charge and jump. Killing the ship is worth 1 fuel, which does not justify the hull.
  *Opinion*, from the ship block.
- The practical lesson is upstream: reaching the exit beacon before the fleet is worth more
  than one extra beacon of scrap, because the ordinary exit rolls `EXIT_LIST` and this one
  does not.

## Related
- [[event-fleet-easy-beacon-dlc]] — the AE id, which **adds a hostile PDS barrage**
- [[event-finish-beacon]] — the exit beacon when the fleet has not claimed it
- [[event-finish-beacon-nebula]] — the nebula exit variant
- [[event-fleet-easy]], [[event-fleet-hard]] — fleet takeover at a non-exit beacon
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether the base id is genuinely used in Advanced Edition, or only the `_DLC` one —
      the PDS difference means the answer changes how the encounter plays.
- [ ] Whether "survive long enough" is a fixed timer or the ordinary FTL charge.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `LONG_FLEET` block)
