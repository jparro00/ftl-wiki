---
id: source-fandom-trade-resources-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/trade-resources-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, trading, resources, unique]
---

# Fandom — "Trade resources in nebula"

## Summary
The community wiki page for `NEBULA_TRADER`. Retrieved via the MediaWiki API at revision
74847. Two choices; the interesting content is the exact numbers on the four possible
trades.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_TRADER' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `nebula=true`, `alsooccur=nebulafiller`, `LRSmap=noship+nebula`, `unique=true`.
- **Enumerates all four trades exactly**, and they match `TRADER_LIST` in `events.xml`
  item-for-item:
  - −1–2 drone parts → +5–10 fuel
  - −1–2 fuel → +4–5 missiles
  - −2–3 missiles → +2–3 drone parts
  - −2–4 missiles → +4–10 fuel
- Adds the important UI fact the XML cannot express: *"the actual trade offer is shown
  prior to making the choice"* — so the roll happens before you commit.
- Categorised `Trading Events`.

## Events Covered
- [[event-trade-resources-in-nebula]]

## Other Pages Touched
- [[sector-uncharted-nebula]], [[concept-scrap-economy]]

## Reliability Notes
`medium`, but this is a strong page: the numbers are a verbatim match to `TRADER_LIST`,
and the "offer shown first" note is genuinely additive over the game files.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Trade_resources_in_nebula
- [[source-events-nebula]], [[source-events-xml]], [[source-text-events-xml]]
