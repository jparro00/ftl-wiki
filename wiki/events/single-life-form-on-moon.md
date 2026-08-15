---
id: event-single-life-form-on-moon
type: event
event_name: STRANDED_BEACON
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: [medbay 2, medbay 3, clonebay 2, slug crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [unique, distress, crew-reward-opportunity, crew-loss-risk, hull-damage-risk, system-damage-risk, hull-repair-chance, blue-option, ae-only-branch]
---

# Single life form on moon — `STRANDED_BEACON`

## Summary
The widest crew-reward event in the base game and the deepest nested tree in `events.xml`.
A distress beacon from a moon surface splits into two completely different scenarios — a
colony survivor (always good) and a madman in a cave (a genuine gamble). Medbay level 2 or
3 turns the madman branch from a coin flip into a guaranteed crew member; a Slug crew
member turns it into a safe check.

## Trigger & Where It Appears
- Sectors: [[sector-abandoned-sector]], [[sector-civilian-sector]],
  [[sector-federation-space]], [[sector-pirate-controlled-sector]],
  [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]]
- Lists: `DISTRESS_BEACON`, `DISTRESS_BEACON_LANIUS`, `DISTRESS_BEACON_PIRATE`,
  `DISTRESS_BEACON_ROCK`, `DISTRESS_BEACON_ZOLTAN`
  ([[source-events-xml]], [[source-dlcevents-anaerobic]], [[source-newevents]]).
  Allocation of those lists per sector is in [[source-sector-data-xml]] — see
  [[concept-sector-event-allocation]].
- Beacon: carries `<distressBeacon/>`, so it shows as a distress signal on the map.
- > ⚠️ **CONTRADICTION:** [[sector-federation-space]] coverage.
  > The Fandom `{{Locations}}` template omits Federation Space
  > ([[source-fandom-single-life-form-on-moon]]), but `STANDARD_SPACE` allocates
  > `<event name="DISTRESS_BEACON" min="1" max="2"/>` ([[source-sector-data-xml]]) and this
  > event is a member of `DISTRESS_BEACON` ([[source-newevents]]) — so it can appear there.
  > Trusting the game files (`high` vs `medium`); reading this as a gap in the Fandom
  > location list rather than a version difference, since no DLC marker is involved.
- `unique="true"` — at most once per run.

## Text
> It appears the distress beacon is coming from the surface of a nearby moon. Your sensors
> are picking up a single life form.

(`event_STRANDED_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Go down to the surface to investigate. | — | One of the two members of `STRANDED` — the **colony survivor** or the **madman**. | 1/2 each (assumes uniform selection across list entries, [[concept-event-list-weighting]]) |
| 2 | Ignore the signal. | — | Nothing happens. | 100% |

### (a) The colony survivor — `STRANDED_1`
> You find a colony that seems to have been recently attacked. Exploring the devastation,
> you find a lone survivor.

| Choice | Requirement | Outcome |
|--------|-------------|---------|
| Invite him to join your crew. | — | Loads `STRANDED_CHARLIES` (marked `<!--DLC!-->`): six members, each a crew member **named Charlie** with 1 skill in weapons / shields / piloting / engines / combat / repair respectively. 1/6 each on the uniform-selection assumption. |
| Take him home to his family on a nearby planet in this system. | — | Loads `FAMILY_RETURN`: three members — `autoReward level="HIGH"` `scrap_only`; `autoReward level="MED"` `scrap_only`; or `<damage amount="-10"/>` (**10 hull repaired**). 1/3 each on the same assumption. |

Both branches are strictly positive — there is no bad outcome anywhere under the colony
survivor.

### (b) The madman — `STRANDED_2`
> You find a man living alone in a cave. From the appearance of his wrecked ship, it seems
> he's been here for many years. He looks healthy, but his mental state is questionable.

| Choice | Requirement | Outcome |
|--------|-------------|---------|
| Bring him back to your ship in hopes of finding some help for him. | — | Loads `MADMAN` — four members, see below. 1/4 each on the uniform assumption. |
| Leave the madman to his ravings, he's not worth the risk. | — | Nothing happens. |
| **(Improved Medbay)** Bring him to your medbay. | `req="medbay" lvl="2"` (`max_group="0"`) | Guaranteed crew member named Charlie. |
| **(Advanced Medbay)** Bring him to your medbay. | `req="medbay" lvl="3"` (`max_group="0"`), marked `<!--DLC!-->` | Guaranteed crew member named Charlie with **`all_skills="1"`** — 1 skill level in every skill. |
| **(Slug Crew)** "Sir, allow me to assess his mental state." | `req="slug"` | Loads `MADMAN_SLUG`: either nothing happens, or you gain a **Human** crew member. 1/2 each on the uniform assumption. |

#### `MADMAN` — the four unguarded outcomes

1. > Once back in orbit, the man turns increasingly violent. Eventually he turns on your
   > crew and manages to kill one before you can subdue him.

   `<removeCrew><clone>true</clone></removeCrew>` — **lose a crew member**, but a Clone
   Bay revives them ("Luckily, your clone bay is able to revive your crewmember.").
2. Crew member named Charlie joins.
3. > Being back in space terrifies him. He goes mad and nearly blows a hole in the side of
   > your ship with a makeshift explosive [...] He dies in the explosion.

   `<damage amount="4"/>` plus `<damage amount="1" system="random"/>` (the second line is
   marked `<!--DLC-->`).
4. He collapses on the way up. Then:
   - *Continue…* → nothing happens.
   - **(Improved Medbay)** `req="medbay" lvl="2"` → crew member named Charlie.
   - **(Improved Clonebay)** `req="clonebay" lvl="2"`, marked `<!--DLC!-->` → crew member
     named Charlie.

(All structure per [[source-events-xml]]; all prose per [[source-text-events-xml]].)

## Blue Options
- **Medbay level 2** (`req="medbay" lvl="2"`) — converts the madman coin-flip into a
  guaranteed crew member. Also available as a rescue inside `MADMAN` outcome 4.
- **Medbay level 3** (`req="medbay" lvl="3"`) — the best outcome in the event: Charlie
  with 1 level in **every** skill. Advanced Edition only (`<!--DLC!-->`).
- **Clone Bay level 2** (`req="clonebay" lvl="2"`) — the Clone Bay's equivalent of the
  Medbay-2 rescue, but only inside `MADMAN` outcome 4. Advanced Edition only.
  A Clone Bay of any level also silently undoes the crew loss in `MADMAN` outcome 1.
- **Slug crew** (`req="slug"`) — no crew reward guarantee, but removes every downside:
  the two `MADMAN_SLUG` outcomes are "nothing" and "free Human crew member".

## Rewards & Risks
- **Rewards:** a crew member (frequently a skilled one), HIGH or MED `scrap_only`, or
  10 hull repaired.
- **Risks:** confined entirely to the unguarded madman branch — one crew death (1/4) and
  one hull/system hit (1/4).
- Choice 2 at the top level costs nothing and risks nothing.

## Version differences
Four `<!--DLC-->` markers sit inside this tree ([[source-events-xml]]):
the `STRANDED_CHARLIES` load on the survivor's "join your crew" branch, the Medbay-3
choice on the madman, the random-system damage in `MADMAN` outcome 3, and the Clonebay-2
rescue in `MADMAN` outcome 4. The vanilla event therefore has **no** all-skills Charlie,
**no** Clone Bay rescue, and takes hull damage only (no system damage) on the explosion.
What the vanilla "Invite him to join your crew" branch did instead of loading
`STRANDED_CHARLIES` is not recoverable from the shipped Advanced Edition files — see Open
Questions.

> ⚠️ **CONTRADICTION:** hull damage on `MADMAN` outcome 3.
> - Game files: `<damage amount="4"/>` plus a separate, DLC-marked
>   `<damage amount="1" system="random"/>` ([[source-events-xml]]).
> - Fandom: *"Your ship takes 5 hull damage, 1 damage to a random system"*
>   ([[source-fandom-single-life-form-on-moon]]).
>
> These reconcile if a `<damage>` entry that names a system also costs 1 hull — 4 + 1 = 5.
> That behaviour is not stated in any source here, so it stays a discrepancy rather than a
> resolution. Trusting the game files on the literal tag values (`high` vs `medium`);
> note that in **vanilla**, without the DLC line, the outcome should be 4 hull and no
> system damage.

## Strategy Notes
- With Medbay 2+, this event is close to free value: the survivor branch is all upside and
  the madman branch is guarded. Without a Medbay and without Slug crew, choice 1 is a 1/8
  chance of losing a crew member outright (1/2 madman × 1/4 outcome 1). *Opinion, derived
  from the tables above.*
- A Clone Bay makes the worst `MADMAN` outcome free, which is worth remembering when
  deciding whether to investigate at all.
- Charlie counts as a **Human** crew member; the Slug branch explicitly awards
  `class="human"`.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[event-asteroid-belt-distress]] — Fandom notes its Teleporter blue option
  loads the same `FAMILY_RETURN` sub-event
  ([[source-fandom-single-life-form-on-moon]])
- [[concept-event-list-weighting]] — the assumption behind every fraction above
- [[concept-sector-event-allocation]]
- [[entity-slugs]] — the blue option's requirement

## Open Questions
- [ ] What did the vanilla "Invite him to join your crew" branch do? The load target is
      DLC-marked, and no vanilla data file is in `raw/gamedata/` to compare against.
- [ ] Does a system-targeted `<damage>` entry also remove hull? This is what the
      contradiction above hinges on.
- [ ] Exact scrap values behind `HIGH scrap_only` and `MED scrap_only`.
- [ ] Are the two `STRANDED` members really equally likely? Nothing in the file weights
      them.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-dlcevents-anaerobic]] (per `raw/gamedata/dlcEvents_anaerobic.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-fandom-single-life-form-on-moon]] (per `raw/wiki/single-life-form-on-moon.md`)
</content>
