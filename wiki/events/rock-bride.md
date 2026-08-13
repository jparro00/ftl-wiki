---
id: event-rock-bride
type: event
event_name: ROCK_QUEST_MARRIAGE_START
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-rock-bride]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rock, quest, quest-marker, crew-reward, augment-reward, unique, named-crew]
---

# Rock bride — `ROCK_QUEST_MARRIAGE_START`

## Summary
A two-beacon quest: accept a Rock bride as cargo, then decide at Numa V whether to deliver
her or keep her. Delivering pays a **random augment plus low scrap**; refusing gives you a
**named Rockman crew member, Ariadne**, and a fight. It is the only quest in the Rock
event lists that hands out a crew member with a fixed name.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `QUESTS_ROCK`, allocated `min="0" max="1"` per Rock sector — so **at most
  one** quest beacon per Rock sector, and this event is one of five candidates in that
  list ([[source-sector-data-xml]], [[source-events-rock]])
- Beacon: no ship present ([[source-fandom-rock-bride]], `LRSmap=noship`)
- `unique="true"` — at most once per sector ([[source-events-rock]])
- Step 2 is a **quest marker** added to your sector map by `<quest event="ROCK_QUEST_MARRIAGE"/>`

## Text
> A Rock captain hails you: "It is improper of me to contact off-worlders, but this is an
> emergency. We were on our way to deliver our passenger to her new husband - the Grand
> Basilisk of Numa V - when our engines broke down. Will you take possession of her and
> make haste to Numa V?"

(`event_ROCK_QUEST_MARRIAGE_START_text`, per [[source-text-events-xml]])

## Choices & Outcomes

### Step 1 — the hail

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept the passenger. | — | *"You surprise me, off-worlder. Thank you…"* → `<quest event="ROCK_QUEST_MARRIAGE"/>` places a quest marker on the map. No immediate reward or cost. | 100% |
| 2 | Refuse. | — | *"Arranged marriages aren't on your list of worthy causes. You leave the Rock to their business."* Nothing happens. | 100% |

### Step 2 — the quest beacon, `ROCK_QUEST_MARRIAGE`
Documented here rather than on its own page: it is the `quest` target of choice 1 and is
not reachable any other way ([[source-events-rock]]).

> A vast tunnel network near the surface of Numa V indicates an advanced Rock
> civilization. This must be where you were asked to deliver the passenger.

Continue, then:

> Realizing arrival is imminent, the passenger - silent so far - pleads with you not to
> hand her over. She's interrupted by the Grand Basilisk's Chief Aid: "To the alien vessel
> holding the Basilisk's wife. Deliver her to us. You will be rewarded... well."

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 2a | Hand her over. | — | *"'May your children erode into dust!' she screams…"* → `<augment name="RANDOM"/>` **plus** `<autoReward level="LOW">scrap_only</autoReward>`. No fight. | 100% |
| 2b | Refuse to comply. | — | *"'I was led to believe your kind did not know mercy. I will join you…'"* → `<crewMember amount="1" class="rock" id="name_Ariadne"/>` **and** `<ship load="ROCK_QUEST_MARRIAGE" hostile="true"/>`. | 100% fight |

### The escort ship — `ROCK_QUEST_MARRIAGE`
Defined in `events_rock.xml` itself ([[source-events-rock]]):
- `auto_blueprint="SHIPS_ROCK"`
- `destroyed` → `<autoReward level="MED">standard</autoReward>`
- `deadCrew` → `<autoReward level="HIGH">standard</autoReward>`
- Both branches share the text: *"His escort eliminated, the Grand Basilisk dispatches his
  entire fleet. There's just time to take your pick from the wreck before you jump out of
  their reach."*
- **No `<surrender>` and no `<escape>`** — you cannot buy your way out of this fight.

Note the asymmetry: killing the *crew* (boarding, suffocation) pays **`HIGH`**, destroying
the *hull* pays only **`MED`** — a rare case where the game explicitly rewards boarding.

## Blue Options
None at any step. Neither Rock crew, nor Sensors, nor any augment opens an extra branch.

## Rewards & Risks
| Path | Reward | Cost |
|---|---|---|
| Refuse at step 1 | nothing | nothing |
| Hand her over | random augment + `LOW` scrap only | 2 beacons of travel |
| Refuse to comply | **Ariadne**, a named Rockman crew member, + `MED` (hull kill) or `HIGH` (crew kill) scrap with resources | a no-surrender `SHIPS_ROCK` fight |

- Risk is concentrated entirely in step 2b. Step 1 and the trip to the marker cost only
  fuel and time.
- The augment is `name="RANDOM"` — you do not get to choose, and it may be one you already
  have or cannot use ([[source-events-rock]]).

## Strategy Notes
- **Refusing to comply is the higher-value branch** if you can win the fight: a permanent
  crew member plus `MED`/`HIGH` scrap beats a random augment plus `LOW` scrap-only in most
  runs. *(Opinion; the sources give the payouts, not the ranking.)*
- If you have a working boarding party, kill the escort's crew rather than its hull — that
  is a `HIGH` vs `MED` reward difference stated directly in the ship definition.
- The `QUESTS_ROCK` allocation is `min="0"`, so a Rock sector may contain **no** quest
  beacon at all ([[source-sector-data-xml]]).

> ⚠️ **CONTRADICTION (transcription):** several small wording differences between the
> Fandom page and the game files ([[source-text-events-xml]] vs
> [[source-fandom-rock-bride]]):
> - *"Will you take possession of her and make haste"* (files) vs *"…of her, and make
>   haste"* (Fandom).
> - *"the Grand Basilisk's Chief **Aid**"* (files) vs *"Chief **Aide**"* (Fandom).
> - *"the passenger - silent so far"* (files) vs *"your passenger - silent so far"* (Fandom).
> - *"jump out of **their** reach"* (files) vs *"jump out of reach"* (Fandom).
>
> All cosmetic; no mechanical claim differs. Trusting the game files (`high` vs `medium`)
> — the quoted text on this page is the files'. These are most likely wiki transcription
> drift rather than a vanilla/AE difference, since `events_rock.xml` is not overridden by
> `dlcEventsOverwrite.xml`.

## Related
- [[chain-rock-bride]] — the two-step chain this begins
- [[event-rock-atheists]] — the other free-Rockman source in Rock space
- [[entity-rock-men]], [[item-rock-crew]]
- [[concept-quest-markers]] — how `<quest event="…"/>` places a beacon
- [[event-rock-quest-marriage]] — step 2, the Numa V quest beacon (`ROCK_QUEST_MARRIAGE`)

## Open Questions
- [ ] Which augments the `RANDOM` roll can produce, and whether duplicates are excluded.
- [ ] Whether the quest marker can spawn in the *next* sector rather than the current one.
- [ ] Whether Ariadne has any properties beyond the fixed name (`id="name_Ariadne"`).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-bride]] (per raw/wiki/rock-bride.md)
