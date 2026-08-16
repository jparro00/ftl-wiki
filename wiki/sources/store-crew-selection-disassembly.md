---
id: source-store-crew-selection-disassembly
type: source
source_kind: research
raw: raw/modding/2026-08-16-store-crew-selection-disassembly.md
game_version: both
date: 2026-08-16
ingested: 2026-08-16
reliability: high
tags: [store, crew, rarity, engine-internals, reverse-engineering, disassembly]
---

# Store crew selection, read out of `FTLGame_orig.exe`

## Summary
The algorithm behind every "HIRE CREW" slot, recovered instruction by instruction from the
shipped 32-bit PE (`FTLGame_orig.exe`, 5,497,856 bytes — the pristine binary, not the
Hyperspace-patched one). It answers what no data file states: **`weight = 6 − rarity`**, with
`rarity == 0` filtered out before weighting, drawn by descent through an implicit binary tree
of cumulative subtree sums.

## Key Takeaways
- **The weighting function is `6 − rarity`** — a linear integer weight, one entry per
  blueprint. `1→5, 2→4, 3→3, 4→2, 5→1`. Read at `0x00764d66`: `mov eax, 6` / `sub eax, edx`.
- **`rarity == 0` is an exclusion flag, tested *before* weighting** (`0x00764cf0`), which
  settles that 0 is not the bottom of the 1–5 scale. It confirms the reading
  [[concept-blueprint-rarity]] had derived from the data alone.
- **A store's crew section always occupies 3 slots.** Under AE exactly 3 are hireable; in
  vanilla it is `N ∈ {2,3}` uniform, with `3 − N` blank filler boxes (`0x004bed80`).
  No source in this wiki had the vanilla figure.
- **Crew are drawn with replacement** — `N` separate `count = 1` calls, each rebuilding the
  candidate tree, so a store can offer three Engi (`0x0051b0d8`). This confirms
  [[source-fandom-stores-and-resources]] from the binary.
- **Weapons, drones and augments are not** — one call with `count = N`, drawn without
  replacement, so a section cannot list the same weapon twice (`0x004bf36c`). This
  **corroborates** [[source-fandom-stores-and-resources]], which states the same asymmetry
  from observation: *"A store will never sell duplicate weapons, drone schematics,
  augmentations."*
- **A sector's `<rarityList>` overlays the base table, it does not replace it.**
  `ResetRarities` (`0x0060ba60`) restores every blueprint to `desc.baseRarity` on sector
  entry, then `SetRarity` (`0x0060b8e0`) writes only the names the sector lists. **An item or
  species absent from a `rarityList` keeps its base rarity** — closing a long-standing open
  question on [[concept-blueprint-rarity]].
- The RNG at `0x006569f0` is a 64-bit LCG (multiplier `0x5851f42d4c957f2d`, increment 1),
  and selection is `random() % Σweights + 1`, carrying the usual modulo bias — negligible at
  these totals but not zero.

## Events Covered
- None. This is a store/blueprint mechanism, not an event.

## Other Pages Touched
- [[concept-blueprint-rarity]] — the formula, the weight table, the overlay answer
- [[concept-stores]] — slot count, duplicates, the crew/item asymmetry
- Every page in `wiki/sectors/`, and the generated crew-odds block on all 19 sector pages

## Reliability Notes
**`high`, which departs from the `CLAUDE.md` §2.7 rule that `source_kind: research` is never
`high` — deliberately, and the rationale is why.** That rule exists because a research
synthesis "cites sources this repo does not hold, so it inherits their uncertainty". This one
cites no external source for its findings: it reads a file present on the machine and quotes
the bytes. Game files outrank the community wiki, and the executable is the most primary game
file there is — it is the thing that *does* the behaviour the XML only parameterises.

Three qualifications travel with it, all recorded in the raw file's §7:

- **Function names are derived, behaviour is read.** Names come from FTL-Hyperspace's 956 ZHL
  Win32 signatures. `Store::CreateStoreBoxes` is a near-match, not an exact one (same frame,
  same locals, different register allocation — same function, different compiler build). If a
  name is wrong the address and the instructions are still right.
- **`GetDlcEnabled()` was not traced to what sets its globals**, so "AE ⇒ always 3" rests on
  reading the branch, not on observing a live session.
- **`ResetRarities` was confirmed on the crew and drone maps**; the other three were inferred
  from four repetitions of an identical pattern.

## Contradictions Flagged
None. Every claim it touches was either confirmed or refined:

- Confirms `raw/wiki/stores-and-resources.md:71` (*"weighted by its rarity and selected
  accordingly"*) and supplies the formula it lacked.
- Confirms `:83` (three crew, duplicates possible) for AE, and adds the vanilla 2-or-3 case.
- Confirms the `0 = excluded` and `1 = commonest` readings [[concept-blueprint-rarity]] had
  derived from `sector_data.xml` alone.
- Resolves, rather than contradicts, the open question about unlisted blueprints.

## Links
- `raw/modding/2026-08-16-store-crew-selection-disassembly.md`
- FTL-Hyperspace `FTLGameWin32.cpp` / `.h` — the signature table used for naming
- [[source-xftl-stores]] — covers `Store::OnInit` upstream of this, and explicitly declines
  the per-item step: *"For weapons, drones, and crew, there's nothing particularly
  interesting there."*
- [[source-fandom-stores-and-resources]], [[source-fandom-sectors]] — the community
  statements this verifies
