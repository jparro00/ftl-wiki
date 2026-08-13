---
id: source-fandom-no-fuel-auto-ship-warning
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-auto-ship-warning.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, rebel, rebel-fleet, auto-ship]
---

# Fandom — "No fuel: Auto-ship warning"

## Summary
Community wiki page for `FUEL_ON_REBEL_WARNING`, retrieved at revision 74039. Short but
carries a mechanically important note about the escape timer that the raw XML only implies.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_ON_REBEL_WARNING' in the
  datafiles."*
- Marks it `{{Locations|outoffuel=distresson}}`, matching the XML.
- **The 40-second timer is the exception.** Fandom states that every other out-of-fuel event
  uses 80 seconds, and any hostile ship met after running dry uses 90 — this scout starts
  its escape immediately on a 40s timer, like *Auto-ship warning*, *Auto-ship warning in
  nebula* and *Rebel ship warning*. The `timer="40"` value in the ship block corroborates
  ([[source-events-ships]]).
- Reads the destroyed reward as low standard (scrap with resources).

## Events Covered
- [[event-no-fuel-auto-ship-warning]]

## Other Pages Touched
- [[event-auto-ship-warning]], [[event-auto-ship-warning-in-nebula]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`, `game_version: unknown`.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** the escape penalty.
> Fandom: *"Rebel Fleet pursuit is **doubled**."* Game files: `<modifyPursuit amount="1"/>`
> ([[source-events-ships]]) — one extra advance. Recorded on
> [[event-no-fuel-auto-ship-warning]]; game files trusted. The two may describe the same
> effect, but no source confirms the equivalence.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_Auto-ship_warning
- [[source-events-fuel]], [[source-text-events-xml]], [[source-events-ships]]
