---
id: event-mantis-named-thief-stash
type: event
event_name: MANTIS_NAMED_THIEF_STASH
sectors: [[[sector-mantis-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-mantis-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [quest-marker, weapon-reward, no-choice, mantis, orphan-by-list]
---

# KazaaakplethKilik's stash — `MANTIS_NAMED_THIEF_STASH`

## Summary
The payoff beacon of [[chain-mantis-cruiser-unlock]]: a hidden weapon cache you can open
with codes taken from the dying thief. Two lines of XML, no choices, no fight — arrive and
collect a weapon plus high scrap.

## Trigger & Where It Appears
- **Not in any sector event list.** `MANTIS_NAMED_THIEF_STASH` is never loaded by an
  `<eventList>`; it is reached only as a **quest marker** placed on your map by
  `<quest event="MANTIS_NAMED_THIEF_STASH"/>` ([[source-events-xml]], per
  `raw/gamedata/events_mantis.xml`).
- That quest tag fires from three different branches of
  [[event-legendary-thief-kazaaakplethkilik]]'s aftermath:
  1. "Listen to what he has to say." (Teleporter branch)
  2. "Dock and try to speak with him." (Sensors 3 branch)
  3. Accepting KazaaakplethKilik's offer after saving him with an Adv. Medbay or Adv.
     Clonebay — the full ship-unlock branch
- Sector: [[sector-mantis-homeworlds]], since that is where the parent beacon is
  guaranteed to spawn ([[source-sector-data-xml]]). Whether the marker can land in a
  *later* sector is not stated in any source read here.
- Long-range scanners show **no ship** at the marker
  ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Text
> You arrive at small asteroid field and discover the hidden cache among the debris. You
> input the codes given to you by KazaaakplethKilik and find a weapon inside.

(`event_MANTIS_NAMED_THIEF_STASH_text`, per [[source-text-events-xml]])

Note the prose mentions an asteroid field, but the event declares **no**
`<environment type="asteroid"/>` — there is no hazard here, only scenery
([[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | `<autoReward level="HIGH">weapon</autoReward>` — a weapon plus high scrap. | 100% |

Fandom describes the same result as *"a weapon with high scrap"*
([[source-fandom-legendary-thief-kazaaakplethkilik]]), which matches the file's
`HIGH`/`weapon` autoReward exactly. **Which** weapon is not specified by either source —
`autoReward` draws from the game's reward pools, not a named blueprint.

## Blue Options
None.

## Rewards & Risks
- Reward: one weapon plus HIGH-level scrap. No fight, no cost, no downside stated.
- Risk: only opportunity cost — reaching the marker consumes a jump and fuel, and the
  marker sits wherever the map placed it.

## Strategy Notes
- *(Opinion.)* Free weapon with no combat is among the better quest markers in the game;
  route to it if fuel allows. Note that all three ways of earning the marker are strictly
  better than the "strip the ship" / "let him die" branches, which give the same HIGH
  scrap tier **without** the marker — so on the teleporter/sensors branch there is no
  reason not to talk to him.

## Related
- [[event-legendary-thief-kazaaakplethkilik]] — the parent event that places this marker
- [[chain-mantis-cruiser-unlock]] — the chain this closes
- [[entity-mantis-cruiser]]
- [[sector-mantis-homeworlds]]

## Open Questions
- [ ] Which weapon pool `autoReward level="HIGH" weapon` draws from, and the scrap value.
- [ ] Can the quest marker be placed in a sector after the Mantis Homeworlds?
- [ ] Does the marker expire if you leave the sector without visiting it?

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-legendary-thief-kazaaakplethkilik]] (per raw/wiki/legendary-thief-kazaaakplethkilik.md)
