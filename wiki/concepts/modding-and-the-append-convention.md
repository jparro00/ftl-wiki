---
id: concept-modding-and-the-append-convention
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 1
related_events: []
tags: [modding, file-format, tooling, methodology]
---

# Modding FTL — the `.ftl` format, the append convention, and what it would take to ingest a mod

## Definition & Context
This wiki reads FTL's data files in one direction: XML in `raw/gamedata/` → events → pages.
Mod authors write the same files in the other direction, and the conventions they follow
explain *why the vanilla data looks the way it does* — and define exactly what
`tools/extract-event.py` would have to learn before a modded event could be ingested at all.

Everything here is from [[source-modding-research]] (per
`raw/modding/2026-08-12-ftl-modding-research.md`), a synthesis of Slipstream's own reference
documentation, Subset Games' official mods page, and the Hyperspace README.

## How the game stores data

Content ships in packed archives — `ftl.dat` in older builds, `data.dat` + `resource.dat` in
1.6.x. Modders never touch the archive directly; **Slipstream Mod Manager** (by Vhati,
endorsed by Subset Games as *"the go-to method of using mods with FTL"*) unpacks and repacks
it.

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

## Advanced XML — the `mod:` namespace

Appending can only *add*. Slipstream's Advanced XML lets a mod **find and edit** existing tags,
which is how mods coexist rather than clobber.

| Find | Purpose |
|---|---|
| `<mod:findName type="…" name="…">` | match a tag by type and `name` |
| `<mod:findLike type="…">` + `<mod:selector>` | match by attributes / value |
| `<mod:findWithChildLike type="…" child-type="…">` | match a parent via one of its children |
| `<mod:findComposite>` + `<mod:par op="AND\|OR">` | combine criteria |

All find tags accept `reverse`, `start`, `limit` and `panic`. Inside a match:
`<mod:find>`, `<mod:setValue>`, `<mod:setAttributes>`, `<mod:removeAttributes>`,
`<mod:removeTag>`, `<mod-append:Element>`, `<mod-overwrite:Element>`.

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

## Related
- [[concept-event-tree-grammar]] — the grammar a mod author writes into
- [[concept-sector-event-allocation]] — step 3 of the chain, read forwards here
- [[concept-event-list-weighting]] — step 2, and the claim this source corroborates
- [[concept-blue-options]] — the `req=` vocabulary Hyperspace extends

## Open Questions
- [ ] Whether malformed mod XML fails loudly or silently in game — no source says.
- [ ] Slipstream's behaviour when two mods use Advanced XML against the same tag.
- [ ] Whether the `OVERRIDE_*` lists in the AE data are a modding hook or purely internal —
      relevant to [[concept-sector-event-allocation]]'s unreachable-content question.
- [ ] The `.dat` archive format itself — not needed while Slipstream abstracts it.

## Sources
- [[source-modding-research]] (per raw/modding/2026-08-12-ftl-modding-research.md)
