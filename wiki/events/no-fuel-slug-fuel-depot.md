---
id: event-no-fuel-slug-fuel-depot
type: event
event_name: FUEL_ON_SLUG_OVERPRICED
sectors: []
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, distress-beacon, slug, trading, hostile-option, derived-odds]
---

# No fuel: Slug fuel depot — `FUEL_ON_SLUG_OVERPRICED`

## Summary
A mobile Slug fuel depot with the worst prices in the game — 10 scrap per fuel unit,
against the 3-per-unit the same sector's [[event-no-fuel-slug-fuel-trader]] charges and the
4-per-unit at [[event-no-fuel-automated-refueling-ship]]. Haggling is the only free option
and it starts a fight. Notably, **neither purchase option is hidden**: you can see both
prices before committing.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL_DISTRESS` list — the
  distress-beacon-**on** out-of-fuel pool ([[source-events-fuel]]). Fandom marks it
  `outoffuel=distresson` ([[source-fandom-no-fuel-slug-fuel-depot]]).
- Prerequisites: 0 fuel, distress beacon on, and you choose to wait.

**Derived odds.** 1/12 (~8.3%) per wait in AE; 1/11 (~9.1%) in vanilla. *Assumes uniform
selection across list entries.*

## Text
> A mobile Slugman fuel depot enters scanning range. "My prices are fair, but I ask one
> thing - do not insult me with negotiation!" You check out his price list.

(`event_FUEL_ON_SLUG_OVERPRICED_text`, per [[source-text-events-xml]])

A friendly `JELLY_OVERPRICED` ship is present from the start ([[source-events-ships]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Buy 5 fuel for 50 scrap. | `hidden="false"` — price visible up front | "The trader looks shocked. You're struck by the sense that this is the first time anyone's ever paid him these prices." **−50 scrap, +5 fuel.** | 100% |
| 2 | Buy 10 fuel for 95 scrap. *(BEST DEAL!)* | `hidden="false"` | Same text. **−95 scrap, +10 fuel.** | 100% |
| 3 | Negotiate. | — | "You offer a more reasonable price but the Slugman is outraged! He moves in to attack!" → the `JELLY_OVERPRICED` ship turns **hostile**. | 100% |

### Ship: `JELLY_OVERPRICED` when hostile ([[source-events-ships]])

| Result | Effect |
|---|---|
| Escapes (80s timer, 30s charge) | "The ship jumps away without a word…" Nothing gained. |
| Destroyed | "You try and collect as much fuel from the wreckage as possible." → `autoReward level="MED"` **fuel**. |
| Crew killed | "With the Slug ship subdued you are free to collect as much fuel as possible." → `autoReward level="HIGH"` **fuel**. |

No `<surrender>` block — once provoked, it fights or runs.

## Blue Options
None. (Unlike [[event-no-fuel-slug-fuel-trader]], having a Slug crew member does **not**
help here.)

## Rewards & Risks
- Purchases are guaranteed and cost 10 scrap/fuel (option 1) or 9.5 scrap/fuel (option 2).
- Negotiating is a free path to `MED`/`HIGH` fuel — but only if you win inside 80 seconds,
  and losing while stranded ends the run.
- No hidden branches on either purchase: what is printed is what you get.

## Strategy Notes
- *Opinion:* if your ship can beat a Slug fighter, negotiate — the fight pays fuel *and*
  scrap and costs nothing. The prices here are bad enough that buying is a concession.
- If you cannot risk combat, option 2 is strictly the better buy per unit (9.5 vs 10 scrap
  per fuel), and 10 fuel comfortably ends the crisis.
- Cross-check the pool before spending: [[event-no-fuel-automated-refueling-ship]] gives
  free `LOW` fuel and sells at 4 scrap/unit, and it is equally likely to appear.

## Related
- [[event-no-fuel-slug-fuel-trader]] — the cheaper, theft-prone Slug vendor
- [[event-no-fuel-automated-refueling-ship]] — the cheapest vendor in this pool
- [[entity-slugs]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact fuel/scrap values behind `autoReward` `MED` / `HIGH` fuel.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `JELLY_OVERPRICED`)
- [[source-fandom-no-fuel-slug-fuel-depot]] (per raw/wiki/no-fuel-slug-fuel-depot.md)
