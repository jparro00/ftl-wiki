---
id: event-no-fuel-slug-fuel-trader
type: event
event_name: FUEL_ON_SLUG_CHUCKLE
sectors: []
beacon_type: distress
hostile: false
blue_options: [slug crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, slug, trading, theft-risk, blue-option, derived-odds]
---

# No fuel: Slug fuel trader — `FUEL_ON_SLUG_CHUCKLE`

## Summary
A chuckling Slug offers a fair-looking price on fuel. The price *is* fair — 15 scrap for
5 fuel — but half the time he plants a teleporter in your cargo bay and takes 20–35 scrap
and 2–4 missiles on the way out. A **Slug crew member** removes the theft entirely.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-slug-fuel-trader]]).
- The "should eventually be tied to the slug sector" developer comment above it never took
  effect — it is not sector-gated ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
> A poorly armed Slug ship cruises by and offers assistance. Their captain seems to be
> chuckling to himself, perhaps at the prices he's charging.

(`event_FUEL_ON_SLUG_CHUCKLE_text`, per [[source-text-events-xml]])

A friendly `JELLY` ship (auto-blueprint `SHIPS_JELLY`) is present throughout; it never turns
hostile in this event ([[source-events-fuel]], [[source-events-ships]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Pay 15 scrap for 5 fuel. | — | Loads `FUEL_ON_SLUG_CHUCKLE_LIST` (2 entries) — see below. Both pay **−15 scrap, +5 fuel** first. | — |
| 2 | Ignore the offer. | — | "You know better than to do business with a Slugman who seems like he knows something you don't. He jumps off with another chuckle." Nothing happens. | 100% |
| 3 | **(Slug Crew)** Have your Slug make the purchase. | `req="slug"` | "…you wonder what mental battles are telepathically occurring between the two Slugs." **−15 scrap, +5 fuel**, no theft. | 100% |

### Choice 1 — `FUEL_ON_SLUG_CHUCKLE_LIST` (2 entries, 1/2 each)

Both entries open with the same line — *"You doubt he is trustworthy but have no choice but
to make the deal. However you complete the exchange without event."* — and both apply
−15 scrap / +5 fuel. They differ only in what follows:

| Outcome | Result | Odds |
|---|---|---|
| Clean deal. | Trade completes; nothing further. | 1/2 |
| Hidden teleporter. | A forced *Continue…* leads to: "Everything looks secure but suddenly a number of supplies disappear!" → `<item_modify steal="true">` **−20–35 scrap and −2–4 missiles**. | 1/2 |

The 1/2 split is derived from the two `<event>` entries in the `<eventList>` and **assumes
uniform selection across list entries** ([[source-events-fuel]]).

## Blue Options
- **Slug crew member** (`req="slug"`) — gives the identical 15-scrap-for-5-fuel trade with
  the theft branch removed. Expected saving over choice 1: roughly half of 20–35 scrap and
  2–4 missiles.

## Rewards & Risks
- Reward: +5 fuel for 15 scrap — a good rate, and enough to jump several times.
- Risk: the theft branch turns the deal into 35–50 scrap and 2–4 missiles for 5 fuel.
- No combat risk at all; the Slug ship stays friendly regardless of what you pick.

## Strategy Notes
- *Opinion:* with a Slug aboard this is a free-roll — take choice 3 every time. Without one,
  the trade is still usually worth it when stranded, because being unable to jump costs
  more than 35 scrap.
- If you are missile-dependent and low on ammunition, the theft branch stings more than the
  scrap; ignoring is defensible then.

## Related
- [[event-no-fuel-slug-fuel-depot]] — the other Slug fuel vendor in the same pool, at four
  times the price but with no theft risk
- [[event-no-fuel-automated-refueling-ship]] — the cheapest reliable vendor in the pool
- [[entity-slugs]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Does the theft branch check for Blast Doors / a manned Doors system, as some
      teleport-theft events do? Nothing in the XML suggests so.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `JELLY`)
- [[source-fandom-no-fuel-slug-fuel-trader]] (per raw/wiki/no-fuel-slug-fuel-trader.md)
