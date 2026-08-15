#!/usr/bin/env python3
"""Render a built sector page as text and check it for the defects that hide in HTML.

    python tools/smoke-sector.py sectors/sector-engi-homeworlds.html

Prints the whole page — header, facts, stat tiles, beacon budget, every pool row,
the chain, the panels and the footnotes. Anything the page can show must appear in
this dump, or a defect there is invisible.

Exit code 1 if any check fails. Required before publishing (tools/SECTOR-PAGE.md §7).
"""

import argparse
import html.parser
import pathlib
import re
import sys

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

# Markup the copy layer owns. Any of these surviving into the output means the
# renderer failed to consume it, which would show as literal asterisks on the page.
LEAKS = [("{{", "unresolved {{EVENT_ID}} reference"),
         ("**", "unrendered **bold** markup"),
         ("<!--SECTOR-CONTENT-->", "unfilled content marker")]

# A *paired* asterisk inside one run of text means the author reached for italics, which
# the copy layer does not support — it renders literally. Single asterisks are legitimate
# and must not fire: the footnote names "events*.xml", and chain refs carry ids like
# "BOSS_1_*". So the match requires an opening and closing asterisk with no markup
# between them.
STRAY_ASTERISK = re.compile(r"\*[^\s*<][^*<]{0,80}\*")


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.nodes = [], [], []
        self.title = None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = (attrs.get("class") or "").split()
        if tag == "title":
            self._in_title = True
        if tag not in VOID:
            self.stack.append((tag, classes, len(self.nodes)))
        self.nodes.append({"tag": tag, "classes": classes, "attrs": attrs, "text": []})

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in VOID:
            return
        while self.stack:
            open_tag, _, _ = self.stack.pop()
            if open_tag == tag:
                return
            self.errors.append(f"unclosed <{open_tag}> before </{tag}>")
        self.errors.append(f"stray </{tag}>")

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
        text = data.strip()
        if not text:
            return
        for _, _, index in self.stack:
            self.nodes[index]["text"].append(text)


def texts(page, klass, tag=None):
    return [" ".join(n["text"]) for n in page.nodes
            if klass in n["classes"] and (tag is None or n["tag"] == tag)]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", type=pathlib.Path)
    args = ap.parse_args()

    if not args.page.exists():
        sys.exit(f"{args.page}: not found")
    source = args.page.read_text(encoding="utf-8")

    page = Page()
    page.feed(source)
    problems = list(page.errors)
    problems += [f"unclosed <{t}>" for t, _, _ in page.stack]

    body = re.sub(r"<style>.*?</style>", "", source, flags=re.DOTALL)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    for needle, why in LEAKS:
        if needle in body:
            problems.append(why)
    if STRAY_ASTERISK.search(body):
        problems.append("literal '*' in the page — *italics* is not supported markup, use **bold**")

    if not page.title or "EDIT" in (page.title or ""):
        problems.append("title was not stamped")

    stats = [n for n in page.nodes if "stat" in n["classes"]]
    numbers = texts(page, "n")
    labels = texts(page, "k")
    if not numbers:
        problems.append("no stat tiles")
    for value in numbers:
        if not re.fullmatch(r"\d+(–\d+)?", value):
            problems.append(f"stat tile is not a number: {value!r}")

    events = [n for n in page.nodes if "ev" in n["classes"]]
    for node in events:
        if not node["text"]:
            problems.append("empty event row")
    rows = [n for n in page.nodes if "brow" in n["classes"]]
    if not rows:
        problems.append("no beacon-budget rows")

    # A beacon box that links to a card no one built is worse than an inert box: it
    # looks live and lands on a 404. The link is relative, so resolve it the way the
    # browser will — against the directory the page sits in.
    links = [n for n in events if n["tag"] == "a"]
    dead = set()
    for node in links:
        href = node["attrs"].get("href", "")
        if not href:
            problems.append("event link with no href")
            continue
        target = (args.page.parent / href).resolve()
        if not target.exists():
            dead.add(href)
    for href in sorted(dead):
        problems.append(f"event link points at a missing card: {href}")
    expanders = [n for n in page.nodes if n["tag"] == "details" and "bwrap" in n["classes"]]

    out = []
    out.append(f"TITLE     {page.title}")
    out.append(f"HEADING   {' / '.join(texts(page, 'eyebrow') + [t for n in page.nodes if n['tag'] == 'h1' for t in [' '.join(n['text'])]])}")
    out.append(f"LEDE      {' '.join(texts(page, 'lede'))}")
    out.append(f"FACTS     {' | '.join(texts(page, 'fact'))}")
    out.append("")
    out.append("STATS")
    for value, label in zip(numbers, labels):
        out.append(f"  {value:>9}  {label}")
    out.append("")
    out.append("BUDGET")
    for node in rows:
        out.append("  " + "  ".join(node["text"]))
    out.append("")
    for node in page.nodes:
        if node["tag"] == "h2":
            out.append("## " + " — ".join(node["text"]))
        elif "ev" in node["classes"]:
            out.append("   - " + " · ".join(node["text"]))
        elif "note" in node["classes"] or "callout" in node["classes"]:
            out.append("   " + " ".join(node["text"]))
        elif "step" in node["classes"]:
            out.append("   " + " · ".join(node["text"]))
    out.append("")
    out.append("PANELS")
    for node in page.nodes:
        if "panel" in node["classes"]:
            out.append("  " + " | ".join(node["text"]))
    out.append("")
    out.append("FOOTER")
    for node in page.nodes:
        if node["tag"] == "footer":
            for line in node["text"]:
                out.append("  " + line)

    print("\n".join(out))
    print()
    if problems:
        print(f"FAIL — {len(problems)} problem(s):")
        for problem in problems:
            print(f"  - {problem}")
        sys.exit(1)
    print(f"OK — {len(events)} event rows ({len(links)} linked to cards), "
          f"{len(rows)} budget rows ({len(expanders)} expandable), {len(stats)} stat tiles")


if __name__ == "__main__":
    main()
