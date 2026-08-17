# Event labels mod — specification

Normative spec for the `event-labels` mod pipeline. Self-contained: an agent with no prior
context can rebuild, verify and extend the mod from this document alone.

The mod prints each event's **card title** above its in-game text, so the player can name the
encounter they are looking at. It changes text and nothing else — no choices, effects, odds,
ships or rewards are touched.

```
cards/trees/*.tree.json ──► mods/event-labels/src/ ──► event-labels.ftl ──► Slipstream
   (title = the label)      build-mod.py              --pack
```

---

## 1. Quick start

```bash
python tools/build-mod.py            # generate mods/event-labels/src/
python tools/build-mod.py --pack     # ... and zip it to mods/event-labels/event-labels.ftl
python tools/build-mod.py --verify   # re-check a generated tree without rebuilding
```

The build runs the full verification suite (§5) every time and exits non-zero on any failure.
There is no way to produce an unverified tree short of editing it by hand afterwards.

---

## 2. Where the label comes from

`cards/trees/<slug>.tree.json` → the root `title` field, which the card pipeline derives from
the H1 of `wiki/events/<slug>.md` (`tools/EVENT-CARD.md` §4.7). **The wiki is the label
source.** Retitle a wiki page, rebuild the card, rebuild the mod, and the in-game label
follows. Every tree also supplies `id` (the `<event name>`) and `source` (the file holding the
winning definition), which is all the generator needs to find the definition.

Coverage is therefore exactly the carded set — **386 of the 449 top-level event definitions**.
An event with no wiki page has no title, so it gets no label. This is the intended failure
mode: the mod never invents a name.

Titles are ASCII-folded (`—` → `-`, curly quotes → straight) because FTL's bitmap fonts have
no glyphs for typographic punctuation. Verification fails on any non-ASCII byte that survives.

---

## 3. Label format

```
[ Ancient device ]

An ancient device is orbiting within the crystal rings of a nearby gas giant. …
```

`LABEL_OPEN` / `LABEL_CLOSE` / `LABEL_GAP` in `build-mod.py` are the only place this is
defined. The verifier matches on the same constants, so changing them stays consistent.

---

## 4. The two mechanisms

Both rest only on the plain append convention. Slipstream's own `readme_modders.txt` states
the rule this mod is built on, verbatim:

> Keep in mind that you can override vanilla events (among other things) to your pleasure by
> writing an event of the same name. **Whenever multiple tags share the same name, only the
> last one counts.** When you're not overriding something, try to use unique names, so that it
> won't clobber another mod and vice versa.

That file ships inside the Slipstream download and is the primary source for everything here;
`raw/modding/2026-08-12-ftl-modding-research.md` had summarized it secondhand.

Neither mechanism uses Advanced XML (`mod:findName` and friends), which would be tidier —
one `mod:findLike` per event could edit the vanilla `<text>` in place instead of redefining
35 events, and would conflict with almost nothing. `readme_modders.txt` §"Advanced XML"
documents the full tag set and its nesting, and Slipstream ships an **XML Sandbox** under its
File menu for testing such patches interactively. **That is the upgrade path**, and the
reason it was not taken is now only that the append version was already built and verified.

The generator picks the *least invasive* mechanism that can carry a per-event label:

### 4.1 STRING — 351 events, no structure touched

Used when the event's own `<text>` resolves to a `<text name=…>` string that **exactly one**
event can reach. Relabelling the string then relabels exactly that event, so the mod emits
only a replacement string into `text_events.xml.append` and never mentions the event at all.

Two shapes qualify:

- `<text id="event_X_text"/>` where the id is referenced once game-wide. All 261 such events
  qualify — measured, not assumed.
- `<text load="LIST"/>` where the list is loaded by one event *and* every `<text id=…/>`
  variant inside it is referenced once. 90 of 118 list-backed events qualify; each variant
  gets its own labelled replacement, so the game's random pick still varies.

This path cannot break an event's structure, and it coexists with mods that change choices or
effects. Prefer it. 701 strings are emitted for 351 events — most of them list variants.

### 4.2 EVENT — 35 events, definition re-emitted

Used when no string is private to the event: the string or list is shared with another event,
or the prose is inlined in the event definition (7 events do this, e.g. `LONE_SHUTTLE`).

The event's **verbatim source bytes** are copied out of the vanilla file and re-emitted with
only its own `<text>` element rewritten. Nothing is re-serialized from a parse tree, so
comments (including the `<!--DLC-->` markers), attribute order and whitespace survive intact.

- A shared `<textList>` becomes a **new** list named `EVLBL_<EVENT_ID>` holding inline
  labelled copies of the variants. The vanilla list is never redefined, so the other events
  loading it keep their own labels.
- A shared or inline string becomes an inline `<text>` on the event.

Each redefinition is appended to **the file its winning definition lives in**, so the copy
lands after the original within the same file and the file's place in load order is unchanged.

### 4.3 Why the event's *own* text, not the first one found

An event's `<text>` is its depth-1 child. The `<text>` elements inside its `<choice>` children
are option labels — relabelling one of those would put the event name on a button. The
generator and the verifier both select on depth, never on document order.

Likewise, `<event name="X"/>` **inside an `<eventList>` is a reference, not a definition**.
Definitions are the ones at the files' root depth (inside the `<FTL>` wrapper where present).
Counting references as definitions is what makes `NOTHING` and `STORE` look like they are
defined five times.

---

## 5. Verification

Every build runs all of it; `--verify` runs it against an existing tree.

| Check | Catches |
|---|---|
| Each `.append` parses as XML under a synthetic root | malformed emission |
| No `.append` carries its own `<FTL>` wrapper | Slipstream strips and restores the root itself |
| Each `.append` targets a file present in `raw/gamedata/` | a typo'd filename, which appends to nothing |
| Every one of the 386 titles appears | a silently dropped event |
| No byte above 0x7E | a glyph FTL cannot render |
| No string carries two labels | a double-prefixed rebuild |
| Every emitted `name=` is either a vanilla name or `EVLBL_`-prefixed | an accidental new definition, or a typo'd override that silently does nothing |
| **Every redefined event matches vanilla byte-for-byte outside its `<text>`** | the dangerous one — a copy that loses a `<choice>` still parses and still shows its label, and would surface only as a missing option mid-run |
| `mod-appendix/metadata.xml` has all five elements, none empty | Slipstream's `JDOMModMetadataReader` parses it **strictly** and rejects the whole mod on the first missing value. An empty `<threadUrl/>` — which a locally built mod has no real value for — earns `Missing threadUrl.` in `modman-log.txt`, and the mod simply never appears in the list. This cost a build/patch cycle to find; the check exists so it cannot recur |

The last check is worth a negative test after any change to the slicer: delete a `<choice>`
from a generated append, run `--verify`, and confirm it fails.

---

## 6. Invariants

- **L1 — The label is the card title, verbatim.** No re-wording, no ids, no annotations.
- **L2 — Text only.** No choice, effect, reward, ship, odds or list membership is altered.
  A tree diff of vanilla vs. modded events must show changes under `text` and nowhere else.
- **L3 — Nothing hand-written per event.** Format changes go in the constants; mechanism
  changes go in `build()`. Never edit a generated `.append`.
- **L4 — New names are namespaced.** Anything this mod introduces starts `EVLBL_`, so it can
  never collide with vanilla or another mod. Only deliberate overrides reuse a vanilla name.
- **L5 — Deterministic.** Same trees + same gamedata → byte-identical output.

---

## 7. Known limits

- **63 top-level events carry no label**, having no wiki page and therefore no title. Most are
  things a player never meets as a beacon encounter — developer tests (`ASTEROID_TEST`,
  `BIG_NAME_TEST`) and mid-event continuations loaded from a choice (`BOARDERS_HACKING_2`).
  Give one a wiki page and a card, and the next build picks it up with no code change.
- **Conflicts with mods that redefine the same 35 events** — whichever loads last wins
  outright. The 351 string-override events conflict only with mods that rewrite the same
  prose.
- **English only.** Labelled strings are emitted into `text_events.xml.append`; a localized
  install reading a different string table would not see them.
- ~~Not yet patched into the game.~~ **Confirmed live 2026-08-15.** A `continue.sav` written by
  the running game carried the encounter text `"[ Start game ]\r\n\r\nThe data you carry is
  vital to the remaining Federation fleet. …"` — the label, the `LABEL_GAP` blank line and the
  vanilla prose, in the format §3 specifies. The labels render. (Read out of the save by
  `tools/ftlsave.py`, which reads what the game itself is displaying.)

Verified against the install this was written on — Slipstream 1.9.1 on Java 8 at
`C:\Users\jparr\Documents\Slipstream`, pointed at
`D:\Steam\steamapps\common\FTL Faster Than Light`. Those paths are a record of that
check, not a configuration: the build tools read `$SLIPSTREAM_DIR` and `$FTL_DIR`
(`SETUP.md` §6). All 14 vanilla files this mod
appends to were confirmed byte-identical to that install's `ftl.dat` contents, so the 35
copied event definitions match the installed vanilla exactly.
