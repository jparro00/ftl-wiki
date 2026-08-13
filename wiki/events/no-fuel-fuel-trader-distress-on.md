---
id: event-no-fuel-fuel-trader-distress-on
type: event
event_name: FUEL_TRADER_DISTRESS
sectors: []
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, distress-beacon, trading, barter, derived-odds]
---

# No fuel: fuel trader (distress on) — `FUEL_TRADER_DISTRESS`

## Summary
The distress-beacon-on twin of [[event-no-fuel-fuel-trader-distress-off]]. Mechanically
**identical**: same friendly `CIVILIAN_SHIP`, same two choices, same
`FUEL_TRADER_HIGH_LIST` / `FUEL_TRADER_PT2` tree. Only the intro prose differs — here the
merchant explicitly responds to your distress signal. As with the twin, declining the first
offer is usually the better line.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-fuel-trader-distress-on]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
Prose is drawn from `FUEL_TRADER_DISTRESS_TEXT_LIST`, **4 variants**
([[source-text-events-xml]]). For example:

> A merchant ship jumps into the sector, obviously responding to your ship's distress
> beacon. They hail you offering a trade for fuel.

> A mercenary ship arrives at the beacon. "We have a bit of extra fuel we can give you...
> for a price."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Gladly trade. | — | Loads `FUEL_TRADER_HIGH_LIST` (3 entries, 1/3 each): **+2–4 fuel** for 1–2 drone parts; **+2–5 fuel** for 2–4 missiles; **+2–5 fuel** for 15–25 scrap. | — |
| 2 | Respectfully decline. | — | Loads `FUEL_TRADER_PT2` (3 entries, 1/3 each) — see below. | — |

The actual trade is displayed before you commit
([[source-fandom-no-fuel-fuel-trader-distress-on]]).

### `FUEL_TRADER_PT2` — after declining (3 entries, 1/3 each)

| Outcome | Result | Odds |
|---|---|---|
| "Seeing that you're in need, is this trade acceptable?" | *Accept* → `FUEL_TRADER_LOW_LIST` (3 entries, 1/3 each): **+4–7 fuel** for 1–2 drone parts; **+4–7 fuel** for 1–2 missiles; **+3–7 fuel** for 5–12 scrap. *Decline again* (hidden) → `FUEL_TRADER_PT3` (2 entries, 1/2 each): **+1–6 fuel free**, or nothing. | 1/3 |
| "I'm not doing this for charity, you know." | *Accept* → `FUEL_TRADER_HIGH_LIST` again. *Decline again* → nothing happens. | 1/3 |
| "I'm sorry, but we are unable to help in any other way." | Nothing happens. | 1/3 |

All 1/N figures are derived from `<eventList>` entry counts and **assume uniform selection
across list entries** ([[source-events-fuel]]). Full tree with the file's own developer
commentary is documented on [[event-no-fuel-fuel-trader-distress-off]].

## Blue Options
None.

## Rewards & Risks
- Best realistic outcome: 4–7 fuel for 5–12 scrap, or 1–6 fuel free.
- Worst outcome: nothing.
- No combat, no theft, no resource loss you did not agree to.

## Strategy Notes
- *Opinion:* decline the first offer unless it is already cheap. The low list beats the
  high list on both axes, and the whole tree is risk-free.
- With the beacon on, this event competes with [[event-no-fuel-automated-refueling-ship]],
  which sells at a flat 4 scrap/fuel *and* gives some free. If your problem is scrap rather
  than fuel, the barter tree's drone-part and missile options are the ones the auto-seller
  cannot match.

## Related
- [[event-no-fuel-fuel-trader-distress-off]] — the distress-off twin (`FUEL_TRADER`), and
  the fuller write-up of the shared trade tree
- [[event-no-fuel-prepare-to-dock]] — drops into the same trade tree from one of its accept
  branches
- [[event-no-fuel-automated-refueling-ship]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Whether offers you cannot afford are filtered out of the list.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-fuel-trader-distress-on]] (per raw/wiki/no-fuel-fuel-trader-distress-on.md)
