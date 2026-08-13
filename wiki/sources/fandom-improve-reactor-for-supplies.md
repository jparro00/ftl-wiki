---
id: source-fandom-improve-reactor-for-supplies
type: source
source_kind: wiki
raw: raw/wiki/improve-reactor-for-supplies.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, reactor, items-pool, bug]
---

# Fandom — "Improve reactor for supplies"

## Summary
Community wiki page for `TRADER_UPGRADES_EXCHANGE`, retrieved at revision 74242. Short and
accurate; its unique contribution is a reported bug about trading with a maxed reactor.

## Key Takeaways
- Names the in-game id in Notes: *"This event is called 'TRADER_UPGRADES_EXCHANGE' in the
  datafiles."*
- Locations: the 14 `ITEMS` sectors plus `alsooccur=exit`.
- Transcribes all three resource bundles — (3–5 missiles, 0–2 drones), (0–2 missiles, 2–3
  drones), (2–3 fuel, 0–2 missiles, 0–2 drones) — **matching the XML exactly**.
- Notes the required amount is shown before you choose, which makes the 1/3 list roll
  effectively front-loaded.
- **Reported bug:** *"having a maxed-out reactor does not prevent the trade, though you
  will simply lose the designated amount of missiles, drone parts, and/or fuel."* The
  premise is supported by the files — no `req` or `max_lvl` gate appears anywhere on this
  event — but the consequence is Fandom's observation.
- `unique=true`.

## Events Covered
- [[event-improve-reactor-for-supplies]]

## Other Pages Touched
- [[event-trade-scrap-for-upgrades]], [[event-crew-hiring-station]],
  [[concept-event-list-weighting]]

## Reliability Notes
`medium`. Every stated resource band checks out against `newEvents.xml`. The bug is a
single-source behavioural claim and is recorded as such.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Improve_reactor_for_supplies
- [[source-newevents]], [[source-text-events-xml]], [[source-dlceventsoverwrite]]
