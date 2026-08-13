---
id: source-fandom-friendly-ship-out-of-fuel
type: source
source_kind: wiki
raw: raw/wiki/friendly-ship-out-of-fuel.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, trading, fuel, weapon-reward-chance, map-reveal]
---

# Fandom — "Friendly ship out of fuel"

## Summary
The community wiki page for the event the game files call `FRIENDLY_BEACON`. Retrieved via
the MediaWiki API at revision 74075. Its most useful contribution is spelling out the
four-way gift pool that the parsed event structure hides behind a `load="RANDOM_GIFT"`.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FRIENDLY_BEACON' in the
  datafiles."* This is the join key.
- Marks the high-scrap gift with `{{DuplicateEvent|2}}` — an explicit acknowledgement that
  that outcome **appears twice** in the `RANDOM_GIFT` list, which is exactly what the files
  show. This independently corroborates the weighting derived on
  [[event-friendly-ship-out-of-fuel]].
- Documents the reactor-upgrade gift and adds the failure case the files do not state:
  *"If your ship reactor was already fully upgraded, you will receive the message: 'Could
  not upgrade the Reactor, it's maxed' — and nothing happens."*
- Confirms the fuel cost is shown to the player before committing (*"the requested amount
  of fuel is shown before you make the choice"*), and renders `min="-4" max="-2"` as a
  **2–4 fuel** payment.
- Confirms `distress=true`, `LRSmap=ship` (a civilian ship is present), `unique=false`.
- Categorised `Random_Events`, `Trading_Events`, `Weapon reward chance`,
  `Beacon Map reveal chance`, `Reactor Upgrade chance`.

## Events Covered
- [[event-friendly-ship-out-of-fuel]]

## Other Pages Touched
- [[item-reactor]], [[concept-scrap-economy]], [[concept-fuel]]

## Reliability Notes
`medium`. No game version stated — and the reactor-upgrade gift it lists is flagged
`<!--DLC!-->` in the files, so this page describes the Advanced Edition pool.

## Contradictions Flagged
> ⚠️ **Version gap, not an error.** The reactor-upgrade entry in `RANDOM_GIFT` carries a
> `<!--DLC!-->` marker in `events.xml` ([[source-events-xml]]). The vanilla gift pool is
> therefore four entries, not five. Fandom lists all four distinct gifts with no version
> note. Recorded on [[event-friendly-ship-out-of-fuel]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Friendly_ship_out_of_fuel
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]]
