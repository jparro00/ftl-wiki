---
id: event-improve-reactor-for-supplies
type: event
event_name: TRADER_UPGRADES_EXCHANGE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [trading, reactor, resource-cost, unique, advanced-edition, items-pool]
---

# Improve reactor for supplies — `TRADER_UPGRADES_EXCHANGE`

## Summary
A refugee convoy that will add a reactor bar in exchange for missiles, drone parts and/or
fuel — no scrap involved. Which bundle they ask for is rolled after you accept, one third
each. Guaranteed reactor upgrade, zero combat risk; the only question is whether the
resources are ones you can spare.

## Trigger & Where It Appears
- Event list: `ITEMS` in `newEvents.xml`, tagged `<!--DLC - down below-->`
  ([[source-newevents]]), and `OVERRIDE_ITEMS` in the Advanced Edition replacement,
  tagged `<!-- dlcEvents-->` ([[source-dlceventsoverwrite]]). It is **not** in
  `NEUTRAL_EXIT`, unlike its sibling [[event-trade-scrap-for-upgrades]].
- `ITEMS` is allocated by 14 sector definitions ([[source-sector-data-xml]]) and is also
  half of `EXIT_LIST`, so this can also fill an exit beacon — which is what Fandom's
  `alsooccur=exit` records ([[source-fandom-improve-reactor-for-supplies]]).
- `unique="true"` — at most once per run.
- Beacon: ordinary, no ship on Long-Ranged Scanners.

### Odds of drawing it
`ITEMS` has 13 distinct members (14 in `OVERRIDE_ITEMS`), none duplicated. **Assuming
uniform selection across list entries** ([[concept-event-list-weighting]]), each `ITEMS`
beacon is this event with probability **1/13** (base) or **1/14** (Advanced Edition).

## Text
`[varies: textList TRADER_UPGRADES_EXCHANGE_TEXT]` — two entries, no repeats
([[source-newevents]], [[source-text-events-xml]]):

1. *"You look like a military vessel. We're trying to get back to our homes alive. I'm an engineer by trade and could try to improve your reactor if you have any extra supplies."*
2. *You receive a message from a small convoy. They're looking for some military supplies and are offering to try to improve your reactor in exchange.*

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Agree to the trade. | — | Loads `TRADER_UPGRADES_EXCHANGE_LIST` — one of three price bundles, each granting `<upgrade amount="1" system="reactor"/>`. | 100% |
| 2 | Respectfully decline. | — | *"You decide you need what supplies you have."* → nothing. | 100% |

### `TRADER_UPGRADES_EXCHANGE_LIST` — three entries, no repeats (1/3 each)
All three share the same result text — *"You make the exchange and their team comes on
board to try to improve your reactor."* — and all three grant **+1 reactor bar**. Only the
bill differs. **Assuming uniform selection across list entries**
([[concept-event-list-weighting]]):

| Odds | Missiles | Drone parts | Fuel | Result |
|---|---|---|---|---|
| 1/3 | −3 to −5 | −0 to −2 | — | Reactor +1 |
| 1/3 | −0 to −2 | −2 to −3 | — | Reactor +1 |
| 1/3 | −0 to −2 | −0 to −2 | −2 to −3 | Reactor +1 |

([[source-newevents]]) Fandom lists the same three bundles and notes that **the required
amount is shown before you make the choice**
([[source-fandom-improve-reactor-for-supplies]]) — so in practice the 1/3 roll happens up
front and you are agreeing to a known bill.

Note that the second and third bundles have `min="-2" max="0"` on missiles and drones,
so a roll of **zero** is possible: the third bundle can cost nothing but 2–3 fuel.

### Fandom-only claim: the maxed-reactor bug
> *"Bug: having a maxed-out reactor does not prevent the trade, though you will simply
> lose the designated amount of missiles, drone parts, and/or fuel."*
> ([[source-fandom-improve-reactor-for-supplies]])

The files support the premise — unlike [[event-trade-scrap-for-upgrades]], **no `req` or
`max_lvl` gate appears anywhere on this event's choices** ([[source-newevents]]), so
nothing in the data stops the trade at a full reactor. The consequence (paying for
nothing) is Fandom's observation, not a file claim.

## Blue Options
None. No `req` attribute appears on any choice at any depth.

## Rewards & Risks
- **Reward:** a guaranteed reactor bar — normally a store-only purchase.
- **Cost:** 0–5 missiles, 0–3 drone parts, 0–3 fuel, depending on the bundle.
- **Risk:** none mechanically — no fight, no boarders. The real risk is agreeing while
  low on fuel and drawing the fuel bundle, or spending missiles a missile-dependent build
  needs.

## Strategy Notes
- *Opinion:* on a beam/laser ship carrying dead missiles this is close to a free reactor
  bar and should almost always be taken. On a Missile-heavy or drone-heavy build the
  first two bundles bite.
- Because the bill is shown first, the decision is fully informed — there is no gamble in
  accepting once you have seen the price.
- Skip it outright if the reactor is already maxed; per Fandom you will pay and receive
  nothing.

## Related
- [[event-trade-scrap-for-upgrades]] — the sibling shipwright event, same pool, pays in
  scrap and can upgrade subsystems as well as the reactor
- [[event-crew-hiring-station]] — the third AE trading event in `ITEMS`
- [[concept-event-list-weighting]] — basis for the 1/3 and 1/13 figures

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] What happens if you accept without enough of a resource — does it clamp at zero or
      is the choice hidden?
- [ ] Confirm the maxed-reactor bug against a run.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-improve-reactor-for-supplies]] (per raw/wiki/improve-reactor-for-supplies.md)
