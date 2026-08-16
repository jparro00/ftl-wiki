# Save watcher — specification

Normative spec for `tools/ftlsave.py` and `tools/save-watch.py`. Self-contained: an agent
with no prior context can rebuild, verify and extend the watcher from this document.

The watcher shows the card for the event you are looking at, without you doing anything.
It reads the game's save file; it does not modify the game.

```
continue.sav    ──► ftlsave.parse ──► EncounterState.text ──► card slug ──► browser
hs_continue.sav ──► ftlsave.scan  ──►      (string id)        (cards/trees)  (localhost)
                    (Hyperspace)
```

Two ways in, because there are two save layouts. Section 3b says which runs when.

---

## 1. Running it

```bash
python tools/save-watch.py --open          # watch + serve + open the page
python tools/save-watch.py --once          # resolve the current save once, print JSON
python tools/save-watch.py --no-sector     # cards only; never show a sector profile (§5b)
python tools/save-watch.py --index-report  # measure how well texts pin to cards
python tools/ftlsave.py <continue.sav>     # dump the parsed encounter
python tools/ftlsave.py <continue.sav> --beacons   # what the save gives away about the sector
```

Park the page on the second monitor and leave it. It repaints on every save write.
There is nothing to click — that is the point.

### If you are an agent launching this

**`save-watch.py` without `--once` or `--index-report` is a server that never returns.**
Launch it in the background (Bash `run_in_background: true`), never in the foreground —
a foreground call blocks until the tool times out and you learn nothing.

Check the pipeline with `--once` first. It parses the current save, prints one JSON
object, and exits, so it tells you whether the parser, the index and the paths all work
without starting anything:

```bash
python tools/save-watch.py --once
```

A `status` of `ok` means it resolved a card. `nosave` means no run is in progress —
that is the save file's absence, not a fault. See §5 for the rest.

**Start it whenever you like, including before FTL.** There is no `continue.sav` between
runs; the game deletes it when a run ends. The watcher therefore resolves the save's
*location* rather than requiring the file, sits in `nosave`, and picks the run up when one
begins. Never treat a missing save as a reason not to start.

Then, to actually serve it:

```bash
python tools/save-watch.py --open        # run_in_background: true
```

Confirm it came up by fetching `http://127.0.0.1:8787/current`. Use `--port` if 8787 is
taken. `--open` launches the user's browser — omit it if you only want the server up, and
hand the user the URL instead.

To stop it, kill whatever is listening on the port. Do **not** reach for `pkill` (absent
from this machine's Git Bash) or match on `python.exe` (the interpreter here is
`python3.10.exe`, from the Windows Store build). Killing by port avoids both traps:

```powershell
Get-NetTCPConnection -LocalPort 8787 -State Listen |
    ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

If you launched it as a harness background task, stopping that task is equivalent and
simpler.

Do not add a "press enter to continue" or a confirmation step around any of this. The
value of the watcher is that it costs zero interactions once running.

### Paths

Both are auto-detected, and both defaults are correct on this machine:

| What | Path |
|---|---|
| save | `%USERPROFILE%\Documents\My Games\FasterThanLight\{continue,hs_continue}.sav` |
| archive | `D:\Steam\steamapps\common\FTL Faster Than Light\ftl.dat` |

Override with `--save` and `--ftl-dat`. The save lives under **Documents\My Games**, not
`%APPDATA%\FasterThanLight` — that directory exists too but holds only `settings.ini`.
`ftl.dat` must be the installed game's, since layouts are read from it live; a stale copy
would desynchronise the parse.

---

## 2. Why the save file, and not a mod

FTL cannot display HTML and no mod can make it. Hyperspace's Lua sandbox has `io`, `os`,
`package` and `debug` all commented out of its `linit.c`, so no in-game script can open a
browser or write an arbitrary file. Any display of a card is therefore an external process,
and the only question is how that process learns which event is on screen.

The save file answers it with no game modification at all: no Hyperspace, no Slipstream
patch, nothing to uninstall. It also composes with `event-labels`, which changes only prose.

---

## 3. The format, and the one thing that makes this possible

`SavedGameParser.java` in Vhati/ftl-profile-editor is the normative format spec, together
with `DatParser.readLayout` for the ship layout grammar. `ftlsave.py` is a port of the
`readSavedGame` prefix; every field order and version conditional is copied from there.

**The parse deliberately stops at `EncounterState`.** That is not laziness — it is what
makes the approach work on FTL 1.6.14. The reference parser cannot read 1.6.14 saves at
all: it throws `Unsupported projectileType flag: 6` (ftl-profile-editor issue #119). Every
byte it chokes on lives *after* the encounter block, so stopping early sidesteps the bug
entirely. Do not extend the parser past the encounter without rediscovering that problem.

Layout data (room count, per-room square dimensions, door ordering) is not in the save. It
is read live from the installed `ftl.dat` through `tools/ftlpkg.py`. Ship blueprints —
layout id, and how many rooms hold each system — come from `raw/gamedata/`.

Two subtleties the byte layout depends on, both from the reference implementation:

- A system with capacity `0` is not on the ship and occupies only the 4 bytes that declared
  the capacity. Systems spanning several rooms write one `SystemState` per room.
- Doors are stored in layout order **except** that vacuum-adjacent doors (either side
  opening onto space) are plucked out and appended at the end.

### Verified against a live save

Format 11 (`FTL 1.6.1+`), `PLAYER_SHIP_ANAEROBIC_2` / `anaerobic_cruiser_2`: the parser
consumed 4082 of 6212 bytes and landed on a coherent `EncounterState` whose five ship-event
ids were all real event names (`PIRATE_SURRENDER`, `PIRATE_ESCAPE`, `DESTROYED_DEFAULT`,
`DEAD_CREW_DEFAULT`). Landing on five valid ids simultaneously is the check that the whole
preceding parse was byte-correct.

### What the beacon list holds — and what it does not

The beacon list sits *before* the encounter block, so the parser already walked it; as of
2026-08-15 it keeps the fields instead of discarding them. `--beacons` reports them.

Per beacon: `visitCount`, `seen`, `enemyPresent` + `shipEventId` + `autoBlueprintId`,
`fleetPresence`, `underAttack`, and a store's entire stock. Alongside them the save holds
`questEventMap` — quest marker event names against their beacon ids — which `--beacons`
prints too.

**No beacon stores its event.** That is not a gap in this parser: the save does not contain
it. Beacon events are regenerated from `sectorLayoutSeed`, so naming every beacon on the map
cannot be done from the save at all — it needs the running engine, which means Hyperspace.
See `raw/modding/2026-08-15-beacon-name-labels-mod.md`.

**Measured 2026-08-15: for an unvisited beacon, none of it.** A live sector-1 save with 21
beacons reported `unvisited ships 0 (named 0) | stores 0` across all 20 of them — a sector-1
map certainly holds both, so `enemyPresent` and the store block are written on arrival, not at
sector generation. `seen` was set on the current beacon and its three neighbours, matching the
one-jump marker rule, and even those held no ship or store data.

So the beacon list describes where you have **been**, not where you are going. It cannot feed a
spoiler map. That is a property of the save format, not of this parser.

## 3b. Two save layouts — parse, or scan

Installing Hyperspace changes both **where** the run save is and **what shape** it is.

### Where: `hs_continue.sav`

Hyperspace hooks `FileHelper::readBinaryFile` / `fileExists` / `createBinaryFile` and rewrites
the game's save paths through its own prefix (`SaveFile.cpp`, prefix `hs`). A modded install
therefore writes **`hs_continue.sav`** and never touches `continue.sav`, which sits there stale
— for an hour on 2026-08-15 that looked like "FTL isn't saving", when in fact it was saving next
door. `find_save` watches both names in both directories and takes the **most recently written**,
re-resolved on every poll, so installing or removing Hyperspace needs no restart and no flag.

### What shape: not FTL's

`parse` reaches the encounter by walking every preceding byte, which requires the ship block to
be exactly FTL's. Under Hyperspace it is not. Enumerated from the source (v1.22.2), the hooks
that splice data into the run save are:

| Hook | Where it writes | Files |
|---|---|---|
| `ShipManager::ExportShip` | **before** `super` | `CustomSystems.cpp` (removed starting systems) |
| `ShipManager::ExportShip` | after `super` | `CustomAugments`, `CustomShips` (per **room**: stat boosts, erosion, animation), `CustomSystems`, `OxygenWithoutSystem`, `TemporalSystem` |
| `CrewMember::SaveState` | per **crew member** | `CustomCrew.cpp` |
| `StarMap::SaveGame` | in the map block | `CustomEvents` (×2), `CustomSectors`, `Infinite`, `Seeds` (×2), `TriggeredEvents` |

Twelve insertion points, several of them variable-length and nested (`StatBoost::Save`,
`Animation::SaveState`, `ShipSystem::CompleteSave`). Tracking them in Python would be a
reimplementation of Hyperspace's serialisation that breaks whenever it gains a field.

### So the Hyperspace path does not walk — it looks

`ftlsave.scan_encounter_text` scans the file for length-prefixed UTF-8 strings matching
`^(event|text)_[A-Za-z0-9_]+$` and returns them in file order; the watcher takes the last.
Measured on a real 5524-byte Hyperspace save, the whole file yields **exactly one** candidate —
`text_START_BEACON_ENGI_1`, the event that was on screen. The encounter block sits after the
ship and the map, so anything else of that shape would precede it.

The scan runs **only as a fallback**, after `parse` raises. A vanilla save therefore keeps the
structured read and everything it knows; the reported `source` field says which ran (`parse` or
`scan`), and `save` names the file.

**What the scan gives up**, stated plainly because it is a real loss: no sector number, no beacon
number (both `null`), and no five-valid-event-ids self-check — its correctness argument is the
index lookup that follows, not the parse itself. It also cannot see an encounter whose text is
stored as prose rather than an id. It answers only the question the watcher asks: *which event is
on screen*.

A save caught mid-write also lands in the fallback, and is distinguished by yielding nothing:
a torn read produces no candidate, so it reports `error` and the next poll retries.

### The save is written mid-encounter

Observed directly on 2026-08-13: `continue.sav` was rewritten at 19:20:31 with no jump,
shrinking 6909 → 6212 bytes, while its encounter text changed from
`event_ROGUE_REBEL_SEARCH_2_text` to `event_DEAD_CREW_DEFAULT_1_text` as a fight resolved.
The watcher's responsiveness rests on this: FTL flushes the save as an encounter
progresses, not only on beacon arrival.

> ⚠️ **Superseded for the hidden-choice case — see §4b.** On 2026-08-16, under Hyperspace,
> the save was *not* rewritten at that transition: the screen showed the rolled event while
> the save still held `FINISH_BEACON`. The observation below stands as recorded (vanilla
> `continue.sav`, pre-Hyperspace); it is no longer safe to rely on.

Confirmed again on 2026-08-14 for the case that matters most, a `<choice hidden="true">`
chaining into another event. At the sector exit beacon the save held
`event_FINISH_BEACON_text` with `choices []`; one write later it held
`event_REBEL_TRANSPORT_text` with `choices [0]`. **The roll behind a hidden choice is
visible to the watcher.** That is what lets `FINISH_BEACON` be a pointer card rather than
30 inlined events (`EVENT-CARD.md` §4.2b) — the pool card is on screen only until the
player clicks Continue, and the rolled event's own card replaces it on the next poll.

---

## 4. From text to card

`EncounterState.text` is *"the last situation-describing text shown in an event window"*.
In FTL 1.6.1+ it usually holds a string-table id (`event_ROGUE_REBEL_SEARCH_2_text`), but
the format docs are explicit that it may be the prose itself, so both forms are indexed.

**The index is built from `cards/trees/*.tree.json`, not from `raw/gamedata`.** Each tree
carries a `text` node with `ref` (string id) and `value` (prose) for every node in the
expanded event tree. Indexing the trees therefore answers exactly the right question —
"which card's tree contains the text on screen?" — and needs no traversal logic of its own.

Indexing `raw/gamedata` directly does not work, and the reason is worth recording: the text
on screen is usually an *outcome* sub-event, not the top-level event. A save showing
`event_ROGUE_REBEL_SEARCH_2_text` is inside an anonymous `<event>` within
`<eventList name="ROGUE_REBEL_SEARCH">`, which the card `rebel-fight-chance` (`ROGUE_REBEL`)
covers but does not name.

### textLists must be expanded — the trees alone are not enough

A tree records a `<text load="…">` as the **list name plus a variant count**, never the
individual variants: `{"ref": "PIRATE_BRIBER", "variants": 3}`. The save records the
variant actually displayed — `text_PIRATE_BRIBER_3`. Nothing in any tree contains that
string, so indexing trees alone leaves every list-backed event unresolvable.

`load_textlists()` closes the gap by expanding each `<textList>` from `raw/gamedata`
(reusing `build-mod.py`'s `load_game` / `variants_of`) and indexing every variant's id and
prose against the card whose tree loads that list. Omitting this is not a small loss: it
costs **1033 of the 1782 root texts**, i.e. most beacon arrivals resolve to nothing.

### Resolution order

A single text often cannot name one card — every ship fight ends in `DESTROYED_DEFAULT`.
`Resolver.resolve` applies, in order:

| # | Rule | Meaning |
|---|------|---------|
| 1 | text is exactly one card's **root** | that event just started — switch to it |
| 2 | the card already on screen contains the text | we are deeper in the same event — stay |
| 3 | text is several cards' root | near-identical siblings; show the first |
| 4 | exactly one card's tree contains it | unambiguous |
| 5 | several contain it, nothing to continue from | **show no card** |

Rule 5 is a deliberate refusal. It happens when the watcher starts mid-combat, where
guessing would put a confidently wrong card on screen. The page says the text is shared and
that the next beacon resolves it, which it does.

### Whitespace is normalised on both sides

Prose keys are compared exactly, and `EncounterState.text` "may include line breaks"
(`SavedGameParser`), so the game's copy of a string need not agree with the XML's on where
whitespace falls. `_norm` collapses every run of whitespace to one space at both index and
lookup.

This changes the index by **nothing** — measured: zero of the 4516 keys differ with it on
or off, because the tree values are already clean. Its entire value is on the query side,
where an unmatched save string is the difference between the right card and none. Do not
remove it on the grounds that it has no measurable effect on the index; that is the wrong
side to measure.

### Measured coverage

`--index-report` on the current 386 cards:

```
cards                      386
text keys indexed          4516
root texts (event start)   1782
  pinning exactly one card 1741
  shared by several cards    41
keys in >1 card's tree      738
  of those, not a root      582   <- resolved by stickiness
```

1741 of 1782 root texts pin a single card outright. The 41 that do not are genuine
near-duplicates (the `refugee` variants, the `rebel-auto` ones, the `slug-fight` ones),
where any of the siblings is a fair reading of the screen.

---

## 4b. The log channel — because the save can be a whole event behind

**Measured 2026-08-16, at the exit beacon.** The screen showed *Refueling platform*
(`FUELING_STATION`); `hs_continue.sav`, last written two minutes earlier, still held
`event_FINISH_BEACON_text`, and the watcher was faithfully showing the finish-beacon card.
The save is not rewritten when a `<choice hidden="true">` chains into the event it rolls.

> ⚠️ This **contradicts** §3b, which recorded the opposite for the same transition on
> 2026-08-14: `event_FINISH_BEACON_text` → `event_REBEL_TRANSPORT_text`, "one write later".
> That observation was on a **vanilla `continue.sav`, before Hyperspace was installed**;
> this one is on `hs_continue.sav` under Hyperspace v1.22.2. Both are recorded. Which
> component changed the flush behaviour is not established here — only that the guarantee
> §3b rested on does not hold on the current install.

`FTL_HS.log` does not have the problem. The engine logs every event as it instantiates it:

```
Creating event: FINISH_BEACON
Creating event: FUELING_STATION      <- what is actually on screen
```

So the watcher reads the log too, and **where the log has an answer it wins**. Two reasons,
and the second matters as much as the first:

1. **It is not late.** The line is written when the event is created, not when the game
   next decides to flush a save.
2. **It is an id, not prose.** `event_DESTROYED_DEFAULT_1_text` is shared by sixty cards
   and resolves to `ambiguous`; `Creating event: PIRATE_ESCAPE` names one event outright.

### The rule: the most recent created event that has a card

Sub-events are logged too — `DESTROYED_DEFAULT`, `LANIUS_TRADER_LIST`, `DOWNLOAD_DRONE_DATA`
— and have no cards of their own. Scanning backwards past them lands on the parent, which is
the card that should be on screen. That is the same answer the text index's stickiness rule
computes the long way round, from one line of the log. `Creating ShipEvent:` lines are ship
spawns and are not matched.

The id → slug index is built from `cards/trees/*.tree.json` alongside the text index — 386
cards, same source, no second list to maintain.

**What still comes from the save:** whether a run exists at all (no save, no card, and the
log's last event is the previous run's), the `text_key` reported for debugging, and — on the
vanilla parse path — the sector and beacon numbers. `source` says which channel decided:
`log`, `parse` or `scan`.

**Without Hyperspace there is no log**, and everything falls back to §4 exactly as before.

## 5. The page

A single shell at `http://127.0.0.1:8787/` polls `/current` twice a second and swaps an
iframe to `/card/<slug>` — or to `/sector/<slug>`, per §5b. Serving locally rather than launching a browser per event is what
keeps it to one window that never steals focus — relevant because the point of the second
monitor is that FTL stays drawn on the first (see `mods/fullscreen-no-minimize/`).

Cards are served from `cards/card-<slug>.html` verbatim. They are fragments with their data
inlined, which browsers render directly; no publish step and no network access is involved.

Non-event states render as a short message rather than a blank page. A save caught
mid-write raises `SaveFormatError`; the next poll retries, so a torn read is invisible.

### 5b. Two pages in one frame — the sector profile

The same shell also serves `/sector/<slug>`, the built sector profile
(`tools/SECTOR-PAGE.md`), and `view` in `/current` says which of the two belongs on screen:

| `view` | When | Frame shows |
|---|---|---|
| `choose` | **the sector map is open** — the screen that offers the next sectors (§5d) | `/sectors/index.html?pick=…`, the offer already pinned |
| `sector` | the beacon map is open (§5c), **or** the resolved event is a `START_BEACON_*`, **or** no card resolves at all, **or** within `--sector-hold` seconds of arriving in a new sector | `/sector/<slug>` |
| `card` | none of the above | `/card/<slug>` |

The order is the priority: choosing a sector outranks everything, because it is the one
moment the player is asked a question the wiki can answer.

**The entry beacon is the good trigger.** A `START_BEACON_*` card says "you jump in" and
nothing more, and it is on screen at exactly the moment the question is *what is this
sector* — so the sector profile replaces it. Better still, it stays the last resolved event
for as long as the player sits on the map planning a route, since nothing writes the save
in between. **That covers the map screen, by reading state rather than guessing at it** —
which is most of what the timed window below was for.

The set is read from each sector's `<startEvent>` (`start_event.slug` in the profiles),
never listed in code, so a sector whose entry event changes needs no edit here. Eleven
slugs today. The Last Stand drops out on its own: its `startEvent` is `BOSS_NEUTRAL`, a
*list* rather than an event, so it carries no card slug — and its members are real fights
that must keep showing their own cards. `at_start_beacon` in `/current` reports the test.

**Which sector, and where it comes from.** Not the save — a vanilla parse yields a sector
*number*, the Hyperspace scan not even that, and neither yields the sector *type*, which is
what names a page: the type is regenerated from `sectorTreeSeed` and never stored (§3).
Hyperspace prints it instead. Every generation logs

```
-- Generating Events --
Sector: CIVILIAN_SECTOR
```

to `FTL_HS.log`, and `sectors/data/<slug>.sector.json` carries that same `id`, so the
mapping is a dict lookup over the built profiles — no mod, no inference. `SectorLog` reads
the tail of the log on any mtime change and takes the **last** `Sector:` line; earlier
blocks are the sectors already flown. `--hs-log` overrides the path, which defaults to
beside `ftl.dat`.

**Beacon boxes still open onto cards.** A sector page loads `../cards/runtime/*.js` and
`../cards/data/<slug>.js` when a box is opened (`SECTOR-PAGE.md` §6.1). Served at
`/sector/<slug>`, those resolve to `/cards/...`, which the server serves out of `cards/`.
So the watcher gets the full local behaviour — the version a published artifact cannot have.

**The one heuristic in the whole watcher, stated as such.** *Is the star map open* is not
in the save, and cannot be: the save is written during encounters and is silent while the
player sits on the map. So the arrival window is a guess about attention, not a reading of
state. Two consequences kept deliberately:

- The window is **time-boxed** (`--sector-hold`, default 40s, `0` disables), because
  nothing signals its end either. With the entry-beacon rule above it is now a backstop
  rather than the main path — it earns its keep in The Last Stand, whose entry event is a
  `BOSS_NEUTRAL` fight and therefore triggers nothing. Install `map-signal` (§5c) and it
  is suppressed entirely.
- **Starting the watcher is not an arrival.** On the first read the sector is known but its
  age is not, so it counts as no arrival at all — otherwise every restart would seize the
  screen mid-event on the strength of a log line written an hour ago. Only a *change*
  starts the window.

`--no-sector` turns the whole thing off and restores card-only behaviour.

### 5c. `map-signal` — the exact answer, when the mod is installed

`tools/build-map-signal-mod.py` builds a Hyperspace mod whose only job is to say which
screen the player is on. It reads `starMap.bOpen` — the flag the game itself uses — in a
`MOUSE_CONTROL` render hook, draws nothing, and logs one line per transition:

```
map-signal: loaded
map-signal: open sector 3
map-signal: closed sector 3
```

Lua cannot write files: `io`, `os`, `package` and `debug` are cut from Hyperspace's sandbox
(§2). `log()` is the exception that makes this work — it writes to `FTL_HS.log`, which is
already the file this watcher tails for the sector. So the channel costs nothing new.

**What it changes here.** `SectorLog` takes the **last** `open`/`closed` line as the current
screen and publishes `map_open`. Three states, deliberately distinct:

| `map_open` | Means |
|---|---|
| `true` / `false` | the mod is installed and reporting; `view` follows it exactly |
| `null` | no `map-signal` line in the log — the mod is not installed, and §5b's rules apply unchanged |

The timed window is **suppressed** whenever `map_open` is non-null: a guess is only worth
making where nothing is being reported. The entry-beacon rule stays either way — a
`START_BEACON_*` card is useless whether or not the map is up.

**Only the two state words match.** `map-signal: loaded` and the mod's error lines share the
prefix and must not read as transitions; the regex requires `open` or `closed`. The build
checks its own emitted lines against `save-watch.py`'s actual `MAP_SIGNAL` pattern — imported,
not restated — because a drift between the two halves fails silently: the mod would log
happily and the watcher would ignore every line.

**Hyperspace stamps `[Lua]: ` on every scripted line**, so what reaches the file is

```
[Lua]: map-signal: open sector 2
```

with trailing spaces. The pattern allows that tag and the build tests both forms. This is
worth stating because it is exactly what the first version got wrong: a regex anchored at
`^map-signal:` passed a synthetic test written from the mod's `log()` calls and matched
nothing at all in the real log. **Test the line the file receives, not the line the code
emits.**

**Known limit:** if the game exits with the map open, the last line still says `open` and the
watcher believes it until the next launch truncates the log. Harmless — between runs there is
no card to show anyway, so the sector page is what `view` would choose regardless.

Installing costs a Slipstream patch and a restart (`mods/map-signal/README.md`). Without it
the watcher still works, on §5b's rules.

### 5d. The sector map — the chooser, with the offer already pinned

The same mod reports the *sector* map, which is a different screen from the beacon map and
a different question: not "what is here" but "which of these two do I fly to". It logs the
screen **and the offer**, because the offer is the part nothing else holds:

```
map-signal: choosing 4 -> Rock Homeworlds | Slug Home Nebula
map-signal: chosen
```

`bChoosingNewSector` is the screen; `currentSector.neighbors` is the offer — the engine's
own adjacency, which is what "can travel to" means. The next *column* of the sector map is
not the same set.

The watcher resolves each name against `display_name` / `title` / `short_name` in the
profiles and serves `/sectors/index.html?pick=<slug>,<slug>` — the chooser (`SECTOR-PAGE.md`
§7b) with those sectors already in the comparison panel. A name that resolves to nothing is
**dropped, never guessed**, so a renamed sector shows a short offer rather than a wrong one;
an offer that cannot be read at all still shows the chooser, unpinned, because the screen
being up is itself the fact.

Three or two: the map usually offers two and the panel is built for two, but it can offer
three, and `?pick=` accepts three — the panel grows a column. Pinning by hand stays capped
at two.

**Why the URL beats what was pinned by hand.** The chooser remembers pins in `localStorage`;
`?pick=` overrides them. The offer is not a preference to be remembered over.

### The last card stays up — except when we know it is wrong

Once a card has been displayed it stays there through anything that leaves us *unsure*
what the player is looking at: shared outcome prose, a torn read, a finished run, no event
text. None of those are worth blanking a card the player may still be reading.

**`nocard` is deliberately excluded.** There we have positively identified the event and
simply have no card for it, so holding would assert something false — showing "Pirate
engine hacker" while the screen reads "Pirate briber". That is worse than showing nothing,
and it did happen: it is what made a missing textList index look like a working watcher.
Hold when uncertain, never when known-wrong.

`held: true` marks the display as stale while `status` keeps telling the truth about what
the save says, so the two questions — "what is shown" and "what does the save contain" —
stay separately answerable.

Holding is display-only. The resolver's stickiness (§4 rule 2) runs off a separate anchor
that is **cleared when a run ends**, so a card still on screen from a finished run cannot
capture a shared text in the next one. Conflating the two would make the first shared
outcome of a new run silently continue the old run's card.

### States

`/current` and `--once` return the same object. Its `status` is one of:

| status | Means | Is it a fault? |
|---|---|---|
| `ok` | A card was resolved; `slug` names it. `source` says which channel decided — `log` (§4b), or the structured `parse` / Hyperspace `scan` of the save (§3b) | no |
| `ambiguous` | Shared outcome text, nothing to continue from | no — resolves at the next beacon |
| `nocard` | Event identified, but no card exists for it | no — 386 of 449 events have one |

`ambiguous`, `noevent`, `nosave`, `error` and `waiting` leave the previous card on screen
with `held: true`, if there was one. `ok` replaces it; `nocard` clears it.

| `noevent` | Save holds no event text | no |
| `nosave` | `continue.sav` absent — no run in progress | no |
| `waiting` | Server up, first poll not done | no |
| `error` | Parse failed; `detail` carries the message | usually transient |

Only `error` warrants investigation, and only if it persists across several polls — a
single one is almost always a save caught mid-write.

### When it misbehaves

- **Nothing is picked up at all, and `--once` works fine.** The running watcher is older
  than the code. Python reads `save-watch.py` and `ftlsave.py` once, at import, so an edit
  never reaches a watcher that is already up — and the watcher is designed to be left
  running for hours, which makes this the most likely explanation for a sudden total
  stop. Observed 2026-08-15: a watcher started at 11:46 was still following
  `continue.sav` at 16:50, because `SAVE_NAMES` learned `hs_continue.sav` at 15:44.
  `--once` passed the whole time, because it runs the code on disk.

  The watcher now says so itself, once, on the first poll after either source changes:

  ```
  [stale] ftlsave.py changed on disk since this watcher started at 11:46.
  [stale] This process is still running the old code -- restart it.
  ```

  **Restart it after any edit to `tools/`.** Nothing hot-reloads.

  The startup line names the save it resolved, which is the other half of this check —
  under Hyperspace it must read `hs_continue.sav`:

  ```
  watching C:\Users\...\FasterThanLight\hs_continue.sav   (auto, re-resolved each poll)
  ```

- **Card never changes.** The save's mtime drives everything; confirm the game is writing
  by re-running `--once` after a jump.
- **Wrong card, and `reason` is `continued`.** Stickiness latched onto the wrong tree.
  Restarting the watcher clears it; the next root text re-pins it correctly.
- **Card looks stale.** Check `held`. If it is true the save no longer names that event,
  and the card is deliberately still up; `status` says why.
- **`error: no <shipBlueprint name=…>`.** The player is flying a ship this repo's
  `raw/gamedata/` does not define — a modded ship, or gamedata older than the install.
- **`error: unexpected first byte`.** Not a format-11 save. See §6.

---

## 6. What is not handled

- **Save formats other than 11.** `ftlsave.py` refuses anything else rather than
  mis-parsing it. FTL 1.03.3 and 1.5.x saves would need the older branches, which the
  reference parser has and this port omits.
- **Multiverse saves.** Untested. Multiverse adds content on top of Hyperspace; the scan
  below should still find the encounter text, but nothing has verified it.

- **Events with no card.** 386 of 449 top-level events have one; the rest report the raw
  text id, matching `event-labels`, which also never invents a name.
