---
id: event-boss-automated
type: event
event_name: BOSS_AUTOMATED
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [endgame, last-stand, orphan, scripted, flagship, boss, text-only]
---

# Flagship goes automated — `BOSS_AUTOMATED`

## Summary
The one-line event that fires when you wipe out the Rebel Flagship's crew instead of its
hull: an onboard AI takes over and the fight continues without anyone aboard. It is a bare
`<text>` tag — no ship, no reward, no status effect — because the ship is already on screen
when it plays.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_AUTOMATED` appears in no `eventList`, no
  `sectorDescription`, and is `load`ed by nothing; the only references in `raw/gamedata/`
  are its own definition and the header comment in `events_boss.xml` that groups it with
  the boss-sequence events ([[source-events-boss]], [[source-sector-data-xml]]).
- Fired by the endgame scripting during a Flagship phase when the crew is eliminated. The
  text is the only statement of the trigger: *"Now that the crew is dead, it has taken
  control!"* No `deadCrew` block anywhere in `raw/gamedata/` loads it.
- Sector: [[sector-the-last-stand]] (`FINAL`).

## Text
> It appears this ship is also equipped with an advanced AI system. Now that the crew is
> dead, it has taken control!

(`event_BOSS_AUTOMATED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a single `<text>` tag)* | — | Text only. The fight continues against a crewless Flagship. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither is defined on the event. Its practical significance is that **killing the
Flagship's crew does not win the fight** — the ordinary `deadCrew` shortcut that ends
almost every other encounter in the game is explicitly denied here
([[source-events-boss]]).

## Strategy Notes
- None sourced. Note only that the usual boarding-to-crew-kill line of play does not
  shortcut any Flagship phase; the hull still has to come down. *(Reading of the event's
  existence and text, not a sourced strategy claim.)*
- None of the phase blueprints in `bosses.xml` carries a `<crewCount>` tag, so the data
  examined here does not state how many crew the Flagship has to lose before this fires
  ([[source-bosses]]).

## Related
- [[event-boss-text-1]], [[event-boss-text-2]], [[event-boss-text-3]] — the three phases
- [[event-boss-escaped]] — the other mid-fight interrupt
- [[event-boss-destroyed]] — the ending
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]]

## Open Questions
- [ ] Whether this fires once per phase or once per run.
- [ ] Whether the AI takeover changes the ship's behaviour mechanically (e.g. immunity to
      further boarding), which no file examined here states.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
