---
id: event-rock-unlock1
type: event
event_name: ROCK_UNLOCK1
sectors: [[[sector-rock-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-rock-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rock, ship-unlock, quest, guaranteed, unique]
---

# Rock cruiser unlock, step 1 — `ROCK_UNLOCK1`

## Summary
The opening beacon of the Rock Cruiser unlock quest. A Rock war vessel challenges you to
prove the Federation is worth saving and gives you coordinates. It is **guaranteed** in
[[sector-rock-homeworlds]] — `min="1" max="1"` — so every visit to the Rock Homeworlds
offers this chain once.

## Trigger & Where It Appears
- Sector: **[[sector-rock-homeworlds]] only** (`ROCK_HOME`, `minSector="4"`,
  `unique="true"` sector)
- Allocation: `<event name="ROCK_UNLOCK1" min="1" max="1"/>` — guaranteed exactly once
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`). It is **not** in any
  `eventList`; the sector places it directly.
- Notably **absent** from [[sector-rock-controlled-sector]], which allocates neither this
  nor `ROCK_CRYSTAL_BEACON` ([[source-sector-data-xml]]).
- Beacon: ship present but non-hostile — `<ship load="ROCK_UNLOCK2" hostile="false"/>`
  ([[source-events-rock]])
- `unique="true"` ([[source-events-rock]])
- **Fandom coverage:** [[source-fandom-rock-war-vessel-encounter]] (per
  `raw/wiki/rock-war-vessel-encounter.md`) documents this beacon and both of its quest
  markers as a single article, *Rock war vessel encounter*. It independently confirms the
  sector (**Rock Homeworlds**, `unique`), and adds that **Long-Ranged Scanners show a ship**
  at this beacon.
  - Its Trivia section states the event *"is called `ROCK_UNLOCK` in the datafiles"*. No
    event with that bare id exists; the datafiles use `ROCK_UNLOCK1` / `ROCK_UNLOCK2` /
    `ROCK_UNLOCK3` ([[source-events-rock]]). Read `ROCK_UNLOCK` as the family name the
    article covers, not an exact id.

## Text
> You are immediately messaged by an imposing looking Rock war vessel, "You're the ship
> off to 'save the Federation,' aren't you? And you expect to survive with that hunk of
> junk?"

(`event_ROCK_UNLOCK1_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | "We're going to save them or die trying." | — | *"The latter being more likely. Still... we can potentially help you and your precious fleet, but you'll need to prove yourself first. Meet us at these coordinates." They jump away.* → `<quest event="ROCK_UNLOCK2"/>` | 100% |
| 2 | "We're strong enough to destroy you!" | — | *"One ship is not the same as a fleet, but at least you've got some fire. Meet us at these coordinates if you want to prove to us that the Federation is worth saving." They jump away.* → `<quest event="ROCK_UNLOCK2"/>` | 100% |
| 3 | Ignore them. | — | *"Heh. Like I expected. If the Federation is as weak as you it deserves to fall." They jump away without another word.* **Chain over.** | 100% |

Choices 1 and 2 are mechanically identical — both place the same quest marker. Only
choice 3 differs, and it ends the chain permanently for that run
([[source-events-rock]]).

## Step 2 — `ROCK_UNLOCK2` (the quest marker)
Walked through here because it is the `quest` target of this event and has no separate entry
in any sector event list. It also has its own page — [[event-rock-unlock2]] — which carries
the `ROCK_UNLOCK2` join key.

> You arrive at the coordinates given and find yourself dangerously close to an M-class
> star! The other ship messages you, "Let's see how long your puny ship can handle this
> heat! Prepare for a challenge!"

- `<ship load="ROCK_UNLOCK2" hostile="true"/>` and `<environment type="sun"/>`
  ([[source-events-rock]])
- The enemy is `auto_blueprint="ROCK_ASSAULT_ELITE"` — an elite hull, not the ordinary
  `SHIPS_ROCK` ([[source-events-ships]])

**The win condition is to *not* win.** The ship definition reads:

| Branch | Text | Effect |
|---|---|---|
| `<escape timer="32" min="28" max="28">` | *"The Rock ship starts to power up their FTL drive. If we're going to earn their trust we must endure the heat for as long as they can!"* | they begin to flee |
| `<gotaway>` | *"As they jump away they relay coordinates to your navigation system. They must mean for you to follow them!"* | **`<quest event="ROCK_UNLOCK3"/>`** — the chain continues |
| `<destroyed>` | *"Their ship breaks apart and you feel a twinge of guilt. Perhaps they could have helped the Federation if this had gone another way."* | `<autoReward level="MED">standard</autoReward>` — **chain ends** |
| `<deadCrew>` | *"Their ship goes quiet and you feel a twinge of guilt…"* | `<autoReward level="HIGH">standard</autoReward>` — **chain ends** |

Killing them pays scrap and forfeits the ship unlock. Letting them escape — surviving the
sun for the escape timer — is the only path to [[event-rock-unlock3]].

Fandom corroborates every branch of this table and adds two things the files do not state:
the escape countdown is **32 seconds** of real time (so `timer="32"` is seconds, not turns
or jumps), and **Long-Ranged Scanners report "ship + red giant"** at the quest marker, which
is how you identify it on the map before jumping
([[source-fandom-rock-war-vessel-encounter]]). It also glosses the `MED` / `HIGH`
`standard` payouts as *"scrap with resources"*, matching this wiki's reading of `standard`.

> ⚠️ **CONTRADICTION (Fandom-only, unverified):** Fandom's lede states *"the ship can also
> be unlocked by winning the game with the Slug Cruiser"*
> ([[source-fandom-rock-war-vessel-encounter]]). `achievements.xml` contains **no**
> unlock-condition entries at all — the string `unlock` does not appear in the file — so
> nothing in this raw set supports or refutes a victory-based alternative path
> ([[source-achievements]]). Recorded as a Fandom-only claim. The same pattern appears on
> [[event-legendary-thief-kazaaakplethkilik]], where Fandom asserts a Zoltan-Cruiser-victory
> unlock that is likewise absent from `achievements.xml`; whatever encodes these paths is
> not in the extracted files.

## Blue Options
None anywhere in the chain's first two steps.

## Rewards & Risks
- Step 1 itself: no reward, no cost, no risk. The ship is non-hostile.
- Step 2: a fight beside a **sun** against an elite Rock hull, which you are supposed to
  *survive rather than win*. Solar flares set your rooms on fire while an all-Rock crew
  ignores them ([[entity-rock-men]]).
- Killing the step-2 ship converts the chain into `MED`/`HIGH` scrap. That is the
  consolation prize, not the goal.

## Strategy Notes
- The developer comment in `events_rock.xml` states the design intent plainly:
  *"unlock - Asked to prove the federation is worth of rock fighters - follow him to a sun
  - fight in an sun - must let them escape. then a normal fight and you must let them
  surrender"* ([[source-events-rock]]). Note the comment describes a *surrender* at the
  final step that the shipped `ROCK_UNLOCK3` event does not contain — see
  [[event-rock-unlock3]].
- Do not over-damage the step-2 ship. The escape has a timer (`timer="32"`,
  `min="28" max="28"`); you need it alive when that fires.
- Fire suppression, or a Rock crew member, materially changes how survivable step 2 is.

## Related
- [[chain-rock-cruiser-unlock]] — the chain this starts
- [[event-rock-unlock3]] — step 3, the payoff
- [[event-ancient-device]] — the *other* guaranteed unlock beacon in the same sector
- [[sector-rock-homeworlds]], [[entity-rock-cruiser]], [[concept-solar-flares]]
- [[event-rock-unlock2]] — step 2, the sun duel (`ROCK_UNLOCK2`)

## Open Questions
- [x] ~~What the `escape timer="32"` number denotes~~ — **seconds**, per
      [[source-fandom-rock-war-vessel-encounter]]. What `min="28" max="28"` denotes is still open.
- [ ] Whether the `ROCK_UNLOCK3` quest marker appears in the current sector or the next.
      Fandom's `{{Locations|Rock Homeworlds}}` header covers the whole article, but that
      template describes the *entry* beacon, so it is not evidence about the markers.
- [ ] Whether choices 1 and 2 differ in any way not visible in the XML.
- [ ] Does ignoring at step 1 lock the unlock for the whole run, or only that sector?
- [ ] Where the Slug-Cruiser-victory unlock path is encoded, if it exists — it is in
      neither `achievements.xml` nor any event file.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml — checked for the
  Slug-Cruiser-victory unlock path; no unlock conditions present)
- [[source-fandom-rock-war-vessel-encounter]] (per raw/wiki/rock-war-vessel-encounter.md)
