---
id: source-slipstream-readme-modders
type: source
source_kind: wiki
raw: raw/modding/slipstream-1.9.1-readme_modders.txt
game_version: both
date: 2018-01-07
ingested: 2026-08-13
reliability: high
tags: [modding, file-format, tooling, slipstream, primary-source]
---

# Slipstream Mod Manager — `readme_modders.txt` (v1.9.1)

## Summary
Vhati's own reference documentation for writing FTL mods, shipped inside the Slipstream Mod
Manager 1.9.1 distribution. It is the **primary source** behind
[[source-modding-research]], which had summarized it secondhand from a GitHub copy. It
specifies the `.ftl` archive layout, the `.xml.append` convention and its override rule, the
complete Advanced XML (`mod:`) tag set, the raw-append escape hatch, Slipstream's command-line
flags, and the encoding rules that govern what text FTL can display.

Obtained by installing Slipstream 1.9.1 from
[SourceForge](https://sourceforge.net/projects/slipstreammodmanager/) — **not** the GitHub
releases page, which has no releases — and copying the file out of the distribution.

## Key Takeaways

- **The override rule, verbatim:** *"Keep in mind that you can override vanilla events (among
  other things) to your pleasure by writing an event of the same name. Whenever multiple tags
  share the same name, only the last one counts."* This is the mechanism
  [[concept-modding-and-the-append-convention]] describes and the one the event-labels mod is
  built on. The Raw XML section states it a second time about the *game* rather than the
  patcher — *"FTL honors the last it sees"* — which matters, because those are two different
  claims and the wiki previously had only the first.
- **`.ftl` is a renamed `.zip`** whose root holds only `data/`, `audio/`, `fonts/`, `img/`,
  `mod-appendix/`. Ship only the files you modify.
- **`mod-appendix/metadata.xml` is documented as "Optional"** — but see Contradictions: if
  present it is parsed strictly, and a missing element rejects the entire mod.
- **`<FTL>` wrapper (1.6.1+):** Slipstream removes it, appends, and restores it. Mod files may
  include one or not; either way it is stripped. **Advanced XML tags are unaware of the
  wrapper.**
- **Line endings and encoding:** save as ASCII or UTF-8 (UTF-16 and Windows-1252 tolerated).
  LF is fine for XML — Slipstream converts everything to CR-LF while patching — but LF
  *crashes* the game in `layout.txt`. File and directory names must be plain ASCII.
- **What FTL can display:** *"FTL 1.01-1.5.13 assumes text to be windows-1252 … Since FTL
  1.6.1, it assumes UTF-8 (no worries). After the game has read the text, another issue is
  whether the fonts contain the glyphs to display the characters. You may need to replace the
  fonts."* So on 1.6.x, non-ASCII text is *read* correctly and the open question is glyph
  coverage, not encoding.

### Advanced XML — the full specification

The tag set [[source-modding-research]] could only list is fully specified here, including the
argument defaults that decide what a patch actually hits.

- Every `<mod:find…>` accepts `reverse`, `start`, `limit`, `panic` (default: forward, skip 0,
  unlimited, do not error on no match).
- **`<mod:findName type="abc" name="def">` — defaults are `reverse="true" start="0" limit="1"`,
  i.e. it finds the *last* matching tag, not the first.** `type` is optional. This is the one
  detail most likely to make a hand-written patch silently hit the wrong element.
- `<mod:findLike type="abc">` with `<mod:selector a="1">value</mod:selector>` — matches by
  attributes and value; the selector may be omitted entirely if neither is needed.
- `<mod:findWithChildLike type="abc" child-type="def">` — matches a parent by its children;
  the children are criteria, never results.
- `<mod:findComposite>` with `<mod:par op="AND|OR">` — set intersection or union over several
  finds. Commands inside the nested finds are ignored.
- Commands, valid inside a find: `<mod:find…>` (recurse into children), `<mod:setValue>`,
  `<mod:setAttributes/>`, `<mod:removeAttributes/>` (SMM 1.7+), `<mod:removeTag/>`,
  `<mod-append:XYZ>`, `<mod-overwrite:XYZ>` (replaces the first such child, else appends).
- **Ordering:** special tags and plain append content are processed in the order they occur in
  the mod, and *"when patching several mods at once, later mods edit in the wake of earlier
  ones."*
- Slipstream ships an **XML Sandbox** under its File menu for testing these interactively.

### Raw XML and the command line

- `X.xml.rawappend` appends without any parsing; `X.xml.rawclobber` replaces the file
  outright. Both are last-resort tools — any later mod must treat the same file as raw too.
- `--patch`, `--validate`, `--runftl`, `--global-panic`. Two are directly useful to this repo:
  **`--patch` and `--validate` accept directories as well as `.ftl` files**, so a generated mod
  tree can be tested without zipping it first, and `--global-panic` turns every `<find…>` that
  matches nothing into an error rather than a silent no-op.

### Pitfalls it records

- **FTL does not like event loops** — a choice loading an event whose choice loads the first
  crashes the game at the main menu or hangar. Relevant to any generated event content.
- Modded level-5 shields make asteroid storms abnormally fast (FTL bug, fixed in 1.03.3).
- Paired explore/battle music tracks play simultaneously and should match in duration.

## Events Covered
None. This source describes the toolchain and file format, not game content.

## Other Pages Touched
- [[concept-modding-and-the-append-convention]] — upgraded from a secondhand summary to a
  cited primary source, and corrected on one point (below)
- [[source-modding-research]] — this is the document it was summarizing; its account of the
  append convention and the `mod:` tag set holds up

## Reliability Notes
`high`, with a scope limit worth stating. This is the tool author's own reference
documentation, shipped in the distribution rather than transcribed, so for **Slipstream's
behaviour** it is first-party and authoritative — it outranks the community wiki and
[[source-modding-research]], which was summarizing it. It is *not* authority on FTL's internals
beyond what it asserts about patching, and its statements about the game (encoding eras, the
event-loop crash) are Vhati's observations, not datamined facts.

**Schema note:** `source_kind: wiki` is the closest existing value for a captured external
document, but `reliability: high` on a `wiki` source departs from the `CLAUDE.md` §2.7
convention that reads *high = game files, medium = community wiki*. First-party vendor
documentation has no value in that scale. Flagged rather than silently filed, exactly as
[[source-modding-research]] flagged `research` and `raw/modding/`.

## Contradictions Flagged

> ⚠️ **CONTRADICTION — `metadata.xml` optional vs. strictly required.** This document says
> `mod-appendix/metadata.xml` is an *"Optional embedded description."* Observed behaviour in
> Slipstream 1.9.1 is that the file is optional but, **once present, is parsed strictly**: a
> `metadata.xml` with an empty `<threadUrl/>` produced `strict parsing failed: Missing
> threadUrl.` in `modman-log.txt` and the mod did not appear in the list at all. Both are true
> — "optional" describes the file, not its contents. Trusting the observation, since it is a
> direct log from the shipped binary; recorded because "optional" reads as "lenient" and is
> the more natural misreading.

> ⚠️ **CONTRADICTION — which archive 1.6.x uses.** Not from this document, but surfaced while
> obtaining it. [[concept-modding-and-the-append-convention]] states *"`ftl.dat` in older
> builds, `data.dat` + `resource.dat` in 1.6.x"*, sourced from [[source-modding-research]]. The
> local FTL 1.6.x install has a **single `ftl.dat`** whose magic bytes are `PKG\n`, matching
> `tools/ftlpkg.py`'s docstring (*"Read-only extractor for FTL 1.6.x `PKG\n` archives
> (ftl.dat)"*). The eras are reversed on the concept page. Trusting the install and the
> extractor over the synthesis.

## Links
- [Slipstream Mod Manager on SourceForge](https://sourceforge.net/projects/slipstreammodmanager/)
  — where the binaries actually live
- [Slipstream Mod Manager on GitHub](https://github.com/Vhati/Slipstream-Mod-Manager) — source
  only; its releases page is empty
- [Slipstream forum thread](https://subsetgames.com/forum/viewtopic.php?f=12&t=17102)
- Raw file: `raw/modding/slipstream-1.9.1-readme_modders.txt`
