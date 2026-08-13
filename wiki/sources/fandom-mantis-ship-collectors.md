---
id: source-fandom-mantis-ship-collectors
type: source
source_kind: wiki
raw: raw/wiki/mantis-ship-collectors.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, quest-marker, ship-escape, surrender]
---

# Fandom — "Mantis ship-collectors"

## Summary
The community wiki page for the event the game files call `DONOR_MANTIS_CHASE`.
Retrieved via the MediaWiki API at revision 74723. It covers both halves of the
encounter — the first fight and the quest-marker rematch (`DONOR_MANTIS_CHASE2`) — on a
single page, which the game files split across two event definitions.

## Key Takeaways
- **Names the in-game id explicitly**: *"This is a donor event called
  'DONOR_MANTIS_CHASE' in the datafiles."* This is the join key.
- Identifies the two ship blueprints by name: a **Mantis Fighter** for the first fight and
  a **Mantis Bomber** for the rematch, both crewed entirely by Mantis. The game files only
  give `auto_blueprint="MANTIS_FIGHTER"` / `"MANTIS_BOMBER"`.
- Reads the first ship's `<escape timer="5" min="5" max="5"/>` as **escape chance 100%**
  with a 5-second timer at 50% hull.
- Reads the rematch's escape/surrender thresholds as *"attempts to escape at 60% hull
  (12 second timer) and makes a surrender offer at 20% hull"*, with an explicit tooltip
  caveat that the *"actual in-game value may be 6 hull + additional hull adjusted by sector
  progression"* / *"2 hull + …"*. That caveat matches the raw `min`/`max` values being hull
  points rather than percentages — see [[concept-surrender-offers]].
- Adds a mechanical note the files don't state: the `standard` scrap-with-resources roll
  *"will never give a bonus weapon, drone schematic or augmentation, due to its interaction
  with a guaranteed weapon/drone schematic reward"* — relevant to the rematch's destroyed /
  deadCrew payouts, which pair a guaranteed weapon with a `standard` roll.
- Notes that the surrender offer's weapon and scrap amounts are shown **before** you accept.
- Categorised as `Random_Events`, `Unique_Events`, `Donor Events`, `Ship escape Events`,
  `Events with Quest Markers`, `Ship surrender Events`, `Weapon reward opportunity`.

## Events Covered
- [[event-mantis-ship-collectors]]

## Other Pages Touched
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[entity-mantis]],
  [[concept-surrender-offers]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Its percentage readings of
`escape`/`surrender` `min`/`max` are an interpretation of raw hull values, and the page
says as much in its own tooltips.

## Contradictions Flagged
None material. Wording differs trivially from the files (*"impressive-looking"* vs
*"impressive looking"*).

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_ship-collectors
- [[source-events-xml]], [[source-text-events-xml]]
