---
id: source-fandom-the-mercenary
type: source
source_kind: wiki
raw: raw/wiki/the-mercenary.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [fleet-delay, map-reveal, pirate-fight]
---

# Fandom — "The mercenary"

## Summary
The community wiki page for the event the game files call `MERCENARY`. Retrieved via the
MediaWiki API at revision 73898. Short page; its value is the scrap ranges, the explicit
statement of what each service does, and the surrender/escape figures for the generic
`PIRATE` ship.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'MERCENARY' in the datafiles."*
- Quotes all six intro text variants, matching `textList MERCENARY`.
- Scrap costs: 10–25 for the fleet delay, 10–20 for the map reveal — identical to the XML.
- States the delay is **2 turns** and adds *"[no effect in The Last Stand sector]"*, which
  the game files do not encode anywhere.
- Fight branch: generic `PIRATE` ship, default rewards, 50% surrender and 50% escape —
  consistent with `1 − chance` on `chance="0.5"` ([[concept-surrender-offers]]).
- Categorised `Random_Events`, `Filler_Events`; `unique=false`, `LRSmap=ship`,
  `alsooccur=filler`.

## Events Covered
- [[event-the-mercenary]] — costs, effects, fight profile

## Other Pages Touched
- [[sector-civilian-sector]], [[sector-pirate-controlled-sector]],
  [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[entity-pirates]], [[event-pirate-fight]]

## Reliability Notes
`medium`. The page states no game version, so `game_version` is `unknown`. Its numbers
agree with the extracted 1.6.x files throughout.

## Contradictions Flagged
None material. The location template omits [[sector-federation-space]] even though
`NEUTRAL` / `OVERRIDE_NEUTRAL` reaches it as filler — noted on
[[event-the-mercenary]] as a listing-convention gap rather than a substantive disagreement.
The Last Stand claim is unverifiable from the files and is recorded as Fandom-only.

## Links
- Source URL: https://ftl.fandom.com/wiki/The_mercenary
- [[source-events-xml]], [[source-events-ships]], [[source-text-events-xml]]
