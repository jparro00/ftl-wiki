---
id: event-rock-zoltan-help
type: event
event_name: ROCK_ZOLTAN_HELP
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [rock, zoltan, cut-content, disabled, orphan, moral-choice, unique, no-fandom-page]
---

# Rock/Zoltan intervention — `ROCK_ZOLTAN_HELP`

## Summary
A finished moral-choice event that **is disabled in the shipped game**: a Zoltan ship
fleeing a Rock settlement it tried to "liberate" arrives at your beacon with its pursuers
behind it, and you pick a side. Its entry in `NEUTRAL_ROCK` is commented out, with a
developer note giving the reason — the Zoltan super shield was not balanced yet.

## Trigger & Where It Appears
- **Unreachable in normal play.** `events_rock.xml` contains
  `<!--<event load="ROCK_ZOLTAN_HELP"/>-->` inside `<eventList name="NEUTRAL_ROCK">`
  ([[source-events-rock]]).
- Appears in **no** other event list and **no** `sectorDescription`
  ([[source-sector-data-xml]]).
- The event definition is intact and `unique="true"`. Its own definition line carries the
  comment: `<!-- JUSTIN TO DO - Maybe don't include this since the zoltan super shield
  isn't balanced yet? -->` ([[source-events-rock]]) — a direct statement of why it was
  disabled.
- **No Fandom page** in this raw set covers `ROCK_ZOLTAN_HELP`.
- Had it been enabled, `NEUTRAL_ROCK` would have placed it in
  [[sector-rock-controlled-sector]] and [[sector-rock-homeworlds]]. `sectors:` is left
  empty because it cannot appear.

## Text
> It seems a Zoltan ship came here to liberate a Rock settlement from their 'oppressive
> belief system', and that the settlement did not appreciate it - long-range scanners
> suggest the Zoltan and their pursuers will be here at any moment!

(`event_ROCK_ZOLTAN_HELP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Stay and defend the Zoltan. | — | *"The pursuing Rock ship quickly assesses the situation and decides two captured alien ships are better than one."* → `<ship load="ROCK_ZOLTAN_HELP_ROCK" hostile="true"/>` | 100% fight |
| 2 | Stay and capture the Zoltan. | — | *"This is Rock territory, and therefore Rock law… You'll have to disable their engines and piloting to ensure their safe capture."* → `<ship load="ROCK_ZOLTAN_HELP_ZOLTAN" hostile="true"/>` | 100% fight |
| 3 | Leave. | — | *"This is none of your concern - power up the jump drive!"* Nothing happens. | 100% |

### Choice 1's enemy — `ROCK_ZOLTAN_HELP_ROCK`
`auto_blueprint="SHIPS_ROCK"` ([[source-events-rock]]). Unusually, **both** end states
chain a second reward:

| Branch | Text | Effect |
|---|---|---|
| `destroyed` | *"The Rock ship's hull breaks apart. You salvage the wreck before contacting the Zoltan ship."* | `<autoReward level="LOW">standard</autoReward>`, then a continue → *"The Zoltan show little emotion, but express their gratitude with a small payment."* → `<autoReward level="RANDOM">stuff</autoReward>` |
| `deadCrew` | *"With the ship's crew dead you salvage the ship before contacting the Zoltans."* | `<autoReward level="HIGH">standard</autoReward>`, then the same continue → `<autoReward level="RANDOM">stuff</autoReward>` |

### Choice 2's enemy — `ROCK_ZOLTAN_HELP_ZOLTAN`
`auto_blueprint="SHIPS_ZOLTAN"` ([[source-events-rock]]). No follow-up payment:

| Branch | Text | Effect |
|---|---|---|
| `destroyed` | *"The Rock ship arrives just as you put the finishing blows to the Zoltan ship. They're not of a mind to thank you, and you get the impression it'd be best if you left post-haste..."* | `<autoReward level="LOW">standard</autoReward> ` |
| `deadCrew` | *"By the time the Rock ship arrives you've all but tied a bow around their quarry. The injured and dying Zoltan are easily taken into custody and the Rock ship grudgingly transfers over what you assume must be the bounty."* | `<autoReward level="HIGH">standard</autoReward>` |

Neither enemy ship declares a `<surrender>` or `<escape>` branch.

## Blue Options
None. No `req` appears anywhere in the event — no Zoltan crew option, no Rock crew option,
despite both species being central to the story.

## Rewards & Risks
- Both fighting branches pay **`LOW`** on a hull kill and **`HIGH`** on a crew kill — the
  same boarding-favours-you asymmetry seen in [[event-rock-bride]], and a large gap here
  (LOW vs HIGH, not MED vs HIGH).
- Choice 1 additionally pays a `RANDOM` "stuff" reward from the grateful Zoltan on **both**
  end states, making it the better-paying branch of the two.
- Choice 3 costs and gives nothing.
- Risk: a full `SHIPS_ROCK` or `SHIPS_ZOLTAN` hull with no surrender option. The
  developer's own reservation about the Zoltan super shield suggests choice 2's enemy was
  considered overtuned ([[source-events-rock]]).

## Strategy Notes
None applicable — the event cannot occur. Were it enabled, choice 1 dominates choice 2:
the same LOW/HIGH structure plus an extra `RANDOM` payout, against a Rock hull rather than
a super-shielded Zoltan one.

> ⚠️ **Why this page exists at all:** like [[event-rock-nursery]], this is neither a test
> stub nor a UI string — it is finished content with no route to it. Paged because the
> disabling itself, and the reason recorded in the file, are findings worth keeping.
> Tagged `disabled` and `cut-content` so it is never read as reachable.

## Related
- [[event-rock-nursery]] — the other event commented out of `NEUTRAL_ROCK`
- [[event-rock-bride]] — the same LOW/MED vs HIGH boarding-reward asymmetry
- [[entity-zoltan]], [[entity-rock-men]]
- [[item-zoltan-shield]] — the balance concern named in the developer comment
- [[concept-cut-content]]

## Open Questions
- [ ] Was this ever enabled in a shipped build (vanilla 1.0), or disabled before release?
      The comment lives in the base `events_rock.xml`, which `dlcEventsOverwrite.xml` does
      not touch ([[source-events-rock]]).
- [ ] What `autoReward level="RANDOM">stuff` resolves to.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
