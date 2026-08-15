---
id: event-settlement-mercenary-work
type: event
event_name: MERCENARY_WORK_START
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-settlement-mercenary-work]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [quest-start, unique, pirate-fight, store-chance, weapon-reward]
---

# Settlement mercenary work — `MERCENARY_WORK_START`

## Summary
A quest-start beacon that offers you one of **two different jobs**, picked at random: rescue
a space dock from a Rebel scout (a quest marker that ends in a **free store plus hull
repairs**), or beat up some amateur pirates on the spot for a **weapon**. Which job you are
offered is decided before you choose anything, so this is really two events sharing a
front door.

## Trigger & Where It Appears
- Event lists: `QUESTS`, `QUESTS_ENGI`, `QUESTS_PIRATE`, `QUESTS_ROCK`, and
  `OVERRIDE_QUESTS` under AE ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sectors and their quest-slot allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `QUESTS min=1 max=1`, [[sector-civilian-sector]] `QUESTS 0–2`,
  [[sector-engi-controlled-sector]] / [[sector-engi-homeworlds]] `QUESTS_ENGI 1–1`,
  [[sector-pirate-controlled-sector]] `QUESTS_PIRATE 0–1`,
  [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] `QUESTS_ROCK 0–1`
- `unique="true"` — at most once per run ([[source-events-xml]])
- Beacon: no ship staged on arrival; [[source-fandom-settlement-mercenary-work]] marks
  `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `QUESTS` is allocated in `STANDARD_SPACE` at `min=1 max=1`, i.e.
>   [[sector-federation-space]] always places a quest beacon ([[source-sector-data-xml]]).
> - Fandom: lists six sectors and omits Federation space
>   ([[source-fandom-settlement-mercenary-work]]).
>
> Trusting the game files (`high` vs `medium`). Consistent with the same omission on other
> `QUESTS`-list events; it reads as a wiki location-template convention, not a version
> difference.

## Text
> You are immediately contacted by a settlement, "Hello, travelers. Your ship seems to be
> outfitted for combat...care to take up a bit of mercenary work?"

(`event_MERCENARY_WORK_START_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Listen to their offer. | — | Loads `eventList MERCENARY_WORK_LIST` — 2 entries, below. | see below |
| 2 | Decline. | — | Nothing happens. | 100% |

### `eventList MERCENARY_WORK_LIST` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
each job is offered **1/2** of the time.

**Entry 1 — the space dock**
> "A space dock is under assault from the Rebels. Although the dock is... technically...
> illegal within their laws, it's very important for our trade. We'll pay you in fuel and
> scrap if you promise to save them."

| Choice | Outcome |
|---|---|
| Agree to rescue the store. | *"They transmit the space dock's coordinates."* → `<quest event="QUEST_STORE_RESCUE"/>` — a quest marker is added. See [[event-quest-store-rescue]]. |
| Decline. | *"They regretfully accept your decision."* → nothing. |

Note the offer promises payment "in fuel and scrap" but the `<quest>` tag is the **only**
effect on this branch — nothing is paid up front ([[source-events-xml]]).

**Entry 2 — the amateur pirates**
> "Some of our friends have taken to piracy in the recent chaos of the war. We'd like you
> to "convince" them of their poor decision by severely damaging their ship. We'll pay you
> well as long as you don't kill them all."

| Choice | Outcome |
|---|---|
| Accept. | *"Just be sure not to blow them up!"* → `<ship load="SQUAT_PIRATE_MERCENARY" hostile="true"/>` |
| Decline. | *"Fine. I don't know what we'll do about them though..."* → nothing. |

### Fighting `SQUAT_PIRATE_MERCENARY`
([[source-events-ships]])

- `<surrender min="3" max="4">` — **no `chance` attribute**, so the offer is not gated by a
  roll ([[concept-surrender-offers]] covers what `chance` means when present).
  [[source-fandom-settlement-mercenary-work]] renders it as surrendering at 30–40% hull
  with no probability attached.
- **No `<escape>` element** — the ship never flees. Fandom's Trivia states the same.
- Surrender text: *"You win! We're not cut out for this!"*
  - **Let them live and then return to the settlement** → `<ship hostile="false"/>`,
    *"…they returned to us before you did. I don't think we'll need this anymore."* →
    `autoReward level="MED"` **`weapon`**.
  - **Forget your promise, they die!** → the fight continues.
- `destroyed` / `deadCrew` → *"With all of the would-be pirates dead, you think it best not
  to return to the settlement..."* → `autoReward level="LOW"` `standard`.

**Killing them is the worse outcome by the game's own numbers**: `LOW standard` instead of
`MED` plus a weapon. The settlement's "don't kill them all" is a real mechanical condition.

## Blue Options
None. No choice in this event or its sub-events carries a `req` ([[source-events-xml]]).

## Rewards & Risks
- Entry 1 pays nothing immediately; the payoff is at [[event-quest-store-rescue]]
  (`MED scrap_only`, 5 hull repairs, and a **store**).
- Entry 2 pays `MED weapon` if you let them surrender, `LOW standard` if you finish them.
- Risk: an ordinary pirate-hull fight you cannot escape from and that will not run away
  from you.

## Strategy Notes
- On entry 2, accept the surrender. Giving up a `MED weapon` for a `LOW standard` is a
  straight downgrade, and the ship has no escape branch to punish you for waiting.
  *(Derived from the reward tags above; no source states the comparison.)*
- Entry 1's store is the more valuable of the two jobs on a run that needs to shop, but it
  costs jumps to reach the marker.

## Related
- [[chain-settlement-mercenary-work]] — the full quest line this belongs to
- [[event-quest-store-rescue]] — the destination of entry 1's quest marker
- [[event-quest-store]] — an unreferenced hidden-space-dock store event with the same premise
- [[event-the-mercenary]] — the other "mercenary" beacon, unrelated mechanically
- [[entity-pirates]]

## Open Questions
- [ ] Does a `<surrender>` with no `chance` attribute always fire, or default to some
      internal value? Every page that hits one needs the same answer.
- [ ] Confirm `eventList` selection is uniform — the 1/2 split depends on it.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-settlement-mercenary-work]] (per raw/wiki/settlement-mercenary-work.md)
