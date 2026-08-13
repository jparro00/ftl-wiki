---
id: event-rock-unlock2
type: event
event_name: ROCK_UNLOCK2
sectors: [[[sector-rock-homeworlds]]]
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-rock-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rock, ship-unlock, quest, combat, sun-hazard, ship-escape, chain-breaker]
---

# Rock cruiser unlock, step 2 — `ROCK_UNLOCK2`

## Summary
The trial by fire. The Rock war vessel from [[event-rock-unlock1]] challenges you to a duel
beside an M-class star, and the *only* way to advance the chain is to **let it escape**.
Destroying it — or killing its crew — pays scrap and silently ends the Rock Cruiser unlock.
It is the single most common way the chain is lost.

## Trigger & Where It Appears
- **Not in any sector event list.** It is a **quest-marker beacon**, placed by
  `<quest event="ROCK_UNLOCK2"/>` on *both* accepting branches of [[event-rock-unlock1]]
  ([[source-events-rock]]). The third branch ("Ignore them") places no marker and ends the
  chain immediately.
- Sector: [[sector-rock-homeworlds]], inherited from step 1, which `sector_data.xml`
  allocates `min="1" max="1"` — guaranteed once per Rock Homeworlds visit
  ([[source-sector-data-xml]]).
- `<environment type="sun"/>` — **the beacon is a solar flare hazard**: periodic fires and
  hull damage on both ships for the duration of the fight.
- Long-Range Scanners show a ship, and the beacon renders with the red-giant hazard art
  ([[source-fandom-rock-war-vessel-encounter]]).
- **Version:** `both`. `events_rock.xml` is a base file, the definition carries no
  `<!--DLC-->` markers, and the `sector_data.xml` allocation of step 1 is unmarked.

> ⚠️ **CONTRADICTION (internal to this wiki, not the sources):** [[event-rock-unlock1]] and
> [[event-rock-unlock3]] are both tagged `version: ae` and state that *no Fandom page covers
> them*. Neither holds up: the chain is base-file content with no DLC markers, and
> [[source-fandom-rock-war-vessel-encounter]] documents all three stages. Flagged for a
> human to reconcile the sibling pages rather than edited here.

## Text
> You arrive at the coordinates given and find yourself dangerously close to an M-class
> star! The other ship messages you, "Let's see how long your puny ship can handle this heat!
> Prepare for a challenge!"

(`event_ROCK_UNLOCK2_text`, per [[source-text-events-xml]])

Combat starts immediately — `<ship load="ROCK_UNLOCK2" hostile="true"/>` sits in the event
body and the event has **no choices at all**.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is text, ship and environment only)* | — | Fight the `ROCK_UNLOCK2` hull beside a sun. | 100% |

### The `ROCK_UNLOCK2` hull ([[source-events-ships]])

`auto_blueprint="ROCK_ASSAULT_ELITE"` — the Rock Assault (Elite), the heaviest Rock hull
the game fields outside the Flagship.

| Resolution | Declaration | Outcome |
|---|---|---|
| **Escape attempt** | `<escape timer="32" min="28" max="28">` — no `chance` attribute; a source comment records the timer *"was 24"* | *"The Rock ship starts to power up their FTL drive. If we're going to earn their trust we must endure the heat for as long as they can!"* The block re-asserts `<ship hostile="true"/>`, so the fight continues while the FTL charges. |
| **Got away** ✅ | — | *"As they jump away they relay coordinates to your navigation system. They must mean for you to follow them!"* → `<quest event="ROCK_UNLOCK3"/>` — **the chain continues.** No scrap. |
| **Destroyed** ❌ | — | *"Their ship breaks apart and you feel a twinge of guilt…"* → `MED standard`. **Chain over.** |
| **Dead crew** ❌ | — | *"Their ship goes quiet and you feel a twinge of guilt…"* → `HIGH standard`. **Chain over.** |

The developer comment above `ROCK_UNLOCK1` states the design in as many words: *"follow him
to a sun - fight in an sun - **must let them escape**. then a normal fight and you must let
them surrender"* ([[source-events-rock]]).

## Blue Options
None. The event has no choices, and the ship block declares no `req` anywhere.

## Rewards & Risks
- **Advancing the chain pays nothing here.** The reward is the `ROCK_UNLOCK3` quest marker.
- Killing the ship pays `MED standard` (destroyed) or `HIGH standard` (dead crew) and costs
  you the Rock Cruiser, the Rock Plating augment and 29 hull repairs at step 3
  ([[source-fandom-rock-war-vessel-encounter]]).
- **Risk: the sun.** Solar flares set fires on your ship throughout, and you must survive
  the full escape countdown rather than ending the fight quickly.
- Risk of accidental failure is high — a Rock Assault (Elite) at low hull dies easily to a
  beam or a stray volley you did not mean to fire.

## Strategy Notes
- *Opinion:* **stop shooting once the FTL starts charging.** Damage output is actively
  harmful from that moment. Vent fires, repair, and wait out the 32-second timer.
- If you have boarders, do not send them — a dead crew ends the chain just as surely as a
  destroyed hull.
- Fire suppression, or Rock crew (immune to fire), materially changes how survivable this
  beacon is. Consider making the purchase before taking the marker.
- If you do not want the Rock Cruiser, killing the ship for `HIGH standard` is a legitimate
  play — just make it a decision rather than an accident.

## Related
- [[event-rock-unlock1]] — step 1, which places this marker
- [[event-rock-unlock3]] — step 3, reached only via the *got away* branch
- [[chain-rock-cruiser-unlock]] — the chain
- [[event-ancient-device]] — the other guaranteed quest beacon in the same sector
- [[sector-rock-homeworlds]], [[entity-rock-men]]
- [[concept-surrender-offers]] — on reading `min`/`max` as hull points

## Open Questions
- [ ] What `escape timer="32" min="28" max="28"` means precisely — Fandom reads the timer as
      32 seconds, but the `min`/`max` hull band is unexplained.
- [ ] Whether the `ROCK_UNLOCK3` marker lands in the current sector or the next.
- [ ] Whether solar-flare damage can destroy the enemy hull for you and break the chain by
      accident.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-war-vessel-encounter]] (per raw/wiki/rock-war-vessel-encounter.md)
