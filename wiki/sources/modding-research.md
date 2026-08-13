---
id: source-modding-research
type: source
source_kind: research
raw: raw/modding/2026-08-12-ftl-modding-research.md
game_version: both
date: 2026-08-12
ingested: 2026-08-13
reliability: medium
tags: [modding, file-format, methodology, tooling, external-research]
---

# FTL modding — research notes (2026-08-12)

## Summary
A synthesis of external modding documentation — Subset Games' official mods page, Slipstream
Mod Manager's `readme_modders.txt`, the FTL Hyperspace MOD README, and two community tutorials
— written into `raw/` by instruction rather than dropped in as a captured page. It documents
the `.ftl` archive format, the `.xml.append` convention, Slipstream's `mod:` Advanced XML
namespace, and the event → eventList → sector wiring needed to add an event to the game. Its
own header says: *"Treat the citations, not this document, as authority."*

## Key Takeaways

- **`.ftl` is a renamed `.zip`**, containing only `data/`, `audio/`, `fonts/`, `img/` and
  `mod-appendix/` at its root. `mod-appendix/` is not inserted into game resources; Slipstream
  reads `metadata.xml` from it.
- **The append convention.** `events.xml.append` is appended to the vanilla `events.xml`
  rather than replacing it. Overriding vanilla content works by reusing an identical tag name —
  *"only the last one counts"*. Slipstream **strips the `<FTL>` root before appending and
  restores it after**, so an append file must not carry its own wrapper.
- **Advanced XML.** Plain appending can only add; the `mod:` namespace lets a mod find and
  edit existing tags (`mod:findName`, `mod:findLike`, `mod:findWithChildLike`,
  `mod:findComposite`; then `mod:setValue`, `mod:setAttributes`, `mod:removeAttributes`,
  `mod:removeTag`, `mod-append:`, `mod-overwrite:`). This is the mechanism that lets two mods
  coexist.
- **Wiring a new event is a four-file chain** — `events*.xml` defines it, `<eventList>` groups
  it, `sector_data.xml` allocates it to beacons via `<event name="…" min="…" max="…"/>` inside
  a `<sectorDescription>`, and `text_events.xml` holds the prose behind an id. Exactly the
  structure this wiki reads in reverse.
- **FTL Hyperspace** patches the executable for engine-level modding: custom species, systems,
  augments, unlimited ships, a larger event vocabulary including `req` checks against cargo,
  custom secret-sector warps, and a Lua API from 1.2.0. Caveats: custom ships get no
  achievements and no high scores; uninstalling requires deleting `Hyperspace.dll` by hand.
- **No Steam Workshop** — distribution is the Subset Games forum.
- **Subset's own conflict warning:** *"if two mods write over the same files, they will never
  be able to work together successfully"* — the reason the append convention exists.

## Claims it verified against this repo's own data

The document marks three checks **[verified locally]**, all of which hold:

- `raw/gamedata/` is the **unpacked** archive contents — no `.dat` is present, so unpacking
  happened before drop-in. This is what `raw/gamedata/_PROVENANCE.md` describes.
- **Every data XML is wrapped in a single `<FTL>` root**, which is why `tools/extract-event.py`
  descends through the wrapper.
- **No shipped `<eventList>` carries weights**, so duplicating an entry is the only weighting
  mechanism available — independently the central finding of
  [[concept-event-list-weighting]].

## What this means for the wiki's own tooling

The document's §9 is the part with teeth for this repo:

- If a **mod** were ever ingested as a source, `tools/extract-event.py` would need two things it
  does not have: `.xml.append` handling (concatenate onto the vanilla tree, last definition
  wins) and the `mod:` namespace, under which the effective event tree becomes *vanilla plus a
  patch script* rather than a set of flat definitions. Today the extractor assumes one flat
  definition per name, with DLC-file load order as the only override mechanism.
- The `<FTL>` wrapper handling and the load-order override rule the extractor already
  implements are the same mechanics Slipstream operates on — mild corroboration that both
  readings of the format are right.

## Events Covered
None. This source describes the file format and the toolchain, not game content.

## Other Pages Touched
- [[concept-modding-and-the-append-convention]] — new, the filed form of this source
- [[concept-event-list-weighting]] — corroborated from outside the data
- [[concept-event-tree-grammar]] — the `<FTL>` wrapper and load-order override
- [[concept-sector-event-allocation]] — the `sectorDescription` allocation step, from the
  mod-author's direction

## Reliability Notes
`medium`, and the reason is worth stating: the underlying citations are strong — Slipstream's
`readme_modders.txt` is the tool's own reference documentation and Subset Games' page is
first-party — but this file is a **synthesis written by an LLM**, not a captured document, so
the wording between the citation and this page has no independent check. It outranks a single
observed run and does not outrank `raw/gamedata/`. Where it makes a claim about *this repo's*
data it marks the check inline, and all three of those held up on re-verification.

**Schema note:** `source_kind: research` and the `raw/modding/` directory are both extensions
beyond `CLAUDE.md` §2.7 (`gamedata | wiki | run`) and §1's layout. Flagged for the schema, not
silently absorbed into `wiki`.

## Contradictions Flagged
None with anything in the wiki. It corroborates three existing findings and contradicts none.

## Links
- [Subset Games — official mods page](https://subsetgames.com/ftl_mods.html)
- [Slipstream Mod Manager — readme_modders.txt](https://github.com/Vhati/Slipstream-Mod-Manager/blob/master/skel_common/readme_modders.txt)
- [FTL Hyperspace — MOD README](https://github.com/FTL-Hyperspace/FTL-Hyperspace/blob/master/MOD%20README.txt)
- [Steam guide — Making Mods for FTL](https://steamcommunity.com/sharedfiles/filedetails/?id=277959176)
- [CaptainShooby FTL modding tutorial](https://docs.google.com/document/d/18DgjbF054eNRNNRwg_cuDT2DatdRpnW16mzX32GB-Dw/pub)
- Full citation list in `raw/modding/2026-08-12-ftl-modding-research.md`
