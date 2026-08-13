---
id: event-lanius-ship-salvager
type: event
event_name: LANIUS_SOLO_SALVAGE
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, neutral, blue-option, optional-fight, repeatable, advanced-edition]
---

# Lanius ship salvager — `LANIUS_SOLO_SALVAGE`

## Summary
A lone Lanius ship is picking over wreckage and has not noticed you, or does not care. You
can jump it, ignore it, or — with a Lanius crew member — ask for a cut of the salvage. It is
one of the few `NEUTRAL_LANIUS` events **not marked `unique`**, so it can recur within a
single Abandoned sector.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `NEUTRAL_LANIUS`, allocated `min="5" max="6"` beacons per sector
  ([[source-sector-data-xml]]). Thirteen members, none duplicated → **1/13** of any neutral
  beacon *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- **No `unique` attribute** → it can be drawn more than once
  ([[source-dlcevents-anaerobic]]; [[source-fandom-lanius-ship-salvager]] renders
  `unique=false`).
- `<ship load="LANIUS_SHIP" hostile="false"/>` at the top level — a ship is present but not
  hostile; long-range scanners show a ship (`LRSmap=ship`).

> **AE-only.** AE data file, AE sector, no `OVERRIDE_NEUTRAL_LANIUS` in
> `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]).

## Text
`[varies: textList LANIUS_SOLO_SALVAGE_TEXT]` — the list has **10** `<text>` entries drawn
from **5** distinct strings, each appearing exactly twice
([[source-dlcevents-anaerobic]]). The doubling is uniform, so all five framings are equally
likely at **2/10 = 1/5** *assuming uniform selection across list entries*. All five are
transcribed on [[source-fandom-lanius-ship-salvager]] and live at
`text_LANIUS_SOLO_SALVAGE_TEXT_1` … `_5` in `raw/gamedata/text_events.xml`
([[source-text-events-xml]]). The framings: a civilian craft being stripped; a battlefield
of hulks with one Lanius ship isolated; a picked-clean debris ring; a Lanius ship docked on
a mineral-rich asteroid; a half-salvaged research station.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the ship. | — | "You move in and power up your weapons. Detecting the threat, they stop what they were doing and prepare for a fight." → the loaded `LANIUS_SHIP` flips hostile; default Lanius rewards. | 100% |
| 2 | Leave them alone. | — | "You ignore the ship and prepare to jump." Nothing happens. | 100% |
| 3 | **(Lanius Crew)** Request some scrap. | `req="anaerobic"` | Loads `LANIUS_SOLO_SALVAGE_LIST` — see below. | 100% |

### `LANIUS_SOLO_SALVAGE_LIST` (choice 3)
Three entries, none duplicated → **1/3 each** *assuming uniform selection across list
entries* ([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| "Your crew hails their ship, wondering if they have any extra salvage. Their crew seems happy to share." | `autoReward level="MED">scrap_only` |
| "Your crewmember hails them, asking if they have any extra scrap. They state that they are extremely low and cannot spare any." | nothing |
| "They scoff at your crewmember's request and utter something that was translated as, 'Get your own, lazy solder.'" | opens a further choice — see below |

The third branch offers:

| # | Choice | Outcome |
|---|--------|---------|
| 3c-i | Attack the ship. | `<ship hostile="true"/>` — the same `LANIUS_SHIP` fight as choice 1 |
| 3c-ii | Leave. | "You ignore their derisive tone and prepare to jump." Nothing happens. |

Note that the insult branch never *forces* a fight — declining is always available. The blue
option therefore carries **no risk**: worst case is a wasted screen.

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — a free 1/3 roll on `MED scrap_only` with no
  downside. Unlike [[event-lanius-lone-ship]]'s blue option this one is not a guaranteed
  payout, but it also cannot cost you anything ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- Choice 1 (or the optional fight in 3c): `LANIUS_SHIP` — surrender `chance="0.2"`, escape
  `chance="0.2"`, "default Lanius rewards"; full tables on [[event-lanius-fight]].
- Choice 3: 1/3 `MED scrap_only`, 2/3 nothing, no risk.
- No resource cost on any branch.
- `MED` is the game's own `autoReward` level; no source read here converts it to a number.

## Strategy Notes
- *Opinion, derived from the tables:* with Lanius crew, always take choice 3 first — it is
  free, and the fight is still available afterwards through the insult branch (though only
  in 1/3 of rolls).
- Without Lanius crew this is a straight "do I want a Lanius fight?" question. The default
  Lanius reward table is decent but the `LANIUS_SHIP` block has a 20% escape clause, so a
  slow kill can end with nothing.
- Because the event is not `unique`, seeing it once does not remove it from the pool.

> ⚠️ **CONTRADICTION (minor, wording):** Fandom renders choice 1's outcome as *"they stop
> what they **are** doing"* ([[source-fandom-lanius-ship-salvager]]) while the game files
> read *"they stop what they **were** doing"* ([[source-text-events-xml]], per
> `raw/gamedata/text_events.xml`). Fandom also transcribes the third intro variant with
> "striped" where the files read "stripped". Trusting the game files — reliability `high`
> vs `medium`. Both look like transcription slips rather than version differences.

## Related
- [[event-lanius-lone-ship]] — the sibling `NEUTRAL_LANIUS` event whose Lanius blue option
  buys a store instead of scrap
- [[event-lanius-fight]] — documents the shared `LANIUS_SHIP` enemy block
- [[event-lanius-ship-in-rich-debris-field]] — the other salvage-framed Lanius beacon
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-blue-options]]

## Open Questions
- [ ] Numeric scrap value behind `MED scrap_only`.
- [ ] Whether the doubled `textList` block is deliberate weighting or a copy-paste artefact
      — the effect is neutral either way, since every string is doubled.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-ship-salvager]] (per raw/wiki/lanius-ship-salvager.md)
