---
id: event-no-fuel-prepare-to-dock
type: event
event_name: FUEL_APPROACH
sectors: []
beacon_type: any
hostile: unknown
blue_options: [sensors level 3, [[item-long-ranged-scanners]], [[item-cloaking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [out-of-fuel, trading, pirate, boarding-risk, blue-option, derived-odds]
---

# No fuel: prepare to dock — `FUEL_APPROACH`

## Summary
One of the encounters that can fire when you sit at a beacon with **zero fuel**. A ship
offers to dock and refuel you. It is genuinely one of the better out-of-fuel draws — two
of its three branches can hand you free fuel — but every branch also has a pirate outcome,
and the scan blue options are what turn the gamble into information.

## Trigger & Where It Appears
- **Not a sector event.** `FUEL_APPROACH` is drawn from the out-of-fuel wait pools, not
  from any sector's event list. It is a member of **both** `NO_FUEL` (distress beacon off)
  and `NO_FUEL_DISTRESS` (distress beacon on) ([[source-events-fuel]]).
- Fandom classes it `outoffuel=distressboth`, which agrees
  ([[source-fandom-no-fuel-prepare-to-dock]]).
- Prerequisites: 0 fuel, and you choose to wait at the beacon.

**Derived odds.** `NO_FUEL` has 11 `<event load=…>` entries in Advanced Edition and
`NO_FUEL_DISTRESS` has 12, so this event is **1/11 (~9.1%)** per wait with the beacon off
and **1/12 (~8.3%)** per wait with it on. *This assumes uniform selection across list
entries* — an assumption the game files corroborate: the same arithmetic reproduces
Fandom's independently stated 36.4% and 16.7% figures for `FUEL_NOTHING` /
`FUEL_NOTHING_DISTRESS` exactly ([[source-events-fuel]],
[[source-fandom-no-fuel-wait-fail-distress-off]]).

Without the AE-only refugee entries the vanilla lists are 10 and 11 long, giving
**1/10 (10%)** and **1/11 (~9.1%)** respectively (rule: the `NO_FUEL_REFUGEE*` entries
carry `<!-- DLC -->` comments, [[source-events-fuel]]).

## Text
> A ship approaches. They hail you saying, "You need some fuel? We'll prepare to dock to
> help."

(`event_FUEL_APPROACH_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Graciously accept their offer. | — | Loads `FUEL_APPROACH_ACCEPT_LIST` — see below. | — |
| 2 | Request that they keep their distance. | — | Loads `FUEL_APPROACH_DECLINE_LIST` — see below. | — |
| 3 | **(Advanced Sensors)** Run a detailed scan with your sensors before responding. | `req="sensors" lvl="3"` | Loads `FUEL_APPROACH_SCAN_LIST` — see below. | — |
| 4 | **(Long-Ranged Scanners)** Run a detailed scan before responding. | `req="ADV_SCANNERS"` | Same list as choice 3. | — |

### Choice 1 — `FUEL_APPROACH_ACCEPT_LIST` (4 entries, 1/4 each)

| Outcome | Result | Odds |
|---|---|---|
| "They pull close to your ship and unload some fuel…" | Friendly `CIVILIAN_SHIP`, **+2–6 fuel**. | 1/4 |
| "They approach and dock with your ship. On board they present an offer." | Friendly `CIVILIAN_SHIP`, then the standard fuel-trade tree — *Gladly trade* → `FUEL_TRADER_HIGH_LIST`, *Respectfully decline* → `FUEL_TRADER_PT2`. Same tree as [[event-no-fuel-fuel-trader-distress-off]]. | 1/4 |
| "…Help to relieve you of that nice ship!" | Hostile `PIRATE_FUEL` **plus 2–3 human boarders** teleported aboard. | 1/4 |
| "As they approach, you detect their weapons powering up." | Hostile `PIRATE` (default rewards). | 1/4 |

### Choice 2 — `FUEL_APPROACH_DECLINE_LIST` (3 entries, 1/3 each)

| Outcome | Result | Odds |
|---|---|---|
| "I assure you that we mean no harm… we'll send some fuel over on a transport." | Friendly `CIVILIAN_SHIP`, **+1–4 fuel**. | 1/3 |
| "No one trusts anyone these days…" | Nothing happens. | 1/3 |
| "Keep our distance? Let's see if you can stop us!" | Hostile `PIRATE_FUEL`. | 1/3 |

### Choices 3 & 4 — `FUEL_APPROACH_SCAN_LIST` (2 entries, 1/2 each)

| Outcome | Result | Odds |
|---|---|---|
| "Sensors indicate their ship is without military-grade weaponry…" | **+3–7 fuel**, no ship. | 1/2 |
| "Sensors are picking up armed crew and considerably more weaponry than is legal… This is surely a trap." | Two follow-up choices: **Power up weapons** → hostile `PIRATE_FUEL`; or **(Cloaking)** `req="cloaking"` → you slip out of range, nothing happens. | 1/2 |

All the 1/N figures above are derived from entry counts in the `<eventList>` blocks and
**assume uniform selection across list entries** ([[source-events-fuel]]).

## Blue Options
- **Sensors level 3** (`req="sensors" lvl="3"`) — replaces the blind accept/decline gamble
  with a 50/50 that is *strictly better*: the good half pays 3–7 fuel (more than either
  blind branch) and the bad half at least lets you choose to fight on your terms.
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — identical effect, granted by
  the augment instead of the system, so ships without Sensors can still take it.
- **[[item-cloaking]]** (`req="cloaking"`, nested inside the trap outcome) — the only way
  to walk away from the ambush without a fight. It gives no fuel; it just cancels the
  encounter.

## Rewards & Risks
- Best case: +3–7 fuel from a scan, or +2–6 from a blind accept.
- Fuel-trade branch: see [[event-no-fuel-fuel-trader-distress-off]] for the price ranges
  (`FUEL_TRADER_HIGH_LIST` costs drones, missiles or 15–25 scrap for 2–5 fuel).
- Risks: `PIRATE_FUEL` with **2–3 human boarders** while you have no fuel to run on, or a
  plain `PIRATE`. `PIRATE_FUEL` has an 80-second escape timer and a 50% surrender chance;
  `PIRATE` also escapes ([[source-events-ships]]).
- Note that a hostile outcome here is not automatically bad — killing the ship still pays
  default rewards, and you cannot flee anyway.

## Strategy Notes
- *Opinion:* if you have Sensors 3 or Long-Ranged Scanners, always scan. Two of the four
  accept-branch outcomes and one of the three decline-branch outcomes are hostile; the
  scan branch caps the downside at a fight you get to see coming
  ([[source-fandom-no-fuel-prepare-to-dock]], and derivable from the list structure in
  [[source-events-fuel]]).
- Blind, *accept* has the higher ceiling (2–6 fuel or a trade) and the worse floor
  (boarders); *decline* has a 1/3 nothing outcome and a smaller fuel payout.

## Related
- [[event-no-fuel-explore-the-system]] — the other event that sits in both out-of-fuel pools
- [[event-no-fuel-fuel-trader-distress-off]] / [[event-no-fuel-fuel-trader-distress-on]] —
  share the `FUEL_TRADER_HIGH_LIST` / `FUEL_TRADER_PT2` trade tree
- [[event-no-fuel-wait-fail-distress-off]] — the far more common "nothing happens" draw
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Does the scan list actually differ from the underlying reality, or is it purely a
      re-roll? The two branches are separate `<event>` entries, so the game re-rolls
      rather than revealing the pre-decided ship.
- [ ] Whether Sensors 3 and the augment are additive in any way (they load the same list).

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `PIRATE_FUEL`, `PIRATE`, `CIVILIAN_SHIP`)
- [[source-fandom-no-fuel-prepare-to-dock]] (per raw/wiki/no-fuel-prepare-to-dock.md)
