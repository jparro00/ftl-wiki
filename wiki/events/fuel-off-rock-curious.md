---
id: event-fuel-off-rock-curious
type: event
event_name: FUEL_OFF_ROCK_CURIOUS
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, rock, unreachable, orphan, fuel-reward, system-lockout, derived-odds]
---

# No fuel: curious Rock ship — `FUEL_OFF_ROCK_CURIOUS`

## Summary
A complete out-of-fuel encounter — prose, two choices, an outcome list, a bespoke enemy hull
with its own escape and reward blocks — that **no list in the game references**. It is the
twin of [[event-no-fuel-drifting-debris]], written for the same pool and never added to it.
Fully authored content that cannot fire.

## Trigger & Where It Appears
- **Unreachable.** `FUEL_OFF_ROCK_CURIOUS` appears in `raw/gamedata/` only inside
  `events_fuel.xml`, and only in its own definitions: the `<event>`, the
  `FUEL_OFF_ROCK_CURIOUS_LIST` it loads, the `<ship>` block, and the two `<ship load=…>`
  references *within* those. There is **no `<event load="FUEL_OFF_ROCK_CURIOUS"/>` anywhere**
  ([[source-events-fuel]]).
- This is the positive evidence [[concept-sector-event-allocation]] requires: not a missing
  sector allocation, but no reference of any kind. Out-of-fuel events are never
  sector-allocated — they are drawn from the `NO_FUEL` and `NO_FUEL_DISTRESS` lists — and
  this event is in **neither**:
  - `NO_FUEL` (distress off): `FUEL_FLEET_DELAY`, `FUEL_NOTHING` ×4, `FUEL_TRADER`,
    `FUEL_EXPLORE`, `FUEL_APPROACH`, `FUEL_OFF_ENGI_DUBIOUS`, `FUEL_OFF_ROCK_WRECK`,
    `NO_FUEL_REFUGEE_FRIENDLY`
  - `NO_FUEL_DISTRESS` (distress on): `FUEL_NOTHING_DISTRESS` ×2, `FUEL_SELLER_DISTRESS`,
    `FUEL_TRADER_DISTRESS`, `FUEL_EXPLORE`, `FUEL_APPROACH`, `FUEL_ON_SLUG_OVERPRICED`,
    `FUEL_ON_SLUG_CHUCKLE`, `FUEL_ON_MANTIS_ATTACK`, `FUEL_ON_REBEL_WARNING`,
    `FUEL_ON_REBEL_ATTACK`, `NO_FUEL_REFUGEE`
  - `dlcEventsOverwrite.xml` redefines neither list ([[source-dlceventsoverwrite]]).
- The `FUEL_OFF_` prefix places it in the **distress-beacon-off** family, sitting in the file
  immediately after `FUEL_OFF_ROCK_WRECK` — which *is* in `NO_FUEL`. Everything about its
  placement says it was meant for that list.
- Not a stub: two choices, a two-entry outcome list, a bespoke ship with escape, gotaway,
  destroyed and deadCrew blocks, and localised strings for all of it.
- **Version:** `both`. `events_fuel.xml` is a base file and nothing here is `<!--DLC-->`
  marked — though the distinction is academic for content that never runs.
- No Fandom page documents it, consistent with it never appearing in play.

## Text
> A curious Rock ship comes in for a closer look at you. They refuse all hails.

(`event_FUEL_OFF_ROCK_CURIOUS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack. | — (`hidden="true"`) | *"The Rock people are not renowned for their generosity. If it's fuel you need, it's fuel you must take!"* → fight the `FUEL_OFF_ROCK_CURIOUS` hull. | 100% |
| 2 | Wait and see. | — (`hidden="true"`) | Loads `FUEL_OFF_ROCK_CURIOUS_LIST` — two entries, no repeats, **1/2 each** assuming uniform selection across list entries ([[concept-event-list-weighting]]). | — |

### `FUEL_OFF_ROCK_CURIOUS_LIST`

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *"…the scans pause on your fuel tank. They obviously have no wish to communicate, but they transfer over a cache of fuel before flashing their lights and jumping away!"* | **+3 to +8 fuel** |
| 1/2 | *"…they identify your engines and teleport a bomb straight onto it! Combat ready!"* | Fight the `FUEL_OFF_ROCK_CURIOUS` hull **and** `<status type="limit" target="player" system="engines" amount="1"/>` — your Engines are capped at 1 bar for the fight |

### The `FUEL_OFF_ROCK_CURIOUS` hull ([[source-events-fuel]])
`auto_blueprint="SHIPS_ROCK"`, with **no `<surrender>` block** — it will not offer to
surrender.

| Resolution | Declaration | Outcome |
|---|---|---|
| **Escape** | `<escape timer="80" min="30" max="30"/>` — no text, no `chance` | An unusually long 80-unit timer with a hull band of 30 |
| **Got away** | — | *"The ship jumps away without a word. You hope they didn't leave to get reinforcements."* — no reward |
| **Destroyed** | — | *"You take care to salvage as much fuel as possible from the wreck."* → `MED fuel`, and `<status type="clear" target="player" system="pilot" amount="100"/>` |
| **Dead crew** | — | same text → `HIGH fuel`, and `<status type="clear" target="player" system="engines" amount="100"/>` |

> ⚠️ **Apparent data bug.** The only system this event ever limits is **engines** (list entry
> 2). The `destroyed` block clears **pilot** instead; only `deadCrew` clears engines. Read
> literally, destroying the ship leaves your Engines capped while lifting a pilot limit that
> was never applied. No source explains the mismatch, and since the event is unreachable it
> was presumably never tested ([[source-events-fuel]]).

## Blue Options
None. Neither choice carries a `req` — unusual for this file, where most out-of-fuel events
carry at least one species or system gate.

## Rewards & Risks
Not applicable in play. Had it been listed, its profile would be: a free coin-flip between
**+3–8 fuel** and a crippled-engines fight, or an immediate fight for `MED`/`HIGH` fuel — a
notably fuel-rich event for a pool you only enter when stranded.

## Strategy Notes
None — the event cannot occur. If you are stranded and a Rock ship appears, you are in
[[event-no-fuel-drifting-debris]] or one of the listed `NO_FUEL` events, not this one.

## Related
- [[event-no-fuel-drifting-debris]] (`FUEL_OFF_ROCK_WRECK`) — the sibling immediately above
  it in the file, which *is* in `NO_FUEL`
- [[event-no-fuel-engi-ship-repair]], [[event-no-fuel-explore-the-system]],
  [[event-no-fuel-wait-fail-distress-off]] — the rest of the distress-off pool
- [[entity-rock-men]] — the faction
- [[concept-sector-event-allocation]] — the evidence bar for calling something unreachable
- [[concept-event-list-weighting]] — basis for the 1/2 figures

## Open Questions
- [ ] Is the pilot/engines mismatch a bug, or does `status type="clear"` behave differently
      than read here?
- [ ] What `escape timer="80"` means relative to the 5–32 values used elsewhere.
- [ ] Was this event cut, or simply never wired up? Nothing in the files records an intent.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
