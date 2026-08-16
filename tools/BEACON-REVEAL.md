# Beacon reveal mod — specification

Normative spec for the `beacon-reveal` mod pipeline. Self-contained: an agent with no prior
context can rebuild, verify and extend the mod from this document alone.

The mod labels every beacon on the sector map, **whether or not it has been explored**. It is a
deliberate map spoiler. It draws and does nothing else — no event, choice, reward, ship, odds or
save byte is touched.

Two layers, so the map stays readable:

| Where | Shows | Example |
|---|---|---|
| Boxed label on the beacon | the **category** — the sector event pool the beacon was rolled from | `DISTRESS_BEACON_ENGI` |
| The game's own tooltip, on hover | the **concrete event**, by its card title, in place of "An unvisited location." | `Pirate ship distress trap` |

The box is drawn to match the game's own `STORE` / `EXIT` labels, and its outline is coloured by
the pool's section — green store, orange distress, red hostile, purple nebula, blue quest.

```
cards/trees/*.tree.json ──► mods/beacon-reveal/src/ ──► beacon-reveal.ftl ──► Slipstream
   (title = the label)      build-beacon-mod.py         --pack                (after Hyperspace)
                            + beacon-reveal.lua.tmpl
```

**Requires FTL Hyperspace.** See §6 for why nothing else can do this.

---

## 1. Quick start

```bash
python tools/build-beacon-mod.py            # generate mods/beacon-reveal/src/
python tools/build-beacon-mod.py --pack     # ... and zip it to beacon-reveal.ftl
python tools/build-beacon-mod.py --install  # ... and patch it into the game
python tools/build-beacon-mod.py --verify   # re-check a generated tree without rebuilding
```

**Use `--install`, and restart FTL afterwards.** A rebuilt `.ftl` that is never patched into
`ftl.dat` is invisible: the game keeps running the previous build and the only symptom is that
the change "didn't work". That cost a full debugging round during development — the log said
`using fallback origin 45,40` long after the constant had been corrected in the source. The
game reads the Lua from `ftl.dat` at startup, so a running instance never picks up a rebuild.

`--install` does the equivalent of, from `C:\Users\jparr\Documents\Slipstream`:

```powershell
java -jar modman.jar --patch Hyperspace.ftl event-labels.ftl beacon-reveal.ftl
```

Slipstream's CLI is the whole interface — `--patch` reverts to vanilla and applies the named
mods in order, so there is no GUI step. `modman_admin.exe` demands elevation; `java -jar
modman.jar` does not. `--patch` with **no** mods throws a NullPointerException; to get back to
vanilla, copy `Slipstream\backup\ftl.dat.bak` over the game's `ftl.dat`.

---

## 1a. Turning it on and off

**There is no in-game toggle.** No hotkey, no config file, no menu entry — the script draws
whenever the star map is open, and the only switch is whether it is patched into `ftl.dat`.
Toggling is therefore a Slipstream re-patch, and **FTL must be closed** for it: Slipstream
cannot rewrite `ftl.dat` underneath a running game.

**On** — from the repo root:

```
python tools\build-beacon-mod.py --install
```

**Off** — from `C:\Users\jparr\Documents\Slipstream`, the same patch minus this mod:

```
java -jar modman.jar --patch Hyperspace.ftl event-labels.ftl
```

`--patch` reverts to vanilla *first* and then applies exactly the mods named, so omitting
`beacon-reveal.ftl` removes it while leaving Hyperspace and the event-labels mod in place.
`PATCH_ORDER` in `tools/build-beacon-mod.py` is the authoritative list of what a full install
applies — read it rather than trusting the command above if the two ever differ.

Do **not** run `--patch` with no mods at all (NullPointerException, §1). To reach true vanilla,
copy `Slipstream\backup\ftl.dat.bak` over the game's `ftl.dat`.

Before toggling, two checks that cost a run if skipped:

- **Is FTL running?** `Get-Process FTLGame`. If it is, the game may be holding an unsaved run —
  confirm `hs_continue.sav` exists (Hyperspace's run save) before closing it, and ask the user.
- **Relaunch through `mods\fullscreen-no-minimize\launch-ftl.cmd`**, never `FTLGame.exe`
  directly, or the two-monitor fix is lost (CLAUDE.md §5.2d).

Toggling is safe mid-run: the mod is draw-only (invariant B2) and writes no save byte, so a run
in progress survives being switched either way. Confirm the result in `FTL_HS.log` — a
`beacon-reveal: loaded, N names` line after the next launch means on, its absence means off.

---

## 1b. Where the category comes from

The runtime gives an event id (`DISTRESS_ENGI_REBEL`), not a category. The category is the
**sector event pool** that can produce it — an `<eventList>` named in `sector_data.xml`, e.g.
`<event name="DISTRESS_BEACON_ENGI" min="1" max="3"/>`.

That mapping is generated from `sectors/data/*.sector.json`, which the sector-profile pipeline
already expands from pool to concrete events. The category table is therefore a **projection of
`extract-sector.py`'s work**, not a second parse of the game files — retitle or re-extract a
sector and the categories follow.

**It is scoped per sector**, because pool membership overlaps far more across sectors than
within one: `ASTEROID_EXPLORE` sits in six different `NEUTRAL_*` pools game-wide, but only one
of them belongs to any given sector.

Three rules decide the pool, in order. All three are in `load_categories()`.

**1 — a nested list beats the list that contains it.** A sector list can load another list
wholesale: `NEUTRAL_CIVILIAN` contains `<event load="DISTRESS_BEACON"/>`
(`raw/gamedata/newEvents.xml:158`), so flattening makes all 14 distress events members of both.
`extract-sector.py` records the inner list as `via`, and it wins whenever it is itself one of
**that sector's** allocation lines — a restriction that keeps every label inside the vocabulary
of the sector page's budget table rather than inventing pool names the player has never seen
(`NEBULA` nests `NEBULA_REBEL`, which is not a Civilian line, so those stay `NEBULA`). 28 pairs
resolve this way.

**2 — Advanced Edition additions count.** `entry["override"]["added"]` holds what an `OVERRIDE_X`
list adds to `X`; 31 pairs across 16 sectors. Merging them is not a guess — see §1c.

**3 — otherwise first pool in sector order wins**, deterministically. 91 of 1307 sector/event
pairs (7.0%) are still genuine non-nesting overlap; the build prints the count so it cannot
drift unnoticed.

> ⚠️ Rule 1 was added after rule 3 alone was found to make an entire allocation line
> **unreachable**. Every one of `DISTRESS_BEACON`'s 14 events in Civilian Sector and Federation
> Space drew `NEUTRAL_CIVILIAN`, so a line that rolls 1–2 beacons every single game could never
> be named — the map reported it under another line's name and nothing in the build said so.
> `verify()` now fails on any allocation line whose every event resolves elsewhere.

Three fallbacks, in order: the current sector's table → `ANY_SECTOR` (events whose pool is the
same in every sector that has them, 190 of them) → the raw event id, drawn with a dim outline so
"no category known" is visible rather than silently wrong.

**The shared `NEUTRAL` fallback is in the table too.** A beacon left over once a sector's table
is exhausted draws from `NEUTRAL` / `OVERRIDE_NEUTRAL`, which almost no sector names in
`sector_data.xml` — so without it those beacons either drew a raw id or, worse, were
mis-attributed to a real pool by the reverse lookup and inflated its apparent count.
`extract-sector.py` emits the membership as `generation.fallback_events` (AE ∪ vanilla), and the
build appends it **last**, after every real line, so an allocated beacon always keeps its own
line's name.

The sector is identified at runtime by
`starMap.currentSector.description.name:GetText()` — its **display** name ("Engi Controlled
Sector"), which is why `BY_SECTOR` is keyed by `display_name` from the sector profiles.

## 2. Where the label comes from

Identical to `tools/EVENT-LABELS.md` §2: the root `title` of `cards/trees/<slug>.tree.json`,
which is the H1 of the wiki event page. **The wiki is the label source**, so the map, the card
and the in-event label all say the same string, and retitling a page moves all three.

Coverage is the carded set — **386 of 449 top-level event definitions**. An event with no card
shows its **raw event id** instead (`ROGUE_REBEL`), which is deliberate: the mod never invents
a name, and an id is still a useful answer.

Titles are ASCII-folded because FTL's bitmap fonts have no glyphs for typographic punctuation;
verification fails on any byte above 0x7E.

---

## 3. How it works

`StarMap::GenerateMap` picks each beacon's event when the **sector** is generated, not when the
player arrives — `StarMap::AddQuest` filters unvisited beacons on their store/distress flags,
which only an already-assigned event can have
(`raw/modding/2026-08-15-xftl-sector-map.txt`). The engine simply declines to draw it until you
are one jump away. `Location.event` reads fine on an unvisited beacon, so the mod is a
**reveal, not a computation**.

The save file cannot substitute for this: it stores no beacon event at all, only
`sectorLayoutSeed` to regenerate them from — measured, `tools/SAVE-WATCH.md` §3.

### 3.1 The three Hyperspace facts it rests on

| Need | Binding |
|---|---|
| Every beacon in the sector | `starMap.locations` — `std::vector<Location>`, read-only |
| Is the map on screen | `starMap.bOpen`, inherited from `FocusWindow` |
| What is at this beacon | `Location.event.eventName`, plus `.loc` for where to draw |

Reached from `Hyperspace.Global.GetInstance():GetCApp().world.starMap`.

### 3.1b Drawing the box

`Graphics.CSurface.GL_DrawRect(x, y, w, h, colour)` and `GL_DrawRectOutline(..., lineWidth)`,
with `GL_Color(r, g, b, a)` on 0–1 floats, and `easy_measureWidth` to size the box to the text.
The namespaces are resolved once at load (`Graphics.CSurface or Hyperspace.CSurface`) so a
future rename fails loudly instead of per frame.

`easy_printCenter`'s `y` is the **vertical centre of the glyphs** — established by measurement,
not assumed — so the box is centred on the same point, with `GLYPH_H = 8` at font id 10.

**Hover** is resolved by comparing `starMap.hoverLoc.loc` against each location's `loc` **by
coordinates, not by object identity**: SWIG does not promise to hand back the same wrapper
object for the same underlying pointer, so `==` on the userdata is not reliable.

`Defines.InternalEvents.GET_BEACON_HAZARD` (`Location loc → string hazardText`) is the *native*
way to attach a tooltip to a beacon, and was deliberately not used: it marks the beacon as a
**hazard**, adding an icon and implying danger on every beacon. Drawing our own box below the
beacon keeps the map honest.

### 3.2 Where the text goes

`Defines.RenderEvents` has **no star-map layer**. `MOUSE_CONTROL` renders on every screen, so
it fires over the map; `bOpen` is what keeps the labels off every other screen. Text is drawn
with `Graphics.freetype.easy_printCenter(FONT, x, y, text)` — the first argument is a **font
id, not a point size** (see `fonts.png` in the Hyperspace zip).

Screen position is **`starMap.position + loc.loc`**, read out of Hyperspace's own
`StarMap::OnRender` reimplementation in `CustomMap.cpp`, which translates by `position` once
and then by each `loc.loc`.

**Measured 2026-08-15: `starMap.position` is not exposed to Lua**, and **the xftl notes' 45,40
origin is wrong** — it drew every label 337 px left and 90 px above its beacon. The mod runs on
a measured constant instead: **ORIGIN = (382, 116)**.

How it was measured, since this is the one number not derived from the running engine. With the
labels drawn at a known formula (`loc + ORIGIN`, minus `RISE` in y), three beacons were paired
against their own labels on screen and the delta computed in FTL's 1280x720 virtual space
(physical pixels ÷ 3 at 4K):

| pair | beacon | label centre | delta |
|---|---|---|---|
| `FINISH_BEACON` — "Long-range beacon (sector exit)" | 999, 483 | 661, 393 | 338, 90 |
| `EMPTY_STATION2` — "Abandoned station" | 397, 506 | 61, 415 | 336, 91 |
| `GIANT_ALIEN_SPIDERS` — "Giant alien spiders" | 574, 258 | 237, 168 | 337, 90 |

Three widely separated beacons agreeing to within 1 px is what establishes that the mapping is
a **pure translation with no scale factor** — a scaling error would have diverged across the
map. Each pair was identified unambiguously (the exit marker, and two labels whose events are
uniquely identifiable), so no guesswork entered the pairing.

If a future Hyperspace exposes `starMap.position`, the mod prefers it automatically and says so
in the log. The hover probe (§5) re-measures the constant at any time without a rebuild.

### 3.3 Vector indexing — measured, not assumed

SWIG's `std::vector` binding **raises `SWIG_IndexError` on an out-of-range index** rather than
returning nil. A tolerant loop over `0 .. size()` is therefore not tolerant at all: it throws on
the last iteration and, under `pcall`, silently kills the whole frame's drawing. That is exactly
what the first build did, and the log is how it was caught:

```
[Lua]: beacon-reveal: [string "data/beacon-reveal.lua"]:458: SWIG_IndexError:in vector::__getitem__()
```

`detect_base` now probes `locations[0]` once per session under `pcall`, logs the answer, and the
loops run `base .. base + size() - 1`.

---

## 4. Registration, and the one XML subtlety

Hyperspace loads Lua through a `<scripts>` list in `hyperspace.xml`, and that file states that
**"only one `<scripts>` is allowed"** while multiple `<script>` children are fine. A plain
append would declare a second `<scripts>` element. So the mod ships Advanced XML that edits
Hyperspace's existing element in place:

```xml
<mod:findLike type="scripts">
	<mod-append:script>data/beacon-reveal.lua</mod-append:script>
</mod:findLike>
```

This is the first mod in this repo to use Advanced XML; `event-labels` deliberately uses only
plain appends (`EVENT-LABELS.md` §4). Confirmed working: `FTL_HS.log` reports
`Loading Lua file: data/beacon-reveal.lua` followed by the script's own load line.

**Patch order matters** — Hyperspace must be patched before this mod, or there is no
`<scripts>` element to find.

---

## 5. Verification

`--verify` runs all of it; a build runs it automatically and exits non-zero on failure.

| Check | Catches |
|---|---|
| No byte above 0x7E in the Lua | a glyph FTL cannot render |
| Every one of the 386 labels appears in the Lua | a silently dropped event |
| Every sector appears in `BY_SECTOR`, and the category tables are non-empty | a sector-profile rename silently emptying the categories |
| No allocation line is unreachable — every line with events must be drawable | a category the map can never name, so a line that rolls is reported under another line's name (§1b) |
| No pool name collides with a card title | category and event name cross-wired in the template, which would only show on the map |
| `GL_DrawRect`, `GL_DrawRectOutline` and `easy_measureWidth` are all present | a boxed label that cannot render |
| Exactly one `script.on_render_event` registration | a double-registered hook, which Hyperspace warns is easy to do |
| No unsubstituted `%%` placeholder | a template token that never got filled |
| The append parses as XML, and carries no `<FTL>` wrapper | malformed emission; Slipstream adds the root itself |
| The append does **not** declare its own `<scripts>` | the one-`<scripts>` rule in §4 |
| The append uses `mod:findLike` + `mod-append:script` | a registration that silently registers nothing |
| `metadata.xml` has all five elements, none empty | Slipstream parses it strictly and rejects the whole mod on the first missing value |

Beyond the build, two runtime signals in `FTL_HS.log`, neither needing a screenshot:

- `beacon-reveal: loaded, 386 names` — the script parsed and registered.
- `beacon-reveal: sector N: named K beacons, U of them unvisited -- e.g. …` — once per sector,
  proof that unvisited beacons are being read and named.

Errors inside the render hook are caught by `pcall` and logged **once per distinct site**, so a
fault cannot spam a per-frame log or take the game down with it.

---

## 6. Why there is no non-Hyperspace version

The sector map is drawn by compiled code in `FTLGame.exe`. Slipstream patches data and images
only, and Advanced XML edits the XML tree — neither reaches a renderer. The save file holds
nothing about an unvisited beacon (measured: zero ships, zero stores across 20 unvisited
beacons). Hyperspace is the only route, and it costs a downgrade to FTL 1.6.9. The full
argument, with sources, is `raw/modding/2026-08-15-beacon-name-labels-mod.md`.

---

## 7. Invariants

- **B1 — The label is the card title, verbatim**, or the raw event id when there is no card.
  Never an invented name.
- **B2 — Draw only.** No event, choice, effect, reward, ship, odds or save byte is altered.
  The mod adds one Lua file and one `<script>` entry; it touches no game XML.
- **B3 — Nothing hand-written per event.** Labels are generated; the code lives in
  `tools/beacon-reveal.lua.tmpl`. Never edit `mods/beacon-reveal/src/`.
- **B4 — Deterministic.** Same trees → byte-identical `.ftl`, including zip timestamps.
- **B5 — Fails quiet, logs loud.** A binding that is missing or renamed by a future Hyperspace
  must degrade to "no labels" plus one log line, never to a crash.

---

## 8. Known limits

- **63 events carry no card**, and show their raw id. Give one a wiki page and a card, and the
  next build picks it up with no code change.
- **Boxes on a crowded map can still overlap** each other and the vanilla `STORE` / `EXIT`
  tags. Category names are much shorter than event titles, which is most of why the switch to
  categories helped, but nothing de-collides them yet.
- **ORIGIN is resolution-assumed.** It was measured at 3840x2160 and converted to FTL's
  1280x720 virtual space, where it should be resolution-independent — but that has only been
  checked at one resolution. If labels drift after a resolution change, re-measure with the
  hover probe.
- **English only**, as with `event-labels`: labels come from the wiki, not the string table.
- **Conflicts** with any mod that also edits `<scripts>` only in the trivial sense that both
  scripts load; the mod defines no game content, so it cannot clobber events or ships.
