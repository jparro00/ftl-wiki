---
id: source-fandom-lanius-ship-absorbing-automated-scout
type: source
source_kind: wiki
raw: raw/wiki/lanius-ship-absorbing-automated-scout.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, combat, fleet-delay, map-reveal, advanced-edition]
---

# Fandom — "Lanius ship absorbing automated scout"

## Summary
The community wiki page for `LANIUS_AUTO_REBEL`. Retrieved at revision 74231. Its most
valuable content is the "Inspect the automated ship" follow-up, which every win path
reaches — including the one where the Lanius escapes.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_AUTO_REBEL' in the datafiles."*
- Locations: Abandoned Sector, `LRSmap=ship`, `unique=true`.
- Enemy is the `LANIUS_AUTO_REBEL` ship definition: **escape-capable, no surrender**.
- Both `LANIUS_AUTO_REBEL_LIST` outcomes are transcribed: one reveals the sector map, the
  other delays the Rebel fleet by 1 turn; both also pay scrap.
- **Engine-behaviour claim:** an inline HTML comment notes the XML writes
  `<autoReward level="low">` in lowercase where it should be `LOW`, and asserts the game
  therefore treats the value as `RANDOM`. This is the page's own interpretation, not
  something the XML states.
- Categories: `Advanced Edition Content Events`, `Rebel Fleet delay chance`,
  `Beacon Map reveal chance`.

## Events Covered
- [[event-lanius-ship-absorbing-automated-scout]]

## Other Pages Touched
- [[entity-lanius]], [[sector-abandoned-sector]]

## Reliability Notes
`medium`. Text transcriptions match. The lowercase-`low` claim is a plausible reading of a
real quirk in the file, but it is an inference about the engine and is not verifiable from
the data in `raw/`.

## Contradictions Flagged
None outright — but see the `autoReward level="low"` note above, recorded on
[[event-lanius-ship-absorbing-automated-scout]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_ship_absorbing_automated_scout
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
