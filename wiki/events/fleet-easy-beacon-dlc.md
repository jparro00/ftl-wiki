---
id: event-fleet-easy-beacon-dlc
type: event
event_name: FLEET_EASY_BEACON_DLC
sectors: []
beacon_type: exit
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rebel-fleet, exit-beacon, structural, engine-event, orphan, no-choice, combat, pds, advanced-edition]
---

# Rebels at the exit beacon (AE id) — `FLEET_EASY_BEACON_DLC`

## Summary
The Advanced Edition variant of [[event-fleet-easy-beacon]]. Same prose, same elite Rebel
ship, same +1 fuel payout — but it **adds a hostile planetary-defence barrage** that the
base id does not have. Unlike the `FLEET_EASY` / `FLEET_EASY_DLC` pair, this is not a
cosmetic duplicate: the AE version is genuinely harder.

## Trigger & Where It Appears
**Not in any sector event list.** A structural event the engine calls by name when the
Rebel fleet has claimed the sector's exit beacon. It carries `<fleet>rebel</fleet>`
([[source-events-xml]]).

The `_DLC` suffix marks it as the Advanced Edition variant, matching the convention of
`FLEET_EASY_DLC` and `NO_FUEL_FLEET_DLC`. **The engine's selection rule between the two ids
is not stated anywhere in `raw/gamedata/`** — that it is an edition switch is inference
from the naming convention.

**No Fandom page joins it**; the slug comes from the in-game id.

## Text
> You've found the exit beacon but the Rebels got here first! You must survive long enough
> to be able to jump to the next sector.

(`event_FLEET_EASY_BEACON_DLC_text`, per [[source-text-events-xml]] — a separate string
entry with wording identical to `event_FLEET_EASY_BEACON_text`.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with `LONG_FLEET`, inside `<environment type="PDS" target="player"/>` — an anti-ship battery firing **on you** throughout. | 100% |

`LONG_FLEET` pays **+1 fuel** on destroyed or dead crew, with no surrender and no escape
block ([[source-events-ships]]).

> **Version difference, recorded rather than resolved.** The two ids differ by exactly one
> element ([[source-events-xml]]):
>
> | Event | `<fleet>` | `<ship>` | `<environment>` |
> |---|---|---|---|
> | `FLEET_EASY_BEACON` | `rebel` | `LONG_FLEET` | **none** |
> | `FLEET_EASY_BEACON_DLC` | `rebel` | `LONG_FLEET` | `PDS` on the player |
>
> If the `_DLC` id is what Advanced Edition actually fires, then AE's fleet-held exit
> beacon is strictly more dangerous than vanilla's. No source states that outright; the
> XML difference is the whole of the evidence.

## Blue Options
None.

## Rewards & Risks
- **Reward:** +1 fuel for a kill.
- **Risk:** an elite Rebel warship *and* a PDS barrage chipping your hull on a timer, with
  the exit jump as the only exit.

## Strategy Notes
- Charge and jump. With PDS fire added, staying to kill the scout for one fuel is worse
  here than in the base version. *Opinion*, from the ship block and the environment tag.

## Related
- [[event-fleet-easy-beacon]] — the base id, **without** the PDS barrage
- [[event-fleet-easy-dlc]], [[event-fleet-easy]] — fleet takeover at a non-exit beacon
- [[event-fleet-hard]]
- [[event-finish-beacon]] — the exit beacon when the fleet has not claimed it
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Confirm which id Advanced Edition actually fires; the PDS difference makes this
      matter in play, not just in bookkeeping.
- [ ] Whether the PDS here is the same hazard as at an ordinary PDS beacon, or a
      fleet-specific barrage.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `LONG_FLEET` block)
