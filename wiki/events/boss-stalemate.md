---
id: event-boss-stalemate
type: event
event_name: BOSS_STALEMATE
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, engine-event, no-choice, text-only, stalemate, no-fandom-page]
---

# Stalemate — the ship jumps away — `BOSS_STALEMATE`

## Summary
A single line of prose the engine appears to call when a fight ends without a winner and
the enemy FTLs out. No choices, no reward, no ship — one `<text>` tag and nothing else. It
belongs to the small block of hard-coded one-liners `events.xml` keeps for engine-driven
situations rather than beacon encounters.

## Trigger & Where It Appears
**Not in any sector event list.** `BOSS_STALEMATE` appears exactly once in the whole of
`raw/gamedata/` — its own definition in `events.xml`. No `<eventList>`,
`<sectorDescription>` or `load=` reference points at it ([[source-events-xml]],
[[source-sector-data-xml]]).

How it is reached is an **inference, not a sourced fact**:

- It sits in a contiguous block of one-line, choice-free events that the engine plainly
  invokes by hard-coded name: `STALEMATE_SURRENDER` immediately above it, then
  `CREW_STUCK`, `FUEL_ESCAPE_SUN`, `FUEL_ESCAPE_STORM`, `FUEL_ESCAPE_ASTEROIDS`,
  `AUGMENT_FULL` and `EQUIP_FULL` ([[source-events-xml]]). None of those are in any list
  either, and several are unmistakably UI messages.
- Its immediate neighbour `STALEMATE_SURRENDER` describes the *other* half of the same
  situation: *"The ship suddenly disables their weapons. There's no explanation and they
  don't respond to hails. It seems during the battle they lost some fuel cells from their
  storage."* → `item_modify` +2 fuel, `<ship hostile="false"/>`. Two named
  `*STALEMATE*` events, one where the enemy gives up and one where it leaves, reads as a
  matched pair for an unwinnable-fight condition.
- The `BOSS_` prefix is the one thing that does **not** fit that reading. The Flagship
  sequence lives in `events_boss.xml` ([[source-events-boss]]); this event does not, and no
  boss event references it. Whether the prefix means "boss fight" or is a leftover label is
  not established by any source here.

Conclusion recorded with the uncertainty: this reads as **engine-called text for an enemy
breaking off an unresolvable fight**, but no source in `raw/` states the trigger.

- **No Fandom page.** Nothing in the 293 pages under `raw/wiki/` mentions this event, its
  id, or its prose — so there is no community documentation to cross-check against.

## Text
> The ship jumped away without warning. You prepare to pursue.

(`event_BOSS_STALEMATE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | The text is displayed. The event body contains a single `<text>` tag — no `<choice>`, no `<ship>`, no `<autoReward>`, no `<status>`. | 100% |

## Blue Options
None.

## Rewards & Risks
None. The event has no mechanical payload whatsoever.

## Version Differences
Base-`events.xml`, no DLC-marked tags — identical in both editions
([[source-events-xml]]).

## Related
- [[event-boss-escaped]] — the Flagship-phase equivalent, in `events_boss.xml`, which *does*
  pay out
- [[event-crew-stuck]] — the neighbouring engine one-liner in the same block
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]] — the AE additions to the same
  family of hard-coded escape lines
- [[event-federation-base]] — another orphan text-only event, documented the same way

## Open Questions
- [ ] What condition actually fires this event. "Stalemate" is read from the id and the
      neighbouring `STALEMATE_SURRENDER`, not from any source.
- [ ] Why the `BOSS_` prefix, given the event is not in `events_boss.xml` and the Flagship
      sequence never references it.
- [ ] Does `STALEMATE_SURRENDER` share the same trigger as an alternative outcome, or is it
      a separate condition entirely? Nothing in the files links them.
- [ ] Is there in-game footage or a community report of this line appearing? No Fandom page
      exists.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml` — confirming it is in no list)
- [[source-events-boss]] (per `raw/gamedata/events_boss.xml` — where the Flagship sequence
  actually lives, and where this event is *not*)
