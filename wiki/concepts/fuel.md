---
id: concept-fuel
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, economy, resource, fuel, trade]
---

# Fuel

## Definition & Context

Fuel is the only resource whose absence is not merely inconvenient but **changes which events
you can have at all**. One unit per jump; at zero you cannot move, and the game switches to a
dedicated pool of stranded-ship events — documented at [[concept-out-of-fuel]], which covers
that failure state in full. **This page covers fuel as an economy**: where it comes from, what
it costs, and what it buys.

## The game gives fuel away

Across the event files, `<item type="fuel">` appears **73 times — 59 gains against 14 losses**
([[source-events-xml]] and siblings). That is the exact inverse of scrap, which is 84 losses to
32 gains (see [[concept-scrap-economy]]).

Fuel also has its own `autoReward` tiers, which no other single resource does:

| Tier | Uses | Meaning |
|---|---|---|
| `fuel` | 32 | a fuel-weighted mixed reward |
| `fuel_only` | 13 | fuel and nothing else |

**45 fuel-specific reward records** on top of the 59 explicit gains. The design intent is
plain: the game does not want you stranded, and it hands out fuel more freely than anything
else it tracks.

## What fuel is spent on

- **Jumping** — one per jump, the constant drain.
- **Quest detours.** Every chain in this wiki costs fuel for the extra beacons; that is the
  real price of a quest marker, and the reason [[concept-quest-beacon-placement]]'s
  sector-7 cancellation stings.
- **Being asked for it.** A recurring event shape trades fuel for goodwill or scrap:
  [[event-friendly-ship-out-of-fuel]] (give 2–4 fuel, get a four-outcome gift pool),
  [[chain-construction-yard]]'s third destination (give 4 fuel for `MED scrap_only`, or 1 fuel
  for nothing at all), and [[event-trade-fuel-for-drone-parts]].
- **Buying it back.** Stores sell fuel, which makes scrap and fuel partially fungible in one
  direction only — see [[concept-stores]].

## The asymmetry that matters

Giving fuel away is usually a **bad trade in isolation and a good one in context**. Handing over
4 fuel for `MED scrap_only` is a poor exchange rate, but the events that ask for fuel almost
always pay in something you cannot otherwise buy — goodwill branches, crew, or a store. The
exception is [[chain-construction-yard]]'s 1-fuel option, which pays literally nothing and
exists as a trap for players trying to be generous cheaply.

## Implications For Play

- **Never hold the minimum.** The stranded-ship pool ([[concept-out-of-fuel]]) is survivable but
  costly, and the buffer that avoids it is small — a few units.
- **Fuel-for-scrap trades are worth taking when you are above about eight units**, and never
  when you are near the floor. *(Opinion, derived from the trade rates recorded on the event
  pages above.)*
- **A nebula sector costs more fuel than it looks** — jumps are the same, but the slower Rebel
  advance ([[concept-nebula-mechanics]]) rewards exploring more beacons, which is more jumps.

## Where It Applies
[[event-friendly-ship-out-of-fuel]], [[event-trade-fuel-for-drone-parts]],
[[chain-construction-yard]], [[chain-escort-civilians]] (whose down-payment is `LOW fuel_only`),
[[event-improve-reactor-for-supplies]], and the whole `NO_FUEL` / `NO_FUEL_DISTRESS` family at
[[concept-out-of-fuel]].

## Related
- [[concept-out-of-fuel]] — the failure state, in full
- [[concept-scrap-economy]] — the resource fuel is the mirror of
- [[concept-autoreward-tiers]] — the `fuel` and `fuel_only` tiers
- [[concept-stores]] — where fuel is bought back
- [[concept-quest-beacon-placement]] — why a detour has a fuel price

## Open Questions
- [ ] How much fuel a store sells per unit of scrap.
- [ ] Whether `autoReward fuel` and `fuel_only` differ in quantity or only in what accompanies
      them.
- [ ] Whether any event can take your **last** unit of fuel, forcing the stranded pool
      deliberately.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
