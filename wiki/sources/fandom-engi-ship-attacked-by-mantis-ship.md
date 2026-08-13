---
id: source-fandom-engi-ship-attacked-by-mantis-ship
type: source
source_kind: wiki
raw: raw/wiki/engi-ship-attacked-by-mantis-ship.md
game_version: unknown
ingested: 2026-08-09
reliability: medium
tags: [fandom, engi, quest-marker, blue-option]
---

# Fandom — Engi ship attacked by Mantis ship

## Summary
FTL Fandom wiki page for `ENGI_STATION_DISTRESS` (revision 74854, retrieved 2026-08-09).
The largest Engi-sector reward tree: a distress call that is either a Mantis boarding
trap or a rescuable Engi station with a four-way reward list.

## Key Takeaways
- States that the event is *meant* to occur at a distress beacon but does not, because the
  `<distressBeacon/>` tag is missing from its definition. Verified against
  `raw/gamedata/events_engi.xml`, which indeed omits the tag.
- Puts concrete numbers on the `SAVE_ENGI_STATION` fuel rewards — "medium (2-4)" and
  "high (3-6)" — which the game files do not state.
- Documents the Engi-crew blue option ("Protocol 52.34") that adds the
  **Hidden Federation Base** quest marker plus a weapon and 10 hull repairs.

## Events Covered
- [[event-engi-ship-attacked-by-mantis-ship]] — `ENGI_STATION_DISTRESS`

## Other Pages Touched
- [[chain-hidden-federation-base]], [[entity-mantis]], [[entity-engi]]

## Contradictions Flagged
Fuel quantities are Fandom-only; the game files give reward *levels* (`MED`, `HIGH`) with
no numbers. Recorded on [[event-engi-ship-attacked-by-mantis-ship]].

## Links
- https://ftl.fandom.com/wiki/Engi_ship_attacked_by_Mantis_ship
- [[source-events-xml]], [[source-text-events-xml]]
