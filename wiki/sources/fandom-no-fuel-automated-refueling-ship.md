---
id: source-fandom-no-fuel-automated-refueling-ship
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-automated-refueling-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, trading, auto-ship]
---

# Fandom — "No fuel: automated refueling ship"

## Summary
Community wiki page for `FUEL_SELLER_DISTRESS`, retrieved at revision 73275. Notable for two
things the game files cannot say on their own: that the "one-time" fuel allowance is not
actually one-time, and an explicit open question about the ship's second escape tag.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_SELLER_DISTRESS' in the
  datafiles."*
- Marks it `{{Locations|outoffuel=distresson}}`, matching the XML.
- **"The 'one-time complimentary emergency fuel allowance' is mere flavor text and the first
  option will always be available each time the event is encountered."** Nothing in the XML
  tracks such a flag, so this is consistent, but the claim itself is Fandom's.
- Reads `autoReward level="LOW"` fuel_only as 1–3 fuel and the destroyed reward as medium
  (2–4 fuel + scrap).
- Confirms prices: 20 scrap → 5 fuel, 8 scrap → 2 fuel.

## Events Covered
- [[event-no-fuel-automated-refueling-ship]]

## Other Pages Touched
- [[event-no-fuel-slug-fuel-depot]], [[event-no-fuel-fuel-trader-distress-on]]

## Reliability Notes
`medium`, `game_version: unknown`.

## Contradictions Flagged
None outright, but the page raises an unresolved mechanical question in an inline comment:
the `AUTO_FUEL_SELLER` ship block contains a second `<escape chance="0.5" min="2" max="5">`
line alongside its `timer="80"` escape, and Fandom says it *"seems unlikely that it has any
effect… however it needs testing or code evaluation to be 100% sure."* Recorded as an open
question on [[event-no-fuel-automated-refueling-ship]] rather than resolved.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_automated_refueling_ship
- [[source-events-fuel]], [[source-text-events-xml]], [[source-events-ships]]
