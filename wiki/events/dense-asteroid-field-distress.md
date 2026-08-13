---
id: event-dense-asteroid-field-distress
type: event
event_name: ASTEROID_DERELICT_SHIP
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: [[[item-rock-plating]]]
chain: [[[chain-crystal-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [crystal-route, ship-unlock, unique, blue-option, distress, hull-damage-risk, augment-reward]
---

# Dense asteroid field distress — `ASTEROID_DERELICT_SHIP`

## Summary
**Step 1 of [[chain-crystal-cruiser-unlock]]** — the beacon that can hand you the Damaged
Stasis Pod. Searching is a three-way gamble: a hull hit, a random salvage payout, or the
derelict that carries the pod. **Rock Plating skips the gamble entirely** and goes straight
to the derelict. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]]
- Event lists: `NEUTRAL_ENGI` ([[source-events-engi]]), `NEUTRAL_PIRATE`
  ([[source-events-pirate]]), `NEUTRAL_ROCK` ([[source-events-rock]])
- Allocation: `NEUTRAL_ENGI` 4–6 / 5–7, `NEUTRAL_PIRATE` 5–6, `NEUTRAL_ROCK` 7–8
  ([[source-sector-data-xml]])
- Beacon: carries `<distressBeacon/>` — the beacon shows the distress icon — but it lives in
  the **neutral** pools, not the `DISTRESS_BEACON_*` ones. Fandom calls this out as the only
  event in the game where that is true ([[source-fandom-dense-asteroid-field-distress]],
  [[source-events-xml]]).
- Long-range scanners show no ship ([[source-fandom-dense-asteroid-field-distress]])
- `unique="true"` — once per run

## Text
> A ship without life forms within a nearby dense asteroid field is giving off the distress
> call. Shall we investigate? It could be dangerous.

(`event_ASTEROID_DERELICT_SHIP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Search for the ship. | — | Rolls `ASTEROID_DERELICT_SHIP_SEARCH` (3 entries) — see below | 1/3 each |
| 2 | Avoid the area. | — | *"Discretion is the better part of valor. Better not risk it."* → nothing | 100% |
| 3 | **(Rock Plating)** Make a thorough search for the ship without fear of stray asteroids. | `req="ROCK_ARMOR"` | Rolls `ASTEROID_DERELICT_SHIP_ROCK` — a **one-entry** list that is the derelict outcome verbatim | 100% |

### Choice 1 → `ASTEROID_DERELICT_SHIP_SEARCH`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…a few asteroids get past your shields and partially damage your engines. You'll have to pull out!"* → `damage 4` + `damage 1 engines` (AE only) | 1/3 |
| 2 | *"You find a pirate ship, damaged and abandoned. You salvage what you can and move on."* → `autoReward level="RANDOM"` `standard` | 1/3 |
| 3 | The derelict — see below | 1/3 |

Three entries, no duplicates, so **1/3 each** under uniform selection across list entries
([[source-events-xml]]).

### The derelict (entry 3, or choice 3 outright)

> You find the decaying remains of some kind of ship coated with ice or crystal. You send
> some crew aboard to explore. Nearly everything is either destroyed or unidentifiable, but
> one of the weapons appears salvageable and there's a strange stasis pod that catches your
> eye.

> It looks like a massive asteroid is in a direct collision course with the derelict ship!
> You have to pull your crew out but they want to grab what they can first. What do they
> take?

| Choice | Outcome |
|---|---|
| Take the weapon and any spare scrap. | `autoReward level="LOW"` **`weapon`** |
| Grab the stasis chamber. | *"The pod appears to be functioning but you see nothing but shards of crystal inside. Perhaps someone else will know how to open it."* → `<augment name="STASIS_POD"/>` + `autoReward level="LOW"` `scrap_only` |

`ASTEROID_DERELICT_SHIP_ROCK` contains exactly one entry and its text ids duplicate the
`SEARCH_3` ones word for word — the Rock Plating branch is a **guaranteed** route to the
same fork ([[source-events-xml]], [[source-text-events-xml]]).

## Blue Options
- **[[item-rock-plating]]** (`req="ROCK_ARMOR"`, an augment) — converts a 1-in-3 shot at the
  Damaged Stasis Pod into a certainty and removes the 4–5 hull risk entirely. This is the
  single most valuable blue option on the Crystal route.

## Rewards & Risks
- **[[item-damaged-stasis-pod]]** (`STASIS_POD`) + `LOW` `scrap_only` — the chain payload.
- Or a `LOW` `weapon` instead, if you take the gun. Taking the weapon **forfeits the pod**
  and with it [[chain-crystal-cruiser-unlock]].
- Or `RANDOM` `standard` salvage from the pirate wreck.
- Risk: 4 hull (vanilla) / 5 hull and a dead engine (AE) on entry 1. There is no combat and
  no crew risk anywhere in this event.

## Version Differences
Base-`events.xml` event, so it exists in both editions. One `<!--DLC-->`-marked tag:
`<damage amount="1" system="engines"/>` in `SEARCH` entry 1 ([[source-events-xml]]). Vanilla
therefore takes **4 hull with no system damage**; AE takes 5 hull and loses engines.
Fandom's "5 hull damage, 1 damage to engines" describes the AE reading
([[source-fandom-dense-asteroid-field-distress]]).

## Strategy Notes
- *(Opinion.)* If you are running the Crystal route, this beacon is the whole reason to take
  an Engi, Pirate or Rock sector early — the pod must be found before you can reach
  [[event-ancient-device]].
- Taking the weapon is the correct call only if you have already given up on the chain; a
  `LOW` weapon is a poor trade for the run's rarest augment otherwise.
- With Rock Plating equipped there is no reason to pick choice 1.

## Related
- [[chain-crystal-cruiser-unlock]] — this is step 1 of 4. **Note:** that page currently
  links this event as `[[event-dense-asteroid-field-distress]]`, a slug that was never created;
  the page lives here, under the Fandom title. Needs fixing at lint.
- [[event-zoltan-research-facility]] — step 2, where the pod is opened
- [[event-ancient-device]] — step 3, where the pod's occupant matters
- [[event-crystal-unlock]] — the payoff
- [[item-damaged-stasis-pod]], [[item-rock-plating]]
- [[event-asteroid-belt-distress]] — the other asteroid-field distress call
- [[sector-rock-homeworlds]], [[sector-engi-controlled-sector]]

## Open Questions
- [ ] What `autoReward level="RANDOM"` resolves to — it is the only `RANDOM` level in this
      batch and no source states its range.
- [ ] Are `<eventList>` entries selected uniformly? The 1/3 figures assume it.
- [ ] Does taking the weapon permanently lock the Crystal chain for that run, or can the pod
      be found again? The event is `unique="true"`, which suggests not.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml` — `NEUTRAL_ENGI`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml` — `NEUTRAL_PIRATE`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml` — `NEUTRAL_ROCK`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-dense-asteroid-field-distress]] (per `raw/wiki/dense-asteroid-field-distress.md`)
