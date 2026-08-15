#!/usr/bin/env python3
"""Open a sector page in a real browser and check that its beacon boxes open onto cards.

    python tools/smoke-inline.py sectors/sector-rock-homeworlds.html
    python tools/smoke-inline.py --all
    python tools/smoke-inline.py --all --browser chromium

The static check (tools/smoke-sector.py) cannot see any of this: the card is fetched
by a <script> tag and rendered into a shadow root, so it exists only in a live page.
This one drives the page the way a reader does — expand a budget line, open a beacon
box, then open a row inside the card that appears — and fails on:

  · a page error (the loader or the renderer throwing)
  · a box that never reaches data-state="ready"
  · a shadow root with no card in it
  · a card whose heading is not the event the box names — the one failure a length
    check would miss and the one that matters: the wrong card under the wrong box
  · a row inside the card that does not expand

It loads the page from **file://**, which is the case that matters and the one that
constrains the whole design: fetch, XHR and dynamic import are all blocked there, so
the loader uses script tags (tools/SECTOR-PAGE.md §6.1). Firefox is the default
browser here, and Playwright ships it with security.fileuri.strict_origin_policy
turned off — that would hide exactly the failure this test exists to catch, so the
stock value is forced back on.

Needs playwright (`pip install playwright && python -m playwright install firefox`).
"""

import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTORS = ROOT / "sectors"

# Restore what a real Firefox does with local files; Playwright's build relaxes both.
STOCK_PREFS = {
    "security.fileuri.strict_origin_policy": True,
    "privacy.file_unique_origin": True,
}

def normalise(text):
    return " ".join((text or "").split()).casefold()


def check(page, path, boxes_to_open):
    problems, errors = [], []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(path.resolve().as_uri())

    # Budget lines hold the boxes; open them all so every box is clickable.
    lines = page.locator("details.bwrap")
    for i in range(lines.count()):
        lines.nth(i).locator("> summary").click()

    boxes = page.locator("details.evbox")
    total = boxes.count()
    opened = 0
    for i in range(min(boxes_to_open, total)):
        box = boxes.nth(i)
        slug = box.get_attribute("data-card")
        expected = box.locator("> summary .t").inner_text()
        box.locator("> summary").click()
        panel = box.locator(".cardpanel")
        try:
            page.wait_for_function(
                "el => el.parentElement.getAttribute('data-state') === 'ready'",
                arg=panel.element_handle(), timeout=8000)
        except Exception:
            problems.append(f"{slug}: never became ready")
            continue
        heading = panel.evaluate("""el => {
          if (!el.shadowRoot) return null;
          const h = el.shadowRoot.querySelector("h1");
          return h ? h.textContent : "";
        }""")
        if heading is None:
            problems.append(f"{slug}: no card in the shadow root")
            continue
        # The box and the card have to be talking about the same event. A card that
        # renders under the wrong box is the failure worth catching; a *short* card
        # is not a failure at all — a store's card is three lines by nature.
        if normalise(heading) != normalise(expected):
            problems.append(f"{slug}: box says {expected!r}, card says {heading!r}")
            continue
        opened += 1

    # The card is interactive too: a row inside it must still expand in place.
    rows = page.locator("details.evbox[data-state='ready'] .cardpanel").first
    expanded = rows.evaluate("""el => {
      const btn = el.shadowRoot.querySelector("button.row[aria-expanded='false']");
      if (!btn) return "none";
      btn.click();
      return btn.getAttribute("aria-expanded") === "true"
        && !el.shadowRoot.getElementById(btn.getAttribute("aria-controls")).hidden;
    }""")
    if expanded is False:
        problems.append("a row inside an embedded card did not expand")

    problems += [f"page error: {e}" for e in errors]
    return problems, total, opened, expanded


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", type=pathlib.Path, nargs="?")
    ap.add_argument("--all", action="store_true", help="every built sector page")
    ap.add_argument("--browser", default="firefox", choices=["firefox", "chromium"])
    ap.add_argument("--boxes", type=int, default=3, help="boxes to open per page (default 3)")
    args = ap.parse_args()

    if args.all:
        pages = sorted(SECTORS.glob("sector-*.html"))
    elif args.page:
        pages = [args.page]
    else:
        ap.error("give a page or --all")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright is not installed: pip install playwright"
                 " && python -m playwright install firefox")

    failed = 0
    with sync_playwright() as p:
        kind = getattr(p, args.browser)
        browser = kind.launch(firefox_user_prefs=STOCK_PREFS) if args.browser == "firefox" \
            else kind.launch()
        for path in pages:
            if not path.exists():
                sys.exit(f"{path}: not found")
            page = browser.new_page(viewport={"width": 1200, "height": 1000})
            problems, total, opened, expanded = check(page, path, args.boxes)
            page.close()
            name = path.stem.replace("sector-", "")
            if problems:
                failed += 1
                print(f"FAIL {name}")
                for problem in problems:
                    print(f"  - {problem}")
            else:
                inner = "row expanded" if expanded is True else "no expandable row"
                print(f"ok   {name}: {opened}/{total} boxes opened onto a card, {inner}")
        browser.close()

    if failed:
        sys.exit(f"\n{failed} page(s) failed")
    print(f"\nOK — {len(pages)} page(s), {args.browser} over file://")


if __name__ == "__main__":
    main()
