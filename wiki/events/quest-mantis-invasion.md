---
id: event-quest-mantis-invasion
type: event
event_name: QUEST_MANTIS_INVASION
sectors: []
beacon_type: quest
hostile: true
blue_options: [[[item-missile-weapon]], [[item-fire-bomb]]]
chain: [[[chain-mantis-war-camp]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-destination, blue-option, crew-reward, mantis, missile-cost, bugged]
---

# Mantis war camp — the encampment — `QUEST_MANTIS_INVASION`

## Summary
The quest marker placed by [[event-mantis-war-camp]]. Two of the three routes end in a
Mantis patrol fight; the third — gated behind a **Fire Bomb** — is a clean, fight-free
**free Engi crew member plus `HIGH stuff`**, and is the entire reason to visit. The
missile-weapon option is a trap: it costs a missile *and* starts the fight anyway.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via `<quest event="QUEST_MANTIS_INVASION"/>`
  from the accept branch of [[event-mantis-war-camp]] ([[source-events-xml]]) — its sole
  reference in the game files.
- Sectors depend on where the marker was placed, so the frontmatter list is deliberately
  empty.
- `unique="true"`, with a dev note in the XML: *"ADD PDS ENVIRONMENT"* — a planetary defense
  system environment that was planned and never added ([[source-events-xml]]).
- [[source-fandom-mantis-war-camp]] documents it as that page's "Quest Marker" section and
  marks it `shipdetected=noship`.

## Text
> You find the Mantis encampment but there are far too many of them to count accurately. You
> send a long range message back to the settlement with your findings but unfortunately
> there's not much you can do. It would be suicide to attack directly.

(`event_QUEST_MANTIS_INVASION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Leave before they notice you. | — | Loads `eventList MANTIS_LANDING_PARTY_LEAVE` — 2 entries, below. | see below |
| 2 | **(Missile Weapon)** Bombard their key structures. | `req="WEAPONS_MISSILES"` | *"You fire at their fuel depot, but a shot from the surface rips the missile to shreds… a nearby patrol ship moves in to attack."* → **−1 missile** *and* `<ship load="MANTIS_LANDING_PARTY" hostile="true"/>`. | 100% fight |
| 3 | **(2 Fire Bombs)** Teleport fire bombs into key structures. | `req="BOMB_FIRE"` | *"…You deposit one bomb in a fuel depot and another in the barracks…"* → **−2 missiles**, then continue: *"…You find some useful resources and an Engi slave who gladly accepts your liberation."* → `autoReward level="HIGH"` **`stuff`** and `<crewMember amount="1" class="engi"/>`. **No fight.** | 100% |

Choice 2 is *not* hidden; choices 1 and 3 behave as normal ([[source-events-xml]]).

### Choice 1 — `eventList MANTIS_LANDING_PARTY_LEAVE` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
**1/2** each:

| Entry | Text | Effect |
|---|---|---|
| 1 | *"As you try to leave, a patrol spots you. Wailing sirens begin to blare around the camp and the ship moves in to attack!"* | `<ship load="MANTIS_LANDING_PARTY" hostile="true"/>` |
| 2 | *"They must have been focused on setting up camp since you got far enough away to attempt a jump without being noticed."* | nothing |

### The ship — `MANTIS_LANDING_PARTY`
Defined in `events.xml` on an `auto_blueprint="SHIPS_MANTIS"` hull ([[source-events-xml]]).
It has **no `<surrender>` and no `<escape>`** — it neither gives up nor flees.

| Result | Text | Reward |
|---|---|---|
| `destroyed` | *"With the patrol ship destroyed you hasten to leave. It won't be long before the other ships catch up."* | `autoReward level="MED"` `standard` |
| `deadCrew` | *"With the patrol ship taken care of you hasten to leave…"* | `autoReward level="HIGH"` `standard` |

Crew composition: `<crewMember type="mantis" prop="0.80"/>`, `<crewMember type="engi" prop="0.20"/>` —
mostly Mantis, so boarding it is dangerous even though `deadCrew` pays a tier more.

## Blue Options
- **[[item-fire-bomb]]** (`req="BOMB_FIRE"`) — the only good outcome on the page: a **free
  Engi crew member** and `HIGH stuff` for 2 missiles and no combat.
- **[[item-missile-weapon]]** (`req="WEAPONS_MISSILES"`) — **worse than doing nothing**. It
  spends a missile and then hands you the same fight that choice 1 only risks half the time.
  [[source-fandom-mantis-war-camp]] additionally reports it as **bugged**: *"Hull Missile
  doesn't count"* toward the requirement. The game files carry no such note — `WEAPONS_MISSILES`
  is an opaque requirement token in the XML — so this is a Fandom-only observation.

## Rewards & Risks
- Best case: free Engi crew + `HIGH stuff`, no fight (Fire Bomb).
- Middle: leave quietly and nothing happens (1/2 on choice 1).
- Worst: a Mantis patrol fight you cannot escape or negotiate out of, against a
  mostly-Mantis crew. Reward is `MED`/`HIGH standard`, so it is not a disaster — just not
  worth seeking.
- The missile option is a pure loss relative to choice 1.

## Strategy Notes
- **Take choice 3 if you have a Fire Bomb; otherwise take choice 1.** Choice 2 costs a
  missile for a fight choice 1 gives you a 50% chance of avoiding entirely, with no reward
  difference. *(Derived from the outcome table; no source states the comparison.)*
- Do not board the patrol ship for the `HIGH standard` unless your boarders can beat Mantis
  in a straight fight — the crew table is 80% Mantis.

## Related
- [[event-mantis-war-camp]] — the quest start that places this marker
- [[event-mantis-fight]] — the ordinary Mantis encounter
- [[item-fire-bomb]], [[item-missile-weapon]]
- [[entity-mantis]], [[entity-engi]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — the 1/2 split depends on it.
- [ ] Verify Fandom's "Hull Missile doesn't count" claim against the `WEAPONS_MISSILES`
      requirement's actual definition; the token is not expanded anywhere in the XML.
- [ ] The dev note *"ADD PDS ENVIRONMENT"* suggests a planetary-defense hazard was intended.
      Did any build ship it?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-mantis-war-camp]] (per raw/wiki/mantis-war-camp.md)
