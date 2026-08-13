---
id: event-no-fuel-automated-refueling-ship
type: event
event_name: FUEL_SELLER_DISTRESS
sectors: []
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, trading, auto-ship, hostile-option, derived-odds]
---

# No fuel: automated refueling ship — `FUEL_SELLER_DISTRESS`

## Summary
The single best draw in the distress-on pool. An automated refueller answers your beacon
and hands out **free `LOW` fuel** for the asking, then sells more at 4 scrap per unit — the
cheapest rate in the whole out-of-fuel family. You can also just shoot it. There is no
downside branch anywhere in this event.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-automated-refueling-ship]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
> A small ship arrives with a message, "This automated ship will provide refueling services
> once a monetary exchange is complete. Complimentary amounts of fuel are available in
> emergencies only."

(`event_FUEL_SELLER_DISTRESS_text`, per [[source-text-events-xml]])

A friendly `AUTO_FUEL_SELLER` ship (auto-blueprint `SHIPS_AUTO`) is present from the start
([[source-events-fuel]], [[source-events-ships]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Request emergency fuel reserves. | — | "This ship has registered that your one-time complimentary emergency fuel allowance has been consumed." → `autoReward level="LOW"` **fuel_only**. Free. | 100% |
| 2 | Buy 5 fuel for 20 scrap. | `hidden="false"` | "Automated refueling complete." **−20 scrap, +5 fuel.** | 100% |
| 3 | Buy 2 fuel for 8 scrap. | `hidden="false"` | "Automated refueling complete." **−8 scrap, +2 fuel.** | 100% |
| 4 | Attack the automated ship. | — | The `AUTO_FUEL_SELLER` turns **hostile** — see below. | 100% |

### Ship: `AUTO_FUEL_SELLER` when hostile ([[source-events-ships]])

| Result | Effect |
|---|---|
| Escapes (80s timer, 30s charge) | "The ship jumps away without a word." Nothing gained. |
| Destroyed | "As the ship breaks apart, you frantically try to salvage the remaining fuel from its cargo." → `autoReward level="MED"` **fuel**. |

No `deadCrew` block (auto-ship), and no surrender. The block also contains a second,
unusual `<escape chance="0.5" min="2" max="5">` line carrying the text *"It is apparent
that the ship was not intended for combat. It seems to be trying to jump away."*

> ⚠️ **Unresolved, flagged by Fandom rather than contradicted.**
> Fandom's own inline comment on this event says the second `<escape chance="0.5" …>` line
> "seems unlikely to have any effect" and that it is unclear whether it means a 50% chance
> to attempt escape *when damaged enough* versus escaping *immediately*, and that it "needs
> testing or code evaluation to be 100% sure"
> ([[source-fandom-no-fuel-automated-refueling-ship]]). The game files state the tag but
> not its semantics ([[source-events-ships]]). Left open rather than guessed.

Fandom also notes that the "one-time complimentary emergency fuel allowance" line is
**flavour only — choice 1 is available every time the event appears**
([[source-fandom-no-fuel-automated-refueling-ship]]). Nothing in the game files tracks a
one-time flag, which is consistent, but the files do not state it either.

## Blue Options
None.

## Rewards & Risks
- Free `LOW` fuel, unconditionally, with no counterpart cost anywhere in the event.
- 4 scrap per fuel unit on both purchase options — the cheapest rate in the out-of-fuel
  pool (compare 3 scrap/unit at [[event-no-fuel-slug-fuel-trader]] but with a 50% theft
  branch, and 9.5–10 at [[event-no-fuel-slug-fuel-depot]]).
- Attacking risks an 80-second fight against a weak auto-ship for `MED` fuel + scrap.
- **No branch of this event can hurt you** except the fight you choose to start.

## Strategy Notes
- *Opinion:* take the free fuel, then buy if you can afford it — this event alone usually
  ends the crisis.
- *Opinion:* attacking is the greedy line and is often correct: the ship block notes the
  hull "needs a WEAK tag", it has no crew, and destroying it upgrades the reward from `LOW`
  to `MED`. But choice 1 and choice 4 are mutually exclusive — one choice per event.

## Related
- [[event-no-fuel-slug-fuel-depot]], [[event-no-fuel-slug-fuel-trader]] — the other vendors
  in the same pool, both worse
- [[event-no-fuel-fuel-trader-distress-on]] — the barter alternative
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Semantics of the second `<escape chance="0.5" min="2" max="5">` block.
- [ ] Confirm from play that choice 1 really repeats across separate encounters.
- [ ] Exact fuel values behind `autoReward` `LOW` fuel_only and `MED` fuel.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `AUTO_FUEL_SELLER`)
- [[source-fandom-no-fuel-automated-refueling-ship]] (per raw/wiki/no-fuel-automated-refueling-ship.md)
