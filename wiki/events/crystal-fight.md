---
id: event-crystal-fight
type: event
event_name: CRYSTAL_FIGHT
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 5
tags: [combat, surrender, crew-reward, no-choices]
---

# Crystal fight — `CRYSTAL_FIGHT`

## Summary
The backbone of [[sector-hidden-crystal-worlds]]'s hostile pool: a forced fight against a
generic Crystal warship. It has no choices of its own — everything interesting happens in
the `CRYSTAL_SHIP` **surrender** branch, which is the one place in the game where a
defeated enemy can offer you a **Crystal crew member**.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: `CRYSTAL_FIGHT` occupies **3 of the 7** slots in the `HOSTILE_CRYSTAL` event list
  — the most heavily weighted entry — and the sector allocates that list `min=6 max=10`
  times ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — expect several per sector
- Beacon: shows a **ship** on Long-Range Scanners ([[source-fandom-crystal-fight]])

## Text
The intro **varies** — `<text load="CRYSTAL_FIGHT"/>` draws from a 14-slot list built from
7 distinct strings, each listed twice ([[source-events-xml]]). All seven are transcribed
on [[source-fandom-crystal-fight]] and appear verbatim as `text_CRYSTAL_FIGHT_1`–`_7` in
[[source-text-events-xml]]; they range from "you scanned a merchant and its escort
objected" to a warrior demanding a duel to a translator failing on "aliens / allowed /
no".

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<ship load="CRYSTAL_SHIP" hostile="true"/>` → immediate combat, **default rewards** | 100% |

### Sub-outcome: the ship surrenders
`CRYSTAL_SHIP` carries `<surrender chance="0.6" min="3" max="4">` — a **40%** surrender
offer once its hull is low, since `chance` is the probability the ship *keeps fighting*
([[concept-surrender-offers]]) ([[source-events-xml]], per raw/gamedata/events_ships.xml). The offer
text itself varies across 7 strings (`CRYSTAL_SHIP_SURRENDER` text list). Accepting loads
the `CRYSTAL_SHIP_SURRENDER` **event** list — 7 entries:

| Entry | Result |
|---|---|
| 1, 2 | Ship leaves. Nothing gained. |
| 3, 4, 5, 6 | Ship leaves + `autoReward level="RANDOM"` **stuff** (resources with some scrap). |
| 7 | A young Crystal soldier asks to join. **Yes** → `crewMember amount="1" class="crystal"` — a **Crystal crew member**. **No** → `autoReward level="RANDOM"` stuff. |

So 2 of the 7 surrender entries give nothing, 4 give random stuff, and 1 offers crew.
([[source-events-xml]], [[source-fandom-crystal-fight]])

Refusing the surrender (`Ignore them.`) simply continues the fight.

## Blue Options
- None on the event. Note that this is *the* event that can hand you the Crystal crew
  member which unlocks blue options elsewhere in the sector —
  [[event-crystalline-cache]] and [[event-crystal-chat]] both gate on `req="crystal"`.

## Rewards & Risks
- **Reward:** default rewards on a kill; or, on surrender, a 4-in-7 shot at random stuff
  and a 1-in-7 shot at a **Crystal crew member**.
- **Risk:** a full warship fight, repeated up to several times per sector, at a strength
  scaled to the Rock Homeworlds sector number ([[source-fandom-ancient-device]]).

## Strategy Notes
- The Fandom page notes that "the surrender options are unique to this event only"
  ([[source-fandom-crystal-fight]]) — no other Crystal encounter offers the crew branch.
  If you want Crystal crew and the store roll has not obliged, leaving a `CRYSTAL_FIGHT`
  ship alive at low hull is the play.
- The same page lists an open verification request of its own: whether the surrender
  reward is shown *before* you accept the offer. Unresolved.

> ⚠️ **CONTRADICTION:** surrender-offer chance.
> - Game files: `<surrender chance="0.6" min="3" max="4">` on `CRYSTAL_SHIP` — 60%
>   ([[source-events-xml]], per raw/gamedata/events_ships.xml).
> - Fandom: its `SurrenderEscape` footnote for `CRYSTAL_SHIP` passes **40**
>   ([[source-fandom-crystal-fight]]), where the same template's parameter carries 50 for
>   `CRYSTAL_HUNTER` (game file `chance="0.5"`) — so the parameter does mean the surrender
>   percentage, and 40 ≠ 60.
> ~~Trusting the game files (`high` vs `medium`), i.e. **60%**. Not obviously a vanilla/AE
> difference — `chance="0.5"` on `CRYSTAL_HUNTER` matches Fandom exactly in the same file,
> so this looks like a stale or mistyped wiki parameter rather than a version drift.~~
>
> **RESOLVED (lint, 2026-08-13) — and the resolution goes to Fandom, not to us.**
> [[concept-surrender-offers]] establishes that `chance` is the probability the ship **keeps
> fighting**, so `chance="0.6"` *is* a 40% surrender offer and Fandom's 40 was right all
> along. The reasoning above even contains the key: `CRYSTAL_HUNTER` at `chance="0.5"`
> "matches Fandom exactly" precisely because 0.5 is the one value that reads the same under
> both conventions. The **60%** stated here was wrong and is corrected above.

## Related
- [[sector-hidden-crystal-worlds]]
- [[entity-crystal-men]]
- [[event-crystal-fight-with-surrender-offer-hull-repairs]] — `CRYSTAL_CONVOY`, the repair
  surrender
- [[event-crystal-fight-with-surrender-offer-human-crew]] — `CRYSTAL_HUNTER`, the human
  crew surrender
- [[event-store-crystal]] — the other reliable source of Crystal crew
- [[concept-surrender-offers]]

## Open Questions
- [x] ~~Resolve the 60% vs 40% surrender chance above.~~ **40%** — [[concept-surrender-offers]].
- [ ] What "default rewards" resolves to numerically for `CRYSTAL_SHIP`.
- [ ] Is the surrender reward visible before accepting? (raised by
      [[source-fandom-crystal-fight]] itself)

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-fight]] (per raw/wiki/crystal-fight.md)
