---
id: source-fandom-pirate-fight
type: source
source_kind: wiki
raw: raw/wiki/pirate-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, hostile, default-rewards]
---

# Fandom — "Pirate fight"

## Summary
Community wiki page for `PIRATE`, retrieved via the MediaWiki API at revision 73761. The
baseline pirate ambush: five intro variants, one outcome (fight a pirate ship for default
rewards).

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Pirate Controlled
  Sector; `LRSmap=ship`, `unique=false`. It omits Federation Space, which the event lists
  in `events.xml`/`dlcEventsOverwrite.xml` imply via `HOSTILE1`-family membership.
- Transcribes all five `textList PIRATE` variants; they match `text_events.xml` exactly.
- Categorises it under "Fights with Default Rewards" and "Pirate ship fights" but gives no
  numbers of its own — the surrender/escape figures for the `PIRATE` ship live on
  [[source-fandom-pirate-toll]] instead.

## Events Covered
- [[event-pirate-fight]]

## Other Pages Touched
- [[entity-pirates]], [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Reliability Notes
`medium`. No version stated. Location list appears incomplete relative to the event lists.

## Contradictions Flagged
- Sector list omits [[sector-federation-space]] (see above) — recorded, not resolved.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_fight
- [[source-events-pirate]], [[source-events-ships]], [[source-dlceventsoverwrite]]
