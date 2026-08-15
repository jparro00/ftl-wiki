#!/usr/bin/env python3
"""Build an FTL event card from an event tree.

    python tools/build-card.py cards/trees/<slug>.tree.json [-o out.html]
    python tools/build-card.py --all          every tree in cards/trees/
    python tools/build-card.py --runtime      only the shared runtime files

Three kinds of output, all generated from the same two inputs (the tree and
tools/card-vocab.json):

    cards/card-<slug>.html    the standalone card — renderer and data inlined, so a
                              published artifact needs no network at all
    cards/data/<slug>.js      the same tree as one FTLCard.define() call, for a page
                              that wants to render this card inside itself
    cards/runtime/card.js     the renderer plus the vocabulary, loaded once by such a
    cards/runtime/card.css    page; the CSS with the standalone page's own chrome
                              stripped and :root rewritten to :host for a shadow root

Inlining rather than fetching is forced for the card page: published artifacts run
under a strict CSP and file:// blocks cross-origin reads, so a runtime fetch of a
sibling .json would fail in both places. The sector pages get at the runtime and the
payloads with a <script> tag, which is the one cross-directory read file:// allows —
see tools/SECTOR-PAGE.md §6.1.
"""

import argparse
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
TEMPLATE = TOOLS / "event-card-render.html"
RUNTIME_SRC = TOOLS / "card-runtime.js"
SCHEMA = "ftl-event-tree/1"

VOCAB = TOOLS / "card-vocab.json"

TREES = ROOT / "cards" / "trees"
DATA_DIR = ROOT / "cards" / "data"
RUNTIME_DIR = ROOT / "cards" / "runtime"

RUNTIME_MARKER = "<!--CARD-RUNTIME-->"

# The standalone page's own chrome: background, page padding, the centred column.
# An embedded card sits in someone else's page and must not repaint it.
PAGE_ONLY = re.compile(r"[ \t]*/\* PAGE-ONLY-START.*?PAGE-ONLY-END \*/\n", re.DOTALL)
STYLE = re.compile(r"<style>(.*?)</style>", re.DOTALL)

# What a card needs when it is not the page: the inherited text settings the stripped
# body rule used to supply. Everything else it already carries.
HOST_RULE = """
/* Embedded in a shadow root: :root cannot match, so the variables live on :host. */
:host {
  display: block;
  color: var(--ink);
  font-family: var(--sans);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
/* An embedded card is a section of someone else's page, not the page itself: the
   box above it already names the event, so the heading drops to a section's scale. */
:host header { margin-bottom: 1.05rem; }
:host h1 { font-size: 1.2rem; margin-bottom: .6rem; }
"""


def block(element_id):
    return re.compile(
        r'(<script type="application/json" id="%s">)(.*?)(</script>)' % element_id,
        re.DOTALL,
    )


BLOCK = block("event-data")
VOCAB_BLOCK = block("card-vocab")
# Anchored to its own line so a stray "<title>" in a comment cannot be matched.
TITLE = re.compile(r"^<title>[^\n]*?</title>$", re.MULTILINE)


def read_vocab():
    return json.loads(VOCAB.read_text(encoding="utf-8"))


def write_runtime():
    """The two files a page other than a card loads to render cards of its own."""
    source = RUNTIME_SRC.read_text(encoding="utf-8")
    vocab = json.dumps(read_vocab(), ensure_ascii=False, separators=(",", ":"))
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

    js = RUNTIME_DIR / "card.js"
    js.write_text(source + "\nFTLCard.vocab = " + vocab + ";\n", encoding="utf-8")

    css_source = STYLE.search(TEMPLATE.read_text(encoding="utf-8"))
    if not css_source:
        sys.exit(f"{TEMPLATE}: no <style> block to extract")
    css = PAGE_ONLY.sub("", css_source.group(1))
    if "PAGE-ONLY" in css:
        sys.exit(f"{TEMPLATE}: PAGE-ONLY markers are unbalanced")
    css = css.replace(":root", ":host")
    out_css = RUNTIME_DIR / "card.css"
    out_css.write_text(css.rstrip() + "\n" + HOST_RULE, encoding="utf-8")
    return [js, out_css]


def write_payload(slug, data):
    """One define() call — a file:// page can load this with a <script> tag."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out = DATA_DIR / f"{slug}.js"
    body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    out.write_text(f"FTLCard.define({json.dumps(slug)},{body});\n", encoding="utf-8")
    return out


def build(tree_path: pathlib.Path, out_path: pathlib.Path) -> pathlib.Path:
    data = json.loads(tree_path.read_text(encoding="utf-8"))

    schema = data.get("schema")
    if schema != SCHEMA:
        sys.exit(f"{tree_path}: expected schema {SCHEMA!r}, found {schema!r}")
    if not data.get("title"):
        sys.exit(f"{tree_path}: missing 'title'")

    vocab = read_vocab()

    template = TEMPLATE.read_text(encoding="utf-8")
    for name, pattern in (("event-data", BLOCK), ("card-vocab", VOCAB_BLOCK)):
        if not pattern.search(template):
            sys.exit(f"{TEMPLATE}: no #{name} block to fill")
    if not TITLE.search(template):
        sys.exit(f"{TEMPLATE}: no <title> element on a line of its own")
    if RUNTIME_MARKER not in template:
        sys.exit(f"{TEMPLATE}: no {RUNTIME_MARKER} to fill")

    def inline(pattern, doc, html):
        # '<' is escaped so no value in the data can close the script element early.
        payload = json.dumps(doc, indent=2, ensure_ascii=False).replace("<", "\\u003c")
        return pattern.sub(lambda m: m.group(1) + "\n" + payload + "\n" + m.group(3), html, count=1)

    html = inline(BLOCK, data, template)
    html = inline(VOCAB_BLOCK, vocab, html)
    html = TITLE.sub("<title>" + data["title"] + "</title>", html, count=1)
    # The renderer is one file (tools/card-runtime.js) used by cards and by sector
    # pages alike; the card page carries its own copy so it needs nothing at load.
    runtime = RUNTIME_SRC.read_text(encoding="utf-8")
    html = html.replace(RUNTIME_MARKER, "<script>\n" + runtime + "</script>", 1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")

    slug = data.get("slug") or tree_path.name[: -len(".tree.json")]
    write_payload(slug, data)
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tree", type=pathlib.Path, nargs="?", help="path to a <slug>.tree.json")
    ap.add_argument("--all", action="store_true", help="every tree in cards/trees/")
    ap.add_argument("--runtime", action="store_true", help="only rebuild the shared runtime")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output .html (single card only)")
    args = ap.parse_args()

    # The runtime is derived from the same renderer and vocabulary every card inlines,
    # so it is refreshed on every build — the two can never drift apart.
    for path in write_runtime():
        print(path)
    if args.runtime:
        return

    if args.all:
        trees = sorted(TREES.glob("*.tree.json"))
        if not trees:
            sys.exit(f"{TREES}: no trees")
    elif args.tree:
        if not args.tree.exists():
            sys.exit(f"{args.tree}: not found")
        trees = [args.tree]
    else:
        ap.error("give a tree path, --all, or --runtime")

    for tree in trees:
        slug = tree.name[: -len(".tree.json")] if tree.name.endswith(".tree.json") else tree.stem
        # Built cards live together in cards/, outside the wiki layer: they are generated
        # artifacts, and a stable path per slug is what keeps a published URL stable.
        out = args.out if (args.out and len(trees) == 1) else ROOT / "cards" / f"card-{slug}.html"
        print(build(tree, out))


if __name__ == "__main__":
    main()
