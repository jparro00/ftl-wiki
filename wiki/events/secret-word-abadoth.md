---
id: event-secret-word-abadoth
type: event
event_name: SECRET_WORD_ABADOTH
sectors: []
beacon_type: quest
hostile: false
blue_options: [slug crew, engi crew]
chain: [[[chain-secret-word-abadoth]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [quest-marker, blue-option, orphan, dlc, rebel-advance-risk]
---

# Secret word: ABADOTH — `SECRET_WORD_ABADOTH`

## Summary
The quest-marker payoff of [[event-nebula-wreckage]]. A dying survivor gives you
coordinates and one word; at the coordinates a cloaked Zoltan ship demands to know why
you're there. Say the right word and you get medium scrap-with-resources. Say anything
else and you fight a Zoltan ship.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only through
  `<quest event="SECRET_WORD_ABADOTH"/>`, fired by the `BATTLEFIELD_SURVIVOR` sub-event of
  [[event-nebula-wreckage]] when you choose "Make them comfortable for their final
  moments." ([[source-events-slug]])
- The marker therefore appears in whichever Slug sector you were in when the wreckage
  event resolved: [[sector-slug-controlled-nebula]] or [[sector-slug-home-nebula]].
- No `<environment>` tag — the beacon has no forced nebula.

## Text
> You have arrived at the coordinates given to you by the dead crewman you attempted to
> save. There doesn't seem to be anything here - no planets, no vessels, and no clue as to
> what he meant by sending you here.

(`event_SECRET_WORD_ABADOTH_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | **(Slug Crew)** Ask your Slug crewmember to scan for life forms. | `req="slug"` | Straight to `SECRET_WORD_ABADOTH_CONCLUSION`, no cost. | 100% |
| 2 | Do a full system scan - though you're sure to lose some of your lead with the Rebels. | — | "You start the arduous task of a full system scan. This better be worth it." `<modifyPursuit amount="1"/>`, then a *Continue* that also loads `SECRET_WORD_ABADOTH_CONCLUSION`. | 100% |

Both choices reach the same conclusion; the Slug option only saves the pursuit penalty.
(The nested *Continue* under choice 2 is in the game files but is dropped by the batch
extract — see [[source-events-slug]].)

> ⚠️ **CONTRADICTION:** the size of the Rebel penalty.
> - Game files: `<modifyPursuit amount="1"/>` — one step of pursuit
>   ([[source-events-slug]]).
> - Fandom: "Rebel Fleet **pursuit is doubled for 1 jump**"
>   ([[source-fandom-nebula-wreckage]]).
>
> These are two descriptions of the same tag, not two different values — Fandom is
> describing what `modifyPursuit amount="1"` does in play. Recorded rather than resolved
> because no source here defines the tag's exact effect.

### `SECRET_WORD_ABADOTH_CONCLUSION`

> A Zoltan ship decloaks and demands your reason for being here!

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| 1 | Explain about finding the dead crewman. | — | Wrong answer → `<ship load="ZOLTAN_SHIP" hostile="true"/>`, default rewards |
| 2 | **(Engi Crew)** Say ABADOTH. | `req="engi"` | "Your Engi crewman easily recalls the phrase…" → `<autoReward level="MED">standard</autoReward>` |
| 3 | Say ANODYNE. | — | Wrong → Zoltan ship fight |
| 4 | Say ABADOTH. | — | Correct → `<autoReward level="MED">standard</autoReward>` |
| 5 | Say ABATODH. | — | Wrong → Zoltan ship fight |

`ZOLTAN_SHIP` has no surrender or escape block; it uses `DESTROYED_DEFAULT` /
`DEAD_CREW_DEFAULT`. ([[source-events-ships]])

## Blue Options
- **Slug crew member** (`req="slug"`) — avoids the `modifyPursuit` penalty. It does not
  reveal the password.
- **Engi crew member** (`req="engi"`) — an explicitly-labelled safe path to the correct
  word, for players who don't already know it. Mechanically identical to choice 4.

## Rewards & Risks
- Correct word (choices 2 or 4): `MED` `standard` — the game's own words for medium
  scrap-with-resources.
- Wrong word (choices 1, 3, 5): a fight with a [[entity-zoltan-ships|Zoltan ship]] at
  default rewards.
- Choice 2 at the parent beacon costs Rebel-fleet ground.

## Strategy Notes
- The password is stated verbatim in the flavour text of the event that sends you here
  ("the survivor simply says, 'ABADOTH'"), so the Engi blue option is a convenience, not a
  requirement — take choice 4 and skip the fight. *(Opinion, from reading both event
  definitions in [[source-events-slug]].)*
- "ANODYNE" and "ABATODH" are deliberate near-misses. There is no partial credit.

## Related
- [[chain-secret-word-abadoth]] — the full quest line this belongs to
- [[event-nebula-wreckage]] — the only way to reach this beacon
- [[entity-zoltan]] — the enemy on a wrong answer
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- [[event-battlefield-survivor]] — the sub-event that fires this quest marker

## Open Questions
- [ ] Exact mechanical effect of `modifyPursuit amount="1"`.
- [ ] Whether the marker can land outside the Slug sector where the chain started.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-nebula-wreckage]] (per raw/wiki/nebula-wreckage.md)
