---
id: event-intelligent-ponies
type: event
event_name: DONOR_PONY
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [slug crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [slug, unique, donor-event, filler, crew-reward, crew-loss-risk, clone-bay, blue-option, gamble]
---

# Intelligent ponies — `DONOR_PONY`

## Summary
A three-level choice tree on a planet full of small six-legged horses. The peaceful route
is a coin flip for a free Engi crew member; the greedy route is a coin flip for a dead
crew member and gains nothing either way; a Slug crew member converts the whole thing into
a **guaranteed** Engi. One of the clearest cases in the game where the blue option is not a
bonus but the entire point of the event.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Pooled in the base `NEUTRAL` and `NEUTRAL_EXIT` lists (`newEvents.xml`, the names
  `sector_data.xml` actually references) and in their Advanced Edition replacements
  `OVERRIDE_NEUTRAL` / `OVERRIDE_NEUTRAL_EXIT` (`dlcEventsOverwrite.xml`). It is in the
  pool in **both editions**; the `OVERRIDE_` lists simply add nine further AE entries
  alongside it ([[source-newevents]], [[source-dlceventsoverwrite]],
  [[source-sector-data-xml]]).
- The `_EXIT` lists double as the engine's filler pool for a sector that has run out of
  allocated events, so this can appear at an exit beacon too — Fandom's
  `alsooccur=exitandfiller` ([[source-newevents]], [[source-fandom-intelligent-ponies]]).
- `unique="true"` — at most once per run.
- No ship at the beacon; Long-Range Scanners show nothing.

## Text
> Scanners are showing intelligent life forms on a nearby planet. No match for them can be
> found in the database.

(`event_DONOR_PONY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Investigate. | — | *"You land a small shuttle in an enormous field, whose only occupants are small, brightly colored, six-legged, horse-like animals. Could they be what your scans picked up?"* → a second screen with four choices, below. | 100% |
| 2 | Ignore it. | — | *"You ignore the readings and prepare to move on."* → nothing. | 100% |

### Second screen (after "Investigate")

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Try to communicate peacefully. | — | Loads `DONOR_PONY_PEACE` — 2 members. | 1/2 each |
| 1b | Bring some of the creatures on board to sell. | — | Loads `DONOR_PONY_SELL` — 2 members. | 1/2 each |
| 1c | Leave. | — | *"This isn't the time for exobiology. You head back to the ship."* → nothing. | 100% |
| 1d | **(Slugman Crew)** Attempt to communicate telepathically. | `req="slug"` | Guaranteed Engi crew member — see Blue Options. | 100% |

**`DONOR_PONY_PEACE`** — two distinct members; assuming uniform selection across list
entries, **1/2 each** ([[source-events-xml]]):

| Odds | Outcome |
|---|---|
| 1/2 | *"None of your attempts to communicate seem to work… Eventually, they guide you to an old Engi ship's crash site. Inside you are able to find and reactivate an Engi!"* → `<crewMember amount="1" class="engi"/>` **plus** `autoReward level="LOW"` type `standard`. **A free Engi crew member with low scrap and resources.** |
| 1/2 | *"You try to communicate in every possible way you can but they just stand there, silently judging you with their large, expressionless eyes."* → **nothing.** |

**`DONOR_PONY_SELL`** — two distinct members; assuming uniform selection across list
entries, **1/2 each** ([[source-events-xml]]):

| Odds | Outcome |
|---|---|
| 1/2 | *"…Their well-organized stampede forces you to draw weapons and make a rushed and shambolic retreat to the shuttle."* → **nothing.** |
| 1/2 | *"…They stampede with terrifying force, trampling one of your crew before you have time to react."* → `<removeCrew><clone>true</clone></removeCrew>` — **lose a crew member**, but a Clone Bay revives them: *"The trampled crewmate's clone is already ready when you get back to your ship."* |

Note the asymmetry: the "sell them" branch has **no upside at all**. Neither member of
`DONOR_PONY_SELL` awards anything. It is a 1/2 chance of losing a crew member for a
guaranteed nothing.

## Blue Options
- **Slug crew member** (`req="slug"`) — *"(Slugman Crew) Attempt to communicate
  telepathically."* Two chained screens, both automatic:

  > After a moment, your crew tells you that these are simple beings, who enjoy a peaceful
  > life. However, this isn't the first time a ship has landed here. They inform you of a
  > nearby crash site.

  > You follow their directions and discover an ancient Engi ship. You find a deactivated
  > Engi inside and reroute power from your shuttle to resuscitate it. After a while it
  > reboots, rebuilds itself, and offers to join your crew.

  → `<crewMember amount="1" class="engi"/>`, **guaranteed, no roll**. It trades the low
  scrap-with-resources that the lucky peaceful outcome carries for certainty about the
  crew member. ([[source-events-xml]], [[source-text-events-xml]])

## Rewards & Risks
- Best case without Slug crew: an **Engi crew member** plus low scrap with resources (1/2
  on the peaceful branch).
- With Slug crew: an **Engi crew member, guaranteed** — but no scrap.
- Risk: only on the "sell them" branch — 1/2 to lose a crew member, revivable by a
  [[item-clone-bay]], for zero possible gain.
- No combat, no hull damage, no ship at the beacon.

## Strategy Notes
- With a Slug aboard this is a free crew member. Take it every time. *Opinion*, but the
  outcome table leaves no room for another reading.
- Without one, "communicate peacefully" is a free 50/50 for an Engi with no downside.
- "Bring some of the creatures on board to sell" is strictly dominated — every outcome is
  neutral or bad. It exists as a trap.
- Compare [[event-plagued-station]], the other Slug-nebula donor event: there the Clone
  Bay is explicitly defeated (`<clone>false</clone>`); here it works
  (`<clone>true</clone>`). The two events are a matched pair on that mechanic.

## Related
- [[event-plagued-station]] — the sibling donor event in the same pool, opposite Clone Bay
  behaviour
- [[entity-slugs]] — the blue-option gate
- [[entity-engi]] — the reward
- [[item-clone-bay]]
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] The actual distribution across `DONOR_PONY_PEACE` and `DONOR_PONY_SELL` — the 1/2
      figures assume uniform selection across list entries.
- [ ] Whether the Slug blue option is available to any Slug crew member or requires one
      alive and un-suffocating; no source states a condition.

> ⚠️ **CONTRADICTION:** one word in the peaceful-contact success text.
> - Game files: *"Eventually, **they** guide you to an old Engi ship's crash site."*
>   ([[source-text-events-xml]], `event_DONOR_PONY_PEACE_1_text`)
> - Fandom: *"Eventually, **the creatures** guide you to an old Engi ship's crash site."*
>   ([[source-fandom-intelligent-ponies]])
>
> Trusting the game files — reliability `high` vs `medium`, and they are the exact 1.6.x
> build. Cosmetic; most likely a pre-AE wording the wiki never re-transcribed. Not
> confirmed as a version difference.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-intelligent-ponies]] (per raw/wiki/intelligent-ponies.md)
