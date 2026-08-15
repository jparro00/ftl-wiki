---
id: event-pirate-surrender-civilan
type: event
event_name: PIRATE_SURRENDER_CIVILAN
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unreachable, cut-content, surrender, orphan]
---

# Pirate surrender (civilian rescue) — `PIRATE_SURRENDER_CIVILAN`

## Summary
A complete, authored surrender-aftermath event: the pirate harassing a civilian ship breaks
off and jumps away, and you get the civilian rescue table anyway. **Nothing in the game
files loads it.** It appears to have been written as the `<surrender>` branch for the
`PIRATE_CIVILIAN` ship, which was then shipped without any surrender element at all.
Recorded here as unreachable content, not as a playable outcome.

## Trigger & Where It Appears
- Defined at `events.xml` as `<event name="PIRATE_SURRENDER_CIVILAN">` ([[source-events-xml]]).
  Note the misspelling of "CIVILIAN" in the id — that is the id as shipped.
- **No references anywhere.** A search of every `.xml` in `raw/gamedata/` finds the event id
  only in its own definition and in `text_events.xml` for its two strings. No `<event
  load=…>`, no `<surrender load=…>`, no `eventList` membership, no `<quest event=…>`.
- The obvious intended host is the `PIRATE_CIVILIAN` ship used by
  [[event-pirate-ship-attacking-civilian-distress]] and
  [[event-pirate-ship-attacking-civilian]] — but that ship definition has **no
  `<surrender>` and no `<escape>` element at all** ([[source-events-ships]]), which is
  exactly why nothing points here.
- Compare the wired-up sibling `PIRATE_SURRENDER`, which *is* loaded by the generic `PIRATE`
  ship via `<surrender chance="0.5" min="3" max="4" load="PIRATE_SURRENDER"/>`
  ([[source-events-ships]]).

## Text
> The pirates must not have been fully committed to the assault; they have been charging
> their FTL. They jump away, presumably to repair their ship.

(`event_PIRATE_SURRENDER_CIVILAN_text`, per [[source-text-events-xml]])

The event also carries `<ship hostile="false"/>`, i.e. it stands the current enemy down —
the signature of an aftermath event rather than a beacon.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail the civilian ship. | — | Loads `eventList SAVE_CIVILIAN_LIST` — the shared six-entry rescue table. | 100% |

There is only one choice, and it is `hidden="true"` ([[source-events-xml]]).

### `eventList SAVE_CIVILIAN_LIST` (6 entries)
Defined in `events_pirate.xml` ([[source-events-pirate]]). Assuming uniform selection across
`eventList` entries ([[concept-event-list-weighting]]), **1/6** each:

| Entry | Effect |
|---|---|
| 1 | A survivor offers to join — **Welcome aboard!** → `<crewMember amount="1"/>`; **Decline** → nothing |
| 2 | Science vessel → `autoReward level="MED"` `standard` |
| 3 | Crew did not survive → `autoReward level="LOW"` `standard` |
| 4 | Shipwright → `autoReward level="LOW"` **`weapon`** |
| 5 | Hull patch-up → `<damage amount="-5"/>` (5 hull repaired) |
| 6 | Civilian retreated → nothing |

## Blue Options
None.

## Rewards & Risks
Whatever `SAVE_CIVILIAN_LIST` rolls — up to a free crew member or a `LOW weapon` — for no
risk at all, since the fight is already over. Which is presumably why it was never wired
up: it would be a free re-roll of the rescue table on top of the fight rewards.

## Strategy Notes
Not applicable — unreachable in this build.

## Related
- [[event-pirate-ship-attacking-civilian-distress]] — the encounter this was written for
- [[event-pirate-ship-attacking-civilian]] — the same `PIRATE_CIVILIAN` ship
- [[event-pirate-surrender]] — the wired-up generic pirate surrender event
- [[entity-pirates]]

## Open Questions
- [ ] Did `PIRATE_CIVILIAN` carry a `<surrender load="PIRATE_SURRENDER_CIVILAN"/>` in
      pre-AE 1.0? Only the AE build was extracted here, so the vanilla ship definition is
      unverified — this may be cut content rather than never-wired content.
- [ ] Is the id misspelling (`CIVILAN`) the reason a reference failed to resolve at some
      point in development?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
