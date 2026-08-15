---
id: chain-rock-cruiser-unlock
type: chain
trigger_event: [[[event-rock-unlock1]]]
steps: [[[event-rock-unlock1]], [[event-rock-unlock2]], [[event-rock-unlock3]]]
sectors: [[[sector-rock-homeworlds]]]
reward: Rock Cruiser unlock + Rock Plating augment + 29 hull repairs
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 8
tags: [ship-unlock, rock-cruiser, sun-hazard, survive-dont-win, guaranteed-start]
---

# Rock Cruiser unlock

## Summary
Three events, two beacons, and one inverted win condition: the Rockmen challenge you to a
duel beside a star and the way to pass is to **not kill them**. Survive the sun until they
break off and jump, follow the coordinates they leave, and their shipyard hands over the
**Rock Cruiser**, the Rock Plating augment and 29 hull repairs
([[source-events-rock]], [[source-events-ships]]).

The chain is entirely contained in [[sector-rock-homeworlds]] and its entry beacon is
guaranteed there. Fandom covers the whole chain as one article —
[[source-fandom-rock-war-vessel-encounter]], *Rock war vessel encounter* — which
corroborates the sector, the elite hull, the 32-second escape countdown, and every reward
in the payoff step. The mechanical detail below still comes from the game files.

## How It Starts
- Trigger: [[event-rock-unlock1]] (`ROCK_UNLOCK1`), allocated directly on the `ROCK_HOME`
  sector description at `min="1" max="1"` and in no `eventList`
  ([[source-sector-data-xml]]). Guaranteed exactly once per Rock Homeworlds visit.
- `ROCK_HOME` is `unique="true"` with `minSector="4"`, the deepest entry gate of any
  unlock chain — you cannot start this before sector 5 ([[source-sector-data-xml]]).
- Notably **not** allocated in [[sector-rock-controlled-sector]]
  ([[source-sector-data-xml]]).
- The event is `unique="true"` ([[source-events-rock]]).

## Steps

1. **[[event-rock-unlock1]]** — `ROCK_UNLOCK1` (raw: events_rock.xml)
   A Rock war vessel sits at the beacon non-hostile and taunts you. Three choices:
   - *"We're going to save them or die trying."* → `<quest event="ROCK_UNLOCK2"/>`
   - *"We're strong enough to destroy you!"* → `<quest event="ROCK_UNLOCK2"/>`
   - *Ignore them.* → they jump away. **Chain over.**

   The first two are mechanically identical — same marker, different flavour. Only
   ignoring them loses the chain ([[source-events-rock]]).

2. **[[event-rock-unlock2]]** — `ROCK_UNLOCK2`, the sun duel (raw: events_rock.xml)
   The quest marker. It now has its own page carrying the `ROCK_UNLOCK2` join key; it is
   also walked through in context on [[event-rock-unlock1]].

   ```
   <ship load="ROCK_UNLOCK2" hostile="true"/>
   <environment type="sun"/>
   ```
   The enemy is `auto_blueprint="ROCK_ASSAULT_ELITE"` — an elite hull, not the ordinary
   `SHIPS_ROCK` ([[source-events-ships]]).

   | Ship outcome | Payload | Chain |
   |---|---|---|
   | `<escape timer="32" min="28" max="28">` → `<gotaway>` | `<quest event="ROCK_UNLOCK3"/>` | ✅ **the only advancing outcome** |
   | `<destroyed>` | `autoReward MED standard` | ❌ dead |
   | `<deadCrew>` | `autoReward HIGH standard` | ❌ dead |

   > ⚠️ **THE INVERSION.** Winning the fight ends the chain. The quest tag sits on
   > `<gotaway>` — you must keep the Rock ship alive beside a star long enough for its
   > 32-second escape to complete ([[source-events-ships]]). Both kill branches pay scrap
   > and nothing else.

3. **[[event-rock-unlock3]]** — `ROCK_UNLOCK3` (raw: events_rock.xml)
   A Rockman shipyard with your former opponent already docked and under repair. No real
   choices — two nested continues:
   ```
   <unlockShip id="6"/>                 → Rock Cruiser
   … then …
   <augment name="ROCK_ARMOR"/>         → Rock Plating
   <damage amount="-29"/>               → 29 hull repaired
   ```
   No fight, no failure branch ([[source-events-rock]]).

## Requirements
- **Routing** into [[sector-rock-homeworlds]] — `unique="true"`, `minSector="4"`. This is
  the chain's only hard requirement and its main constraint: the Rock Homeworlds compete
  for the same late-run slot as the [[chain-crystal-cruiser-unlock]]'s step 3.
- **Survivability beside a sun for the duration of a 32-second escape timer.** Solar
  flares set rooms alight while the enemy's all-Rock crew ignores fire
  ([[entity-rock-men]]). In practice this means hull to spare, a fire plan, or both.
- **No crew, system or augment gate anywhere in the chain** — not one `req=` attribute
  appears in any of the three events ([[source-events-rock]]).
- Fuel for two extra jumps.

## Reward
- **Rock Cruiser** unlocked (`<unlockShip id="6"/>`)
- [[item-rock-plating]] (`ROCK_ARMOR`) — `stackable=false`, rarity 0, so it is **not sold
  in stores**; this chain and its siblings are the way to get it ([[source-blueprints]])
- **29 hull repairs** — on a 30-hull cruiser, very nearly a full heal
- No scrap. Ironically, killing the step-2 ship pays *more* scrap than completing the
  chain does ([[source-events-ships]]).

Id 6 → Rock Cruiser is corroborated two ways: `blueprints.xml` carries an explicit
`<!-- SHIP ID = 6 -->` comment on the `PLAYER_SHIP_ROCK` block ([[source-blueprints]]),
and the ship's unlock hint reads *"Prove yourself to the Rockmen to earn this powerful
cruiser."* (`ship_PLAYER_SHIP_ROCK_unlock`, [[source-text-blueprints]]) — which is this
chain and no other.

## Failure Modes
- **The Rock Homeworlds never appear**, or appear too late to route to. `minSector="4"` +
  `unique="true"` makes this the commonest failure.
- **Ignoring the challenge at step 1.** No marker is placed.
- **Winning the step-2 duel.** Destroying the ship or killing its crew converts the unlock
  into `MED`/`HIGH` scrap. Like the Engi chain's step 2, this fails silently.
- **Dying to the sun.** You must survive an elite Rock hull *and* solar flares for the
  full escape timer, with no option to disengage.
- The Rebel fleet reaching a marked beacon first.

## Strategy Notes
- *Opinion:* treat step 2 as a survival encounter, not a fight. Power engines and shields,
  leave weapons cold if your damage output risks overkill, and keep crew off burning
  rooms. The only thing you must do is still be alive when their timer runs out.
- Ion or crew-kill weapons are actively dangerous here — `<deadCrew>` ends the chain just
  as `<destroyed>` does.
- The 29-hull repair alone makes the detour worth taking even on a run where the Rock
  Cruiser is already unlocked. *(Opinion.)*
- A developer comment at the top of the SPECIAL block in `events_rock.xml` describes the
  intended shape: *"unlock - Asked to prove the federation is worth of rock fighters -
  follow him to a sun - fight in an sun - must let them escape. then a normal fight and
  you must let them surrender"* ([[source-events-rock]]).

  > ⚠️ **CONTRADICTION (design comment vs. shipped data):** that comment describes a
  > *second* fight with a surrender at the end. The shipped `ROCK_UNLOCK3` contains no
  > fight and no surrender — it is a pure reward event, and the "let them escape"
  > condition sits on `ROCK_UNLOCK2` instead ([[source-events-rock]],
  > [[source-events-ships]]). Read as a stale design note describing a cut step, not as
  > evidence of a missing beacon. Kept because it is the only in-file statement of the
  > chain's intended design.

## Related
- [[sector-rock-homeworlds]] — the chain's sector
- [[chain-crystal-cruiser-unlock]] — the *other* guaranteed unlock beacon in the same
  sector ([[event-ancient-device]]); both compete for the same late-run routing
- [[item-rock-plating]] — the augment awarded
- [[entity-rock-men]], [[concept-solar-flares]]

## Open Questions
- [ ] What the `escape timer="32" min="28" max="28"` numbers denote in combat seconds.
- [ ] Which sector the `ROCK_UNLOCK3` marker is placed in — the files do not pin it, so
      [[event-rock-unlock3]] carries `sectors: []`.
- [ ] Does ignoring at step 1 lock the unlock for the run, or only for that sector?
- [x] ~~Both step pages record `version: ae`; this page records `both`.~~ **Closed (lint,
      2026-08-13):** all three step pages and this page now read `both`. The reasoning stated
      here was right — base `events_rock.xml`, no `<!--DLC-->` markers, no override in
      `dlcEvents*.xml` — and the 2026-08-09 `version:` retrofit applied it; only the question
      was left open. See [[event-rock-unlock2]].
- [ ] [[source-fandom-rock-war-vessel-encounter]] covers the chain but adds no odds and no
      routing advice; in-play timings beyond the 32-second escape countdown remain unsourced.
- [ ] Fandom claims the Rock Cruiser is also unlocked by winning a run with the Slug
      Cruiser. `achievements.xml` records no unlock conditions at all
      ([[source-achievements]]), so this raw set cannot check it — see [[event-rock-unlock1]].
      The nearest thing to a statement is the in-game hint string
      `ship_PLAYER_SHIP_ROCK_unlock` — *"Prove yourself to the Rockmen to earn this powerful
      cruiser"* ([[source-text-blueprints]], per `raw/gamedata/text_blueprints.xml`) — which
      describes **this chain and no other route**. That is suggestive, not decisive: the hint
      strings are one-line marketing copy and the Lanius hint is the only one that spells out
      a second condition, so silence about a Slug-Cruiser route is not evidence of absence.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
- [[source-fandom-rock-war-vessel-encounter]] (per raw/wiki/rock-war-vessel-encounter.md)
