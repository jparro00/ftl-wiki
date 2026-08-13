---
id: event-slug-comm-tapping
type: event
event_name: QUEST_SLUG_PIRATE_TRAP
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, quest-marker, pirate, free-quest]
---

# Slug comm tapping — `QUEST_SLUG_PIRATE_TRAP`

## Summary
Two Slug ships plotting a raid on a wealthy pirate, unaware you are listening. Tapping the
comms is entirely free and adds a quest marker; at the marker you choose whether to play
along with the Slugs' fifty-fifty split or cut them out. Playing along pays the most.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Listed in **two** event lists: `NEBULA_NEUTRAL_SLUG` (`min 3 / max 5` per sector) and
  `QUESTS_SLUG`, with a dev note *"JUSTIN TO DO - For now i'm putting quests into neutral"*
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`

## Text
> You arrive to the sight of two Slug ships in communication range. They don't see you.

(`event_QUEST_SLUG_PIRATE_TRAP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

Both choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Tap their comm frequency. | — | "…you note down their target co-ordinates." → `<quest event="QUEST_SLUG_PIRATE_TRAP2"/>` — a quest marker is added to your map. | 100% |
| 2 | Ignore them. | — | "You have no interest in anything the Slugs could make business out of." Nothing happens. | 100% |

There is no cost or risk attached to choice 1.

### The quest marker — `QUEST_SLUG_PIRATE_TRAP2`

A nebula beacon (`<environment type="nebula"/>`). Documented here as an outcome; it is a
separate event id in the data files ([[source-events-slug]]).

> You catch up with the two Slug ships and they're already carrying out their raid! One is
> in close combat with the pirate, the other seems to be heading for a small space cache
> the pirate was protecting.

Then, after a *Continue*: *"Suddenly the first ship bursts into flames, and an urgent call
arrives from the remaining Slugs. 'We sssugest you distract the pirate vesssel while we
retrieve the valuables. Fifty fifty sssplit.'"*

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Engage the pirate. | `<ship load="QUEST_SLUG_PIRATE_TRAP1" hostile="true"/>` |
| 2 | Head for the cache. | The Slugs jump off — `<ship load="QUEST_SLUG_PIRATE_TRAP2" hostile="true"/>` |

**`QUEST_SLUG_PIRATE_TRAP1`** (`SHIPS_PIRATE`) — `<surrender chance="0" min="3" max="4">`
with a scripted branch, `destroyed` `MED standard`, `deadCrew` `HIGH standard`
([[source-events-ships]]). When it breaks:

> When the pirate ship looks ready to break apart you notice the Slug ship has secured the
> loot and is preparing to jump away!

- *Continue fighting the pirate.* → the fight continues (then `MED`/`HIGH standard`).
- *Let the pirate escape and go after the Slugman ship.* → the Slugs pay up:
  `<autoReward level="HIGH">scrap_only</autoReward>`, pirate set non-hostile.

**`QUEST_SLUG_PIRATE_TRAP2`** (`SHIPS_PIRATE`) — no surrender or escape block;
`destroyed` `LOW standard`, `deadCrew` `MED standard`, and the cache is lost in the clouds
either way ([[source-events-ships]]).

Fandom describes `chance="0"` on `QUEST_SLUG_PIRATE_TRAP1` as "surrenders at 30–40% hull",
i.e. always ([[source-fandom-slug-comm-tapping]]) — the same reading it applies to
[[event-slug-home-nebula-surrender]]. See that page for the discrepancy.

## Rewards & Risks
- Free quest marker; the only cost is the jump to reach it.
- Best payout: **`HIGH scrap_only`** for letting the pirate go and collecting the Slugs'
  split — or `HIGH standard` for killing `QUEST_SLUG_PIRATE_TRAP1`'s crew.
- Worst payout: `LOW standard` for destroying `QUEST_SLUG_PIRATE_TRAP2` after cutting the
  Slugs out.
- Risk: an ordinary pirate ship fight, in a nebula, with no way to decline once you arrive
  at the marker (the only choice is which target).

## Strategy Notes
- Cooperating with the Slugs pays better than double-crossing them: choice 1 at the marker
  leads to `MED`/`HIGH standard` or `HIGH scrap_only`, while choice 2 tops out at `MED`.
  *(Opinion, from the reward levels in [[source-events-ships]].)*
- If you can crew-kill, staying on the pirate is worth more than taking the Slugs' cut
  (`HIGH standard` beats `HIGH scrap_only`).
- Tapping the comms is unconditionally free — there is no reason to pick choice 2 except to
  save the jump.

## Related
- [[event-slug-home-nebula-surrender]] — the other Slug quest marker, and the same
  `chance="0"` reading
- [[entity-pirates]], [[entity-slugs]]
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- [[event-quest-slug-pirate-trap2]] — the `QUEST_SLUG_PIRATE_TRAP2` quest beacon, on its own page

## Open Questions
- [x] ~~Whether `QUEST_SLUG_PIRATE_TRAP2` deserves its own page~~ — it has one:
      [[event-quest-slug-pirate-trap2]], created to carry the distinct join key.
- [ ] What `chance="0"` means in a `<surrender>` block.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-comm-tapping]] (per raw/wiki/slug-comm-tapping.md)
