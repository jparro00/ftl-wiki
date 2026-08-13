---
id: chain-slug-cruiser-unlock
type: chain
trigger_event: [[[event-slug-home-nebula-surrender]]]
steps: [[[event-slug-home-nebula-surrender]], [[event-slug-unlock-surrender]], [[event-slug-unlock-1]]]
sectors: [[[sector-slug-home-nebula]]]
reward: Slug Cruiser unlock + Slug Repair Gel + HIGH scrap (or the Anti-Bio Beam instead)
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [ship-unlock, slug-cruiser, blue-option, hidden-trigger, surrender, chain-failure-risk]
---

# Slug Cruiser unlock

## Summary
The only ship-unlock chain in the game with a **hidden entry point**. Its first beacon is
deliberately disguised as an ordinary Slug nebula fight — same intro text, same ship
blueprint — and the only tell is the surrender offer. Accept it, refuse the weapon they
try to give you, and they hand over the coordinates of a prototype cruiser's mobile
construction platform ([[source-events-slug]], [[source-events-ships]]).

The developer comment in `events_slug.xml` summarises the whole design:

> *"Slug ships in the home sector have a 1/3 chance to pick the trigger event when
> surrendering. It looks like a normal surrender but has another option. They want to give
> you a weapon (BEAM_BIO) and if you refuse it they give you a quest. At the locaton is a
> tough fight that you need to stay away from. If you have cloak or piloting + slug or
> sensors the scary people jump away and you can fight a weaker ship and then get the
> unlock"* ([[source-events-slug]])

> ⚠️ That comment is **partly stale**: the cloak and piloting options it describes are
> commented out in the shipped file, and the "1/3 chance" is not reflected anywhere in the
> data — `sector_data.xml` allocates the trigger event at `min="1" max="1"`, i.e. exactly
> once per Slug Home Nebula ([[source-sector-data-xml]]). Kept because it is the only
> in-file statement of intent.

## How It Starts
- Trigger: [[event-slug-home-nebula-surrender]] (`NEBULA_SLUG_FIGHT_UNLOCK`), allocated
  directly on the `SLUG_HOME` sector description at `min="1" max="1"`
  ([[source-sector-data-xml]]). **Guaranteed** once per Slug Home Nebula.
- `SLUG_HOME` is `unique="true"` with `minSector="3"` ([[source-sector-data-xml]]).
- The event is `unique="true"` with `<environment type="nebula"/>`
  ([[source-events-slug]]).
- It loads `<text load="NEBULA_SLUG_FIGHT"/>` — **the same text list as the ordinary
  [[event-slug-fight-in-nebula]]**. There is no way to identify it on arrival
  ([[source-events-slug]]).

## Steps

1. **[[event-slug-home-nebula-surrender]]** — `NEBULA_SLUG_FIGHT_UNLOCK`
   (raw: events_slug.xml)
   A Slug ship on the standard `SHIPS_JELLY` blueprint, but loaded as `JELLY_UNLOCK1`,
   which carries a special surrender ([[source-events-ships]]):
   ```
   <surrender chance="0"   min="3" max="4" load="SLUG_UNLOCK_SURRENDER"/>
   <escape    chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>
   <destroyed load="DESTROYED_DEFAULT"/>
   <deadCrew  load="DEAD_CREW_DEFAULT"/>
   ```
   Destroying it or killing its crew gives the default payouts and **ends the chain**. The
   escape and surrender rolls sit in the *same* hull band (3–4), so if the ship tries to
   run first you must land more damage before the surrender can fire
   ([[source-fandom-slug-home-nebula-surrender]]).

2. **[[event-slug-unlock-surrender]]** — `SLUG_UNLOCK_SURRENDER` (raw: events_slug.xml)
   The branch point. Its prompt is **byte-identical** to the ordinary
   [[event-slug-surrender]], so the only way to find out which one you are in is to accept
   ([[source-events-slug]], [[source-fandom-slug-home-nebula-surrender]]).

   | Choice | Payload | Chain |
   |---|---|---|
   | *We will not accept surrender!* | `<event/>` — nothing; the fight resumes | ❌ dead |
   | *Let them live* → **Accept the prototype weapon** | `<weapon name="BEAM_BIO"/>` ([[item-anti-bio-beam]]), ship non-hostile | ❌ dead — you take the weapon **instead of** the chain |
   | *Let them live* → **We don't want the weapon, we want information** | `<quest event="SLUG_UNLOCK_1"/>`, ship non-hostile | ✅ |

   The two are mutually exclusive: weapon **or** marker, never both.

3. **[[event-slug-unlock-1]]** — `SLUG_UNLOCK_1` (raw: events_slug.xml)
   The construction platform: a prototype cruiser being towed into the clouds, guarded by
   an assault ship, and you have not been noticed. It declares
   `<environment type="nebula"/>` even though it is a quest marker
   ([[source-events-slug]]). Two live choices — *charge them*, which loads
   `JELLY_UNLOCK2` hostile, or *tail them*, which loads the `SLUG_UNLOCK_2` sub-event.

   A `req="cloaking"` and a `req="pilot" lvl="2"` route into `SLUG_UNLOCK_2` exist in the
   file but are **commented out**, with a dev note *"Changed this part to be easier"* —
   not live in this build ([[source-events-slug]]).

   `JELLY_UNLOCK2` (`auto_blueprint="JELLY_TRUFFLE"`, the Slug Assault escort) pays
   `autoReward HIGH standard` on destroy or dead crew, has no surrender and no escape, and
   carries **no `<unlockShip>`** ([[source-events-ships]]). Fighting it is a good payday
   and a dead chain.

4. **`SLUG_UNLOCK_2`** — the stakeout. A sub-event loaded from step 3 and documented in
   full on [[event-slug-unlock-1]]; it gets no page of its own. Four choices
   ([[source-events-slug]]):

   | # | Choice | Requirement | Result |
   |---|--------|-------------|--------|
   | 2a | Fly slowly toward their last known position | — | `JELLY_UNLOCK2` hostile — the hard escort. ❌ no unlock |
   | 2b | Wait and hope the escort leaves | — | nothing at all. ❌ chain over |
   | 2c | **(Slug Crew)** monitor their life signatures | `req="slug"` | forced continue → `JELLY_UNLOCK3` hostile ✅ |
   | 2d | **(Improved Sensors)** maintain a lock from a distance | `req="sensors" lvl="2"` | forced continue → `JELLY_UNLOCK3` hostile ✅ |

   Choices 2c and 2d are the same outcome by two different gates — the escort jumps away
   and you face the weak interceptor alone.

5. **`JELLY_UNLOCK3`** — the payoff fight (raw: events_ships.xml)
   `auto_blueprint="JELLY_BUTTON"`, a Slug Interceptor, annotated in-file *"this is the
   weak ship that gives you the unlock"*. Both `<destroyed>` and `<deadCrew>` carry the
   identical payload ([[source-events-ships]]):
   ```
   <unlockShip id="5"/>                       → Slug Cruiser
   <autoReward level="HIGH">standard</autoReward>
   <augment name="SLUG_GEL"/>                 → Slug Repair Gel
   ```
   But it also carries `<escape timer="35" min="22" max="22">` with a `<gotaway>` branch
   that pays **nothing** — *"The interceptor jumps away with the cruiser linked to its FTL
   signatures. You were so close..."*. The escape is scheduled, not a chance roll, so you
   are always racing it ([[source-events-ships]],
   [[source-fandom-slug-home-nebula-surrender]]).

## Requirements
- **Routing** into [[sector-slug-home-nebula]] (`unique="true"`, `minSector="3"`).
- **A Slug crew member, or Sensors at level 2+** — at `SLUG_UNLOCK_2`. Without one of
  these there is no live path to `JELLY_UNLOCK3` and therefore no unlock. This is the
  chain's hard gate.
- **Damage control at step 1**: enough to push the Slug ship into the 3–4 hull band for
  the surrender, without destroying it.
- **Enough burst to kill `JELLY_UNLOCK3` inside 35 seconds** — the opposite discipline
  from step 1.
- Fuel for one extra jump to the marker.

Cloaking and Advanced Piloting are **not** requirements despite the dev comment — those
options exist only in commented-out code ([[source-events-slug]]).

## Reward
- **Slug Cruiser** unlocked (`<unlockShip id="5"/>`)
- [[item-slug-repair-gel]] (`SLUG_GEL`)
- `autoReward level="HIGH"` `standard`
- Or, if you take the other branch at step 2: [[item-anti-bio-beam]] (`BEAM_BIO`),
  immediately and with no follow-up.

Ship id `5` → Slug Cruiser is supported by the ship's own unlock hint: *"One of the slug
ships must know something about this advanced cruiser. Perhaps you can 'convince' them to
tell you."* (`ship_PLAYER_SHIP_JELLY_unlock`, [[source-text-blueprints]]) — this chain by
description.

> ⚠️ **BUG (Fandom-only):** Fandom reports that if the `HIGH standard` roll happens to
> include an augment, it **overwrites** the guaranteed Slug Repair Gel
> ([[source-fandom-slug-home-nebula-surrender]]). The file orders `autoReward` before
> `augment`, which is consistent with the claim but does not establish it.

## Failure Modes
This chain has more ways to fail than any other, and most of them are invisible:

1. **Not recognising the beacon.** It is textually identical to
   [[event-slug-fight-in-nebula]]; the ordinary fight has no surrender path to this chain.
2. **Destroying the step-1 ship, or killing its crew.** Default rewards, chain over.
3. **The 50% escape roll firing first** (`<escape chance="0.5" min="3" max="4">`) — you
   must then do more damage before the surrender band can be re-entered.
4. **Taking the Anti-Bio Beam.** A real reward, and a permanent end to the chain.
5. **Refusing the surrender outright.**
6. **Charging the platform at `SLUG_UNLOCK_1`, or attacking at `SLUG_UNLOCK_2`.** Both
   give the hard escort fight and `HIGH standard` scrap — a good payout and no unlock.
7. **Arriving without Slug crew or Sensors 2.** No live choice reaches `JELLY_UNLOCK3`;
   the only non-combat option is to withdraw with nothing.
8. **Letting `JELLY_UNLOCK3` escape** inside its 35-second timer.

> ⚠️ **CONTRADICTION:** the meaning of `chance="0"` on the step-1 surrender.
> - Game files: `<surrender chance="0" min="3" max="4" .../>` ([[source-events-ships]]).
> - Fandom: "surrender offer: **100% chance** at 30–40% hull" — while quoting that same
>   `chance="0"` line in its own notes ([[source-fandom-slug-home-nebula-surrender]]).
>
> Fandom reads it the same way for `QUEST_SLUG_PIRATE_TRAP1`, which is also `chance="0"`.
> So `chance="0"` appears to mean *always take the scripted surrender branch*, not *never
> surrender*. Recorded, not resolved — no source here documents the attribute's semantics.
> Play-wise trust Fandom: an unlock chain whose entry surrender never fired would be
> unreachable. See [[concept-surrender-offers]].

## Strategy Notes
- *Opinion:* in [[sector-slug-home-nebula]], **accept every Slug surrender**. Accepting an
  ordinary one costs you only the kill; refusing the special one costs the ship. Fandom
  gives the same advice ([[source-fandom-slug-home-nebula-surrender]]).
- Take the marker over the Anti-Bio Beam if the cruiser is not yet unlocked. If it is, the
  beam is the better take — it is strong on a boarding build and needs no follow-up jump.
- The chain asks for opposite skills at its two ends: restraint at step 1 (do not overkill)
  and burst at step 5 (kill inside 35 seconds). Plan for both before you jump to the
  marker.
- Fandom notes the Slug Cruiser can also be unlocked by winning a run with the Mantis
  Cruiser ([[source-fandom-slug-home-nebula-surrender]]); `achievements.xml` in this raw
  set states no such condition.

## Related
- [[event-slug-fight-in-nebula]] — the ordinary fight step 1 is disguised as
- [[event-slug-surrender]] — the ordinary surrender step 2 is disguised as
- [[sector-slug-home-nebula]] — the chain's sector
- [[item-anti-bio-beam]], [[item-slug-repair-gel]] — the two mutually exclusive rewards
- [[concept-surrender-offers]] — what `chance="0"` means
- [[chain-mantis-cruiser-unlock]] — the other chain gated on systems rather than choices
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] **Broken link:** [[event-slug-home-nebula-surrender]] links `[[event-slug-unlock-1]]`,
      which does not exist. `SLUG_UNLOCK_2` is a sub-event of `SLUG_UNLOCK_1` and is
      correctly documented on [[event-slug-unlock-1]] instead — that link should be
      repointed.
- [ ] What `chance="0"` actually means in a `<surrender>` block.
- [ ] The dev comment's "1/3 chance to pick the trigger event when surrendering" is not
      reflected in the shipped allocation. Was the trigger once list-driven?
- [ ] Whether the augment-overwrite bug Fandom describes is present in this 1.6.x build.
- [ ] The two step pages disagree on `version` (`ae` on the parent, `both` on the
      surrender). This page records `both` — the events sit in the base `events_slug.xml`
      with no DLC markers and are not overridden in `dlcEvents*.xml`. Needs a lint
      decision.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-slug-home-nebula-surrender]] (per raw/wiki/slug-home-nebula-surrender.md)
