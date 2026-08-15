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

## 5. The page

A single shell at `http://127.0.0.1:8787/` polls `/current` twice a second and swaps an
iframe to `/card/<slug>`. Serving locally rather than launching a browser per event is what
keeps it to one window that never steals focus — relevant because the point of the second
monitor is that FTL stays drawn on the first (see `mods/fullscreen-no-minimize/`).

Cards are served from `cards/card-<slug>.html` verbatim. They are fragments with their data
inlined, which browsers render directly; no publish step and no network access is involved.

Non-event states render as a short message rather than a blank page. A save caught
mid-write raises `SaveFormatError`; the next poll retries, so a torn read is invisible.

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
| `ok` | A card was resolved; `slug` names it. `source` says whether it came from the structured parse or the Hyperspace scan (§3b) | no |
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
