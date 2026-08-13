---
id: event-fleet-hard
type: event
event_name: FLEET_HARD
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rebel-fleet, structural, engine-event, orphan, no-choice, combat]
---

# Rebel fleet takeover (flee) — `FLEET_HARD`

## Summary
The harder framing of the fleet-takeover encounter: a Rebel scout engages and the prose
tells you outright to run — *"You must flee before their cruisers open fire!"* Mechanically
it is the leanest member of the family: the same elite ship, no environment hazard, no
choices, and the same one unit of fuel for a kill.

## Trigger & Where It Appears
**Not in any sector event list.** `FLEET_HARD` is named explicitly in the *Fleet
Progression* section of the summary comment at the top of `events.xml`, alongside
`START_BEACON`, `FINISH_BEACON`, `FINISH_BEACON_NEBULA` and `FLEET_EASY_BEACON` — the
structural events the engine invokes by name ([[source-events-xml]]).

It carries `<fleet>rebel</fleet>`, marking the beacon as fleet-held.

**What makes it "hard" is not stated in any source in `raw/`.** The name and the prose
imply a worse fleet situation than `FLEET_EASY` — cruisers about to open fire rather than
already firing — but there is no threshold, sector number or condition recorded anywhere in
the game files. Notably it is the one member of the family with **no `<environment>`
element at all**, so "hard" does not mean "with PDS".

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> The Rebel fleet has found you, and a nearby scout turns to engage. You must flee before
> their cruisers open fire!

(`event_FLEET_HARD_text`, per [[source-text-events-xml]]. Unlike the `_DLC` pairs in this
family, this string is unique — it is not a copy of `event_FLEET_EASY_text`.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `LONG_FLEET`. No environment hazard. | 100% |

`LONG_FLEET`, on the `SHIPS_REBEL_ELITE` pool and flagged `<!-- NEEDS ELITE BLUEPRINT -->`
([[source-events-ships]]):

| Ship result | Outcome |
|---|---|
| Destroyed | `<item type="fuel" min="1" max="1"/>` — **+1 fuel, nothing else.** |
| Dead crew | The identical +1 fuel. |
| Surrender / escape | Neither is defined. |

## Blue Options
None.

## Rewards & Risks
- **Reward:** +1 fuel for a kill.
- **Risk:** an elite Rebel warship, with the framing that more are inbound. No hazard
  environment, so the danger is purely the ship — which makes this arguably the *least*
  punishing member of the family in raw mechanics, despite the name.

## Strategy Notes
- Jump. The prose is unambiguous and the reward does not argue otherwise. *Opinion*, from
  the ship block.
- The interesting open question is what actually selects this over `FLEET_EASY` — if it is
  fleet proximity, the two events are a soft warning system, and the name is the only clue
  the game gives.

## Related
- [[event-fleet-easy]], [[event-fleet-easy-dlc]] — the PDS-bearing variants of the same
  situation
- [[event-fleet-easy-beacon]], [[event-fleet-easy-beacon-dlc]] — the exit-beacon versions
- [[event-fleet-easy-nebula]] — the nebula version, shipped but unreachable
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What condition selects `FLEET_HARD` over `FLEET_EASY`. Nothing in `raw/gamedata/`
      states it.
- [ ] Why the "hard" variant has *fewer* hazards than the "easy" one — is the difficulty in
      the enemy ship's stats, drawn from the same `SHIPS_REBEL_ELITE` pool but scaled?
- [ ] Whether there is a `FLEET_HARD_DLC` that was never written; the family's naming
      pattern would predict one, and there is none.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `LONG_FLEET` block)
