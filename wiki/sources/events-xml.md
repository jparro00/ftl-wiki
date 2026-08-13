---
id: source-events-xml
type: source
source_kind: gamedata
raw: raw/gamedata/events.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [events, partial-ingest]
---

# events.xml

## Summary
The main event definition file — 91 `<event>` definitions and 56 `<eventList>`s, the
largest single event file in the game. **Only partially ingested so far**: this pass
took `ROCK_CRYSTAL_BEACON` and identified two other chain steps.

## Key Takeaways
- Events carry no prose. Text is referenced by id
  (`<text id="event_ROCK_CRYSTAL_BEACON_text"/>`) and resolved through
  [[source-text-events-xml]].
- `<choice>` elements carry the branching. A `req="..."` attribute is the blue-option
  gate — e.g. `req="crystal"` on [[event-ancient-device]] requires a Crystal crew member.
- Choices resolve either to an inline `<event>` (a fixed outcome) or to a
  `load="SOME_LIST"` reference (a randomised outcome). **Where a choice loads a list, the
  odds are not expressed as percentages anywhere in the file** — the weighting is
  implicit in the list's contents.
- Some events use `<text load="...">` to pull from a text list, so their prose varies
  per encounter and cannot be quoted as a single string.
- Three steps of [[chain-crystal-cruiser-unlock]] live in this one file:
  `ASTEROID_DERELICT_SHIP`, `ZOLTAN_CREW_STUDY`, `ROCK_CRYSTAL_BEACON`.

## Events Covered
- [[event-ancient-device]] — `ROCK_CRYSTAL_BEACON`, fully ingested

Identified but not yet paged: `ASTEROID_DERELICT_SHIP`, `ZOLTAN_CREW_STUDY`, and 88
others in this file.

## Other Pages Touched
- [[chain-crystal-cruiser-unlock]]

## Contradictions Flagged
None internal. One cross-source discrepancy on [[event-ancient-device]]'s choice-3 text
versus Fandom — flagged on that page.

## Links
- [[source-text-events-xml]]
- [[source-sector-data-xml]]
