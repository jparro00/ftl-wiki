---
id: source-fandom-zoltan-ship-asks-to-dock
type: source
source_kind: wiki
raw: raw/wiki/zoltan-ship-asks-to-dock.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, surrender, crew-reward]
---

# Fandom — "Zoltan ship asks to dock"

## Summary
Community wiki page for `ZOLTAN_SCIENCE_DOCK`, retrieved at revision 73916. Its useful
contribution is the observation that this ship's surrender **cannot be declined** — the
fight simply ends — which the XML supports but does not state.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'ZOLTAN_SCIENCE_DOCK' in the
  datafiles."*
- Locations: Zoltan Controlled Sector, Zoltan Homeworlds, `unique=true`,
  `LRSmap=noship` — no ship shows on scanners even though a fight is possible.
- Renders the surrender as **50% chance at 30–40% hull**, agreeing with
  [[concept-surrender-offers]]'s reading of `chance="0.5"`.
- States the ship **never tries to escape**, flagged in an HTML comment as needing
  confirmation — the ship block indeed declares no `<escape>`.
- Correctly separates the three endings' rewards: surrender → Zoltan crewmember + low
  standard; destroyed → low standard; dead crew → **medium** standard.
- *"If surrender is triggered, the fight is over: there is no option or prompt to decline
  the surrender to continue the fight."* Consistent with the `<surrender>` block
  containing no `<choice>` elements.

## Events Covered
- [[event-zoltan-ship-asks-to-dock]]

## Other Pages Touched
- [[event-zoltan-trade-hub]], [[event-zoltan-wise-man]], [[event-zoltan-fight]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]],
  [[concept-surrender-offers]]

## Reliability Notes
`medium`. All mechanical claims check out against `events_ships.xml` and
`events_zoltan.xml`. The author's own uncertainty about the escape behaviour is carried
through to the event page's open questions rather than smoothed over.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_ship_asks_to_dock
- [[source-events-zoltan]], [[source-events-ships]], [[source-text-events-xml]]
