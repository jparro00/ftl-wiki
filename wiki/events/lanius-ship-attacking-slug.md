---
id: event-lanius-ship-attacking-slug
type: event
event_name: LANIUS_SLUG_DISTRESS
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, slug, distress, combat, unique, advanced-edition]
---

# Lanius ship attacking Slug — `LANIUS_SLUG_DISTRESS`

## Summary
The Slug version of the Lanius rescue-or-abandon distress beacon, mechanically identical to
[[event-lanius-ship-attacking-rock]]: fight a no-surrender, no-escape Lanius ship for
`MED standard`, then a coin flip on whether the Slugs pay up. The only differences are the
prose (the Slugs are characteristically ungrateful) and that choice 1 has **no outcome text
at all** — picking it drops you straight into combat.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min="1" max="2"` beacons per sector
  ([[source-sector-data-xml]]). Twelve members, none duplicated → **1/12** of any Lanius
  distress beacon *assuming uniform selection across list entries*
  ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- `<distressBeacon/>` in the event body flags it on the map
  ([[source-fandom-lanius-ship-attacking-slug]] renders `distress=true`, `LRSmap=noship`).
- Commented *"Chris's"* in the source list — a dev attribution note.

> **AE-only.** AE data file, AE sector, no `OVERRIDE_DISTRESS_BEACON_LANIUS` in
> `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]).

## Text
> The distress signal from this system is coming from a Slug vessel under attack by the
> Lanius! The Slugs beg for assistance as the Lanius tear into their hull plating.

(`event_LANIUS_SLUG_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Lanius ship. | — | **No outcome text** — the choice's `<event>` contains only `<ship load="LANIUS_SLUG_DISTRESS_SHIP" hostile="true"/>`. Straight into combat. | 100% |
| 2 | Leave the Slugs to their fate. | — | "You leave the Lanius ship alone, and prepare to jump to the next beacon." Nothing happens. | 100% |

Choice 1's silent transition is a real difference from the Rock and Mantis siblings, both of
which print a line first ([[source-dlcevents-anaerobic]]); Fandom reflects it by showing no
italicised text under that choice ([[source-fandom-lanius-ship-attacking-slug]]).

### The `LANIUS_SLUG_DISTRESS_SHIP` enemy
`auto_blueprint="SHIPS_LANIUS"`. Declares only `destroyed` and `deadCrew` — **no
`<surrender>`, no `<escape>`** ([[source-dlcevents-anaerobic]];
[[source-fandom-lanius-ship-attacking-slug]] shows `SurrenderEscape(alt)|no`).

| Outcome | Text | Payout |
|---|---|---|
| Destroyed | "The ship explodes, leaving behind a collection of useful scrap material." | `autoReward level="MED">standard`, then a hidden *"Contact the Slugs."* choice → `LANIUS_SLUG_DISTRESS_END` |
| Dead crew | "There are no more life-signs remaining on the ship. You strip it of useful materials." | identical |

### `LANIUS_SLUG_DISTRESS_END`
Two entries, neither duplicated → **1/2 each** *assuming uniform selection across list
entries* ([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| "The Slugs, taking advantage of the firefight, have fled the system. So much for gratitude." | nothing |
| "The Slugs reluctantly thank you for your help, protest they had the whole situation under control, attempt to make you pay for them helping you, and an hour later, finally relent and give you some supplies." | `autoReward level="MED">standard` |

## Blue Options
None — no crew, system or augment gate anywhere in the event
([[source-dlcevents-anaerobic]]). Notably there is no Slug-crew option, despite the Slug
framing.

## Rewards & Risks
- Winning: `MED standard` guaranteed plus a 1/2 chance of a second `MED standard`.
- Risk: a Lanius warship that cannot surrender and cannot escape. Committing means fighting
  to a conclusion.
- Leaving costs nothing.
- `MED` is the game's own `autoReward` level; no source read here converts it to a number.

## Strategy Notes
- Identical expected value to [[event-lanius-ship-attacking-rock]]; treat the two the same
  way. Take it with a healthy ship, skip it when hull is low, since there is no escape roll
  to bail you out.
- Boarding gains nothing over shooting — `destroyed` and `deadCrew` pay the same.
- *Opinion:* the "Slugs are ungrateful" flavour is not a hint. The 1/2 split is structural,
  and the Rock version has exactly the same odds with warmer prose.

## Related
- [[event-lanius-ship-attacking-rock]] — the Rock twin, same structure and odds
- [[event-lanius-ship-attacking-mantis]] — the Mantis sibling
- [[event-lanius-fight]] — documents the ordinary `LANIUS_SHIP` block, which *does* have
  surrender and escape
- [[sector-abandoned-sector]], [[entity-lanius]], [[entity-slugs]]

## Open Questions
- [ ] Numeric scrap values behind `MED standard`.
- [ ] Why choice 1 has no outcome text while its Rock and Mantis twins do — deliberate or
      an authoring oversight.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-ship-attacking-slug]] (per raw/wiki/lanius-ship-attacking-slug.md)
