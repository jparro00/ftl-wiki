---
id: event-quest-crewdead
type: event
event_name: QUEST_CREWDEAD
sectors: []
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-capture-the-ship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-destination, boarding, weapon-reward, hull-damage-risk, fire-risk, breach-risk, ae-vs-vanilla]
---

# Capture the ship — the target — `QUEST_CREWDEAD`

## Summary
The quest marker placed by [[event-capture-the-ship]]. A pirate ship you must take
**intact**: kill the crew and you get `HIGH weapon`; blow it up and it detonates in your
face for the largest hull-damage result in the game, plus a system hit, a fire and a
breach. There is no choice and no way to disengage — arriving at the beacon starts the
fight.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via `<quest event="QUEST_CREWDEAD"/>` from
  the accept branch of `QUEST_CREWDEAD_CONTINUE` ([[source-events-xml]]) — its sole
  reference in the game files.
- Sectors depend on where [[event-capture-the-ship]] placed the marker, so the frontmatter
  list is deliberately empty.
- `unique="true"` ([[source-events-xml]]).
- [[source-fandom-capture-the-ship]] documents it as that page's "Quest Marker" section and
  marks it `shipdetected=ship` — long-range scanners *do* show a ship here.

## Text
> You find the ship that you were asked to capture intact. You're not sure why, but they
> stressed that it's of great importance that you kill the crew WITHOUT destroying the ship.

(`event_QUEST_CREWDEAD_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `<ship load="PIRATE_QUEST_CREWDEAD" hostile="true"/>` — an immediate, unavoidable fight. | 100% |

### The ship — `PIRATE_QUEST_CREWDEAD`
Defined in `events.xml` on an `auto_blueprint="SHIPS_PIRATE"` hull, with a dev note
*"TO DO - Start fires on the player ship"* ([[source-events-xml]]). It has **no
`<surrender>` and no `<escape>`** — it will not give up and cannot flee.

| Result | Text | Effect |
|---|---|---|
| `deadCrew` — **the win condition** | *"You secure the ship and wait for the merchants to arrive. Upon arrival they message you, saying 'Good job. We would prefer if you did not speak of this to anyone.'"* | `autoReward level="HIGH"` **`weapon`** |
| `destroyed` — **the failure** | *"The explosion rocks the pirate ship and a brilliant light begins to shine from the wreckage… Apparently when they said the ship should not be destroyed they had good reason..."* | `<damage amount="13"/>`, `<damage amount="1" system="random"/>` *(AE only)*, `<damage amount="1" system="room" effect="all"/>` |

**Version note (rule 10).** The `<damage amount="1" system="random"/>` line carries a
`<!--DLC-->` marker, so the random-system hit is Advanced Edition content. Vanilla takes
the `13` and the room hit but not that line — which is why `version: both` rather than `ae`.

> ⚠️ **CONTRADICTION:** how much damage the failure actually deals.
> - Game files: three separate `<damage>` tags — `13`, `1` to a random system (AE only),
>   and `1` to a random room with `effect="all"` ([[source-events-xml]]).
> - Fandom: *"Your ship takes **15 hull** damage, 1 damage to a random system, 1 damage with
>   1–2 fires and a breach to a random room"* ([[source-fandom-capture-the-ship]]).
>
> These are reconcilable rather than opposed: 13 + 1 + 1 = 15, so Fandom is reporting the
> **total** hull loss across all three tags while the XML lists them separately. Recording
> both because the reading is not obvious, and because under vanilla (no random-system tag)
> the total would be **14**, not 15. Trusting the game files for the tag-level detail and
> Fandom for the observed total.

`effect="all"` on the room damage is what produces the fire and the breach that Fandom
describes.

## Blue Options
None here. The blue options are on [[event-capture-the-ship]], and they are also the tools
you need to win this fight.

## Rewards & Risks
- Win by killing the crew: `HIGH weapon` — one of the better weapon payouts in the game.
- Lose the ship to hull damage: 14–15 total hull, a damaged system, a fire and a breach,
  with no reward at all. [[source-fandom-capture-the-ship]] calls it the most damaging
  single event outcome in the game.
- There is no third outcome. The ship cannot surrender, cannot escape, and you cannot
  decline the fight once you arrive.

## Strategy Notes
- Bring the crew-killing tool you were gated on and **stop shooting the hull**. Boarding,
  Anti-Bio Beam or fire is the intended win; hull weapons are the failure mode.
  *(Read off the two ship results; no source states the tactic.)*
- Because the failure branch fires on `destroyed`, an over-eager autofire weapon can lose
  you the quest outright.

## Related
- [[event-capture-the-ship]] — the quest start that places this marker
- [[item-teleporter]], [[item-anti-bio-beam]], [[item-fire-bomb]] — the tools that make this winnable
- [[chain-capture-the-ship]]
- [[entity-pirates]]

## Open Questions
- [ ] Confirm the vanilla total is 14 hull (13 + 1 room) with the AE random-system tag
      removed.
- [ ] Does `effect="all"` reliably produce both a fire and a breach, or roll between them?
      Fandom reports 1–2 fires *and* a breach.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-capture-the-ship]] (per raw/wiki/capture-the-ship.md)
