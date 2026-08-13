#!/usr/bin/env python3
"""Build an FTL event card from an event tree.

    python tools/build-card.py cards/trees/<slug>.tree.json [-o out.html]

Inlines the JSON into tools/event-card-render.html and stamps the <title>.
Inlining rather than fetching is deliberate: published artifacts run under a
strict CSP and file:// blocks cross-origin reads, so a runtime fetch of a
sibling .json would fail in both places. The card still parses the document as
JSON at load, so the data and the renderer stay separate.
"""

import argparse
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
TEMPLATE = TOOLS / "event-card-render.html"
SCHEMA = "ftl-event-tree/1"

VOCAB = TOOLS / "card-vocab.json"


def block(element_id):
    return re.compile(
        r'(<script type="application/json" id="%s">)(.*?)(</script>)' % element_id,
        re.DOTALL,
    )


BLOCK = block("event-data")
VOCAB_BLOCK = block("card-vocab")
# Anchored to its own line so a stray "<title>" in a comment cannot be matched.
TITLE = re.compile(r"^<title>[^\n]*?</title>$", re.MULTILINE)


def build(tree_path: pathlib.Path, out_path: pathlib.Path) -> pathlib.Path:
    data = json.loads(tree_path.read_text(encoding="utf-8"))

    schema = data.get("schema")
    if schema != SCHEMA:
        sys.exit(f"{tree_path}: expected schema {SCHEMA!r}, found {schema!r}")
    if not data.get("title"):
        sys.exit(f"{tree_path}: missing 'title'")

    vocab = json.loads(VOCAB.read_text(encoding="utf-8"))

    template = TEMPLATE.read_text(encoding="utf-8")
    for name, pattern in (("event-data", BLOCK), ("card-vocab", VOCAB_BLOCK)):
        if not pattern.search(template):
            sys.exit(f"{TEMPLATE}: no #{name} block to fill")
    if not TITLE.search(template):
        sys.exit(f"{TEMPLATE}: no <title> element on a line of its own")

    def inline(pattern, doc, html):
        # '<' is escaped so no value in the data can close the script element early.
        payload = json.dumps(doc, indent=2, ensure_ascii=False).replace("<", "\\u003c")
        return pattern.sub(lambda m: m.group(1) + "\n" + payload + "\n" + m.group(3), html, count=1)

    html = inline(BLOCK, data, template)
    html = inline(VOCAB_BLOCK, vocab, html)
    html = TITLE.sub("<title>" + data["title"] + "</title>", html, count=1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tree", type=pathlib.Path, help="path to a <slug>.tree.json")
    ap.add_argument("-o", "--out", type=pathlib.Path, help="output .html (default: cards/card-<slug>.html)")
    args = ap.parse_args()

    tree = args.tree
    if not tree.exists():
        sys.exit(f"{tree}: not found")

    slug = tree.name[: -len(".tree.json")] if tree.name.endswith(".tree.json") else tree.stem
    # Built cards live together in cards/, outside the wiki layer: they are generated
    # artifacts, and a stable path per slug is what keeps a published URL stable.
    out = args.out or ROOT / "cards" / f"card-{slug}.html"
    print(build(tree, out))


if __name__ == "__main__":
    main()
