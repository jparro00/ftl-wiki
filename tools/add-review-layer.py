#!/usr/bin/env python3
"""Copy a built page and append the in-browser review layer to the copy.

    python tools/add-review-layer.py sectors/sector-rock-homeworlds.html
    python tools/add-review-layer.py cards/card-giant-alien-spiders.html -o /tmp/x.html

The user reads the copy in a browser, selects text, and attaches notes to it; the
notes export as markdown for the next round. tools/REVIEW-LAYER.md is the spec.

Two things this does that appending the file by hand does not:

- **Relative links are rewritten for the copy's directory.** A sector page reaches its
  cards through `../cards/…`; a copy one level deeper needs `../../cards/…`, and a copy
  that keeps the depth needs no change at all. Getting this wrong is silent — the page
  looks right and every beacon box opens onto nothing.
- **The title is suffixed**, so the tab and the exported notes name the review copy
  rather than the page it was cut from.

The original is never modified. The layer is appended, never woven in: everything it
adds lives after the page's own markup, so the copy differs from the source by exactly
one block and the diff stays readable.
"""

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LAYER = ROOT / "tools" / "review-layer.html"

TITLE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
# Any quoted upward-relative path: `href="../cards/x.html"` in the markup, and the same
# paths again as JSON strings in the card loader's config block, which is not an
# attribute and would otherwise be missed — silently, since only an opened box shows it.
RELATIVE = re.compile(r"""(?P<q>["'])(?P<path>\.\./[^"']*)(?P=q)""")

SUFFIX = " (review)"


def relink(source, src_dir, out_dir):
    """Re-point every relative href/src from the source's directory to the copy's."""
    if src_dir.resolve() == out_dir.resolve():
        return source, 0

    changed = 0

    def fix(match):
        nonlocal changed
        target = (src_dir / match.group("path")).resolve()
        try:
            rebased = pathlib.PurePosixPath(
                pathlib.Path(target).relative_to(out_dir.resolve()).as_posix())
        except ValueError:
            # Not under the output directory — walk up with os.path.relpath semantics.
            import os
            rebased = pathlib.PurePosixPath(
                os.path.relpath(target, out_dir.resolve()).replace("\\", "/"))
        changed += 1
        return f'{match.group("q")}{rebased}{match.group("q")}'

    return RELATIVE.sub(fix, source), changed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", type=pathlib.Path, help="the built page to review")
    ap.add_argument("-o", "--out", type=pathlib.Path,
                    help="output path (default: <page>-review.html beside the source)")
    args = ap.parse_args()

    if not args.page.exists():
        sys.exit(f"{args.page}: not found")
    if not LAYER.exists():
        sys.exit(f"{LAYER}: not found — the review layer is the payload, see tools/REVIEW-LAYER.md")

    source = args.page.read_text(encoding="utf-8")
    if 'id="cmt-script"' in source:
        sys.exit(f"{args.page}: already carries the review layer — copy the original instead")

    out = args.out or args.page.with_name(f"{args.page.stem}-review.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.resolve() == args.page.resolve():
        sys.exit("refusing to write over the source page")

    source, relinked = relink(source, args.page.parent, out.parent)

    # The storage key is the filename (REVIEW-LAYER.md §4), and the title is what the
    # exported notes are headed with — so both should say which copy this is.
    match = TITLE.search(source)
    if match and SUFFIX not in match.group(1):
        source = TITLE.sub(lambda m: f"<title>{m.group(1)}{SUFFIX}</title>", source, count=1)

    out.write_text(source + LAYER.read_text(encoding="utf-8"), encoding="utf-8")
    print(out)
    if relinked:
        print(f"  {relinked} relative link(s) rebased for {out.parent}", file=sys.stderr)


if __name__ == "__main__":
    main()
