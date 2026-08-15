---
id: event-quest-store-rescue
type: event
event_name: QUEST_STORE_RESCUE
sectors: []
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-settlement-mercenary-work]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-destination, store-chance, hull-repair, rebel-fight]
---

# Rescue the space dock — `QUEST_STORE_RESCUE`

## Summary
The quest marker where you save an illegal space dock from a Rebel scout. Winning the fight
is a triple payout: **`MED scrap_only`, 5 hull repairs, and a store**. The Rebel ship
neither surrenders nor escapes, so the only decision is whether to fight at all.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via `<quest event="QUEST_STORE_RESCUE"/>`,
  which fires from two places ([[source-events-xml]]):
  - `MERCENARY_WORK_LIST` entry 1 — "Agree to rescue the store" on
    [[event-settlement-mercenary-work]]
  - `STORE_RESCUE` — a separate quest-start event with the same premise
- Sectors depend on where the marker was placed, so the frontmatter list is deliberately
  empty.
- [[source-fandom-settlement-mercenary-work]] documents it as that page's "Quest marker"
  section and marks it `shipdetected=noship`.

## Text
> Once you arrive at the beacon you detect a Rebel scout assaulting a compound on a nearby
> desolate moon.

(`event_QUEST_STORE_RESCUE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Engage the Rebel and rescue the space dock. | — | `<ship load="SQUAT_STORE_RESCUE" hostile="true"/>` — no outcome text of its own; straight into the fight. | 100% |
| 2 | Avoid a fight. | — | *"After a time the ship powers down its weapons and jumps away. No life-signs are detected on the moon."* → nothing, and the dock is destroyed. | 100% |

### The ship — `SQUAT_STORE_RESCUE`
`auto_blueprint="SHIPS_REBEL"` ([[source-events-ships]]). It has **no `<surrender>` and no
`<escape>`** — [[source-fandom-settlement-mercenary-work]] states the same in its Trivia.

Both win conditions pay identically:

| Result | Text | Effect |
|---|---|---|
| `destroyed` | *"The outpost hails you, 'Thank you! I don't know what we did to anger the Rebels, but they were ready to kill us. I'll show you our goods and patch up your hull.'"* | `autoReward level="MED"` `scrap_only`, `<damage amount="-5"/>` (5 hull repaired), **`<store/>`** |
| `deadCrew` | same text | same three effects |

Killing the crew earns no bonus here, unlike most Rebel encounters.

## Blue Options
None. Neither this event nor the ship's outcomes carry a `req` ([[source-events-xml]],
[[source-events-ships]]).

## Rewards & Risks
- Win: `MED scrap_only` **+ 5 hull repaired + a store**. The repair and the store are the
  real value — a free store is worth more than the scrap on most runs.
- Risk: an ordinary Rebel-hull fight with no escape hatch. If it goes badly you cannot
  disengage, and the ship will not offer surrender.
- Choice 2 costs nothing but forfeits the whole payout.

## Strategy Notes
- Take the fight unless you are badly hurt — and note that winning *repairs* 5 hull, which
  partly offsets the damage you take getting there. *(Opinion; derived from the effect
  list.)*
- The store is the reason to route to this marker at all, so it is most valuable when you
  are carrying scrap you have had nowhere to spend.

## Related
- [[chain-settlement-mercenary-work]] — the full quest line this belongs to
- [[event-settlement-mercenary-work]] — one of the two quest starts that place this marker
- [[event-store-rescue]] — the other quest start, same premise
- [[event-quest-store]] — an unreferenced hidden-space-dock store event with a similar premise
- [[event-rebel-fight]] — the ordinary Rebel encounter
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What does the store's inventory roll from — the normal sector store pool, or a
      restricted one?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-settlement-mercenary-work]] (per raw/wiki/settlement-mercenary-work.md)
