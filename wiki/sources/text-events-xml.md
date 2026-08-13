---
id: source-text-events-xml
type: source
source_kind: gamedata
raw: raw/gamedata/text_events.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [strings, partial-ingest]
---

# text_events.xml

## Summary
Every English string used by every event — 3,298 entries, 559 KB. No event file is
readable without it. **Partially ingested**: strings resolved on demand as events are
paged.

## Key Takeaways
- Format is `<text name="ID">prose</text>`; event files reference these via
  `<text id="ID"/>`.
- Naming convention makes the join mechanical:
  - `event_<EVENT>_text` — the event's opening prose
  - `event_<EVENT>_c<N>_choice` — the label on choice N
  - `event_<EVENT>_c<N>_text` — the outcome prose for choice N
- **3,298 strings against 458 events** — roughly 7 strings per event, which is why
  outcome text has to be resolved per choice rather than per event.
- Resolving prose against the whole event corpus succeeds for **445 of 458 events**. The
  13 misses are events whose text comes from a `<text load="LIST"/>` text list rather
  than a fixed id, so they have no single canonical wording.

## Events Covered
- [[event-ancient-device]] — supplied the event text and all three choice outcomes.

## Other Pages Touched
- None directly; this file is a lookup table that every event page depends on.

## Contradictions Flagged
The game-file wording of [[event-ancient-device]]'s Crystal-crew outcome differs from the
Fandom transcription. Flagged on that page; this file is the higher-reliability side.

## Links
- [[source-events-xml]]
