---
id: event-quest-store
type: event
event_name: QUEST_STORE
sectors: []
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [unreachable, cut-content, store, orphan, no-choice]
---

# Hidden space dock — `QUEST_STORE`

## Summary
A one-line store event: you arrive at a hidden space dock that was expecting you, and a
store opens. It is fully written and carries a dev note marking it as a reusable building
block — but **nothing in the game files loads it**, so it never occurs. Recorded as
shipped-but-unreachable content.

## Trigger & Where It Appears
- Defined at `events.xml` as `<event name="QUEST_STORE">`, with the inline dev comment
  *"JUSTIN - Can be used elsewhere"* ([[source-events-xml]]).
- **No references anywhere.** A search of every `.xml` in `raw/gamedata/` finds
  `name="QUEST_STORE"` only in its own definition (the many `QUEST_STORE_RESCUE` hits are a
  different event, [[event-quest-store-rescue]]). No `eventList` membership, no
  `<event load=…>`, no `<quest event=…>`.
- The dev note reads as intent rather than wiring: it was authored as a generic
  "quest hands you a store" payload for some other event to point at, and nothing ever did.
- No Fandom page joins to this id.

## Text
> You follow the directions given to you and find the hidden space dock. The owner hails
> you, "I got a message that you were coming. I don't normally offer goods to strangers, but
> I'll make an exception. Take a look."

(`event_QUEST_STORE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `<store/>` — a store opens. Nothing else. | 100% |

The entire event body is one text id and one `<store/>` tag ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
A free store visit and nothing else. No ship, no cost, no risk — which is presumably why it
was written as a generic payload rather than a beacon in its own right.

## Strategy Notes
Not applicable — unreachable in this build.

## Related
- [[event-quest-store-rescue]] — the similarly-named but genuinely reachable space-dock
  rescue; note the two are **different events** and only the rescue is wired up
- [[event-settlement-mercenary-work]] — the quest that leads to the reachable space dock
- [[event-store-crystal]], [[event-store-pirate]] and the other `STORE_*` events — the
  live store beacons

## Open Questions
- [ ] Was `QUEST_STORE` referenced in pre-AE 1.0? Only the AE build was extracted here, so
      it may be cut content rather than never-wired content.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
