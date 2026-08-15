Synthesised on 2026-08-15 by instruction. Source layer: do not edit.
Title: Naming every beacon on the sector map before it is revealed — what it would take
Question asked: "make a mod that shows the name of the event above each beacon in the sector,
                even if it hasn't been revealed yet — a cheat that tells me where everything is"
Source kind: research. Cites external repositories and documentation this wiki does not hold;
             every claim below carries its URL and the date it was read (2026-08-15).

---

## 0. Verdict

**Vanilla-moddable FTL cannot do this. FTL Hyperspace can, and everything the job needs is
already exposed to its Lua API.** The engine decides each beacon's event when it generates the
sector, long before you jump there, so the information exists in memory the whole time — the
mod's job is only to draw what the game is already holding back.

Two routes, in order of preference:

| Route | Where | Mechanism | Coverage | Effort |
|---|---|---|---|---|
| **A — Lua overlay** | §3 | Read `starMap.locations`, print each event's name at its beacon | Every beacon, every sector, no per-event authoring | One Lua file + a generated name table |
| **B — `<beaconType>` labels** | §5 | Attach a Hyperspace beacon label to each event in XML | Only events the mod explicitly names | ~450 XML patches, and a load-order trap (§5.2) |
| ~~**C — no mod at all**~~ | §4 | Read the save file | **None — measured 2026-08-15, §4.1** | ruled out |

A and B require Hyperspace, and Hyperspace costs more than the mod does (§7). C was measured
first and is dead: the save holds nothing at all about an unvisited beacon (§4.1).

---

## 1. Why no vanilla mod can do it

Slipstream patches `ftl.dat`, which holds XML data, images, audio and fonts. The sector map is
drawn by compiled code in `FTLGame.exe` — `StarMap::RenderSectorMap`, `StarMap::PopulateGrid`
and friends, named in the xftl reverse-engineering notes already in this repo at
`raw/modding/2026-08-15-xftl-sector-map.txt`. No data file describes what is drawn above a
beacon, so no data file can change it. Nothing in Slipstream's Advanced XML (`mod:findName`,
`mod-append`) reaches compiled render code; it edits the XML tree only.

That leaves the engine-level mod as the only in-game option.

---

## 2. The engine already knows, and hides it on purpose

Three independent confirmations that an unvisited beacon's event exists before you arrive:

1. **`StarMap::AddQuest` filters candidate beacons** on properties only an existing event can
   have — "Is not a store", "Is not a distress beacon" — while also requiring the beacon
   "Have not been visited" (`raw/modding/2026-08-15-xftl-sector-map.txt`). Unvisited beacons
   therefore already carry an event whose store/distress flags can be read.
2. **The game reveals store and distress markers when you are within one jump**, per
   `raw/wiki/beacons.md`. It is withholding, not computing late.
3. **The save file does not store beacon events** (§4) — it stores `sectorLayoutSeed`, and
   Vhati's `SavedGameParser` comments that this seed "determines the graphical positioning of
   beacons, as well as their environment hazards (like nebula/storm) and events". The map is
   regenerated from the seed at load, events included.

So the cheat is a *reveal*, not a computation.

---

## 3. Route A — a Hyperspace Lua overlay (recommended)

Everything below is from the Hyperspace wiki, read 2026-08-15:
<https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Hyperspace-Module>,
`.../wiki/Lua-Graphics-Module`, `.../wiki/Lua-Defines-module`, `.../wiki/Lua-Script-Module`.

### 3.1 The data is all exposed

`StarMap` (reached as `Hyperspace.App.world.starMap`, or
`Hyperspace.Global.GetInstance():GetCApp().world.starMap`) exposes verbatim:

```
std::vector<Location> .locations      (Read-only)
Location .currentLoc / .potentialLoc / .hoverLoc
std::vector<Sector*> .sectors
Sector .currentSector
bool .bMapRevealed
Point .dangerZone
int .worldLevel                       (Read-only)
```

and inherits from `FocusWindow`: `bool .bOpen` — the flag that says the map screen is up.

`Location` exposes:

```
Pointf .loc                 -- position on the map
std::vector<Location> .connectedLocations
bool .beacon / .known / .dangerZone / .nebula / .boss
int .visited
LocationEvent .event        <-- the whole point
```

`LocationEvent` exposes, among others:

```
std::string .eventName
TextString .text            -- :GetText() resolves id or literal
bool .store / .distressBeacon / .repair / .beacon / .reveal_map / .secretSector
std::string .quest
int .environment / .fleetPosition
ResourceEvent .stuff / .reward
std::vector<Choice> .choices
```

`Location.event` is readable regardless of `known` or `visited`. **That single fact is the
whole cheat.** `eventName` additionally means the label can be the event's own id without any
text matching.

### 3.2 Drawing it

`Defines.RenderEvents` (full list on the Defines wiki page) contains **no star-map layer**.
The usable hook is `MOUSE_CONTROL`, which renders on every screen including the map — and is
the hook Hyperspace's own text-drawing example uses:

```lua
script.on_render_event(Defines.RenderEvents.MOUSE_CONTROL, function()
	local text = "This text is colored, like [style[color:FF0000]]red[[/style]], …"
	Graphics.freetype.easy_printAutoNewlines(13, 100, 100, 300, text)
end, function () end)
```

Text functions available (`Graphics.freetype.*`):
`easy_print`, `easy_printCenter`, `easy_printAutoNewlines`, `easy_printNewlinesCentered`,
`easy_printRightAlign`, `easy_measureWidth`, `easy_measurePrintLines`. The first argument is a
**font id, not a point size** — valid ids are in `fonts.png` inside the Hyperspace zip.
`CSurface.GL_Translate` / `GL_PushMatrix` / `GL_PopMatrix` are exposed for coordinate work.

Sketch of the whole mod:

```lua
script.on_render_event(Defines.RenderEvents.MOUSE_CONTROL, function()
    local starMap = Hyperspace.App.world.starMap
    if not starMap.bOpen then return end
    for i = 0, starMap.locations:size() - 1 do
        local loc = starMap.locations[i]
        local label = LABELS[loc.event.eventName] or loc.event.eventName
        Graphics.freetype.easy_printCenter(FONT_ID,
            loc.loc.x + MAP_ORIGIN_X, loc.loc.y + MAP_ORIGIN_Y - LABEL_RISE, label)
    end
end, function() end)
```

`MAP_ORIGIN` is the one unknown constant. xftl gives the starting point: beacon coordinates
"are offset such that 0,0 is drawn at 45,40 relative to the outer edge of the window, not
including the glow". Confirm against Hyperspace's own `CustomMap.cpp`, which re-implements
`StarMap::OnRender` and translates by the same offsets, rather than by nudging numbers.

### 3.3 Where the labels come from

`eventName` is a raw id (`GIANT_ALIEN_SPIDERS`). This repo already holds a mapping from id to
a human title for **386 of 449 top-level events** — the card titles used by the `event-labels`
mod (`tools/EVENT-LABELS.md` §2). Generating a Lua table from `cards/trees/*.tree.json` gives
the overlay the same names the cards and the in-event labels use, from one source, for free.

If `eventName` turns out to be empty for engine-generated base events, the fallback is
`loc.event.text` → the string-table id → the same card, which is exactly what
`tools/save-watch.py` already does (`SAVE-WATCH.md` §4). Check this by logging `eventName` for
every location in one sector — not by trial and error on the label format.

### 3.4 Free extras, same API

- `starMap.bMapRevealed = true` — the engine's own map-reveal flag, now settable from Lua.
- `<showAllConnections enabled="true"/>` in `hyperspace.xml` — "Shows all beacon connections in
  the beacon map" (verbatim comment in Hyperspace's `Mod Files/data/hyperspace.xml`).
- Hyperspace's command console has `EXIT` and `STORE` commands that convert your current
  location, per the same file.

---

## 4. Route C — no mod at all, and why it can only be partial

The save file is parsed by this repo already (`tools/ftlsave.py`), and its beacon list sits
*before* the encounter block, so it is inside the range the parser already walks safely. Per
Vhati's `SavedGameParser` (`readBeacon`), each beacon stores exactly:

```
visitCount, [background images + sprite pos/rotation if visited],
seen, enemyPresent, [shipEventId, autoBlueprintId, shipEventSeed if enemyPresent],
fleetPresence, underAttack, [store inventory if a store]
```

**There is no field for the beacon's event.** What leaks is genuinely useful — which beacons
hold a ship and which ship event, which hold a store and its entire stock, fleet presence — but
the general event id is absent, recoverable only by reimplementing FTL's map generation from
`sectorLayoutSeed` bit-exactly, PRNG included. That is a reverse-engineering project, not a mod.

### 4.1 Measured, 2026-08-15 — the answer is zero

`tools/ftlsave.py --beacons` on a live sector-1 save (Crystal Cruiser B, 21 beacons, player at
beacon 3):

```
beacons       21 total, 20 unvisited
  unvisited  ships 0 (named 0) | stores 0 | seen-flag 3
  all        ships 0 (named 0) | stores 0 | seen-flag 4
```

**Not one unvisited beacon carries a ship event, a ship blueprint or a store.** A sector-1 map
of 20 unvisited beacons certainly contains both, so these fields are runtime state written on
arrival, not generation-time state serialised for the whole sector. `seen` behaves exactly as
`raw/wiki/beacons.md` describes — set on the current beacon and its three neighbours — and even
those carry no ship or store data.

The parse is trustworthy here: the only beacon with `visit_count > 0` is beacon 3, which equals
the save's own `current_beacon_id`, and the encounter block after it decodes to coherent start
text. A misaligned read would not land on both.

**Route C is therefore dead for this purpose.** It cannot name beacons, and it cannot even
pre-empt ships or stores. Nothing about an unvisited beacon reaches the save; it exists only in
the running engine's `Location.event`, which is Route A.

---

## 5. Route B — `<beaconType>` XML labels

Hyperspace supports per-event map labels natively. From `CustomEvents.h`
(<https://github.com/FTL-Hyperspace/FTL-Hyperspace/blob/master/CustomEvents.h>, read
2026-08-15):

```cpp
struct BeaconType
{
    std::string eventName;
    GL_Color color;
    bool global = false;
    bool persistent = false;
    bool hideVanillaLabel = false;
    TextString beaconText;
    TextString undiscoveredTooltip;
    TextString unvisitedTooltip;
    TextString visitedTooltip;
    std::string equipmentReq;
};
```

`CustomEvent` carries `BeaconType *beacon`, plus `loadBeacon` and `renameBeacon`.
`ParseCustomBeaconType` in `CustomEvents.cpp` reads attributes `id` (localization id) or `text`
(literal), `req`, `global`, `persist`, `hideVanillaLabel`, and child nodes `unvisitedTooltip`,
`visitedTooltip`, `undiscoveredTooltip`, `color`. `<beaconType>` is handled inside
`ParseCustomEventNode`, i.e. it is a child of `<event>`.

The three separate tooltips — **undiscovered**, unvisited, visited — are strong evidence that
labels are shown for beacons the player has not reached. Vanilla precedent agrees: quest
beacons "are marked as 'QUEST' on the map and can be seen from any distance away once spawned"
(FTL Fandom, *Beacons*). The `req` attribute gates a label behind carrying a piece of
equipment, which is the idiomatic way to make this an opt-in cheat: an augment you install to
turn the map spoiler on.

### 5.2 The trap

Beacon labels are read from the **first** declaration of an event, not the last —
FTL-Hyperspace issue #216: "Normally, the last declaration of an event determines the options.
However, beacon labels are set by the first instance of an event rather than the last." The
entire `event-labels` mod is built on the opposite rule ("whenever multiple tags share the same
name, only the last one counts", Slipstream's `readme_modders.txt`). So a `.append` that
redefines an event to add `<beaconType>` **will silently do nothing**. Route B must instead use
Advanced XML to insert the tag into the original definition in place — the upgrade path
`tools/EVENT-LABELS.md` §4 already flags for other reasons.

This is why Route A is preferred: one file, no per-event patching, no load-order semantics.

---

## 6. Unresolved

- **Exact render conditions for `<beaconType>` labels.** The parsing code was located; the
  drawing code was not — it is in neither `StarMap.cpp` nor `CustomMap.cpp` as far as could be
  read, and `CustomEvents.cpp` is 270 KB and could not be fetched whole. Whether an undiscovered
  beacon draws its *label* (as opposed to its tooltip) is therefore inferred from the struct and
  from vanilla quest behaviour, not read from the source. Only affects Route B.
- **Whether `LocationEvent.eventName` is populated for engine-generated base events**, or only
  for events Hyperspace's `CustomEvents` has processed. Affects the label lookup in Route A;
  the `text` fallback covers it either way.
- **The map origin constant** for drawing in `MOUSE_CONTROL`'s coordinate space (§3.2).
- **Whether `locations` covers only the current sector** (near-certain — `StarMap::GenerateMap`
  builds one sector's beacons at a time) and what it holds while `bChoosingNewSector` is true.

---

## 7. What Hyperspace costs

From the official Steam/Windows install guide
(<https://ftl-hyperspace.github.io/FTL-Hyperspace/install-guides/windows/steam-install/>,
read 2026-08-15) and this repo's own notes:

- **It downgrades the game.** "This downgrader will **ONLY** work for Steam's 1.6.14 version of
  FTL" — and downgrades it to **1.6.9**. `raw/gamedata/` was extracted from a 1.6.14 install
  (`raw/gamedata/_PROVENANCE.md`), and `tools/save-watch.py` reads ship layouts live from the
  installed `ftl.dat`, so both would then be describing a different build than the one running.
- **"Uninstall any other FTL mods before proceeding!"** — `event-labels` would need re-patching
  through Slipstream afterwards.
- **It probably breaks the save watcher.** `tools/SAVE-WATCH.md` §6 already records that
  Hyperspace extends the save format and that `ftlsave.py` targets vanilla AE. The watcher and
  this mod may be mutually exclusive until the parser is taught the extended format.
- **Uninstalling means deleting `Hyperspace.dll` by hand**; unticking it in Slipstream is not
  enough (`raw/modding/2026-08-12-ftl-modding-research.md` §7).
- Installation is: run `downgrade.bat` next to `FTLGame.exe` (which becomes 122 MB), then patch
  `Hyperspace.ftl` with Slipstream 1.9.1 — the same Slipstream already installed here.

### 7.1 What 1.6.9 actually differs by

The downgrade sounds worse than it is. The Hyperspace project's own position, stated twice in
its community: "the versions between 1.6.9 and 1.6.14 only add a Japanese translation and Steam
achievements." Corroborated by Subset's own announcements — FTL 1.6.12 (2019-12-19) "adds
Japanese to the list of supported languages", and Steam achievements arrived in the 2020-01
update. Subset's public changelog at `subsetgames.com/ftl_changelog.html` stops at 1.6.2, so
there is no first-party per-version list beyond those announcements; a secondhand report that
1.6.12 also fixed pre-1.5.12 saves and a charge-weapon bug could not be traced to a primary
source and is recorded here as unconfirmed.

| | 1.6.9 | 1.6.14 |
|---|---|---|
| Events, ships, weapons, sectors, balance | identical | identical |
| Japanese localisation | no | yes (1.6.12) |
| Steam achievements | no | yes (2020-01) |
| Hyperspace | works | impossible |

**Steam achievements are the only real loss**, and only while downgraded: FTL keeps its own
achievement state in `ae_prof.sav` regardless, so what stops is the Steam-side unlocking, not
the game's own tracking.

### 7.2 What the downgrade touches, and what it does not

From the install steps: the game folder "should look exactly the same" afterwards except that
`FTLGame.exe` is replaced (122 MB) and the original is preserved beside it as
`FTLGame_orig.exe`. `ftl.dat` is only *checked* ("should be very close or exactly the same
size", a test that you have no mods patched in) — the downgrader does not rewrite it.

Two consequences for this repo:

- **`raw/gamedata/` stays valid.** It was extracted from this install's `ftl.dat`, which the
  downgrade leaves alone. The ship layouts `tools/save-watch.py` reads live from `ftl.dat`
  likewise stay correct, since Hyperspace's own patch appends rather than replaces.
- **Reverting is a file swap** — restore `FTLGame_orig.exe` and unpatch in Slipstream, which
  keeps a pristine backup of the data anyway. The one irreversible-feeling step, deleting
  `Hyperspace.dll` by hand, is also just a file.

Undocumented and worth expecting: Steam updating or verifying the install will put 1.6.14's
`FTLGame.exe` back, at which point `downgrade.bat` has to be re-run. The install guide says
nothing about this either way.

---

## Links

- Hyperspace Lua — Hyperspace module (classes and fields):
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Hyperspace-Module>
- Hyperspace Lua — Graphics module (freetype text, CSurface):
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Graphics-Module>
- Hyperspace Lua — Defines module (full `RenderEvents` list):
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Defines-module>
- Hyperspace Lua — Script module (`on_render_event` and friends):
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Script-Module>
- `CustomEvents.h` — `BeaconType`:
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/blob/master/CustomEvents.h>
- `CustomMap.cpp` — Hyperspace's `StarMap::OnRender` re-implementation:
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/blob/master/CustomMap.cpp>
- Issue #216 — beacon labels take the *first* event declaration:
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/issues/216>
- Release notes (StarMap exposure, `GET_BEACON_HAZARD`, `bMapRevealed`):
  <https://github.com/FTL-Hyperspace/FTL-Hyperspace/releases>
- Steam/Windows install guide (the 1.6.14 → 1.6.9 downgrade):
  <https://ftl-hyperspace.github.io/FTL-Hyperspace/install-guides/windows/steam-install/>
- Vhati's `SavedGameParser` — beacon fields and `sectorLayoutSeed`:
  <https://github.com/Vhati/ftl-profile-editor/blob/master/src/main/java/net/blerf/ftl/parser/SavedGameParser.java>
