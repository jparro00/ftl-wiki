---
id: event-boss-escaped
type: event
event_name: BOSS_ESCAPED
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [endgame, last-stand, orphan, scripted, flagship, boss, sensors, autoreward]
---

# Flagship escapes a phase — `BOSS_ESCAPED`

## Summary
Fires when the Flagship breaks off and jumps rather than dying — the transition between one
phase and the next. It is the only event in the boss sequence that pays out: an
`autoReward level="HIGH"` `standard`, plus a `status` tag that clears a sensors effect on
your ship.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_ESCAPED` appears in no `eventList`, no `sectorDescription`,
  and is `load`ed by nothing; the only references in `raw/gamedata/` are its own definition
  and the header comment in `events_boss.xml` ([[source-events-boss]],
  [[source-sector-data-xml]]).
- Fired by the endgame scripting when a Flagship phase ends with the ship FTL-ing out. The
  text is the only statement of the trigger.
- Sector: [[sector-the-last-stand]] (`FINAL`).

## Text
> Just as you finally gain the upper hand it finds a way to make an FTL jump. You've got to
> keep up the assault!

(`event_BOSS_ESCAPED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `autoReward level="HIGH"` **`standard`**, and `<status type="clear" target="player" system="sensors" amount="100"/>`. | 100% |

The full definition ([[source-events-boss]]):

```xml
<event name="BOSS_ESCAPED">
    <text id="event_BOSS_ESCAPED_text"/>
    <autoReward level="HIGH">standard</autoReward>
    <status type="clear" target="player" system="sensors" amount="100"/>
</event>
```

`type="clear"` targeting the player's `sensors` removes a status effect from your own
sensors system. The same tag appears on [[event-boss-destroyed]]. What sets that status in
the first place is not stated in any file examined here.

## Blue Options
None.

## Rewards & Risks
- **`autoReward level="HIGH"` `standard`** — scrap with resources, at the game's top tier.
  This is the payout for surviving a Flagship phase ([[source-events-boss]]).
- No risk defined on the event itself.

## Strategy Notes
- Each survived phase pays a HIGH standard reward, which is the resource budget you carry
  into the next phase alongside the three
  [[event-repair-station-in-last-stand]] beacons. *(Reading of the reward tag, not a
  sourced strategy claim.)*

## Related
- [[event-boss-text-1]], [[event-boss-text-2]], [[event-boss-text-3]] — the phases this
  event sits between
- [[event-boss-automated]] — the other mid-fight interrupt
- [[event-boss-destroyed]] — the ending, which carries the same `status` clear
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]]

## Open Questions
- [ ] What applies the sensors status that this event clears.
- [ ] Whether the HIGH reward is granted after every phase or only some.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
