---
id: concept-modding-and-the-append-convention
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [modding, file-format, tooling, methodology]
---

# Modding FTL — the `.ftl` format, the append convention, and what it would take to ingest a mod

## Definition & Context
This wiki reads FTL's data files in one direction: XML in `raw/gamedata/` → events → pages.
Mod authors write the same files in the other direction, and the conventions they follow
explain *why the vanilla data looks the way it does* — and define exactly what
`tools/extract-event.py` would have to learn before a modded event could be ingested at all.

The primary source is [[source-slipstream-readme-modders]] (per
`raw/modding/slipstream-1.9.1-readme_modders.txt`), Vhati's own reference documentation shipped
inside the Slipstream distribution. [[source-modding-research]] (per
`raw/modding/2026-08-12-ftl-modding-research.md`) is a synthesis that summarized it secondhand
alongside Subset Games' official mods page and the Hyperspace README; where the two differ, the
readme wins. The event-labels mod (`tools/EVENT-LABELS.md`) is this page applied.

## How the game stores data

Content ships in packed archives, which modders never touch directly — **Slipstream Mod
Manager** (by Vhati, endorsed by Subset Games as *"the go-to method of using mods with FTL"*)
unpacks and repacks them.

> ⚠️ **CONTRADICTION — which archive 1.6.x uses.** [[source-modding-research]] says *"`ftl.dat`
> in older builds, `data.dat` + `resource.dat` in 1.6.x"*. A local **FTL 1.6.x install has a
> single `ftl.dat`** whose first four bytes are `PKG\n`, and `tools/ftlpkg.py` — written to read
> it — describes itself as an extractor for *"FTL 1.6.x `PKG\n` archives (ftl.dat)"*. The eras
> are reversed in the synthesis: `data.dat` + `resource.dat` is the **1.5.13-and-earlier**
> layout, and 1.6.x merged them into one `PKG\n` archive. Trusting the install and the
> extractor, which agree with each other, over the summary that agrees with neither.
> (Observed 2026-08-13 at `D:\Steam\steamapps\common\FTL Faster Than Light`.)

`raw/gamedata/` in this repo is that archive **already unpacked** — no `.dat` is present, so
unpacking happened before drop-in. Every file is wrapped in a single `<FTL>` root element,
which is why the extractor descends through the wrapper before looking for `<event>`.

## The `.ftl` format

An `.ftl` file **is a renamed `.zip`**. Its root may contain only:

```
data/    audio/    fonts/    img/    mod-appendix/
```

Ship only the files you modify. `mod-appendix/` is *not* inserted into game resources —
Slipstream reads `metadata.xml` from it for the mod's title and description.

> ⚠️ **CONTRADICTION — `metadata.xml` "optional".** [[source-slipstream-readme-modders]] calls
> it an *"Optional embedded description"*. It is optional to include, but **once present it is
> parsed strictly**: an empty `<threadUrl/>` produced `strict parsing failed: Missing
> threadUrl.` in `modman-log.txt` under Slipstream 1.9.1, and the mod vanished from the list
> entirely rather than loading without a description. Both statements are true of different
> things — the file is optional, its contents are not — but "optional" invites the wrong
> reading. Observed while building the event-labels mod, 2026-08-13.

## The append convention — the important part

A file named `events.xml.append` is **appended to** the vanilla `events.xml`, not substituted
for it. The rule that falls out of that:

- **Overriding vanilla content means reusing an identical tag name — "only the last one
  counts."**
- **New content should use unique names**, so two mods do not collide.
- **An append file must not carry its own `<FTL>` wrapper.** Slipstream strips the root before
  appending and restores it afterwards (FTL 1.6.1+).

Subset Games' own warning is the reason all of this exists: *"if two mods write over the same
files, they will never be able to work together successfully."*

This is the same last-definition-wins rule the extractor already implements for the shipped
DLC files — `dlcEventsOverwrite.xml` redefining a name from `events.xml` is vanilla FTL doing
to itself what a mod does from outside. ([[concept-event-tree-grammar]],
[[source-dlceventsoverwrite]])

**Two rules, not one.** [[source-slipstream-readme-modders]] states last-wins twice, about
different actors, and only the first was previously recorded here:

- *"Whenever multiple tags share the same name, only the last one counts"* — how **Slipstream**
  resolves duplicates while patching.
- *"You can still override existing tags by adding your own with the same 'name' attribute,
  since **FTL honors the last it sees**"* — said of `.rawappend`, where Slipstream deliberately
  does no parsing at all. So the resolution is the **game's**, not the patcher's.

That distinction is what makes a text-only mod safe: a mod need not redefine an event to change
what it says, because the engine itself takes the last definition of any name.

### Line endings, encoding, and what the game can display

- Save as ASCII or UTF-8; UTF-16 and Windows-1252 are tolerated. **Slipstream converts all line
  endings to CR-LF while patching**, so LF source files are fine — except in `layout.txt`,
  where LF crashes the game. File and directory names must be plain ASCII.
- **FTL 1.01–1.5.13 assumes windows-1252; 1.6.1+ assumes UTF-8.** On a modern install, non-ASCII
  text is therefore *read* correctly, and the remaining question is *"whether the fonts contain
  the glyphs to display the characters. You may need to replace the fonts."* Encoding and glyph
  coverage are separate failure modes, and only the second still bites on 1.6.x.

## Advanced XML — the `mod:` namespace

Appending can only *add*. Slipstream's Advanced XML lets a mod **find and edit** existing tags,
which is how mods coexist rather than clobber.

| Find | Purpose |
|---|---|
| `<mod:findName type="…" name="…">` | match a tag by type and `name` |
| `<mod:findLike type="…">` + `<mod:selector>` | match by attributes / value |
| `<mod:findWithChildLike type="…" child-type="…">` | match a parent via one of its children |
| `<mod:findComposite>` + `<mod:par op="AND\|OR">` | combine criteria |

All find tags accept `reverse`, `start`, `limit` and `panic` — defaulting to search forward,
skip none, return everything, and **not** error when nothing matches. Inside a match:
`<mod:find>` (recurse into children), `<mod:setValue>`, `<mod:setAttributes>`,
`<mod:removeAttributes>` (SMM 1.7+), `<mod:removeTag>`, `<mod-append:Element>`,
`<mod-overwrite:Element>` (replaces the first such child, else appends).

Three details from [[source-slipstream-readme-modders]] that a summary of the tag list loses:

- **`<mod:findName>` searches backwards.** Its defaults are `reverse="true" start="0"
  limit="1"` — it finds the *last* match, not the first. Given that last-definition-wins is the
  override rule, matching the last one is the correct behaviour, but a patch written assuming
  "first match" will silently hit a different tag.
- **`panic="false"` by default means a typo is silent** — a `<find…>` matching nothing is a
  no-op, not an error. The `--global-panic` command-line flag turns every such miss into a
  failure, which is the only way to catch a typoed patch.
- **Order is document order**, and *"when patching several mods at once, later mods edit in the
  wake of earlier ones"* — so a mod's effect depends on the patch order the user sets.

Slipstream ships an **XML Sandbox** under its File menu for testing these interactively, and
`--patch` / `--validate` accept **directories** as well as `.ftl` files, so a generated mod tree
can be tested without zipping it.

### Raw append — the escape hatch

`X.xml.rawappend` concatenates with no parsing at all; `X.xml.rawclobber` replaces the file
outright. Both exist for XML too non-standard to parse, and both are last resorts: any mod
patched afterwards must treat the same file as raw as well, or avoid it.

## Wiring an event into the game — the chain in reverse

A mod author adds an event in four steps, which are precisely the four layers this wiki reads
backwards:

1. **`events.xml`** (or any `events_*.xml`) — `<event name="MY_EVENT">` with its `<text>`,
   `<choice>` children and effects. → [[concept-event-tree-grammar]]
2. **`<eventList name="MY_LIST">`** — group related events; the engine picks one member.
   **No shipped list carries weights**, so duplicating an entry is the only weighting
   mechanism available — an outside confirmation of what
   [[concept-event-list-weighting]] concluded from the data alone.
3. **`sector_data.xml`** — `<event name="MY_LIST" min="1" max="2"/>` inside a
   `<sectorDescription>` allocates it to beacons. A custom sector needs `name`, `minSector`, a
   `startEvent`, and its own allocations. → [[concept-sector-event-allocation]]
4. **`text_events.xml`** — prose lives behind an id (`<text id="event_MY_EVENT_text"/>`), which
   is why every quoted string in this wiki is resolved through the string table rather than
   read inline. → [[source-text-events-xml]]

Tutorial testing trick: comment out the vanilla `<sectorDescription>` entries so the map
generator can only offer your custom sector.

## FTL Hyperspace — engine-level modding

A separate project that patches the executable, going well past XML: custom species with new
abilities, custom systems, unlimited custom ships, custom augments, a much larger event
vocabulary (including `req` checks against cargo — compare [[concept-blue-options]]), custom
secret-sector warps, and a Lua API from 1.2.0.

- Windows; Linux via WINE with `xinput1_4` and the Hyperspace DLL as library overrides.
- Install by extracting next to `FTLGame.exe`, then installing `Hyperspace.ftl` through
  Slipstream. **Uninstalling requires deleting `Hyperspace.dll`** — removing the mod in
  Slipstream is not enough.
- Configured via `data/hyperspace.xml`; mods ship a `hyperspace.xml.append`.
- Custom ships get **no achievements and no saved high scores**.

Tools beyond Slipstream: **Superluminal2** (visual ship/layout editor), 7-Zip (inspect `.ftl`
archives), GIMP (art). Distribution is the Subset Games forum — FTL has **no Steam Workshop**.

## Implications For This Wiki

- **The extractor is vanilla-only, and that is a real boundary.** `tools/extract-event.py`
  assumes one flat definition per name with DLC-file load order as the only override
  mechanism. Ingesting a mod would need `.xml.append` handling (concatenate onto the vanilla
  tree, last definition wins) and `mod:`-namespace support — under which the effective event
  tree is *vanilla plus a patch script*, not a set of definitions. Nothing in the pipeline
  models that today.
- **A mod source would need its own `version` value.** The frontmatter vocabulary is
  `ae | vanilla | both | unknown`; modded content is none of those, and quietly filing it as
  `ae` would corrupt the one field this wiki uses to resolve contradictions.
- **Mild corroboration of existing readings.** The `<FTL>` wrapper and the last-one-wins
  override rule the extractor already implements are the same mechanics Slipstream operates
  on.
- **The wiki can now write in the other direction.** `tools/build-mod.py` generates the
  event-labels mod from `cards/trees/*.tree.json` — the same data the cards render — so a wiki
  page's title becomes text the game prints. Reading FTL and writing FTL now use one pipeline;
  see `tools/EVENT-LABELS.md`.

### Pitfalls worth knowing before generating event content

- **FTL crashes on event loops.** If a choice loads an event whose choice loads the first, the
  game dies at the main menu or hangar. Any tool that emits `<event load="…"/>` chains can
  produce one, and the failure appears nowhere near the mod.
- Modded level-5 shields make asteroid storms abnormally fast (FTL bug, fixed in 1.03.3).
- Paired explore/battle music tracks play simultaneously; mismatched durations leave silence.

## Related
- [[concept-event-tree-grammar]] — the grammar a mod author writes into
- [[concept-sector-event-allocation]] — step 3 of the chain, read forwards here
- [[concept-event-list-weighting]] — step 2, and the claim this source corroborates
- [[concept-blue-options]] — the `req=` vocabulary Hyperspace extends

## Open Questions
- [ ] Whether malformed mod XML fails loudly or silently **in game** — still no source. Partly
      answered for the *patcher*: Slipstream validates archive structure and metadata before
      patching (`Validate`, `--validate`), and `--global-panic` catches Advanced XML finds that
      match nothing. Neither says what the engine does with XML that patched cleanly but is
      wrong.
- [ ] Slipstream's behaviour when two mods use Advanced XML against the same tag. Narrowed:
      *"later mods edit in the wake of earlier ones"*, so the second sees the first's output —
      but whether that is always well-defined is untested.
- [ ] Whether FTL 1.6.x fonts carry glyphs beyond ASCII. The engine reads UTF-8 fine; the
      readme warns only that fonts may lack glyphs. `tools/build-mod.py` folds labels to ASCII
      rather than find out.
- [ ] Whether the `OVERRIDE_*` lists in the AE data are a modding hook or purely internal —
      relevant to [[concept-sector-event-allocation]]'s unreachable-content question.
- [ ] The `.dat` archive format itself — not needed while Slipstream abstracts it.

## Sources
- [[source-slipstream-readme-modders]] (per raw/modding/slipstream-1.9.1-readme_modders.txt) —
  primary; the tool author's own reference documentation
- [[source-modding-research]] (per raw/modding/2026-08-12-ftl-modding-research.md) — the
  secondhand synthesis it supersedes on the append convention and Advanced XML
