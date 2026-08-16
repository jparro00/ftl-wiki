# The review layer — specification

Normative spec for the in-browser commenting layer. Self-contained: an agent with no prior
context can produce a reviewable copy of any built page from this document alone.

A **review copy** is a built page with a commenting layer appended. The user reads it in a
browser, selects any text, attaches a note to the selection, and exports every note as
markdown for the agent to act on. It is how the sector-page redesign was done — five rounds,
no screenshots, no describing-the-thing-you-mean-in-chat.

It works on **any** self-contained HTML this repo builds — sector pages, event cards, the
sector index, a one-off mock.

---

## 1. Quick start

```bash
python tools/add-review-layer.py sectors/sector-rock-homeworlds.html
# → sectors/sector-rock-homeworlds-review.html
```

Then hand the user the `file:///…` URL. That is the whole flow — the script copies the page,
appends `tools/review-layer.html`, rebases relative links and stamps the title.

`-o` puts the copy somewhere else:

```bash
python tools/add-review-layer.py cards/card-giant-alien-spiders.html -o /tmp/card-review.html
```

**Never append the layer to a page that ships.** A review copy is a scratch artifact; the
original is never modified, and the script refuses to overwrite its source or to double-append
to a page that already carries the layer.

---

## 2. Components

| Path | Role | Hand-written? |
|---|---|---|
| `tools/review-layer.html` | the layer itself — style, markup, script, in that order | yes, this is the whole implementation |
| `tools/add-review-layer.py` | copies a page and appends the layer | code only |

The layer is a **fragment**, not a document: no `<html>`, `<head>` or `<body>`. It appends to
the end of a page's markup and its own elements live in `#cmt-ui`, outside everything the page
renders. That is what keeps the copy one readable block away from its source.

---

## 3. What the user gets

- **Select text → a "Comment" button appears at the selection.** Click it, type, save
  (`Ctrl`/`Cmd`+`Enter` also saves, `Esc` cancels). The selection stays highlighted.
- **Click a highlight** to open the panel at that note; **click a note** to scroll to its text.
- **The Comments tab** on the right edge carries a live count and opens the notes panel. Each
  note shows the quoted text, the note, and Edit / Delete.
- **Copy for Claude** puts every note on the clipboard as markdown. **Download .md** writes the
  same thing to a file for when the clipboard is blocked. **Clear all** wipes them, with a
  confirm.

Export format — quote, then note, in page order, so an agent can read them top to bottom:

```markdown
# Review notes — <page title>

File: /C:/Users/…/sector-rock-homeworlds-review.html

## 1
> the quoted text, newlines flattened

what the user wants changed
```

---

## 4. How anchoring works, and what it costs

A note anchors to a **character range in the page's visible text** — `[start, end)` counted from
the top of `<body>`, skipping `#cmt-ui`, `<script>`, `<style>` and `<title>`. Not DOM paths,
not CSS selectors.

That choice is what lets a note survive a rebuild: regenerate the page, reopen the copy, and
every highlight is still on its words. The consequences are worth knowing before you edit a
page someone is reviewing:

- **Anything added above an anchor shifts it.** The layer re-reads the text at each stored
  range on load and compares it to the quote; a mismatch is kept as an **orphan** — still
  listed, still exported, no longer highlighted. It never silently re-attaches to the wrong
  place.
- **The comparison ignores whitespace.** A selection spanning two elements reads back with the
  line break the browser inserted between them, while the markup often has no whitespace there
  at all. Comparing raw text would orphan every multi-element note on the first reload.
- **CSS `::before` / `::after` content is not a text node**, so a label added that way moves no
  anchors. That is the tool for annotating a page under live notes — the redesign used it to
  tag a variations page's baseline without disturbing the notes on it.
- **A range boundary is not always inside a text node.** Triple-click, select-all and any drag
  crossing an element edge hand back `(element, childIndex)` instead, and both forms have to
  resolve to the same character scale. Early versions did not, so triple-click selections
  silently produced no Comment button.

Highlights are painted by wrapping each covered text-node slice in `<mark class="cmt-hl">`.
Wrapping splits text nodes but changes no text, so offsets stay valid and notes can be painted
in any order. A slice that would straddle an element edge is skipped rather than forced.

**Storage is `localStorage`, keyed by the copy's filename** (`ftl-review:<basename>`). Three
things follow: renaming or moving a copy loses its notes; rebuilding a copy in place keeps
them; and two copies with the same basename in different directories share one set. On a
`file://` origin some browsers treat storage as opaque and throw — the layer probes for this
on load and, if it is blocked, toasts once so the user knows to download before closing.

---

## 5. Interaction with the page underneath

- **Cards still open.** Beacon boxes in a sector page load `cards/runtime/*` and `cards/data/*`
  by relative path; `add-review-layer.py` rebases every quoted `../…` path — in attributes
  **and** in the card loader's JSON config block, which is not an attribute and is the one
  people miss. A copy written beside its source needs no rebasing and gets none.
- **Clicks are shared.** The layer listens on `document` and ignores clicks inside `#cmt-ui`;
  the sector page's own toggle ignores clicks that end a text selection. Without that second
  rule, selecting text inside an expandable box would collapse it mid-drag.
- **Shadow DOM is out of reach.** An opened event card renders into a shadow root, and the
  layer's walker does not descend into it. Selections there produce no Comment button. Comment
  on the row instead, or on the standalone card page, which is ordinary markup.
- **Smoke tests pass on a review copy.** `smoke-sector.py` strips `<style …>` and `<script …>`
  including attributed tags, so the layer's own CSS comments and JavaScript are not read as
  page prose. If a review copy fails smoke, the failure is the page's.

---

## 6. Reading the notes back

The user exports to `~/Downloads/review-notes*.md` — take the newest. Then:

- **Read a note against what the page is for, not only against what it is anchored to.** The
  user selects whatever is nearest to what they mean. Real examples from the redesign: *"remove
  all this"* on a 4,000-character selection meant "delete the pool sections, they duplicate the
  budget"; notes left on a variations page's untouched baseline were the user drawing the shape
  they wanted, not describing the baseline.
- **A note can be a question** — *"explain to me what the any category is"* — and the answer
  belongs in chat, not on the page.
- **Say what you concluded** when you report back, especially where you read a note as meaning
  something other than its literal text. That is the round trip that keeps the loop honest.
- **Old notes come back.** Exports include every note still stored, so a fresh file can repeat
  items already applied. Compare against what the page now says rather than assuming the list
  is only new.

Rebuild the copy after applying a round — same path, so the notes survive — and hand back the
same URL.

---

## 7. Verification

There is no dedicated smoke test. What to check after changing `tools/review-layer.html`:

```bash
python tools/add-review-layer.py sectors/sector-rock-homeworlds.html -o /tmp/probe.html
python tools/smoke-sector.py /tmp/probe.html      # the page underneath still checks out
python tools/smoke-inline.py /tmp/probe.html      # boxes still open onto their cards
```

Then drive it in a browser — Playwright over `file://`, which is the scheme it runs under.
**Cover all three selection shapes**, because they take different paths through the anchoring
code and two of them were broken at different times:

1. a drag inside one text node,
2. a triple-click (element boundaries),
3. a selection spanning several elements.

For each: the Comment button appears, saving paints a highlight, and **after a reload every
highlight is still painted** and the note count is unchanged. That last check is the one that
catches an anchoring regression — notes surviving while highlights quietly do not is the
failure mode this design exists to avoid.

---

## 8. Where fixes go

| Symptom | Fix in |
|---|---|
| The commenting UI looks or behaves wrong | `tools/review-layer.html` |
| Highlights do not survive a reload | the boot block at the foot of `tools/review-layer.html` |
| A copy's cards do not open | `relink()` in `tools/add-review-layer.py` |
| A review copy fails a smoke test | usually the page, not the layer — check the source page first |
| The exported markdown is awkward to read back | `markdown()` in `tools/review-layer.html` |

---

## 9. Limits

- **One page, one set of notes.** Nothing aggregates notes across pages; review one page at a
  time, which is also how the feedback is worth most.
- **Notes live in one browser profile.** They are not in the repo, do not sync, and a cleared
  browser store loses them. Export anything that matters.
- **A published artifact cannot download.** The viewer sandbox blocks page-initiated downloads,
  so "Download .md" is inert on a published page and only "Copy for Claude" works there. Review
  copies are meant to be read off disk anyway — that is also where cards open.
- **The layer assumes the page is static.** A page that rewrites its own text after load can
  move anchors under the notes; nothing re-anchors them. Sector pages and cards do not do this
  — an opened card renders into a shadow root, which the walker never counted.
