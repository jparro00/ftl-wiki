---
id: event-rock-nursery
type: event
event_name: ROCK_NURSERY
sectors: []
beacon_type: unknown
hostile: false
blue_options: [[[item-weapons]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rock, cut-content, disabled, orphan, crew-risk, weapon-reward, unique, no-fandom-page]
---

# Rock nursery — `ROCK_NURSERY`

## Summary
A fully written, fully wired away-team event that **is disabled in the shipped game**. Its
entry in the `NEUTRAL_ROCK` event list is commented out, so no sector can roll it. It is
documented here because it is complete content with real mechanics — an away mission into
a Rock religious school in the middle of a student uprising — and because two of its
sub-branches carry a developer note doubting they work at all.

## Trigger & Where It Appears
- **Unreachable in normal play.** `events_rock.xml` contains
  `<!--<event load="ROCK_NURSERY"/>-->` inside `<eventList name="NEUTRAL_ROCK">` — the
  line is commented out ([[source-events-rock]]).
- It appears in **no** other event list and in **no** `sectorDescription`
  ([[source-sector-data-xml]]).
- The event definition itself is intact and `unique="true"`, so it was live at some point
  and was disabled by deleting the reference, not the event.
- **No Fandom page** in this raw set covers `ROCK_NURSERY` — consistent with it being
  unreachable.
- Had it been enabled, its list placement (`NEUTRAL_ROCK`) would have put it in
  [[sector-rock-controlled-sector]] and [[sector-rock-homeworlds]]. `sectors:` is left
  empty because it cannot actually appear.

## Text
> Fluctuating life-signs are reported near the surface of a hazy, pock-marked moon in the
> vicinity. It seems this is a Rock nursery where the young are 'acclimatized' to their
> religion - only there's been some kind of coup and the students are running amok!

(`event_ROCK_NURSERY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

### Top level

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Transfer an away team to investigate. | — | *"Your away team reports combat between students and authorities - it seems some of the students were considered to have dissident personalities and were to be imprisoned pro-actively."* → opens the side-picking choice below. | 100% |
| 2 | Leave. | — | *"As long as they're not shooting at the ship it's best to leave them be."* Nothing happens. | 100% |
| 3 | **(Improved Weapons)** Fire a warning shot near to the commotion to announce your arrival. | `req="weapons" lvl="6"` | *"…Weapons fire on the surface ceases for as long as it takes for the moon's defense force to be dispatched to your location!"* → `<ship load="ROCK_SHIP" hostile="true"/>` | 100% fight |

Choice 3 is a **blue option that makes things strictly worse** — it requires a Weapons
system at level 6 and its only effect is to start a [[event-rock-fight]] you could have
avoided ([[source-events-rock]]).

### After choice 1 — pick a side

| # | Choice | Loads |
|---|--------|-------|
| 1a | Order the away team to side with the students. | `eventList ROCK_NURSERY_STUDENTS` |
| 1b | Order the away team to side with the authorities. | `eventList ROCK_NURSERY_AUTHORITY` |

Both choices print the **same** intermediate text (`event_ROCK_NURSERY_c1_c1_text`):
*"It's not long before the violence on the planet becomes a full-scale battle, your away
team and their military-grade weaponry in the very center of it."*

### The two side lists
`ROCK_NURSERY_STUDENTS` and `ROCK_NURSERY_AUTHORITY` are **mechanically identical** — five
entries each, same structure, same effects, with only the flavour of who wins swapped
([[source-events-rock]], [[source-text-events-xml]]). Which side you back changes nothing.

| Entry | What happens | Crew effect | Terminates in |
|---|---|---|---|
| 1 | Your team is flanked and retreats. | — | `ROCK_NURSERY_LOSE` |
| 2 | Team is flanked, **one falls**; the survivor drags an injured Rock aboard. | `<removeCrew>` (**`<clone>true</clone>`**) **and** `<crewMember amount="1" class="rock"/>` | `ROCK_NURSERY_LOSE` |
| 3 | Your team holds the main quad and takes the institution. | — | `ROCK_NURSERY_WIN` |
| 4 | Your team holds, but **one falls** past the lip of a quarry. | `<removeCrew>` (**`<clone>true</clone>`**) | `ROCK_NURSERY_WIN` |
| 5 | The battle moves away; your team scavenges abandoned weapons. | — | ends immediately with `<autoReward level="MED">weapon</autoReward>` |

- `ROCK_NURSERY_WIN` — *"In return for your support during the fight the survivors reward
  you with the funds set aside for prison transport."* → `<autoReward level="HIGH">standard</autoReward>`
- `ROCK_NURSERY_LOSE` — *"Fully aware that their victory was threatened by your arrival,
  the survivors immediately dispatch a ship to eliminate you!"* → `<ship load="ROCK_SHIP" hostile="true"/>`

So choice 1 resolves to: **2 of 5** `HIGH` scrap with resources, **2 of 5** a
[[event-rock-fight]], **1 of 5** a `MED` **weapon** — with a crew member lost in 2 of the
5 (revivable via Clone Bay). Assuming uniform `eventList` selection.

## Blue Options
- **Weapons level 6+** (`req="weapons" lvl="6"`) — a genuinely bad blue option: it costs a
  heavily upgraded Weapons system and buys you a hostile Rock ship. No reward is attached
  to the branch.

## Rewards & Risks
- Best outcome: `HIGH` scrap with resources (entries 3 and 4).
- A `MED`-level **weapon** drop on entry 5 — one of few weapon `autoReward`s in the Rock
  event pool.
- Risk: crew loss on 2 of 5 away-team outcomes, and a Rock ship fight on 2 of 5.
- Choice 2 costs nothing.

> ⚠️ **DEVELOPER NOTE / suspected broken branch:** entry 2 of *both* lists carries the
> inline comment `<!-- JUSTIN - TO DO - Test if this works. i dont think it does...-->`
> ([[source-events-rock]]). The structure it doubts is a `<removeCrew>` followed by a
> `<choice>` whose event grants `<crewMember amount="1" class="rock"/>`. Whether the
> lose-one-gain-one swap actually fires is unverified — and unverifiable in play, since
> the whole event is disabled. Recorded as-is.

> ⚠️ **Why this page exists at all:** the brief's orphan rules distinguish test stubs and
> UI strings (no page) from real events reached by another route (page). `ROCK_NURSERY` is
> neither — it is finished content with no route at all. Paged because it is substantive
> and its disabled status is itself a finding worth recording, but flagged `disabled` and
> `cut-content` so it is never mistaken for something a player can encounter.

## Strategy Notes
None applicable — the event cannot occur. If a mod re-enables it, choice 2 (Leave) is the
only risk-free branch and choice 3 is a trap.

## Related
- [[event-rock-zoltan-help]] — the *other* event commented out of `NEUTRAL_ROCK`
- [[event-rock-fight]] — the fight both losing branches load
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]] — where it would have appeared
- [[concept-cut-content]], [[item-clone-bay]], [[entity-rock-men]]
- [[event-rock-ship-surrender]] — the `ROCK_SHIP_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Was `ROCK_NURSERY` live in vanilla 1.0 and disabled for AE, or never shipped
      enabled? `dlcEventsOverwrite.xml` does not touch `NEUTRAL_ROCK`
      ([[source-events-rock]]), so the comment is in the base file — which suggests it was
      disabled before AE, but that is not proof.
- [ ] Does the entry-2 crew swap work?
- [ ] Whether `eventList` selection is uniform (the 2/5 and 1/5 figures depend on it).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
