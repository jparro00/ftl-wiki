---
id: event-lanius-boarders
type: event
event_name: LANIUS_BOARDERS
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [unreachable, cut-content, orphan, boarding, lanius, no-choice, advanced-edition]
---

# Lanius boarders — `LANIUS_BOARDERS`

## Summary
A finished boarding ambush — three Lanius board you out of a derelict husk, with no ship, no
choices and no way out but killing them — whose **only reference in the game files is
commented out**. It is cut content: written, wired, and then explicitly disabled with a
developer note explaining why.

## Trigger & Where It Appears
- **Unreachable / cut.** `LANIUS_BOARDERS` is referenced exactly once in `raw/gamedata/`, and
  that reference is inside an XML comment ([[source-dlcevents-anaerobic]], line 68):

  ```xml
  <eventList name="BOARDERS_LANIUS"> <!-- Prob enough - unless theres something cool -->
      <!--<event load="LANIUS_BOARDERS"/> -->
      <event load="LANIUS_PIRATE_BOARDERS"/>
  </eventList>
  ```

- This is the "sole list entry is commented out" case in its purest form. Per
  [[concept-event-list-weighting]], commented-out entries are excluded from the pool, so
  `BOARDERS_LANIUS` is a **one-member list**: every Lanius-sector boarding beacon resolves to
  [[event-boarders-humans-abandoned]] (`LANIUS_PIRATE_BOARDERS`) instead.
- The list itself is live and well allocated — the Lanius sector gives it
  `<event name="BOARDERS_LANIUS" min="1" max="2"/>` ([[source-sector-data-xml]]) — so this is
  not an allocation problem. The event was deliberately removed from a functioning pool.
- The developer note *"Prob enough - unless theres something cool"* sits on the list, and
  reads as the reason: one boarding event was judged sufficient.
- `unique="true"`. `sectors:` is left empty because the event is not reachable; had it been
  enabled it would appear in the Lanius sector ([[sector-abandoned-sector]]).
- **Version:** `ae`. It lives in `dlcEvents_anaerobic.xml`; neither the Lanius nor this event
  exist in vanilla.
- No Fandom page documents it, consistent with it never firing.

## Text
Written inline rather than as a `text_events.xml` id — one of the few events in the file
that is ([[source-dlcevents-anaerobic]]):

> You detect a small craft in an otherwise empty area and move in to examine it. It appears
> to be the husk of a Lanius ship barely holding together. As you are closely scanning it for
> useful materials, three figures climb out from the wreckage and launch themselves the short
> distance onto your ship. An explosive vibration rocks the ship and Lanius lifeforms are
> detected on board!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event body is text plus `<boarders/>`)* | — | `<boarders min="3" max="3" class="anaerobic"/>` — **exactly three Lanius** board immediately. No enemy ship is staged, so there is nothing to shoot and no ship rewards. | 100% |

The boarder count is fixed at 3, not a range — unusual; most boarding events use a min/max
band.

## Blue Options
None. The event has no choices at all, so no `req` is possible.

## Rewards & Risks
- **No reward whatsoever.** There is no `<ship>`, no `autoReward`, and no follow-up choice —
  killing the boarders is the entire event.
- **Risk:** three Lanius aboard. Lanius drain oxygen from every room they occupy, so a
  fixed three-boarder wave without a ship to destroy is a pure attrition event — arguably why
  it was cut in favour of `LANIUS_PIRATE_BOARDERS`, which at least brings a ship to fight.

## Strategy Notes
None — the event cannot occur. If Lanius board you in the Lanius sector, you are in
[[event-boarders-humans-abandoned]].

## Related
- [[event-boarders-humans-abandoned]] (`LANIUS_PIRATE_BOARDERS`) — the event that replaced it,
  and now the sole member of `BOARDERS_LANIUS`
- [[entity-lanius]] — the boarders' species and their oxygen-draining trait
- [[sector-abandoned-sector]] — where it would have appeared
- [[concept-event-list-weighting]] — why commented-out entries are excluded
- [[concept-sector-event-allocation]] — the evidence bar for calling something unreachable

## Open Questions
- [ ] Whether `class="anaerobic"` boarders drain oxygen at the same rate as Lanius crew.
- [ ] Whether the event was disabled before or after the AE release — the file records only
      the note, not a date.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
