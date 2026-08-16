# Where `rarity` is and is not — an exhaustive search of `ftl.dat` and the source corpus

Search notes, 2026-08-16. Produced by instruction, by reading the installed game archive and
every file in this repo's source layer. Source layer: do not edit.

**The question at the time:** does any *data* file state what the engine does with a
blueprint's `<rarity>` — the weighting function behind store stock? The answer was no, and
this file records the negative in enough detail that it does not have to be re-derived. The
positive answer was found afterwards, in the executable:
`2026-08-16-store-crew-selection-disassembly.md`.

---

## 1. The result in one line

**`rarity` occurs in exactly three data files in the entire game archive** —
`data/blueprints.xml`, `data/dlcBlueprints.xml`, `data/sector_data.xml` — **and all three
were already in `raw/gamedata/`.** `<rarity>` is the only selection metadata that ships. No
data file says what reads it.

Method: extract every non-image/audio/font entry from `ftl.dat` and grep the lot. Not a
file-name inspection.

---

## 2. `ftl.dat` inventory, and the diff against `raw/gamedata/`

Archive: `D:\Steam\steamapps\common\FTL Faster Than Light\ftl.dat`.

| | Count |
|---|---|
| Live entries | 3,465 |
| Excluding `img/`, `audio/`, `fonts/` | **197 data entries** |
| Present in `raw/gamedata/` | 33 |
| **Never copied** | **164** |

The 164 uncopied entries, by category:

| Category | Approx. count | Could it hold store logic? |
|---|---|---|
| Per-ship layout pairs `<ship>.xml` + `<ship>.txt` (kestral, mantis_*, rock_*, jelly_*, fed_*, boss_*, anaerobic_*, circle_*, crystal_*, energy_*, rebel_*, stealth_*, auto_*) | ~140 | No — room and door geometry |
| Localised text `text-de/es/fr/it/ja/ko/pl/pt/ru/zh-Hans.xml` | 10 | No — translations of strings already held |
| `animations.xml`, `dlcAnimations.xml`, `sounds.xml`, `dlcSounds.xml`, `rooms.xml`, `names.xml`, `credits.txt` | 7 | No |
| `tutorial.xml`, `text_tutorial.xml` | 2 | No |
| Mod-injected — see §4 | 7 | No |

**Grep over all 197 extracted entries** hits `rarity` (case-insensitive) in four:
`data/blueprints.xml`, `data/dlcBlueprints.xml`, `data/sector_data.xml` — all three already
held — plus `data/example_system.lua:12`, a Hyperspace sample custom-system blueprint that
merely *contains* a `<rarity>1</rarity>` tag and explains nothing.

**Conclusion: the extraction into `raw/gamedata/` is complete with respect to this question.**
No uncopied file carries rarity data or rarity semantics.

---

## 3. Negatives worth keeping

Each of these was checked rather than assumed, and each closes off a plausible place to look:

- **`<crewBlueprint>` has exactly seven child element types**, enumerated programmatically
  across `blueprints.xml` and `dlcBlueprints.xml`: `desc`, `cost`, `bp`, `title`, `short`,
  `rarity`, `powerList/power`, plus `colorList/layer/color`. **No weight, chance, tier or
  pool field.**
- **`<rarityList>/<blueprint>` carries exactly two attributes** across all 118 entries in
  `sector_data.xml`: `name` and `rarity`. Zero others. 13 `rarityList` blocks.
- **`sector_data.xml`'s complete tag vocabulary** is `FTL, sector, sectorDescription,
  sectorType, name, nameList, rarityList, blueprint, event, startEvent, track, trackList`.
  Nothing store-related; nothing about slot counts.
- **`rarity` appears in neither `text_misc.xml` nor `text_tooltips.xml`** — the game never
  explains the attribute to the player, so there is no in-game string to mine.
- **`slipstream-1.9.1-readme_modders.txt` does not contain the string at all.** It documents
  the `.ftl` append/find-replace format, not engine semantics.
- **`2026-08-15-xftl-stores.txt` declines the step**, in as many words (lines 34–39):

  > `== Filling out a section ==`
  > *"For weapons, drones, and crew, there's nothing particularly interesting there."*
  > *"It appears the same goes for augments, so it can offer non-stacking augments that you
  > already own."*

  Sections (2–4 inclusive), system selection and resource ranges are all documented there;
  per-item selection is the one thing the author skipped.
- **`2026-08-15-xftl-sector-map.txt`** (203 lines) concerns `StarMap::*` only; it mentions
  stores twice, both as a beacon-filter predicate.
- **znixian/xftl's full `doc/` tree** was fetched and searched: `grep -i rarity` over it
  returns nothing. The two files already in `raw/modding/` are all it has on this.

Crew rarities re-verified line-for-line while there: `blueprints.xml:103` human 1, `:127` engi
2, `:140` mantis 2, `:167` slug 0, `:193` rock 3, `:218` crystal 0, `:241` energy 5, `:2164`
battle 0, `:2174` repair 0; `dlcBlueprints.xml:216` anaerobic 0.

---

## 4. This install is Hyperspace-modded — and `raw/gamedata/` is not stale

Worth recording, because it affects how any future extraction from this machine should be
read:

- `ftl.dat` was rebuilt 2026-08-15 and now contains `data/hyperspace.xml` (205 KB) and this
  repo's own `data/beacon-reveal.lua`, plus `example.lua`, `example_system.lua`,
  `examples.lua`, `example_layout_syntax.xml`, `fonts.png`.
- `FTLGame.exe` is 125 MB against a pristine `FTLGame_orig.exe` of 5.5 MB; `patch/` holds
  `.bps` binary patches.
- The archive's `data/blueprints.xml` is **147,424 bytes** against `raw/gamedata/`'s
  **134,064**.

**Checked: the crew `<rarity>` values in the modded archive are byte-identical, at identical
line numbers, to the copies in `raw/gamedata/`.** Hyperspace appends; it did not rewrite crew
rarity. So `raw/gamedata/` is a faithful vanilla snapshot for this purpose.

Two lines of `data/hyperspace.xml` bear on the question and are noted rather than relied on,
since that file is Hyperspace's config reference and not a vanilla data file:

- `:3050` — *"A store category has 3 (or fewer) items of a specific type inside it"* — an
  independent echo of the three-slot count, from a mod that reimplements the store UI.
- `:3068` — *"blueprint can either be empty or a blueprintList — if it is empty, it will use
  vanilla generation"*. **Hyperspace defers to vanilla generation and nowhere documents it.**
  Its own `<groupChance>` / `<chance>` percentages are a replacement mechanism, not a
  description of the vanilla one. A dead end, but a definitively checked one.

---

## 5. One source the corpus points at and does not hold

`raw/wiki/sectors.md` links `[[Rarity|rarity]]` **17 times**. That page is **not** in
`raw/wiki/` — `_manifest.csv` has 292 rows and no `Rarity` entry. It is the only source this
corpus explicitly references and lacks. `tools/pull-fandom.ps1` would fetch it. Recorded as a
known gap; it became a curiosity rather than a blocker once the binary answered the question.

---

Nothing was modified: `ftl.dat`, the game install, both executables and `raw/` were read only.
Extractions went to a session scratchpad.
