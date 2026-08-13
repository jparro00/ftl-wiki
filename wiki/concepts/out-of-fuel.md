---
id: concept-out-of-fuel
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
related_events: []
tags: [mechanics, odds]
---

# Running out of fuel

## Definition & Context
With no fuel you cannot jump. Instead of a normal beacon encounter, each attempt to wait
draws from one of two dedicated event pools. This is the only situation in the game where
the *player's state*, not the beacon, selects the event pool.

Two pools exist, and which one you get depends on whether your distress beacon is on:

| Pool | Distress beacon | Live entries |
|---|---|---|
| `NO_FUEL` | **off** | 11 |
| `NO_FUEL_DISTRESS` | **on** | 12 |

([[source-events-fuel]])

## The trade-off
Turning the distress beacon on changes the odds substantially — it is a real decision, not
flavour.

**With the beacon off (`NO_FUEL`, 11 entries):**

| Outcome | Share |
|---|---|
| [[event-no-fuel-wait-fail-distress-off]] — nothing happens | **4/11 (36.4%)** |
| [[event-no-fuel-rebel-fleet-delay]] | 1/11 |
| [[event-no-fuel-fuel-trader-distress-off]] | 1/11 |
| [[event-no-fuel-explore-the-system]] | 1/11 |
| [[event-no-fuel-prepare-to-dock]] | 1/11 |
| [[event-no-fuel-engi-ship-repair]] | 1/11 |
| [[event-no-fuel-drifting-debris]] | 1/11 |
| [[event-no-fuel-friendly-refugee]] | 1/11 |

**With the beacon on (`NO_FUEL_DISTRESS`, 12 entries):**

| Outcome | Share |
|---|---|
| [[event-no-fuel-wait-fail-distress-on]] — nothing happens | **2/12 (16.7%)** |
| [[event-no-fuel-automated-refueling-ship]] | 1/12 |
| [[event-no-fuel-fuel-trader-distress-on]] | 1/12 |
| [[event-no-fuel-explore-the-system]] | 1/12 |
| [[event-no-fuel-prepare-to-dock]] | 1/12 |
| [[event-no-fuel-slug-fuel-depot]] | 1/12 |
| [[event-no-fuel-slug-fuel-trader]] | 1/12 |
| [[event-no-fuel-mantis-fight]] | 1/12 |
| [[event-no-fuel-auto-ship-warning]] | 1/12 |
| [[event-no-fuel-rebel-fight]] | 1/12 |
| [[event-no-fuel-refugee-damaged]] / [[event-no-fuel-refugee-pirate]] | 1/12 |

The headline: **wasted waits drop from 36.4% to 16.7%** with the beacon on, but the pool
picks up two guaranteed hostile encounters
([[event-no-fuel-mantis-fight]], [[event-no-fuel-rebel-fight]]) that the quiet pool has
none of. You trade dead time for danger.

Shares are derived per [[concept-event-list-weighting]], assuming uniform selection across
list entries.

## Why the odds here are unusually trustworthy
This family is the natural experiment that **validated** the wiki's whole odds-derivation
method. Fandom independently states 9%, 36.4% and 16.7% for three of these events, and
uniform selection over the two lists reproduces all three exactly. See
[[concept-event-list-weighting]] for the working.

A side effect: the match is against the **AE** list lengths (11 and 12), not the vanilla
ones (10 and 11) — which dates Fandom's fuel pages to Advanced Edition even though they
never say so.

## Version differences
The three refugee events (`NO_FUEL_REFUGEE*`) are AE additions, so both pools are one
entry shorter in vanilla (10 and 11). **Every probability on this page therefore differs
between editions** — vanilla shares are 1/10 and 1/11. ([[source-events-fuel]])

## Interaction with the rebel fleet
Waiting costs time, and the fleet keeps advancing. Several events in these pools carry
`<modifyPursuit>` or `<fleet>` tags — [[event-no-fuel-rebel-fleet-delay]] buys time,
[[event-no-fuel-auto-ship-warning]] costs it. See [[concept-rebel-fleet-advance]] for what
those tags do and do not establish.

## Where It Applies
Only when fuel reaches zero. The pools are not reachable any other way, and no
`sectorDescription` allocates them — the engine selects them by player state, an instance
of the direct-call behaviour described in [[concept-sector-event-allocation]].

## Related
- [[concept-event-list-weighting]] — the derivation method this family validated
- [[concept-rebel-fleet-advance]] — what waiting costs you
- [[source-events-fuel]] — the file defining both pools

## Open Questions
- [ ] Can the distress beacon be toggled between waits, and does the pool re-select each time?
- [ ] Do the two `FUEL_ESCAPE_*` families (in `events.xml` and `dlcEvents.xml`) belong to
      this system? They complete the same naming family but sit in a *"Events For Testing"*
      block — see [[event-fuel-escape-sun]].

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-fandom-no-fuel-wait-fail-distress-off]] (per raw/wiki/no-fuel-wait-fail-distress-off.md)
- [[source-fandom-no-fuel-rebel-fleet-delay]] (per raw/wiki/no-fuel-rebel-fleet-delay.md)
