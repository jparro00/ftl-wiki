---
id: source-fandom-rebel-ship-supplying-civilians
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-supplying-civilians.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, filler]
---

# Fandom — "Rebel ship supplying civilians"

## Summary
Documents the five intro variants, the three choices, the `REBEL_HELPERS_SHIP` fight and
both post-fight branches ("Steal the civilian supplies" / "Leave the civilians alone").
Declares the datafile id: **"This event is called `REBEL_HELPERS` in the datafiles."**

## Key Takeaways
- `REBEL_HELPERS_SHIP` neither surrenders nor tries to escape.
- Destroyed → low standard reward; dead crew → medium standard reward. Either way you
  then choose to steal from the civilians or leave them.
- The steal pool has four results: low drone parts, nothing (vaccines), low scrap-only,
  or a booby trap (2 hull + 2 random-room damage).
- Interprets the low `droneparts` reward as **1 drone part**.

## Events Covered
- [[event-rebel-ship-supplying-civilians]] (`REBEL_HELPERS`)

## Other Pages Touched
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[entity-rebels]]

## Contradictions Flagged
- The booby-trap outcome is a single `<damage amount="2" system="room" effect="random"/>`
  in the XML; Fandom reads it as 2 hull **and** 2 room damage. Recorded on the event page.

## Links
- https://ftl.fandom.com/wiki/Rebel_ship_supplying_civilians (revision 73816, retrieved 2026-08-09)
