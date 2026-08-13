---
id: event-slug-ship-boarding-rock-ship
type: event
event_name: SLUG_DISTRESS_ROCK
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, distress, nebula, combat, optional-fight, default-rewards]
---

# Slug ship boarding Rock ship — `SLUG_DISTRESS_ROCK`

## Summary
Slugs are boarding a disabled Rock freighter. Intervening is a coin flip between a free
bloodless win and a fight against a Slug ship worth up to two `MED standard` payouts.
Walking away is usually free, but a third of the time the Rockmen decide you were complicit
and attack you.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `DISTRESS_BEACON_SLUG` event list (`min 3 / max 4` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: **distress** (`<distressBeacon/>`) in a nebula
  (`<environment type="nebula"/>`), `unique="true"` ([[source-events-slug]])

## Text
> You arrive to find a Slug ship in the middle of boarding a disabled Rock freighter.

(`event_SLUG_DISTRESS_ROCK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Engage the Slug ship. | — | Rolls `SLUG_DISTRESS_ROCK_FIGHT` — 2 entries. | see below |
| 2 | Ignore them. | — | Rolls `SLUG_DISTRESS_ROCK_AVOID` — 3 entries. | see below |

Choice 1 is `hidden="true"`; choice 2 is not.

### `SLUG_DISTRESS_ROCK_FIGHT` (choice 1)

| Entry | Text | Effect |
|---|---|---|
| 1 | "You charge weapons and the Slugs immediately back down… the Rockmen have already repaired the worst of their damage and jump away without another word." | Nothing — no fight, no reward |
| 2 | "You charge weapons and the Slugs quickly change course to meet your charge." | `<ship load="JELLY_DISTRESS_ROCK" hostile="true"/>` |

`JELLY_DISTRESS_ROCK` (`SHIPS_JELLY`) — `MED standard` on both `destroyed` and `deadCrew`,
no surrender or escape block, then a *Continue* into `SLUG_DISTRESS_ROCK_RESULT`
([[source-events-ships]]):

| Entry | Text | Effect |
|---|---|---|
| 1 | "It appears that the Rock ship left during your battle. You doubt they could have been more ungrateful…" | Nothing further |
| 2 | "After the battle the Rock ship hails you. Their captain simply says, 'Thanks.' and jumps away." | Nothing further |
| 3 | "It appears the Rock ship was long since abandoned. You strip what you can from it." | `<autoReward level="MED">standard</autoReward>` — a **second** medium payout |

### `SLUG_DISTRESS_ROCK_AVOID` (choice 2)

| Entry | Text | Effect |
|---|---|---|
| 1, 2 | "You have no desire to provoke Slugs in their own territory. You leave them alone." (two near-identical entries) | Nothing |
| 3 | "…the Rock ship spring[s] to life and decimate[s] the other ship. They message you, 'Pathetic. You are either a coward or an ally of the Slugs. Either way, you don't deserve to live.'" | `<ship load="ROCK_SHIP" hostile="true"/>` — default rewards |

`ROCK_SHIP` (`SHIPS_ROCK`) — `<surrender chance="0.7" min="3" max="4" load="ROCK_SHIP_SURRENDER"/>`,
no escape block, default destroyed/deadCrew ([[source-events-ships]]). A 70% surrender roll
is unusually generous.

## Rewards & Risks
- Choice 1: half the time nothing at all; half the time a `MED standard` Slug kill, with a
  1-in-3 chance of a further `MED standard` from the derelict freighter.
- Choice 2: two-thirds nothing, one-third a Rock ship fight at default rewards — with a 70%
  chance the Rock ship surrenders once damaged.
- Neither Slug nor Rock ship can escape, so no reward can run away from you.

## Strategy Notes
- Choice 1 is the higher-EV line and its downside is "nothing happens", not damage. *(Opinion,
  from the entry weightings in [[source-events-slug]].)*
- Choice 2's ambush is the only way to be attacked here, and it fires on a third of
  attempts — "ignore them" is not the safe option it reads as.
- The stacked `MED standard` on choice 1 (Slug kill + abandoned freighter) is the best
  outcome in the event.

## Related
- [[event-mantis-ship-attacking-slug-ship]], [[event-slug-oxygen-malfunction]],
  [[event-slug-moons-question]], [[event-slocknog]] — the rest of `DISTRESS_BEACON_SLUG`
- [[entity-rock-men]], [[entity-slugs]]
- [[event-rock-ship-surrender]] — the `ROCK_SHIP_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Whether the entries in each list are equally weighted.
- [ ] Contents of `ROCK_SHIP_SURRENDER` (defined outside this file).

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-ship-boarding-rock-ship]] (per raw/wiki/slug-ship-boarding-rock-ship.md)
