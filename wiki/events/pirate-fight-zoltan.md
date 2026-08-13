---
id: event-pirate-fight-zoltan
type: event
event_name: ZOLTAN_PIRATE
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [filler-fight, pirate, default-rewards, varies-text, weighted-textlist]
---

# Pirate fight (Zoltan) — `ZOLTAN_PIRATE`

## Summary
Filler combat: a pirate ship in Zoltan space, no choices, default rewards. Its only
distinguishing feature is its text list, which is **weighted** — three of its seven intro
strings appear twice, and the community wiki records only five of the seven.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-pirate-fight-zoltan]]).
- Reached via `HOSTILE_ZOLTAN` (vanilla) / `OVERRIDE_HOSTILE_ZOLTAN` (AE), which the
  Zoltan sectors allocate `min=6 max=8` beacons to — the largest single allocation in the
  sector ([[source-sector-data-xml]]).
- **Not** `unique="true"` — it can repeat within a sector.

## Text
`[varies: textList ZOLTAN_PIRATE]` — the intro is drawn from a text list, so no single
string can be quoted as *the* text.

The list has **ten entries referencing seven distinct strings**
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml):

```
text_ZOLTAN_PIRATE_1, _2, _3, _4, _5,
text_ZOLTAN_PIRATE_1, _6, _3, _7, _5
```

So strings **1, 3 and 5 are twice as likely** as 2, 4, 6 and 7. The file carries the
developer note `<!-- Add more instead of repeating ! -->` immediately above the repeated
block, which explains the duplication as padding rather than intentional weighting.

The seven strings ([[source-text-events-xml]]):

1. *"Emergency, all ships in range, we are under attack!" The frequency matches a nearby Zoltan ship; you move in on their pursuer. They take your intervention as a cue to jump away. Cowards.*
2. *You jump just in time to witness a Zoltan ship's FTL drive overload. In his final moments their captain implores you not to get involved, but it's too late - their attacker is already upon you!*
3. *Despite their precautions, pirates have begun to harass the local Zoltan settlements across this sector. One such pirate spots your ship and moves in to attack.*
4. *A ship with pirate markings demands your surrender. These are sad times when even Zoltan space is beset by pirates. You doubt these fools will be missed.*
5. *You spot a pirate ship looting a small Zoltan cruiser. They spot you and move in to attack before your FTL drive has a chance to recharge.*
6. *You jump just in time to witness a Zoltan ship's FTL drive overload. In their final moments they implore you not to get involved, but it's too late - their attacker is already upon you!*
7. *A ship with pirate markings demand that you surrender. These are sad times when even Zoltan space is beset by pirates. You doubt these fools will be missed.*

Strings 2/6 and 4/7 are near-identical rewrites of each other.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="PIRATE" hostile="true"/>` — immediate fight with a pirate ship ([[entity-pirates]]), **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Default rewards for a pirate ship at the current sector depth. Nothing event-specific
  is granted or lost.
- Risk is entirely the fight itself; no environment hazard, boarders, or scripted system
  damage.

## Strategy Notes
- Nothing to decide — this is a beacon you either fight or avoid on the map.
- Pirate ships in AE can carry a wide loadout range, so this is one of the more variable
  filler fights in the sector.

> ⚠️ **CONTRADICTION:** how many intro variants exist.
> - Game files: **seven** distinct strings (`text_ZOLTAN_PIRATE_1` … `_7`), across a
>   ten-entry list ([[source-events-zoltan]], [[source-text-events-xml]]).
> - Fandom: lists **five** variants ([[source-fandom-pirate-fight-zoltan]]).
>
> Fandom's five correspond to the *second half* of the list — strings 1, 6, 3, 7, 5 — and
> omit strings 2 and 4, which are the near-duplicate rewrites of 6 and 7. Trusting the
> game files (`high` vs `medium`). This looks like an incomplete wiki transcription
> rather than a vanilla/AE difference, but that is unconfirmed.

> ⚠️ **CONTRADICTION (version):** which event list supplies this event.
> - `HOSTILE_ZOLTAN` in raw/gamedata/events_zoltan.xml contains 7 entries.
> - `OVERRIDE_HOSTILE_ZOLTAN` in raw/gamedata/dlcEventsOverwrite.xml contains the same 5
>   Zoltan events plus `REBEL`, `REBEL_AUTO` and an added `REBEL_PULSAR` — 8 entries —
>   and replaces `HOSTILE_ZOLTAN` when Advanced Edition content is enabled
>   ([[source-dlceventsoverwrite]], per raw/gamedata/dlcEventsOverwrite.xml).
>
> This is a genuine **vanilla-vs-AE difference, not an error**: `ZOLTAN_PIRATE` keeps the
> same absolute weight but its share of the hostile pool falls from 1-in-7 to 1-in-8 in AE.

## Related
- [[event-zoltan-fight]] — the other repeatable filler fight in the same pool
- [[event-mantis-fight-zoltan]], [[event-engi-fight]],
  [[event-zoltan-fight-in-asteroid-field]] — the unique members of the same pool
- [[entity-pirates]] — the opponent

## Open Questions
- [ ] Confirm textList selection is uniform over the ten entries (which is what makes
      1/3/5 twice as likely).
- [ ] Which `PIRATE` ship blueprints can spawn here at each sector depth.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-fight-zoltan]] (per raw/wiki/pirate-fight-zoltan.md)
