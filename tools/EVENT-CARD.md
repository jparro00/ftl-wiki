# Event cards — specification

Normative spec for the FTL event-card pipeline. It is self-contained: an agent with no prior
context can build, verify, publish, and extend cards from this document alone.

An **event card** is a single-page, self-contained HTML decision tree for one FTL event,
read in a couple of seconds while the game is paused.

Cards are **generated**. Nothing about a specific event is ever typed into HTML.
`CLAUDE.md` §5.2b is the trigger (a screenshot means build one); this file is how.

---

## 1. Quick start

```bash
python tools/extract-event.py AUTO_DEFENSE_ITEM
python tools/build-card.py cards/trees/auto-ship-near-storage-station.tree.json
node  tools/smoke-card.js cards/card-auto-ship-near-storage-station.html
```

`--all` rebuilds every card; `--runtime` rebuilds only the shared runtime files (§7.3).

Then publish the built file with the Artifact tool (§9).

The **event id is the only input**. Find it by matching on-screen text against
`raw/gamedata/text_events.xml`, or read `event_name:` off the relevant
`wiki/events/<slug>.md`. Output lands at `cards/trees/<slug>.tree.json`, where the slug comes
from the join in §4.7 — it is often *not* the lowercased event id, so use the path the
extractor prints rather than assuming one.

---

## 2. Components

| Path | Role | Hand-written? |
|---|---|---|
| `tools/extract-event.py` | game XML → `ftl-event-tree/1` JSON | code only |
| `tools/build-card.py` | inlines runtime + tree + vocabulary into the shell; emits the payload and the shared runtime | code only |
| `tools/card-runtime.js` | **the renderer**, and the only copy of it | code only |
| `tools/event-card-render.html` | layout, colour, and the page a card is | design only — **no English** |
| `tools/card-vocab.json` | every word and punctuation mark that isn't game text | yes, shared by all cards |
| `tools/smoke-card.js` | runs the renderer under a DOM shim, for testing | code only |
| `cards/trees/<slug>.tree.json` | generated tree (regenerable data, not a page) | never |
| `cards/card-<slug>.html` | the built card; publish target | never |
| `cards/data/<slug>.js` | the same tree as one `FTLCard.define()` call (§7.3) | never |
| `cards/runtime/card.js` `card.css` | renderer + vocabulary, and the CSS, for pages that embed cards (§7.3) | never |

Inputs consumed, all under `raw/gamedata/` except the last:

- `events*.xml`, `newEvents.xml`, `dlcEvents*.xml`, `nameEvents.xml`, `bosses.xml` — events,
  event lists, ships
- `text_events.xml` — every quoted string
- `blueprints.xml`, `dlcBlueprints.xml`, `dlcPirateBlueprints.xml`, `autoBlueprints.xml` —
  blueprint titles, ship classes, `crewCount`
- `text_blueprints.xml` — display names for those blueprints
- `wiki/events/*.md` — the `event_name:` → (slug, title) join (§4.7)

`raw/wiki/` (the Fandom mirror) is **not** an input. Cards use game data only.

---

## 3. Invariants

These hold for every card. Breaking one is a bug, not a preference.

- **I1 — Quoted text is verbatim.** Every string in a tree comes from `text_events.xml` via
  its `ref`. Nothing is paraphrased, shortened, or improved.
- **I2 — No invented odds.** A chip appears only where the data states a number. Event lists
  carry no weights in the shipped files, so their entries get no percentages.
- **I3 — No recommendations, no meta.** State what each option does, never which to pick. No
  event ids, citations, wikilinks, or version notes — on the card or in the chat reply.
- **I4 — No hand-edited HTML.** See §8 for where each class of fix belongs.
- **I5 — Deterministic.** Same inputs → byte-identical output (§7.2).
- **I6 — Nothing unreachable is shown.** If the data proves a branch cannot happen, it stays
  in the JSON, marked, and off the card (R13).

---

## 4. Stage 1 — extraction

`extract-event.py` resolves one event id into a tree. The rules it implements:

### 4.1 Parsing

The event files are XML with quirks. The parser strips the `<?xml?>` declaration, escapes
bare `&`, wraps the body in a synthetic root, keeps comments (they carry meaning), and
descends through the files' own `<FTL>` wrapper. Definitions are indexed in the game's load
order, so DLC overwrites win.

### 4.2 The node grammar

An `<event>` carries presentation (`<text>`, `<img>`), effects (§4.3), and a continuation:

| Continuation | Becomes |
|---|---|
| `<choice>` children | `decision` node |
| membership in an `<eventList>` | `chance` node |
| `<ship load=…>` | `combat` node |
| nothing | terminal |

**These are not exclusive.** An event may have a ship *and* a menu; the ship attaches to the
decision as `combat`. Reading `<ship>` as *the* continuation silently drops the whole menu.

Two more continuations, both of which silently dropped whole subtrees until fixed:

- **`<event load="X"/>` as an eventList entry** — a list entry may delegate wholesale. Only
  choices used to be followed, so such entries became empty records rendering as a blank
  "nothing happens" row (half of `GHOST_SHIP`'s salvage outcomes).
- **A bare `<event>` child** — `<event><text/><event load="GHOST_SPACE"/>…</event>` means
  "then this happens". Emitted as a `sequence` node: one unlabelled option, rendered under
  the "Then" heading, never numbered.

`load=` is a subroutine call and may cross files. A revisited name becomes `{"kind":"ref"}`
(recursion guard, plus a depth backstop).

### 4.2b Dispatch pools are pointed at, not inlined

An `eventList` collapses to one pointer row per entry — `{"kind":"ref", "target", "card"}`,
labelled with the target's title, and the list marked `"dispatch": true` — when **every**
entry is a bare `<event load="X"/>` whose target is a top-level event with a `wiki/events/`
page. Such a list does nothing but pick one complete event to run, and the watcher shows that
event's own card a moment later (FTL rewrites the save when a `hidden` choice chains), so the
pool card only has to say what *can* follow. Inlining them instead put 30 whole events on
`FINISH_BEACON`: 529 text nodes, 2.7× the next largest card.

**All or nothing.** A list mixing `load=` entries with anonymous `<event>` bodies is an outcome
table, not a dispatcher — its loads are outcomes of *this* event. Collapsing per-entry gutted
the eight refugee cards, whose list is four `REFUGEE_TRADER` loads plus four inline ambushes.
Single-entry lists are excluded; R10 already collapses those into the row above.

### 4.3 Effects

A closed set. Source tag → emitted `kind`:

| XML | kind |
|---|---|
| `autoReward level=…>tier` | `reward` (a `level` × `tier` matrix, not a number) |
| `item_modify > item` | `resource` — signed; negative is a cost |
| `crewMember` | `crew_gain` — **signed**: `amount="-1"` takes a crew member away and renders as `crew_lost`. Carries `class`, `all_skills`, and per-skill points (`repair="1"`) |
| `removeCrew` | `crew_loss` — `clone` is the child's **value**, not its presence: `<clone>false</clone>` exists (11 uses) and means the game refuses a revive |
| `damage` | `system_damage` if `system=`; `hull_repair` if negative; else `hull_damage`. An `effect=` attribute (`fire`, `breach`, `random`, `all`) emits a second `hazard` record — it is a payload, not a modifier |
| `store` | `store` — a store opening is a payload the player came for, not just a flag |
| `environment` | `environment` — also recorded in `flags`; emitted as an effect so a row can say the fight happens inside a hazard |
| `boarders` | `boarders` (`class`, `min`/`max`) |
| `augment` / `weapon` / `drone` | `item` (`item_kind`) |
| `upgrade`, `status`, `quest`, `unlockShip`, `modifyPursuit`, `reveal_map`, `repair`, `remove`, `secretSector` | `upgrade`, `status`, `quest`, `unlock_ship`, `fleet_delay`, `reveal_map`, `repair_all`, `remove_augment`, `secret_sector` |
| `<ship hostile=…/>` **with no `load`/`name`** | `ship_hostility` — flips the ship already at the beacon; it does **not** introduce one |

A `<choice>` may carry effects directly, rather than on its inner `<event>`; those merge into
the child's payload. Effects are also read on `<event load="X"/>` delegation (below).

A `<!--DLC-->` comment marks the adjacent element AE-only (`dlc: true`). It appears in **two
placements** and both must be read: as the element's *following sibling* (24 uses) and as its
*first child* (11 uses, e.g. `<choice req="LIFE_SCANNER"><!--DLC-->`). A gated row carrying
the marker renders the `dlc_mark` suffix on its label.

### 4.4 Combat

`<ship>` resolves against `events_ships.xml`. Branches are `destroyed`, `deadCrew`,
`surrender`, `escape`, `gotaway`, each carrying `chance`/`min`/`max` where present.

- **Ship name** — `auto_blueprint` → `shipBlueprint` → `<class>` gives the name the player
  sees (`ship_label`). A `blueprintList` of 2–3 distinct classes gives `ship_labels` (all of
  them). More than three: omitted; falls back to vocabulary or raw id.
- **Developer placeholders** — a branch whose entire text is a known placeholder
  (`"Should not be seen"`, on `GHOST_SHIP`'s `deadCrew`) is marked unreachable. The
  crewCount rule below cannot catch it: that hull declares 7 crew.
- **Crewless hulls** — if every hull the ship can draw declares
  `<crewCount amount="0" max="0"/>`, `deadCrew` is marked `"reachable": false` with a reason.
  An unknown blueprint counts as crewed; absence of data is not evidence.

### 4.5 Attached-ship reachability

A ship attached to a decision is marked `"reachable": false` unless it arrives
`hostile="true"` **or** something in the tree flips it with a bare `<ship hostile="true"/>`.
A derelict no option can activate is not a fight the player can pick.

### 4.6 Quest chains

`<quest event="X"/>` does not resolve at this beacon — it marks a destination reached later.
Targets are collected breadth-first into a top-level `chain[]`, transitively
(`ROCK_UNLOCK1` → `ROCK_UNLOCK2` → `ROCK_UNLOCK3`), across events *and* event lists, with a
visited set, since several paths can plant the same marker. An already-seen marker is emitted
as `{"id":…, "from":…, "repeat": true}` rather than re-expanded.

### 4.6b Text resolution

`<text id=…/>` resolves against `text_events.xml` **and** `text_misc.xml` (shared strings
like `continue`). A `<textList>` entry may itself be a `<text id=…/>` ref rather than inline
prose — reading only the inline body left `GHOST_SHIP` and `FRIENDLY_BEACON` with an empty
hail. Only the first variant is used.

### 4.7 Title and slug

The game files hold no human title — FTL never shows the player an event name. Both come from
a join: every `wiki/events/*.md` declares `event_name:` in frontmatter and has an H1 of the
form ``<Title> — `ID` ``. The filename is the slug; the H1 minus the trailing backticked id is
the title (titles may contain their own em dash, so only the trailing id is stripped). Chain
stages get their titles the same way. `--slug` / `--title` override; an unpaged event falls
back to its id, lowercased and hyphenated.

---

## 5. `ftl-event-tree/1`

An **event record**: `text` (`{value, ref}`), `effects[]`, optional `flags`
(`unique`, `beacon`, `store`, `environment`), an optional continuation `node`, and — at the
root only — `chain[]`.

| Node `kind` | Fields |
|---|---|
| `decision` | `options[]`; optional `combat` (a ship also at the beacon) |
| `chance` | `list`, `odds_basis` (`unweighted` \| `file-weight`), `options[]`; `dispatch` when §4.2b applies |
| `combat` | `ship`, `hostile`, `auto_blueprint`, `ship_label`/`ship_labels`, `branches[]` |
| `sequence` | `options[]` — exactly one, unlabelled: a bare `<event>` continuation ("then this") |
| `ref` | `target` — a definition deliberately not re-expanded; `card` when it is a dispatch (§4.2b) rather than the recursion guard |
| *absent* | terminal |

An **option**: `label`, `label_ref`, `gate` (`req`, `label`, `lvl`, `max_lvl`, `max_group`,
`blue`), `hidden`, `share`, `child` (an event record).

A **branch**: `on`, `chance`, `child`, plus `reachable` / `unreachable_because` when proven
impossible.

Every resolved definition carries `source`; the root also carries `schema`, `id`, `slug`,
`title`, `extracted_from`.

---

## 6. Vocabulary — `card-vocab.json`

The renderer holds no wording. Every key is a lookup it performs.

| Key | Controls |
|---|---|
| `levels`, `tiers`, `tier_tones` | `autoReward` phrasing — `LOW`→"low" into `standard`→"{level} scrap" — and its tone. `tiers` **must cover every tier the data uses** (`standard`, `scrap_only`, `stuff`, `weapon`, `fuel`, `drone`, `fuel_only`, `augment`, `missiles`, `droneparts`, `scrap`); an unmapped tier renders its raw name rather than falling back to scrap |
| `statuses` | `divide`/`limit`/`clear`/`loss` templates, kept literal (`shields divided by 2`) rather than interpreted |
| `random_items`, `ship_lists` | the `RANDOM` blueprint sentinel per item kind; a ship family name (`SHIPS_PIRATE` → "pirate ship") for lists too broad to name |
| `species`, `skills`, `skill_suffix` | internal ids → names (`energy` → Zoltan), and crew skill points |
| `effects.crew_gain` / `effects.crew_lost` | sign again — `crewMember amount="-1"` is a loss |
| `effects.resource` / `effects.resource_spend` | sign again — a resource is a gain or a spend; one flat entry coloured a free fuel pickup as a cost |
| `hazards`, `environments`, `systems` | `fire`/`breach`; `asteroid`/`nebula`/`sun`/`storm`/`pulsar`/`PDS`; `random`/`room` → "a random" |
| `effects.fleet_delay` / `effects.fleet_advance`, `jumps` | `modifyPursuit` reads in both directions — **negative delays the fleet (good), positive advances it (bad)**, per [[concept-rebel-fleet-advance]]. The renderer picks the entry by sign; a single flat entry silently claimed "delayed" for both |
| `effects` | one `{text, tone, if}` per effect kind; `{placeholders}` come from the effect's own fields |
| `resource_labels` | singular/plural pairs for `item_modify` resources |
| `spend_prefix` | sign on a negative resource |
| `nothing`, `dlc_mark`, `merge_chip` | "nothing happens", the AE marker, the `×n` chip |
| `leads.ref` vs `leads.card_ref` | two different refusals to expand — the recursion guard ("the same table again") and a dispatch to a whole event of its own (§4.2b). The renderer picks by whether the `ref` carries a `card` |
| `leads` | what a row says when it has no effects of its own (`combat`, `chance`, `decision`, `ref`) |
| `block_labels` | headings above a nested block |
| `branches` | `destroyed` → "You destroy it", etc. |
| `gate_labels` | overrides for systems and species; blueprint gates resolve their own title. **Also read by `extract-sector.py`** — a sector page's blue-option list uses the same names, and merges two `req`s that share one, so an edit here changes both pipelines (SECTOR-PAGE.md §4.3) |
| `ship_labels` | overrides where a blueprint list is too broad to name |
| `attached_combat.hostile` | the row for a ship that arrives hostile |
| `chain_step`, `chain_heading`, `chain_loop` | quest-stage headings |
| `format` | punctuation and number formats: `arrow`, `effect_join`, `range_join`, `percent`, `gate_open`/`gate_close`, `gate_level_join`, `number_suffix`, `quote_open`/`quote_close`, `or_join`, `caret` |
| `display.eyebrow`, `display.notes` | the header eyebrow and the derived footnote clauses |

Unknown kinds, gates, tiers, hazards and environments fall through to the raw value
**deliberately** — a visible `BOMB_FIRE` says "add a vocabulary entry", where a blank would
hide the gap. A fallback that produces *plausible but wrong* text is the one thing this must
never do. **Four** have now been caught, all the same shape — a signed or typed value read
as if it had one sense: `tiers` once fell back to the `standard` template, so a
missile reward silently read "medium scrap"; and `fleet_delay` had one flat entry, so a
`modifyPursuit amount="1"` — the fleet closing in — rendered as "rebel fleet delayed" in
green; and `crewMember amount="-1"` — a crew member walking off with your ship — rendered
as **"+-1 traitor crew" in green**. **Where a value's sign or type changes the meaning, the
vocabulary needs one entry per sense.** Check this first when adding any effect kind.

---

## 7. Stage 2 — rendering

`build-card.py` inlines the renderer (`tools/card-runtime.js`), the tree and the vocabulary
into `event-card-render.html` and stamps the title. **Inlining is required**: a published
artifact runs under a CSP that blocks all network requests, and `file://` blocks cross-origin
reads, so fetching a sibling JSON fails in both places. Both documents are still parsed as
JSON, so data never becomes code.

The renderer lives in its own file because a card is no longer the only thing that renders
one — see §7.3. The card page is three lines of bootstrap on top of it.

### 7.1 Rendering rules

- **R1** A row with children expands; a row without states its outcome inline.
- **R2** Row label = the option's `label`, else its child's `text.value`.
- **R3** Row body = its effects, else the `leads` phrase for its child node, else `nothing`.
- **R4** Indentation is depth-driven (`--d`); trees may nest arbitrarily deep.
- **R5** Tone is per payload, not per row — one row can be amber and green at once.
- **R6** Chips mean exactly one thing: **this branch is one of several possible outcomes** —
  a `share`, a ship's `chance`, or `×n` for merged duplicates. A `chance="0"` branch prints
  no chip: the files comment those as specially triggered, so the branch stays but "0%"
  would contradict what a chip means. A certain outcome gets no
  chip, gated or not.
- **R7** Root options of a `decision` are numbered `1.` `2.` to match the in-game menu; gated
  rows are unnumbered, since the player only sees the ones they qualify for.
- **R8** A gated row is blue in full — requirement and text. The requirement the game text
  already carries as a leading parenthetical is stripped and re-rendered, resolved
  `gate_labels` → blueprint title → raw `req`.
- **R9** Identical sibling entries merge into one row carrying `×n`.
- **R10** A chance node whose entries all merge to a single row is **certain**; it collapses
  into the row above rather than printing a heading over one line.
- **R11** A row that flips the beacon's ship hostile renders that fight as its children (the
  ship is passed down the tree as "ambient"). Reached from several rows, it renders under
  each.
- **R12** A ship that arrives hostile belongs to no choice and keeps a row of its own, worded
  from `attached_combat.hostile`.
- **R13** Branches and attached ships marked `"reachable": false` are omitted.
- **R14** Quest stages render as their own cards below the main tree — they happen at another
  beacon, later, so nesting them would misrepresent them.
- **R15** The footnote is assembled from flags — `unique`, the beacon's `environment`, chain
  present, any unweighted list, any gate. Each clause appears once per card, never per row.
- **R16** The root record's own `effects[]` — boarders already aboard, a fleet move, damage
  on arrival — belong to no choice and render once under the header, as the arrival line.
  `environment` is excluded there because R15 already states it in the footnote.
- **R17** The fight heading names the ship (`The fight — {ship}`). A row's own effects
  displace the `leads.combat` phrase, so without this the ship is never named on any route
  that flips hostility.

### 7.3 The same renderer, embedded elsewhere

A sector page shows a card inside itself rather than sending the reader away
(`tools/SECTOR-PAGE.md` §6.1). It uses the same renderer on the same data, so there is one
of each — a second implementation would drift within a week.

`build-card.py` emits three things for that:

```
cards/runtime/card.js     tools/card-runtime.js + `FTLCard.vocab = {…}`   (~30 KB, once)
cards/runtime/card.css    the card CSS, page chrome stripped, :root → :host (~7 KB, once)
cards/data/<slug>.js      FTLCard.define("<slug>", {…the tree…})           (~8 KB each)
```

Three constraints shaped this, and each one is load-bearing:

- **`FTLCard.render(root, data, vocab)` must be reentrant.** It builds its own skeleton and
  keeps no module-level state, because a sector page renders many cards into one document and
  a shadow root has no markup to find. Nothing may be looked up by document id.
- **The payload is a `.js` file, not the `.json` tree, because of `file://`.** A local page
  cannot `fetch`, `XHR` or `import()` a sibling file — all three are blocked in Chrome and in
  Firefox with stock prefs — but a classic `<script src>` loads fine. So the tree ships again
  as one `define()` call. That is the only reason for the duplication.
- **The CSS is transformed, not copied.** Everything between the `PAGE-ONLY-START` and
  `PAGE-ONLY-END` markers in `event-card-render.html` is the standalone page's own chrome
  (background, page padding, the centred column) and is stripped; `:root` becomes `:host`
  because `:root` cannot match inside a shadow root. Keep new page-level rules inside those
  markers or an embedded card will repaint the page around it.

The runtime pair is rebuilt on **every** `build-card.py` run, including `--runtime` on its
own, so it cannot drift from what the cards inline.

### 7.2 Verification

```bash
node tools/smoke-card.js cards/card-<slug>.html   # required before publishing
```

Runs the card's real renderer against a DOM shim and prints the tree as indented text. It
catches renderer exceptions, blank rows, vocabulary gaps falling through to raw ids, and
mis-nested chain stages. It prints the **whole** card — title, eyebrow, hail, arrival line,
footnote, tree and chain. Anything the card can show must appear in this dump, or a defect
there is invisible: root effects were dropped for weeks because the dump omitted them. It
does **not** check CSS, layout, colour, or theming.

Determinism check — extract twice and diff:

```bash
python tools/extract-event.py <ID> -o /tmp/a.json
python tools/extract-event.py <ID> -o /tmp/b.json
diff /tmp/a.json /tmp/b.json
```

---

## 8. Where fixes go

| Symptom | Fix in | Never in |
|---|---|---|
| Wording reads wrong | `card-vocab.json` | the card HTML |
| Punctuation or number format | `card-vocab.json` → `format` | the renderer |
| A branch is missing or misplaced | `extract-event.py`, then re-extract | the tree JSON by hand |
| Layout, colour | `event-card-render.html` (changes every card **and** every embedded card) | one card |
| Interaction, row building | `tools/card-runtime.js` (same reach) | a built card |
| Title is wrong | the wiki page's H1 | `--title` as a habit |

After any renderer or vocabulary change, rebuild **every** existing tree and smoke-test them.
These files are shared; a local fix is a global change.

---

## 9. Publishing

**Built cards live in `cards/card-<slug>.html`.** This is the official location and
`build-card.py`'s default, so `-o` is only for throwaway builds; a card written anywhere
else is a mistake. The rules behind it:

- One file per event, named from the slug, so the path is derivable from the event id in any
  future session — which is what keeps a published URL stable across rebuilds (§9).
Generated **trees** live alongside them in `cards/trees/<slug>.tree.json` —
`extract-event.py`'s default, for the same reason. Nothing generated belongs under `wiki/`.

- **A sibling of `wiki/`, never inside it.** Two reasons, and the second is the important
  one: a built card is a generated artifact rather than a page, and — critically — every
  card inlines the whole event tree plus the vocabulary as text, so a card sitting under
  `wiki/` would pollute every grep, index scan and query of the wiki layer with thousands of
  lines of generated HTML. `wiki/` holds the tree JSON (data) and the event page (prose);
  `cards/` holds output. `build-card.py` writes to `ROOT/cards/`, not beside the tree.
- Never edited by hand (I4) and safe to delete: `python tools/build-card.py <tree>` puts it
  back byte-identically.

**Publish only what the user asked to see.** Publishing is gated by its own consent prompt —
independent of `.claude/settings.json` and of `bypassPermissions`, because it mints a hosted
URL — so every publish costs the user a tap they cannot pre-approve. Building and verifying
cost nothing. Therefore:

- **Screenshot / "make me a card for X"** → build, verify, publish, hand over the URL.
- **Bulk or test runs ("do these ten")** → build and verify only. Report the file paths and
  findings; publish on request. Never publish a card nobody asked to read.

Publish with the Artifact tool. Republishing the **same file path** keeps the same URL; a new
path mints a new one, so keep a card's output filename stable even if its slug changes. Give
a one-line description and a favicon, and keep the favicon stable across republishes of the
same card. A raw HTML file sent with SendUserFile does not
render — the card is a fragment the publisher wraps.

---

## 10. Pitfalls

Each of these has bitten. They are guarded now; do not reintroduce them.

- **Test-harness class matching.** `smoke-card.js` must match the *first* class name. An
  exact `className === "row"` check silently hid every gated row once a modifier class was
  added — the cards were correct, the harness was blind.
- **`<title>` substitution** must be line-anchored, or a `<title>` mentioned inside the
  shell's HTML comment is consumed and the comment swallows the page.
- **`label` shadowing.** The renderer has a local `label` inside `buildNode`; the heading
  helper is named `klabel` for that reason.
- **`fill_block` may receive no node** — a row can have children solely from an ambient ship.
- **Windows console is cp1252.** Use `PYTHONIOENCODING=utf-8` when printing vocabulary or
  card text, or the em dash and `−` raise `UnicodeEncodeError`.
- **Never assume the slug** from the event id; use the path the extractor prints.

---

## 11. Known limits

- Chance-entry rows use the full outcome narration as their label, because that is the only
  string the files contain. List-heavy cards run tall — except dispatch pools (§4.2b), whose
  rows are titles.
- A dispatch entry that loads another *list* has no title to borrow, so it renders as the
  unlabelled row: `FINISH_BEACON`'s two `EXIT_LIST` members show as "Outcome → 1 of 17" and
  "1 of 13". The files name those lists only internally, and I3 keeps internal ids off cards.
- An identical subtree repeats wherever the data reaches it; merging collapses siblings only.
- `hidden="true"` on a `<choice>` (797 uses) has no established meaning in any source here;
  it is carried through and ignored. One thing it is *not*, observed on `FINISH_BEACON`
  (see [[event-finish-beacon]]): an automatic chain. The player still dismisses the window
  before the choice's event loads.
- The 2–3 class threshold for naming a `blueprintList` is a judgement, not something the data
  states.
- The gated-label cleanup assumes requirements are written as a *leading* parenthetical.

Background on the grammar these rules encode, with the tag census and citations:
`wiki/concepts/event-tree-grammar.md`. The decision history — why each rule exists — is in
`wiki/log.md` under `tooling` entries.
