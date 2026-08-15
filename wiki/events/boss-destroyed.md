---
id: event-boss-destroyed
type: event
event_name: BOSS_DESTROYED
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [endgame, last-stand, orphan, scripted, flagship, boss, victory, dev-text]
---

# Flagship destroyed — `BOSS_DESTROYED`

## Summary
The win condition's event: the Flagship blows up and the Federation is saved. Two lines of
prose, a `Continue...` choice, and a `status` clear. It is also the single most conspicuous
piece of leftover development text in the shipped data — the follow-up string still
addresses the player as a **beta tester** and points them at the Subset Games forums.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_DESTROYED` appears in no `eventList`, no
  `sectorDescription`, and is `load`ed by nothing; the only references in `raw/gamedata/`
  are its own definition and the header comment in `events_boss.xml`
  ([[source-events-boss]], [[source-sector-data-xml]]).
- Fired by the endgame scripting when the Flagship's third phase is destroyed in
  [[sector-the-last-stand]].

## Text
> Its explosion rocks your ship and you shudder with relief. You did it. The Federation is
> saved....

(`event_BOSS_DESTROYED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Continue... (the shared `continue` string, `raw/gamedata/text_misc.xml` — no source page exists for that file yet) | — | The follow-up text below. No mechanical effect. | 100% (only choice) |

Event-level effect, applied regardless of the choice
(`<status type="clear" target="player" system="sensors" amount="100"/>`): clears a status
effect on your own sensors system — the same tag [[event-boss-escaped]] carries
([[source-events-boss]]).

### The follow-up text
> Thanks for playing! Keep in mind this is still in beta and we have not created a
> satisfying conclusion to the game. Head to our forums to give us some feedback and let us
> know that you beat it. Thanks!

(`event_BOSS_DESTROYED_c1_text`, per [[source-text-events-xml]])

This is a **beta-era developer message that is still present in the 1.6.x Advanced Edition
data** extracted for this wiki (see `raw/gamedata/_PROVENANCE.md`). It is recorded here
because it is what the files say. Whether the running game ever displays it — as opposed to
handing off to the ending sequence and credits — is **not stated in any file examined
here**, and no source in this wiki confirms it either way. Do not read this page as a claim
that the shipped game shows this string.

## Blue Options
None.

## Rewards & Risks
No `autoReward` and no `item_modify` — the event pays nothing, which is consistent with it
being the terminal event of the run ([[source-events-boss]]).

## Strategy Notes
None. There is nothing left to decide.

## Related
- [[event-boss-text-3]] — the phase whose destruction leads here
- [[event-boss-escaped]] — what fires instead when a phase ends without a kill
- [[event-boss-automated]] — what fires when the crew dies but the ship does not
- [[event-federation-base]], [[event-last-stand-start]]
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]], [[entity-federation]]

## Open Questions
- [ ] Whether `event_BOSS_DESTROYED_c1_text` is reachable in the retail build, or is dead
      text superseded by the ending sequence.
- [ ] What applies the sensors status this event clears.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- raw/gamedata/text_misc.xml — the shared `continue` choice string (no source page yet)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
