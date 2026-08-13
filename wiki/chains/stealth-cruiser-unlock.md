---
id: chain-stealth-cruiser-unlock
type: chain
trigger_event: [[[event-engi-fleet-discussion]]]
steps: [[[event-engi-fleet-discussion]], [[event-engi-unlock-2real]], [[event-engi-unlock-3]], [[event-engi-unlock-4]]]
sectors: [[[sector-engi-homeworlds]]]
reward: Stealth Cruiser unlock + Titanium System Casing + HIGH scrap + 20 hull
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [ship-unlock, stealth-cruiser, engi, blue-option, decoy, chain-failure-risk, four-step]
---

# Stealth Cruiser unlock (the Engi Homeworlds quest)

## Summary
Four beacons in the [[sector-engi-homeworlds]] that end with `<unlockShip id="1"/>` — the
**Stealth Cruiser** — plus the Titanium System Casing augment, `HIGH` scrap with resources
and 20 hull repairs ([[source-events-engi]]). Everyone calls it "the Engi quest", which is
the source of the most common naming error in this wiki: **it does not unlock the Engi
Cruiser.** See *The naming trap* below.

Two things make it the most losable chain in the game. It is gated behind an **Engi crew
member** at step 1, and step 2 sends you to two identical-looking beacons, only one of
which is real — and at the real one, the obvious way to win the fight silently kills the
quest.

## The naming trap
`<unlockShip id="1"/>` at [[event-engi-unlock-4]] is the **Stealth Cruiser**, not the Engi
Cruiser. The evidence:

- `ship_PLAYER_SHIP_STEALTH_unlock`: *"This ship is being built near the Engi homeworlds.
  To unlock it you'll need to help them, but they only trust their own kind."* — a
  description of this chain, including its Engi-crew gate ([[source-text-blueprints]]).
- `ship_PLAYER_SHIP_CIRCLE_unlock` (the Engi Cruiser): *"To unlock this Engi ship you'll
  need to get to the 5th sector with any layout of the Kestrel."* — an achievement
  condition, **not an event chain** ([[source-text-blueprints]]).
- `[[event-engi-unlock-4]]`'s own text names the prize: *"Project X-ME56 … Advanced
  stealth cruiser."* ([[source-text-events-xml]])
- No `<unlockShip>` tag anywhere in `raw/gamedata/` uses the Engi Cruiser's id — every
  `<unlockShip>` in the whole data set resolves to id 1, 2, 4, 5, 6, 7 or 8, across
  `events_engi.xml`, `events_mantis.xml`, `events_rebel.xml`, `events_rock.xml`,
  `events_ships.xml`, `events_zoltan.xml` and `events_crystal.xml`.

There is therefore **no Engi Cruiser unlock chain to write**. There is also a second,
dead route to the Stealth Cruiser: [[event-unlock-stealth]] (`UNLOCK_STEALTH`), a shipped
but unreferenced event in `newEvents.xml` that awards nothing ([[source-newevents]]).

## How It Starts
- Trigger: [[event-engi-fleet-discussion]] (`ENGI_UNLOCK_1`), **guaranteed** in
  [[sector-engi-homeworlds]] — `sector_data.xml` allocates it on the `ENGI_HOME` sector
  description at `min="1" max="1"` ([[source-sector-data-xml]]). Its `NEUTRAL_ENGI` list
  entry is commented out, so the sector allocation is the only live reference
  ([[source-events-engi]]).
- `ENGI_HOME` is `unique="true"` with `minSector="2"` ([[source-sector-data-xml]]).
- The event is `unique="true"` ([[source-events-engi]]).

## Steps

1. **[[event-engi-fleet-discussion]]** — `ENGI_UNLOCK_1` (raw: events_engi.xml)
   A civilian Engi fleet arguing over an open channel. Two ordinary choices ("ask if you
   can help", "ignore it") both dead-end. The third is `<choice req="engi" hidden="true">`
   — **(Engi Crew) Have your Engi crewmember contact them.** Offering help then places
   **two** quest markers in one pass:
   ```
   <quest event="ENGI_UNLOCK_2REAL"/>   … then, on the forced continue:
   <quest event="ENGI_UNLOCK_2FAKE"/>
   ```
   One real base, one decoy, and the game does not tell you which is which
   ([[source-events-engi]]).

2. **[[event-engi-unlock-2real]]** — `ENGI_UNLOCK_2REAL` (raw: events_engi.xml)
   *"…It appears abandoned except for one scout ship."* No choices: it loads
   `REBEL_ENGI_UNLOCK_2REAL` hostile immediately, and that ship starts fleeing at once on
   a 40-second `<escape>` timer ([[source-events-ships]]).

   | Ship outcome | Payload | Chain |
   |---|---|---|
   | `<gotaway>` | nothing | ❌ dead |
   | `<destroyed>` | `autoReward MED standard` — **no `<quest>` tag** | ❌ dead |
   | `<surrender min="5" max="5">` → [[event-engi-unlock-2real-surrender]] | `<quest event="ENGI_UNLOCK_3"/>`, no scrap | ✅ |
   | `<deadCrew>` | `autoReward HIGH standard` **and** `<quest event="ENGI_UNLOCK_3"/>` | ✅ |

   > ⚠️ **THE TRAP.** `<destroyed>` carries **no `<quest>` tag**
   > ([[source-events-ships]]). Blowing the scout up pays `MED` scrap and ends the chain
   > with no message, no marker and no indication anything was lost. Only a surrender or a
   > crew kill passes the quest along. Fandom's walkthrough documents escape, surrender
   > and dead crew for this beacon and **omits the destroyed branch entirely**
   > ([[source-fandom-engi-fleet-discussion]]) — this is a game-files-only finding, and
   > the single most important fact in the chain.

   The decoy — **[[event-engi-unlock-2fake]]** (`ENGI_UNLOCK_2FAKE`) — shares the intro
   text word for word and loads a structurally identical Rebel scout. Its surrender goes
   to [[event-engi-unlock-2fake-surrender]] and **no branch of it carries a `<quest>`
   tag** ([[source-events-engi]], [[source-events-ships]]). It is a real fight with real
   scrap and zero chain progress. Expect to visit both markers.

3. **[[event-engi-unlock-3]]** — `ENGI_UNLOCK_3` (raw: events_engi.xml)
   The convoy. *"A hangar-sized cargo ship is being escorted by a number of Mantis ships …
   a squadron of Engi ships with pirate emblems jump in and assist you … scans indicate
   they are manned by Rebels!"* ([[source-text-events-xml]]) No choices; it loads
   `MANTIS_ENGI_UNLOCK_3` hostile ([[source-events-engi]]).

   Unlike step 2 this one is safe either way: `<destroyed load="ENGI_UNLOCK_4"/>`, and the
   `<deadCrew>` block pays `MED standard` and offers a continue into `ENGI_UNLOCK_4`
   ([[source-events-ships]]). Both wins advance.

4. **[[event-engi-unlock-4]]** — `ENGI_UNLOCK_4` (raw: events_engi.xml)
   The payoff, on the same beacon, immediately after the fight. One choice, then one
   forced continue, then:
   ```
   <damage amount="-20"/>                    → 20 hull repaired
   <autoReward level="HIGH">standard</autoReward>
   <augment name="SYSTEM_CASING"/>           → Titanium System Casing
   <unlockShip id="1"/>                      → Stealth Cruiser
   ```
   There is no declining branch and no failure branch ([[source-events-engi]]).

## Requirements
- **An Engi crew member**, at step 1 only (`req="engi"`). Without one, `ENGI_UNLOCK_1` is
  a two-choice flavour beacon and the chain never opens ([[source-events-engi]]). This is
  the hard gate — the ship's own unlock hint spells it out: *"they only trust their own
  kind"* ([[source-text-blueprints]]).
- **Routing** into [[sector-engi-homeworlds]], which is `unique="true"` and
  `minSector="2"` ([[source-sector-data-xml]]).
- **A way to stop a runner and win without destroying it** at step 2 — a boarding party,
  anti-personnel weapons, or enough Engine damage to hold it in place while you force the
  surrender. This is the practical equipment requirement, and it is not signposted
  anywhere in game.
- **Fuel for up to three extra jumps**: both step-2 markers (real and decoy) plus step 3.

## Reward
- **Stealth Cruiser** unlocked (`<unlockShip id="1"/>`)
- [[item-titanium-system-casing]] (`SYSTEM_CASING`)
- `autoReward level="HIGH"` `standard` — scrap with resources
- **20 hull repairs**
- Plus, along the way: `HIGH standard` from a crew-kill at step 2, `MED standard` from a
  crew-kill at step 3, and whatever the decoy fight pays.
  ([[source-events-engi]], [[source-events-ships]])

## Failure Modes
1. **No Engi crew.** The chain never starts. Nothing else on this list matters if this
   one bites.
2. **Destroying the step-2 scout.** Silent failure — `MED` scrap, no marker, no warning.
3. **Letting the step-2 scout escape.** The `<escape>` timer is 40 seconds and starts on
   arrival ([[source-events-ships]]).
4. **Running out of fuel or map after chasing the decoy.** Two markers, one of them
   worthless, and no way to tell them apart before you arrive.
5. **The Engi Homeworlds not appearing on the map.**
6. The Rebel fleet reaching a marked beacon first.

Steps 3 and 4 have **no** failure branch — once the step-2 marker is passed the unlock is
effectively secured.

## Strategy Notes
- *Opinion:* buy or hire toward the step-2 win condition before entering the Engi
  Homeworlds. A teleporter is the cleanest answer — it produces dead crew, which is both
  the advancing outcome *and* the highest-paying one (`HIGH` vs `MED` scrap).
- Do not treat the two step-2 markers as "one is a trap". The decoy is an ordinary,
  winnable Rebel fight worth `MED`/`HIGH` scrap; it just does not advance the chain. Fight
  it the same careful way in case it is the real one.
- Because the decoy is indistinguishable on arrival, the safe habit is to play **every**
  step-2 beacon for a surrender or a crew kill.
- Fandom notes the Stealth Cruiser can alternatively be unlocked by winning a run with the
  Rock Cruiser ([[source-fandom-engi-fleet-discussion]]); `achievements.xml` in this raw
  set does not state that condition, so it is Fandom-only.

## Related
- [[sector-engi-homeworlds]] — the sector the whole chain runs in
- [[event-unlock-stealth]] — the shipped-but-dead alternative unlock event
- [[event-engi-unlock-2fake]] / [[event-engi-unlock-2fake-surrender]] — the decoy branch
- [[event-engi-unlock-2real-surrender]] — the surrender that carries the marker
- [[item-titanium-system-casing]]
- [[chain-the-flagship]] — where the Federation fleet coordinates you trade at step 4
  eventually lead

## Open Questions
- [ ] Are the two step-2 markers placed as a fixed pair (one always real, one always
      decoy), or can the engine place them in either order / in different sectors?
- [ ] What do `min="18" max="18"` on the step-2 `<escape>` tag control?
- [ ] Does the step-2 surrender threshold (`min="5" max="5"`) scale with sector
      progression, as Fandom's caveat suggests?
- [ ] All seven step pages record `version: ae`; this page records `both` — the events sit
      in the base `events_engi.xml` with no DLC markers and are not overridden in
      `dlcEvents*.xml`. Needs a lint decision.
- [ ] Fandom reports an augment-overwrite bug at step 4 (a `HIGH standard` roll containing
      an augment replacing the guaranteed Titanium System Casing). Unverified.

## Sources
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-engi-fleet-discussion]] (per raw/wiki/engi-fleet-discussion.md)
