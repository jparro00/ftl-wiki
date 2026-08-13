---
id: event-no-fuel-fuel-trader-distress-off
type: event
event_name: FUEL_TRADER
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, trading, barter, derived-odds]
---

# No fuel: fuel trader (distress off) — `FUEL_TRADER`

## Summary
A merchant offers to barter fuel while you are stranded with your distress beacon off.
Its one non-obvious mechanic is worth knowing: **refusing the first offer is usually
correct.** Declining leads to a second round whose "low" price list gives *more* fuel for
*less*, and a 1/9 path to free fuel.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-fuel-trader-distress-off]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Derived odds.** 1/11 (~9.1%) per wait in AE; 1/10 (10%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
Prose is drawn from `FUEL_TRADER_TEXT_LIST`, **5 variants** ([[source-text-events-xml]]).
For example:

> A merchant ship jumps into the sector and you quickly hail them asking for help. They
> respond, "Perhaps we could work out an exchange..."

> A modified YT-1300 freighter jumps to an area near your sector. Your gut tells you these
> people are smugglers, but they seem to be feeling altruistic and present an offer of
> assistance.

A friendly `CIVILIAN_SHIP` is present throughout ([[source-events-fuel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Gladly trade. | — | Loads `FUEL_TRADER_HIGH_LIST` — the expensive price list. | — |
| 2 | Respectfully decline. | — | Loads `FUEL_TRADER_PT2` — the second-chance tree. | — |

The game displays the **actual** trade before you commit — the resource amounts are shown
on the choice ([[source-fandom-no-fuel-fuel-trader-distress-off]]).

### `FUEL_TRADER_HIGH_LIST` — the first offer (3 entries, 1/3 each)

| Trade | Odds |
|---|---|
| **+2–4 fuel** for **1–2 drone parts** | 1/3 |
| **+2–5 fuel** for **2–4 missiles** | 1/3 |
| **+2–5 fuel** for **15–25 scrap** | 1/3 |

### `FUEL_TRADER_PT2` — after declining (3 entries, 1/3 each)

The developer comment on this list states its purpose outright: *"this list is if the
player cant afford the initial trade, he'll either give up and leave or give a second
cheaper offer"* ([[source-events-fuel]]).

| Outcome | Result | Odds |
|---|---|---|
| "Seeing that you're in need, is this trade acceptable?" | *Accept the offer* → `FUEL_TRADER_LOW_LIST` (cheaper, below). *Decline again* (hidden) → `FUEL_TRADER_PT3` (below). | 1/3 |
| "I'm not doing this for charity, you know. This is the only other way I'll part with my fuel." | *Accept the offer* → `FUEL_TRADER_HIGH_LIST` again (same prices as round one). *Decline again* → "Their captain disconnects from the channel…" nothing happens. | 1/3 |
| "I'm sorry, but we are unable to help in any other way." | Nothing happens. | 1/3 |

### `FUEL_TRADER_LOW_LIST` — the discounted list (3 entries, 1/3 each)

| Trade | Odds |
|---|---|
| **+4–7 fuel** for **1–2 drone parts** | 1/3 |
| **+4–7 fuel** for **1–2 missiles** | 1/3 |
| **+3–7 fuel** for **5–12 scrap** | 1/3 |

### `FUEL_TRADER_PT3` — after declining twice (2 entries, 1/2 each)

| Outcome | Result | Odds |
|---|---|---|
| "They take pity on you and offer you some fuel free of charge." | **+1–6 fuel, free.** | 1/2 |
| "They end the discussion and prepare to jump away." | Nothing happens. | 1/2 |

Every 1/N above is derived from `<eventList>` entry counts and **assumes uniform selection
across list entries** ([[source-events-fuel]]).

## Blue Options
None.

## Rewards & Risks
- Best realistic outcome: 4–7 fuel for 5–12 scrap via the low list, or 1–6 fuel free via
  `PT3`.
- Worst outcome: nothing at all — reachable through two of the three `PT2` branches.
- **No combat and no resource loss anywhere in this event.** Declining is free; the only
  cost is the chance the trader leaves empty-handed.

## Strategy Notes
- *Opinion:* decline the first offer unless the displayed trade is already good. `PT2`
  gives a 1/3 shot at the strictly cheaper low list, a 1/3 shot at the same prices again,
  and a 1/3 shot at nothing — and the low-list trades beat every high-list trade on both
  fuel gained and price paid.
- Declining twice from the first `PT2` branch is a 1/2 coin flip for free fuel, but forfeits
  the guaranteed low-list trade. Take it only if you genuinely cannot pay.
- Drone parts are usually the cheapest currency to spend here if you are not running drones.

## Related
- [[event-no-fuel-fuel-trader-distress-on]] — the distress-on twin (`FUEL_TRADER_DISTRESS`),
  identical apart from its intro text
- [[event-no-fuel-prepare-to-dock]] — one of its accept branches drops into this same
  `FUEL_TRADER_HIGH_LIST` / `FUEL_TRADER_PT2` tree
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Whether the game filters offers you cannot afford, or shows them anyway.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-fuel-trader-distress-off]] (per raw/wiki/no-fuel-fuel-trader-distress-off.md)
