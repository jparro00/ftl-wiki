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
import json
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
    # The loader and its config are code, not copy: they hold comment asterisks and
    # braces that these checks are meant to catch in prose, and nothing a reader sees.
    body = re.sub(r"<script.*?</script>", "", body, flags=re.DOTALL)
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

    # Every path the page will ask the browser for, resolved the way the browser will:
    # relative to the directory the page sits in. A box that looks live and then lands
    # on a 404 is worse than an inert one, and the loader's failure text is the only
    # thing a reader would ever see of it.
    def resolve(href):
        return (args.page.parent / href).resolve()

    links = [n for n in page.nodes if n["tag"] == "a" and "cardlink" in n["classes"]]
    boxes = [n for n in page.nodes if n["tag"] == "details" and "evbox" in n["classes"]]
    missing = set()
    for node in links:
        href = node["attrs"].get("href", "")
        if not href:
            problems.append("card link with no href")
        elif not resolve(href).exists():
            missing.add(href)

    config = None
    for node in page.nodes:
        if node["attrs"].get("id") == "sector-card-loader":
            config = json.loads(" ".join(node["text"]))
    if config is None:
        problems.append("no card-loader config block")
    else:
        for key in ("runtime", "css"):
            if not resolve(config[key]).exists():
                missing.add(config[key])
        for node in boxes:
            slug = node["attrs"].get("data-card")
            if not slug:
                problems.append("beacon box with no data-card slug")
                continue
            payload = config["data"].replace("{slug}", slug)
            if not resolve(payload).exists():
                missing.add(payload)
    for href in sorted(missing):
        problems.append(f"page asks for a file that is not there: {href}")

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
    # The two generated blocks above the budget. They carry no copy at all, so the only
    # way a wrong label or a missing count shows up is by being printed here.
    glance = [n for n in page.nodes if "gp" in n["classes"]]
    if glance:
        out.append("GLANCE")
        for node in glance:
            out.append("  " + " | ".join(node["text"]))
        out.append("")
    for node in page.nodes:
        if "grow" in node["classes"]:
            if not re.fullmatch(r"\d+", node["text"][-1] if node["text"] else ""):
                problems.append(f"blue-option row without a hit count: {node['text']}")
        if "rrow" in node["classes"] and len(node["text"]) < 3:
            problems.append(f"rarity row missing its move or verdict: {node['text']}")
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
        if "panel" in node["classes"] and "gp" not in node["classes"]:
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
    print(f"OK — {len(events)} event rows ({len(boxes)} open onto their card), "
          f"{len(rows)} budget rows ({len(expanders)} expandable), {len(stats)} stat tiles")


if __name__ == "__main__":
    main()
