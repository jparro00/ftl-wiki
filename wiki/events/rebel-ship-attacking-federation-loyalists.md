---
id: event-rebel-ship-attacking-federation-loyalists
type: event
event_name: REBEL_VS_FEDERATION
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: true
blue_options: [[[item-nano-med-bot-dispersal]], [[item-teleporter]], [[item-healing-burst]]]
chain: [[[chain-hidden-federation-base]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, unique, rebel-fight, crew-reward, blue-option, quest-start, ae-vs-vanilla, bugged]
---

# Rebel ship attacking Federation loyalists — `REBEL_VS_FEDERATION`

## Summary
A Rebel scout is killing a Federation transport. Saving it opens a three-outcome rescue
table that can hand you a **free crew member** or a **quest marker to the hidden Federation
base**. It is one of the better distress-list encounters in the game, and Advanced Edition
adds both a fourth blue option and skill levels on the crew members you rescue.

## Trigger & Where It Appears
- Event lists: `DISTRESS_BEACON`, `DISTRESS_BEACON_REBEL`, `DISTRESS_BEACON_ROCK`
  ([[source-newevents]])
- Sector allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `DISTRESS_BEACON 1–2`, [[sector-civilian-sector]] `1–2`,
  [[sector-uncharted-nebula]] (`NEBULA_SECTOR`) `1–3`,
  [[sector-rebel-controlled-sector]] / [[sector-rebel-stronghold]] `DISTRESS_BEACON_REBEL 1–2`,
  [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] `DISTRESS_BEACON_ROCK 1–2`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged on arrival; `<img back="BACKGROUND" planet="PLANET_POPULATED"/>`.
  [[source-fandom-rebel-ship-attacking-federation-loyalists]] marks `LRSmap=noship`.

**It is not actually flagged as a distress beacon.** The definition contains **no
`<distressBeacon/>` element** ([[source-events-xml]]), despite sitting in the distress lists.
[[source-fandom-rebel-ship-attacking-federation-loyalists]] records this as a bug in exactly
those terms. Both sources agree.

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `DISTRESS_BEACON` is allocated `min=1 max=2` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists seven sectors and omits Federation space
>   ([[source-fandom-rebel-ship-attacking-federation-loyalists]]).
>
> Trusting the game files (`high` vs `medium`) — same omission pattern as other
> `DISTRESS_BEACON` events.

## Text
The intro **varies**: `<text load="REBEL_VS_FEDERATION"/>` draws from a 3-entry `textList`
([[source-events-xml]], [[source-text-events-xml]]). Example:

> Upon arriving at this beacon, you detect a distress call. Local scans reveal that a
> Federation transport is under attack from a Rebel scout!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Aid the Federation ship. | — | *"You power up your weapons and engage the Rebel ship."* → `<ship load="REBEL_VS_FEDERATION" hostile="true"/>`. Win → rescue table, below. | 100% |
| 2 | Use this chance to escape. | — | *"The Rebel's preoccupation with the Federation ship allows you to slip away undetected. However you can't help but feel you should have helped them."* → nothing. | 100% |

### The ship — `REBEL_VS_FEDERATION`
`auto_blueprint="SHIPS_REBEL"` ([[source-events-ships]]). **No `<surrender>` and no
`<escape>`** — Fandom states the same. Both win conditions pay `autoReward level="MED"`
`standard` and then offer a hidden "Contact the Federation ship" choice into the rescue
table:

| Result | Text |
|---|---|
| `destroyed` | *"With the ship destroyed, you quickly collect useful resources."* |
| `deadCrew` | *"With the crew of the Rebel ship dead, you salvage what you can."* |

Unusually, boarding earns no bonus over destroying — both are `MED standard`.

### The rescue table — `eventList REBEL_VS_FEDERATION_SAVED_LIST` (3 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
**1/3** each:

| Entry | Text | Effect |
|---|---|---|
| 1 | *"…I can inform you of a hidden Federation base nearby. Perhaps they can assist you more."* | `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` — see [[chain-hidden-federation-base]] |
| 2 | *"Their ship looks to be on the verge of destruction and life signs are fading quickly."* | a four-way choice, below |
| 3 | *"Thanks, we didn't think there would be Rebel ships all the way out here… Take some extra supplies as thanks for your aid."* | `autoReward level="MED"` `standard` |

**Entry 2 — the dying crew:**

| # | Choice | Requirement | Outcome |
|---|---|---|---|
| 2a | Quickly try to rescue the crew. | — | *"…The sole survivor offers to join your crew…"* → `<crewMember amount="1"/>` + `autoReward level="LOW"` `standard` |
| 2b | **(Nano Med-bot Dispersal)** Pump their ship with Nano Med-bots to aid in the rescue. | `req="NANO_MEDBAY"` | *"…The surviving shields operator offers to join your crew…"* → `<crewMember shields="1" amount="1"/>` *(the `shields="1"` skill is AE-only)* + `autoReward level="HIGH"` `fuel` |
| 2c | **(Teleporter)** Lock on to all remaining life signatures and beam them onto your ship. | `req="teleporter"` | *"…An infantryman offers to join your crew and the rest tell you of a hidden Federation base…"* → `<crewMember combat="1" amount="1"/>` *(AE-only skill)* + `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` + `autoReward level="MED"` `scrap_only` |
| 2d | **(Healing Burst)** Use a healing bomb to keep them alive. **AE only** | `req="BOMB_HEAL"` | **−1 missile**, then continue: *"Now that they're safe an engineer offers to join your crew…"* → `<crewMember engines="1" amount="1"/>` + `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` + `autoReward level="MED"` `scrap_only` |

**Version note (rule 10).** Four `<!--DLC!-->` markers sit inside this branch
([[source-events-xml]]): the whole of choice 2d, and the skill attributes on the crew
members from 2b, 2c and 2d. In vanilla, entry 2 offers **three** choices and the rescued
crew arrive **without** starting skill levels. Everything else on this page is common to
both editions — hence `version: both`.

## Blue Options
- **[[item-nano-med-bot-dispersal]]** (`req="NANO_MEDBAY"`) — upgrades the reward from
  `LOW standard` to `HIGH fuel`, and (AE) gives the crew member a shields skill point.
- **[[item-teleporter]]** (`req="teleporter"`) — the best non-AE option: crew member **plus**
  the hidden-base quest marker **plus** `MED scrap_only`.
- **[[item-healing-burst]]** (`req="BOMB_HEAL"`, AE only) — same package as the Teleporter
  route, for 1 missile, with an engines skill point instead of combat.

Every route on entry 2 gives a crew member; the blue options decide what comes *with* it.

## Rewards & Risks
- Guaranteed on a win: `MED standard`, then a 1/3 shot at each of a quest marker, a crew
  member (with extras), or another `MED standard`.
- Best case: Teleporter or Healing Burst on entry 2 — crew member, quest marker, and scrap
  in one.
- Risk: a Rebel-hull fight with no surrender and no escape branch. Choice 2 is a clean
  opt-out.

## Strategy Notes
- On entry 2, take Teleporter or Healing Burst over Nano Med-bots if you want the hidden
  base — those two are the only rescue choices that also place the marker. *(Read off the
  effect lists; no source ranks them.)*
- Since boarding pays no more than destroying here, there is no reason to risk crew on the
  Rebel ship.

## Related
- [[chain-hidden-federation-base]] — the quest line two of the three rescue entries can start
- [[event-rebel-fight]] — the ordinary Rebel encounter
- [[event-pirate-ship-attacking-civilian-distress]] — the pirate-side equivalent, with its own rescue table
- [[item-nano-med-bot-dispersal]], [[item-teleporter]], [[item-healing-burst]]
- [[concept-rebel-fleet-advance]], [[entity-federation]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — the 1/3 split depends on it.
- [ ] Is the missing `<distressBeacon/>` tag also absent in vanilla, or an AE regression?
- [ ] Fandom describes the Nano Med-bot reward as *"high 3–6 fuel and scrap"*; the XML says
      only `autoReward level="HIGH" fuel`. Are the numbers the tier definition or observed?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-rebel-ship-attacking-federation-loyalists]] (per raw/wiki/rebel-ship-attacking-federation-loyalists.md)
