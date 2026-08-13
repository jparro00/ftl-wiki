---
id: event-zoltan-great-eye
type: event
event_name: NEBULA_ZOLTAN_EYE
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, crew-risk, weapon-reward, gamble]
---

# Zoltan Great Eye — `NEBULA_ZOLTAN_EYE`

## Summary
A pure gamble in a Zoltan nebula. Looking into the "Great Eye" rolls one of four
outcomes ranging from a free [[item-healing-burst]] or high scrap down to losing a crew
member outright — and the crew loss is explicitly flagged non-cloneable. Walking away
costs nothing.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: nebula. The event carries `<environment type="nebula"/>`, so the fight
  outcome is fought under nebula rules (sensors down, no FTL drift).
  ([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml)
- Reached via the `NEBULA_ZOLTAN` event list, which the Zoltan sectors allocate
  `min=2 max=6` beacons to ([[source-sector-data-xml]]).
- `unique="true"` — it can occur at most once per sector.

## Text
> Inside this nebula you detect a rogue planet drifting through space, on its surface a
> huge monolith visible at this distance even to the naked eye. A Zoltan elder hails you
> from the planet. "Through luck or intent, you have discovered the Great Eye. Look into
> its depths and receive your just deserts."

(`event_NEBULA_ZOLTAN_EYE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Pull the ship in closer. | — | Loads `NEBULA_ZOLTAN_EYE_LIST` — one of the four results below. | unknown |
| 2 | Leave. | — | "Your mission is to save the Federation, not discover new wonders around the galaxy. You prepare to jump." Nothing happens. | 100% |

### `NEBULA_ZOLTAN_EYE_LIST` — the four results of choice 1

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"…an ancient alien voice speaks to you: 'Your mission has brought you great battles, and great losses. This will help ease the pain.' …medical equipment has appeared on the ship!"* | `<weapon name="BOMB_HEAL"/>` → you receive [[item-healing-burst]]. |
| 2 | *"You approach the planet and wait, but nothing happens. The Zoltan hail: 'And in the coming times, when the monolith speaks not with a man he has no future and must be left wanting.'"* | `<ship load="ZOLTAN_SHIP" hostile="true"/>` → fight a Zoltan ship ([[entity-zoltan]]), default rewards. |
| 3 | *"You approach the planet carefully… the next thing you know you have enough scrap to patch up your damage and more besides!"* | `autoReward level="HIGH"` `scrap_only`. |
| 4 | *"As you approach, a kaleidoscope of colors fills the viewscreen and one of your crew begins to age rapidly in reverse, eventually disappearing into nothingness…"* | `<removeCrew>` with `<clone>false</clone>` — **you lose a crew member and a [[item-clone-bay]] will not bring them back.** |

Each result appears exactly once in the list. **The game files state no percentages**, so
the split is recorded as `unknown` rather than assumed to be 25% each.
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml)

The Clone Bay failure has its own text: with a Clone Bay installed you get an extra
message confirming it cannot recover the crew member.
([[source-fandom-zoltan-great-eye]])

## Blue Options
None. No `req` attribute appears on either choice.

## Rewards & Risks
- **Best case:** [[item-healing-burst]] free, or `HIGH` scrap-only.
- **Middle:** a Zoltan ship fight with default rewards — survivable but the Zoltan Super
  Shield makes it a slog for missile- and drone-light builds.
- **Worst case:** permanent loss of one crew member, immune to cloning. On a small crew
  this can end a run's viability.

## Strategy Notes
- *Opinion:* three of four listed outcomes are neutral-to-good and one is severe. With a
  large crew and healthy hull the gamble is reasonable; with 2–3 crew the downside is
  disproportionate. No source here quantifies the odds, so this is a judgement call, not
  a computed EV.
- A Clone Bay does **not** insure you against the bad outcome — the game explicitly
  disables it here ([[source-events-zoltan]], [[source-fandom-zoltan-great-eye]]).

> ⚠️ **CONTRADICTION:** wording of the crew-loss text.
> - Game files: *"a kaleidoscope of **colors** fills the **viewscreen**"*
>   ([[source-text-events-xml]], per raw/gamedata/text_events.xml)
> - Fandom: *"a kaleidoscope of **colours** fills the **view-screen**"*
>   ([[source-fandom-zoltan-great-eye]])
>
> Trusting the game files (`high` vs `medium`). Most likely the wiki transcribes a
> localised or pre-AE string; not confirmed as a version difference.

## Related
- [[event-rock-fight-in-nebula]] — the other unique nebula event in the same
  `NEBULA_ZOLTAN` pool
- [[event-pirate-ships-in-plasma-storm]] — third unique member of that pool
- [[item-healing-burst]] — the good outcome
- [[item-clone-bay]] — explicitly disabled by the bad outcome
- [[entity-zoltan]] — the fight outcome

## Open Questions
- [ ] Actual weighting of the four `NEBULA_ZOLTAN_EYE_LIST` entries.
- [ ] Scrap value of `HIGH` `scrap_only` at each sector depth.
- [ ] Is the crew member removed random, or the lowest-value one?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-great-eye]] (per raw/wiki/zoltan-great-eye.md)
