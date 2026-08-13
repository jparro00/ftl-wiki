---
id: source-fandom-trade-scrap-for-upgrades
type: source
source_kind: wiki
raw: raw/wiki/trade-scrap-for-upgrades.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, system-upgrade, reactor, items-pool]
---

# Fandom — "Trade scrap for upgrades"

## Summary
Community wiki page for `TRADER_UPGRADES`, retrieved at revision 73902. Its standout value
is a Trivia note that explains the **`max_group` choice-ordering rule** — a piece of engine
behaviour that shows up across the whole wiki and is not documented anywhere in the game
files.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'TRADER_UPGRADES' in the
  datafiles."*
- Locations: the 14 `ITEMS` sectors plus `alsooccur=exit`, consistent with membership of
  both `ITEMS` and `NEUTRAL_EXIT`.
- All nine price bands transcribed and **all nine match the XML exactly** (Oxygen 15–20 /
  25–40; Piloting 8–15 / 25–40; Doors 8–15 / 25–40; Sensors 10–20 / 35–45; reactor 15–25).
- States three limits: cannot upgrade past maximum, cannot upgrade an uninstalled
  subsystem, cannot take the reactor past 25 power bars.
- **The `max_group` note:** *"outcomes which upgrade (sub)systems use 'max_group' to select
  the right level of (sub)system, and since choices with max_group are moved below choices
  without it, it causes those 'agree' choices to come after the 'decline' choices... This
  is also why blue options tend to be at the bottom of lists."* This is the clearest
  available explanation of the attribute and is reused on
  [[event-battlefield-wreckage]].
- `unique=true`.

## Events Covered
- [[event-trade-scrap-for-upgrades]]

## Other Pages Touched
- [[event-improve-reactor-for-supplies]], [[event-crew-hiring-station]],
  [[event-battlefield-wreckage]], [[concept-blue-options]],
  [[concept-event-list-weighting]]

## Reliability Notes
`medium` — but unusually strong for a Fandom page: every number is verifiable against
`newEvents.xml` and every one checks out. The `max_group` explanation is engine behaviour
that cannot be confirmed from data alone and is attributed rather than asserted.

## Contradictions Flagged
- Trivial: *"Need a tune-up?"* (Fandom) vs *"Need a tuneup?"* (game string). Recorded on
  [[event-trade-scrap-for-upgrades]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Trade_scrap_for_upgrades
- [[source-newevents]], [[source-text-events-xml]], [[source-dlceventsoverwrite]]
