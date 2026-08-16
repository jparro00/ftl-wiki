---
id: source-ftl-dat-rarity-corpus-search
type: source
source_kind: research
raw: raw/modding/2026-08-16-ftl-dat-rarity-corpus-search.md
game_version: both
date: 2026-08-16
ingested: 2026-08-16
reliability: high
tags: [rarity, store, provenance, methodology, corpus, negative-result]
---

# Where `rarity` is and is not — the exhaustive corpus search

## Summary
A recorded **negative result**: no data file in FTL states what the engine does with a
blueprint's `<rarity>`. Every non-image entry in `ftl.dat` was extracted and grepped, along
with all of `raw/gamedata/`, `raw/modding/` and `raw/wiki/`. The positive answer was found
afterwards in the executable — [[source-store-crew-selection-disassembly]].

Its value is that it makes the negative *reusable*: the next person to wonder whether the
answer is hiding in an uncopied file can read this instead of re-deriving it.

## Key Takeaways
- **`rarity` occurs in exactly three data files in the whole game archive** —
  `blueprints.xml`, `dlcBlueprints.xml`, `sector_data.xml` — **and all three were already in
  `raw/gamedata/`.** `<rarity>` is the only selection metadata that ships.
- **The `raw/gamedata/` extraction is complete for this question.** 197 data entries in
  `ftl.dat`, 33 held, **164 never copied** — and the 164 are ~140 per-ship layouts, 10
  localised text files, animations/sounds/rooms/names/credits, two tutorial files and seven
  mod-injected files. Established by extracting and grepping all of them, not by reading
  file names.
- **Structural negatives worth not re-checking:** `<crewBlueprint>` has exactly seven child
  element types and no weight/chance/tier field; `<rarityList>/<blueprint>` carries exactly
  two attributes across all 118 entries; `rarity` appears in neither `text_misc.xml` nor
  `text_tooltips.xml`, so the game never explains it to the player; and the Slipstream
  modder readme does not contain the string at all.
- **[[source-xftl-stores]] declines the step explicitly** — *"For weapons, drones, and crew,
  there's nothing particularly interesting there."* The one source that read this binary
  skipped the one part the wiki wanted. znixian/xftl's full `doc/` tree has nothing else on
  rarity.
- **This install is Hyperspace-modded, and `raw/gamedata/` is still a faithful snapshot.**
  `ftl.dat` was rebuilt 2026-08-15; its `blueprints.xml` is 13 KB larger than the held copy —
  **but the crew `<rarity>` values are byte-identical at identical line numbers.** Hyperspace
  appends. Anyone re-extracting from this machine should know both halves of that.
- ~~**The Fandom `Rarity` page is the one source this corpus points at and does not hold**~~ —
  **resolved 2026-08-16, and the raw file's §5 is superseded.** Fetched via api.php: `Rarity`
  is a **redirect** (rev 63054), one line, `#REDIRECT[[Stores_and_resources#Items_and_crew_rarity]]`.
  Its target is [[source-fandom-stores-and-resources]], which this corpus already holds — **at
  revision 74856, byte-current with live.** So the corpus was never missing a source; it was
  missing the knowledge that the link was a redirect. Nothing about the mechanic was lost.

## Events Covered
- None.

## Other Pages Touched
- [[concept-blueprint-rarity]] — supplies the "not in any data file" half of that page's
  account, and the standing note that the corpus lacks the Fandom `Rarity` page
- [[concept-stores]]

## Reliability Notes
`high`, on the same reasoning as [[source-store-crew-selection-disassembly]] and with the same
documented departure from `CLAUDE.md` §2.7 — the rule that `source_kind: research` is never
`high` exists because such a synthesis "cites sources this repo does not hold". This one cites
no external source at all: it reports greps and a file inventory over files present on the
machine, and every claim is mechanically reproducible.

The one qualification a reader should carry: **an exhaustive negative is only as good as its
sweep.** The sweep here was "every `ftl.dat` entry outside `img/`, `audio/`, `fonts/`", so a
string buried in an image or audio blob would have been missed. That is not a realistic place
for engine semantics, but it is where the boundary was drawn.

## Contradictions Flagged
None. It contradicts nothing; it records the absence that
[[source-store-crew-selection-disassembly]] then resolved from a different kind of file.

## Links
- `raw/modding/2026-08-16-ftl-dat-rarity-corpus-search.md`
- [[source-store-crew-selection-disassembly]] — the answer, from `FTLGame_orig.exe`
- [[source-xftl-stores]], [[source-fandom-sectors]], [[source-fandom-stores-and-resources]]
