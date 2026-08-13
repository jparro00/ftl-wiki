# FTL modding — research notes

**Gathered:** 2026-08-12 · **By:** Claude, at the user's request · **Kind:** web research, synthesised
**Status:** external claims, cited below. Where a claim could be checked against this repo's own
`raw/gamedata/`, that check is recorded inline as **[verified locally]**.

This is not a source file dropped in by the user — it is a synthesis written into `raw/` by
explicit instruction. Treat the citations, not this document, as authority.

---

## 1. How FTL stores its data

The game ships its content in packed archives (`ftl.dat` in older builds; `data.dat` +
`resource.dat` in 1.6.x). Slipstream unpacks and repacks these; modders never touch the archive
directly.

**[verified locally]** `raw/gamedata/` in this repo is the *unpacked* contents of that archive —
the same `events*.xml`, `blueprints.xml`, `sector_data.xml`, `text_events.xml` a modder would
extract. No `.dat` is present, so unpacking happened before the files were dropped here.

**[verified locally]** Every data XML is wrapped in a single `<FTL>` root element. That matters for
modding (§4), and it is why this repo's extractor descends through the wrapper.

## 2. The `.ftl` mod format

An `.ftl` file **is a renamed `.zip`**. At its root it may contain only:

```
data/          audio/          fonts/          img/          mod-appendix/
```

Include *only* the files you modify — smaller archives, fewer conflicts.

`mod-appendix/` holds files that are **not** inserted into the game's resources; Slipstream reads
`metadata.xml` from it for the mod's embedded title and description.

## 3. Slipstream Mod Manager

The de-facto tool, by Vhati, and **officially endorsed by Subset Games** as "the go-to method of
using mods with FTL". Workflow:

1. Extract Slipstream anywhere; run `modman.exe`; point it at FTL's `.dat` when prompted.
2. Drop mods into its `mods/` folder.
3. Tick the mods you want, click **patch**. Untick and re-patch to revert to vanilla.
4. `Preferences` → `allow_zip` lets it accept `.zip` as well as `.ftl`.

Subset's own caveats: mods are unofficial and unsupported, and **"if two mods write over the same
files, they will never be able to work together successfully"** — which is the entire reason the
append convention exists.

## 4. The append convention — `.xml.append`

A file named `events.xml.append` is **appended** to the vanilla `events.xml` rather than replacing
it. This is the single most important practice: *do not edit the vanilla XML, ship an append.*

- Overriding vanilla content works by reusing an identical tag name — **"only the last one
  counts."**
- For *new* content, use unique names so two mods do not collide.
- FTL 1.6.1+ wraps files in `<FTL>` tags; **Slipstream strips the root before appending and
  restores it afterwards**, so an append file must not carry its own `<FTL>` wrapper.

## 5. Advanced XML — the `mod:` namespace

Plain appending can only add. Slipstream's Advanced XML lets a mod *find and edit* existing tags,
which is how mods coexist. All tags live in the `mod:` namespace.

**Find:**

| Tag | Purpose |
|---|---|
| `<mod:findName type="..." name="...">` | match a tag by type and `name` attribute |
| `<mod:findLike type="...">` with `<mod:selector a="1">value</mod:selector>` | match by attributes/value |
| `<mod:findWithChildLike type="..." child-type="...">` | match a parent via one of its children |
| `<mod:findComposite>` with `<mod:par op="AND / OR">` | combine several criteria |

All find tags accept `reverse`, `start`, `limit` and `panic` (error behaviour when nothing matches).

**Commands inside a find:**

| Tag | Effect |
|---|---|
| `<mod:find>` | search within the matched children |
| `<mod:setValue>text</mod:setValue>` | replace the element text |
| `<mod:setAttributes a="1" />` | set attributes |
| `<mod:removeAttributes a="" />` | drop attributes |
| `<mod:removeTag />` | delete the matched element |
| `<mod-append:Element>` | append a child |
| `<mod-overwrite:Element>` | replace a child |

## 6. Wiring a new event into the game

The chain is **event → eventList → sector allocation**, all of which this repo's data already
demonstrates:

1. **`events.xml`** (or any `events_*.xml`) — define `<event name="MY_EVENT">` with its `<text>`,
   `<choice>` children and effects.
2. **`eventList`** — group related events under `<eventList name="MY_LIST">`; the engine picks one
   member. **[verified locally]** No shipped list carries weights, so duplicating an entry is the
   only weighting mechanism available.
3. **`sector_data.xml`** — inside a `<sectorDescription>`, add
   `<event name="MY_LIST" min="1" max="2"/>` to allocate it to beacons in that sector. A custom
   sector needs `name`, `minSector`, a `startEvent`, and its own `<event>` allocations.
4. **`text_events.xml`** — prose is referenced by id (`<text id="event_MY_EVENT_text"/>`), so new
   strings go here. **[verified locally]** That indirection is why this repo resolves every quoted
   string through a string table rather than reading inline text.

**Testing trick from the tutorials:** comment out the vanilla `<sectorDescription>` entries so the
map generator can only offer your custom sector.

## 7. FTL Hyperspace — engine-level modding

A separate project that patches the executable to extend what mods can do, well beyond XML.

- **Platform:** Windows; Linux via WINE with `xinput1_4` and the Hyperspace DLL as library
  overrides.
- **Install:** extract next to `FTLGame.exe`, then install `Hyperspace.ftl` through Slipstream.
  **Uninstalling requires deleting `Hyperspace.dll`** — removing the mod in Slipstream is not
  enough.
- **Adds:** custom species with new abilities, custom systems, unlimited custom ships, custom
  augments, a much larger event vocabulary (including `req` checks against cargo), custom
  secret-sector warps, and a Lua API (1.2.0+).
- **Configured via** `data/hyperspace.xml`; mods ship a `hyperspace.xml.append`. That file inside
  `Hyperspace.ftl` is the practical reference documentation.
- **Caveats:** custom ships get **no achievements and no saved high scores**; Linux fullscreen is
  buggy (use windowed); redefining an existing crew ability means rewriting the original.

## 8. Tools

| Tool | Use |
|---|---|
| **Slipstream Mod Manager** (Vhati) | pack/unpack, install, patch, revert |
| **FTL Hyperspace** | engine extension; new systems, species, Lua |
| **Superluminal2** | visual ship/layout editor |
| Notepad++ or similar | XML editing |
| 7-Zip | inspect existing `.ftl` archives |
| GIMP | ship and weapon art |

Distribution and discussion centre on the **Subset Games forum** (Master Mod List, Slipstream
thread) — FTL has no Steam Workshop support.

## 9. What this means for this repo

- A mod shipping content for this project would be a `.zip` renamed `.ftl` containing
  `data/events.xml.append` and friends — never modified copies of the vanilla files.
- **If a mod were ever ingested as a source**, the extractor would need two things it does not have:
  `.xml.append` handling (concatenate onto the vanilla tree, last definition wins) and the `mod:`
  namespace (which *edits* existing definitions, so the effective event tree becomes vanilla plus a
  patch script). Today it assumes one flat definition per name, with DLC-file load order as the only
  override mechanism.
- The `<FTL>` wrapper handling and the load-order override rule the extractor already implements are
  the same mechanics Slipstream operates on — mild corroboration that both readings of the format
  are right.

## 10. Not established by this research

- Whether malformed mod XML fails loudly or silently in game — no source says, and the one tutorial
  that should have covered it does not.
- Slipstream's behaviour when two mods use Advanced XML against the same tag.
- Whether the `OVERRIDE_*` lists in the AE data are a modding hook or purely internal.
- The `.dat` format itself (not needed — Slipstream abstracts it).

## Sources

- [Subset Games — official mods page](https://subsetgames.com/ftl_mods.html) — Slipstream
  endorsement, conflict warning, forum as the hub
- [Slipstream Mod Manager — readme_modders.txt](https://github.com/Vhati/Slipstream-Mod-Manager/blob/master/skel_common/readme_modders.txt)
  — `.ftl` layout, append rules, full `mod:` tag reference
- [Slipstream Mod Manager — repository](https://github.com/Vhati/Slipstream-Mod-Manager)
- [FTL Hyperspace — MOD README](https://github.com/FTL-Hyperspace/FTL-Hyperspace/blob/master/MOD%20README.txt)
  — install, features, caveats
- [FTL Hyperspace — home page](https://ftl-hyperspace.github.io/FTL-Hyperspace/)
- [Steam guide — Making Mods for FTL](https://steamcommunity.com/sharedfiles/filedetails/?id=277959176)
  — beginner workflow; "use the vanilla XML as reference, never edit it"
- [CaptainShooby FTL modding tutorial](https://docs.google.com/document/d/18DgjbF054eNRNNRwg_cuDT2DatdRpnW16mzX32GB-Dw/pub)
  — custom event and custom sector wiring, sector-forcing test trick
- [Subset Games forum — modding reference links](https://www.subsetgames.com/forum/viewtopic.php?t=17135)
- [FTL Wiki — mods and tools](https://ftl.fandom.com/wiki/Mods_and_tools) *(not retrievable at time
  of research — HTTP 402; listed for completeness)*
