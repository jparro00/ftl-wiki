---
id: concept-rebel-fleet-advance
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 12
related_events: []
tags: [mechanics, rebel-fleet, resolves-contradictions, methodology]
---

# The Rebel fleet advance and `modifyPursuit`

## Definition & Context
The Rebel fleet is the run's clock. The game states the premise itself, in the tutorial:

> *"You will be traveling through dangerous sectors of the galaxy with the Rebel fleet in
> hot pursuit. Make it to the exit beacon of each sector before the Rebels can catch you."*
> — `event_TUTORIAL_START_c1_c1_text` ([[source-text-events-xml]])

Beacons the fleet has taken are marked *"The Rebels have control of this location. Very
dangerous."* (`map_fleet_loc`), and a beacon about to fall reads *"The Rebels are about to
gain control of this beacon!"* (`map_rebels_loc`) ([[source-text-misc]]).

Exactly **one** data tag moves that clock: `<modifyPursuit amount="N"/>`. Everything else on
this page follows from it.

## The tag

```xml
<modifyPursuit amount="1"/>    <!-- bad for the player -->
<modifyPursuit amount="-1"/>   <!-- good for the player -->
<modifyPursuit amount="-2"/>   <!-- twice as good -->
```

**32 live instances** across `raw/gamedata/`, and only three distinct values:

| `amount` | Count | Sense |
|---|---|---|
| `1` | 20 | against the player |
| `-1` | 9 | for the player |
| `-2` | 3 | for the player |

No `2`, no `-3`, no other value anywhere. (Counted with comment blocks stripped, per
[[concept-event-list-weighting]].)

## The open question, resolved: what does `amount="1"` actually do?

Fandom glosses the identical tag three different ways — *"pursuit is doubled"*, *"pursuit is
doubled for 1 jump"*, and (for negative amounts) *"delayed for 1 jump"* / *"delay the Rebels
by 2 jumps"*. Multiple ingest passes flagged this as an unresolved contradiction, on the
reasonable grounds that the game files state only a bare integer and nothing about doubling
or duration.

**The game's own UI string table settles it.** `text_misc.xml` carries the four on-screen
notifications the engine prints when pursuit changes, with the developers' own placeholder
comments:

```xml
<text name="fleet_delayed">Fleet delayed by \1 jumps</text>  <!-- \1: number of jumps -->
<text name="fleet_delayed_1">Fleet delayed by 1 jump</text>

<text name="fleet_speed">Fleet pursuit doubled for \1 jumps</text>  <!-- \1: number of jumps -->
<text name="fleet_speed_1">Fleet pursuit doubled for 1 jump</text>
```

([[source-text-misc]], per raw/gamedata/text_misc.xml)

Three things follow, and they are not interpretation — they are the game's words:

1. **`amount` is a count of jumps.** The developer comment says so explicitly: `\1: number
   of jumps`. Whatever the sign, `N` is jumps.
2. **The two signs are two different effects, not mirror images.**
   - Negative → *"Fleet delayed by N jumps"* — a one-off setback to the fleet's position.
   - Positive → *"Fleet pursuit doubled for N jumps"* — a **rate** change lasting N jumps.
   The engine has separate strings for them, and the wording is not symmetrical.
3. **"Doubled for 1 jump" is the game's phrasing, not Fandom's invention.** Fandom's
   *"pursuit is doubled for 1 jump"* is a verbatim lift of `fleet_speed_1`.

### Where Fandom is right, and where it is loose

Across all 292 pages in `raw/wiki/`, "pursuit … doubled" appears 19 times:

| Fandom phrasing | Uses | Verdict |
|---|---|---|
| *"pursuit is doubled for 1 jump"* | 11 | **Correct** — matches `fleet_speed_1` exactly. |
| *"pursuit is doubled"* | 7 | Correct but abridged — drops the duration the game states. |
| *"pursuit is '''not''' doubled"* | 1 | Correct — [[event-rebel-transport-ship]], see below. |
| *"pursuit is delayed for 1 jump"* | 3 | **Correct** — matches `fleet_delayed_1`. |
| *"delay the Rebels by 2 jumps"* (the mercenary, `amount="-2"`) | 1 | **Correct** — matches `fleet_delayed`. |

So the three-way inconsistency was largely a *transcription* inconsistency on Fandom's side,
not a disagreement about mechanics. The wiki's earlier flags on
[[event-asteroid-belt-distress]] and [[event-rebel-defector]] — "an interpretation, not a
file value" — were correct to be cautious and can now be closed: the file value exists, it
is just in `text_misc.xml` rather than next to the tag.

**A gloss to avoid:** *"advances the fleet 1 jump"*. That is the `fleet_delayed` wording
run backwards, and the game does **not** use it for positive amounts. Positive `amount`
doubles the pursuit *rate* for a duration; it is not stated anywhere to teleport the fleet
forward by N beacons.

### What is still unknown
- **What "doubled" is doubled relative to.** The baseline advance rate — how far the fleet
  moves per player jump under normal conditions — is not in any data file.
- **Whether the two effects are commensurable.** `-1` and `+1` both print "1 jump", but one
  is a position change and the other a rate change for a duration. Nothing in the files says
  a `+1` and a `-1` cancel.
- **Whether effects stack.** Two `+1` events in a row: two jumps of doubling, or a
  four-times rate for one? Undetermined.

## Where the tag actually fires

### Events that delay the fleet (`amount` negative)

| Event | `amount` | How | Page |
|---|---|---|---|
| `MERCENARY` | −2 | Pay 10–25 scrap to hire a decoy | [[event-the-mercenary]] |
| `ENGI_FLEET_DELAY` | −2 | Booby-trap the Engi cache | [[event-engi-cache]] |
| `FLAGSHIP_CONSTRUCTION_DONE` | −2 | Destroy the flagship-construction ship | *(no page yet)* |
| `FUEL_FLEET_DELAY` | −1 | Out of fuel with the distress beacon **off** | [[event-no-fuel-rebel-fleet-delay]] |
| `DEFENSE_RADAR_LIST` entry 1 | −1 | Hack the radar station successfully | [[event-auto-ship-near-radar-station]] |
| `REBEL_AUTO_RADAR` destroyed, `req="hacking"` | −1 | Blue option, costs 1 drone part | [[event-auto-ship-near-radar-station]] |
| `CRYSTAL_REQUEST` / `CRYSTAL_REQUEST_LIST` | −1 | Two branches of the Crystal request | [[event-crystalline-ship-messaging-about-rebels]] |
| `PIRATE_BRIBER_WIN` | −1 | Outcome of taking the pirate's bribe | [[event-pirate-briber]] |
| `LANIUS_AUTO_REBEL_LIST`, `LANIUS_GROUP_AUTO` (×3) | −1 | Lanius absorbing Rebel hardware | [[event-lanius-ship-absorbing-automated-scout]], [[event-lanius-ship-absorbing-rebel-base]] |

The three `−2` sources are the only ones in the game, and all three are deliberate player
actions: pay a mercenary, blow up a cache, or kill the construction ship.

### Events that accelerate the fleet (`amount="1"`)

Two clear families plus scattered one-offs.

**1. An enemy escapes and reports you.** Declared inside `<gotaway>` in `events_ships.xml`:

| Ship | Parent event | Page |
|---|---|---|
| `REBEL_AUTO_WARNING` | `AUTO_WARNING` | [[event-auto-ship-warning]] |
| `SQUAT_WARNING` | `SQUAT_WARNING` | [[event-rebel-ship-warning]] |
| `REBEL_AUTO_BAIT` | `AUTO_BAIT` | [[event-auto-bait]] |

`REBEL_AUTO_BAIT` is the odd one: it carries `modifyPursuit amount="1"` in **both**
`<gotaway>` *and* `<destroyed>` — killing the bait ship advances the fleet anyway
([[source-events-ships]]).

> **Not every escaping ship reports you.** `SQUAT_TRANSPORT` ([[event-rebel-transport-ship]])
> has a `<gotaway>` with no `modifyPursuit`. Fandom notes this explicitly — *"If the enemy
> escapes, the Rebel Fleet pursuit is '''not''' doubled"* — and the file agrees
> ([[source-fandom-rebel-transport-ship]], [[source-events-ships]]). The tag is per-ship, not
> a general rule about escapes.

**2. You give your position away.** `ZOLTAN_PRIMITIVES_ZOLTAN` fires it on both `<destroyed>`
and `<deadCrew>` ([[event-zoltan-quest-primitives]]); `DEFENSE_RADAR_LIST` entry 4 fires it
when the hack trips an alarm ([[event-auto-ship-near-radar-station]]);
`DERELICT_TREASURE_REWARD` fires it when the wreck turns out to be a Rebel tripwire.

**Others:** `CIVILIAN_ASTEROIDS_BEACON_LIST4` ([[event-asteroid-belt-distress]]),
`ALISON_DEFECTOR_HELP` and `_2` ([[event-rebel-defector]]),
`CRYSTAL_REBEL_CRYSTAL` ([[event-rebel-ship-attacking-crystal-ship]]),
`CRYSTAL_REQUEST` and `CRYSTAL_HELP_DIG` ([[event-crystalline-ship-messaging-about-rebels]],
[[event-crystalline-men-buried]]),
`NEBULA_REBEL_UNDETECTED_LIST` ([[event-rebel-fight-choice-in-nebula]]),
`NEBULA_REBEL_CHASE_LIST` ([[event-rebel-fight-chance-in-nebula]]),
`SECRET_WORD_ABADOTH` ([[event-secret-word-abadoth]]),
`ROGUE_REBEL_SEARCH` (in `newEvents.xml`),
and `FUEL_FLEET_DISTRESS` ([[event-fuel-fleet-distress]]).

> ⚠️ **CONTRADICTION (internal to the game files):** `FUEL_FLEET_DISTRESS` uses
> `amount="1"` while its seven prose variants all say the fleet has *lost* you — they are a
> near-verbatim copy of `FUEL_FLEET_DELAY_LIST`, which pairs with `amount="-1"`. The
> developers flagged it themselves with `<!-- MATT FIXME - IS THIS A REPEAT -->` directly
> above the block. The event is not in any live list. ([[source-events-fuel]],
> [[source-text-events-xml]]) See [[event-fuel-fleet-distress]].

`DERELICT_TREASURE_REWARD` lives in `nameEvents.xml` alongside `BIG_NAME_TEST` and
`NEBULA_NOTHING_TEST`, has inline placeholder prose rather than `text_events.xml` ids, and is
referenced by nothing else in `raw/gamedata/`. Treat it as dev/test content until something
says otherwise ([[source-nameevents]]).

## Distraction Buoys — the augment version

`FLEET_DISTRACTION` is the only augment that touches the fleet clock. Its in-game
description is unambiguous:

> *"Leaves a false signal at sector start to delay Rebels 1 jump."*
> — `aug_FLEET_DISTRACTION_desc` ([[source-text-blueprints]])

and the effect message is

> *"You deploy your Distraction Buoys, giving you more time to explore this sector before
> the fleet catches up."* — `distraction` ([[source-text-misc]])

Notes from the data ([[source-dlcblueprints]], [[source-text-blueprints]]):

- It is **Advanced Edition only** — declared in `dlcBlueprints.xml`, and a member of the
  `DLC_AUGMENTS` and `DLC_ITEMS` blueprint lists.
- It fires **at sector start**, automatically, once per sector. It does not use
  `modifyPursuit`; no event applies it.
- Its wording ("delay Rebels 1 jump") is the `fleet_delayed_1` phrasing, which is a second
  independent confirmation that a 1-unit fleet delay is described in jumps.
- It doubles as a **blue-option key**: `req="FLEET_DISTRACTION"` unlocks one choice, in
  `CRYSTAL_REQUEST` ([[event-crystalline-ship-messaging-about-rebels]]), labelled
  *"(Distraction Buoy) Accept the scrap but give them falsified flight plans."*
  See [[item-distraction-buoys]] and [[concept-blue-options]].

## When the fleet catches you: the `FLEET_*` family

Six events represent the fleet arriving. They are **not members of any `<eventList>` and are
allocated by no `sectorDescription`** — grepping `raw/gamedata/` finds each id only in its
own definition. The engine calls them by name, exactly like `NEUTRAL_EXIT` and
`FEDERATION_BASE_ASSIST` (see [[concept-sector-event-allocation]]).

| Event | File | Contents |
|---|---|---|
| `FLEET_EASY` | `events.xml` | `<fleet>rebel</fleet>`, `LONG_FLEET` hostile, `<environment type="PDS" target="player"/>` |
| `FLEET_EASY_DLC` | `events.xml` | same, AE text id |
| `FLEET_EASY_BEACON` | `events.xml` | `<fleet>rebel</fleet>`, `LONG_FLEET` hostile, **no** PDS |
| `FLEET_EASY_BEACON_DLC` | `events.xml` | as above **plus** PDS |
| `FLEET_HARD` | `events.xml` | `<fleet>rebel</fleet>`, `LONG_FLEET` hostile, no PDS |
| `FLEET_EASY_NEBULA` | `events_nebula.xml` | `LONG_FLEET` hostile, `<environment type="storm"/>`, **no `<fleet>` tag** |

Their prose says what each is for ([[source-text-events-xml]]):

- `FLEET_EASY` — *"The Rebel fleet has found you, and a nearby scout turns to engage. The
  cruisers in the distance are firing on you!"*
- `FLEET_HARD` — *"…and a nearby scout turns to engage. **You must flee before their cruisers
  open fire!**"*
- `FLEET_EASY_BEACON` — *"You've found the exit beacon but the Rebels got here first! You must
  survive long enough to be able to jump to the next sector."*
- `FLEET_EASY_NEBULA` — *"An advanced Rebel hunter easily found your ship. You can't see it
  through the nebula, but you can assume the fleet is right on top of you."*

Observations that are safe from the data:

- The enemy is always `LONG_FLEET`, an `auto_blueprint="SHIPS_REBEL_ELITE"` ship whose only
  outcomes are `<destroyed>` and `<deadCrew>`, each granting 1 fuel. It has **no
  `<surrender>` element and no `<escape>`** — per [[concept-surrender-offers]], absence of
  the element is how the game says "never surrenders" ([[source-events-ships]]).
- `_DLC` variants differ from their base twins only by text id and the PDS environment, so
  the anti-ship-battery pressure at fleet beacons is Advanced Edition content.
- `FLEET_EASY_AGAIN` exists but is **commented out** in `events.xml`, with inline prose
  *"Another ship approaches, the reinforcements seem endless! You must jump away!"* — cut
  content ([[source-events-xml]]).

**What the naming implies but the files do not state:** that `FLEET_EASY` vs `FLEET_HARD` is
selected by difficulty setting, or that `_BEACON` fires specifically at the exit. Nothing in
`raw/gamedata/` names the selector. Left open.

### `<fleet>` is scenery, not mechanics
The tag takes three values across 12 live uses — `rebel` (8×), `fed` (2×), `battle` (2×) —
and the developer comments in `events_boss.xml` explain it as beacon backdrop, not as a
pursuit effect ([[source-events-boss]]):

```xml
<event name="BOSS_FLEETS_FED">   <!-- empty nodes that the Rebels have not reached yet.-->
<event name="BOSS_FLEETS_BOTH">  <!-- nodes that have ships fighting  -  unique background -->
<event name="BOSS_FLEETS_REBEL"> <!-- areas that the fleet took over (or will take over soon) -->
```

Outside the boss sector, `<fleet>rebel</fleet>` appears only on the five `events.xml`
`FLEET_*` events and on `NO_FUEL_FLEET` / `NO_FUEL_FLEET_DLC` ([[event-no-fuel-fleet]]) —
i.e. exactly the encounters where the fleet is visibly on top of you. In the boss sector the
three values are the three beacon states: `fed` on `BOSS_FLEETS_FED` and `LAST_STAND_START`,
`battle` on `BOSS_FLEETS_BOTH` and `BOSS_FLEETS_BOTH_FIGHT`, `rebel` on `BOSS_FLEETS_REBEL`
([[event-rebel-fight-among-rebel-fleet]], [[sector-the-last-stand]]).

## Nebulae slow the fleet
The nebula tooltip states the mechanic directly:

> *"You're inside a nebula. Your sensors will not function, but the Rebel fleet will advance
> more slowly towards you."* — `tooltip_nebula` ([[source-text-tooltips]])

and the star-map string agrees: *"The nebula here will make fleet pursuit slower but will
disrupt your sensors."* (`map_nebula_loc`). In nebula **sectors** the benefit is reduced:
*"The Rebel Fleet was prepared for the nebula in this sector, so it won't be as effective a
hiding spot."* (`map_nebula_fleet_loc`) ([[source-text-misc]]). Neither string gives a
number. See [[concept-nebula-mechanics]].

## Implications For Play
- **Only three actions in the whole game buy two jumps**: hiring the mercenary, booby-trapping
  the Engi cache, and destroying the flagship-construction ship. Two of the three cost scrap
  or a fight; all three are worth taking if the sector is running long.
- **The cheapest recurring delay is running dry with your distress beacon off.**
  `FUEL_FLEET_DELAY` is 1 of 11 entries in `NO_FUEL` (≈9.1%, per
  [[concept-event-list-weighting]]) — not a plan, but the reason the distress-off pool is
  strictly better than the distress-on one.
- **Let no marked scout escape.** Three ships turn a lost fight into a doubled pursuit; a
  fourth (`REBEL_AUTO_BAIT`) does it whether you win or lose.
- **Distraction Buoys are a flat 1-jump refund per sector**, applied automatically, and
  therefore scale with the number of sectors left rather than with the current one.

## Related
- [[concept-nebula-mechanics]] — the other lever on fleet speed
- [[concept-sector-event-allocation]] — why the `FLEET_*` events have no sector allocation
- [[concept-event-list-weighting]] — how the fractions above are derived
- [[concept-surrender-offers]] — the sibling raw-value-vs-Fandom-gloss question, also resolved
- [[item-distraction-buoys]] · [[entity-rebels]] · [[concept-rebel-fleet-advance]]
- [[chain-the-flagship]] — where the pursuit ends
- Slug alias: eight pages link this concept as `[[concept-rebel-fleet-advance]]`. Same
  subject; that slug has no page. Worth reconciling on the next lint.
- [[event-fleet-easy-again]] · [[event-derelict-treasure]] — the unlisted events discussed above

## Open Questions
- [ ] What is the **baseline** fleet advance rate that `fleet_speed` doubles? Not in any
      data file; needs the binary or a timed in-game observation.
- [ ] Do multiple `modifyPursuit` effects stack, and do `+1` and `−1` cancel?
- [ ] What selects `FLEET_EASY` vs `FLEET_HARD` vs `FLEET_EASY_BEACON`? Difficulty is the
      obvious guess and is **not** supported by anything in `raw/gamedata/`.
- [ ] How much slower is fleet pursuit inside a nebula, and how much of that is removed in a
      nebula sector? Fandom states 80% for Slug-sector nebula beacons
      ([[concept-nebula-mechanics]]); the files give no number.
- [ ] Is `DERELICT_TREASURE` reachable, or dev-only? It is referenced nowhere in
      `raw/gamedata/`.

## Sources
- [[source-text-misc]] (per raw/gamedata/text_misc.xml) — **the deciding source**: `fleet_delayed`, `fleet_speed`
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-fandom-rebel-transport-ship]] (per raw/wiki/rebel-transport-ship.md)
