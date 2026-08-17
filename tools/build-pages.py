#!/usr/bin/env python3
"""Build the static copy of the site that GitHub Pages serves.

    python tools/build-pages.py                 # -> site/
    python tools/build-pages.py --check         # verify what is in site/, build nothing
    python tools/build-pages.py --deploy        # ...and force-push it to `gh-pages`

`tools/LOCAL-SITE.md` describes the served site; this is the same site with the server
taken out of it. `serve-site.py` is imported and its `resolve()`, `fragment_page()` and
`home_page()` do the rendering, so the hosted pages are the local ones and cannot drift
from them. Three things a static host cannot do, and what replaces each:

  301 redirects        A one-line HTML stub at the built file's name, forwarding to the
                       clean name and carrying the query string across. Same effect as
                       the server's 301, one hop, no server.

  root-absolute URLs   The chrome links `/sectors/`, and a project Pages site lives at
                       `/<repo>/`, where that is a 404. Every absolute URL the chrome
                       emits is rewritten to a *relative* one, computed from the page's
                       own depth -- which also keeps the output openable off `file://`.

  `?raw=1`             There is no server to serve the built file as text, so the nav's
                       `Built file` link points at the file on GitHub instead.

The `?seen=` / `?beacons=` overlay is attached to every sector page rather than only to
the ones asking for it. `SEEN_JS` already returns immediately when neither parameter is
present (LOCAL-SITE.md 5c), so the behaviour is what the server gives; what changes is
that the decision moves from the server to the page.
"""

import argparse
import importlib.util
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"

# serve-site.py is not an importable name -- the hyphen makes it un-`import`able, and
# renaming it would break every command in LOCAL-SITE.md. Load it by path instead.
_spec = importlib.util.spec_from_file_location(
    "serve_site", str(ROOT / "tools" / "serve-site.py"))
site = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(site)

REPO = "jparro00/ftl-wiki"
REF = "main"


# --------------------------------------------------------------------------
# Absolute chrome URLs -> relative ones
# --------------------------------------------------------------------------

# The built pages contain no absolute URL at all -- verified, and asserted below -- so
# every one of these comes from the chrome, and the map is closed. An absolute URL that
# is not in it is a build error rather than something to pass through: passing it
# through produces a link that 404s only once the site is hosted under a path prefix,
# which is the one place nobody looks.
ABS = re.compile(r'((?:href|src)=")(/[^"]*)(")')


def to_relative(url, depth):
    """A root-absolute chrome URL, as a path relative to a page `depth` levels down."""
    if url == "/":
        target = "index.html"
    elif url == "/sectors/":
        target = "sectors/index.html"
    elif url == "/cards/":
        target = "cards/index.html"
    else:
        match = re.fullmatch(r"/(sectors|cards)/(%s)" % site.SLUG, url)
        if not match:
            raise ValueError("no static equivalent for absolute URL %r" % url)
        target = "%s/%s.html" % match.groups()
    return "../" * depth + target


def relativise(page, depth):
    return ABS.sub(lambda m: m.group(1) + to_relative(m.group(2), depth) + m.group(3),
                   page)


SOURCE_LINK = re.compile(r'(<a class="sb-act" )href="\?raw=1"')


def source_on_github(page, built):
    """Repoint the nav's `Built file` link at the file in the repository.

    `?raw=1` is served by `serve-site.py` and by nothing here. The link exists so the
    build output is one click from the page it produced, and GitHub shows exactly that
    -- so the link keeps its meaning rather than being dropped.
    """
    href = 'href="https://github.com/%s/blob/%s/%s" target="_blank" rel="noopener"' % (
        REPO, REF, built)
    return SOURCE_LINK.sub(lambda m: m.group(1) + href, page)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------

STUB = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>%(title)s</title>
<link rel="canonical" href="%(target)s">
<meta http-equiv="refresh" content="0; url=%(target)s">
<script>location.replace(%(js)s + location.search + location.hash);</script>
</head><body><p><a href="%(target)s">%(title)s</a></p></body></html>
"""


def write(rel, body):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body.encode("utf-8") if isinstance(body, str) else body)
    return path


def stub(rel, target, title):
    """The built file's name, forwarding to the clean one.

    This is the server's 301 with the server removed, and it has the same job: the
    built pages link each other by their *built* names (`../cards/card-x.html`), and
    those links must keep working without editing a single built file.

    `location.replace` rather than a plain assignment, so the stub leaves no entry in
    the back button -- and it carries `location.search` across, because `?seen=` and
    `?pick=` are the whole channel the save watcher has (LOCAL-SITE.md 5c). The
    `<meta refresh>` behind it covers a reader with JavaScript off; it loses the query,
    which is the best a meta refresh can do.
    """
    return write(rel, STUB % {"target": target, "title": title,
                              "js": json.dumps(target)})


def _force_unlink(func, path, _exc):
    """Git marks its object files read-only, and Windows honours that against
    `os.unlink`. Nothing here is precious enough to stop for."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clear_output():
    """Empty `site/` — except for `site/.git`, which is the deploy repository.

    `rmtree(OUT)` was the first version and it fails on the *second* build: the deploy
    repo's read-only object files stop the delete halfway through, leaving a half-built
    site behind. Keeping it is also what makes a deploy a one-commit force-push instead
    of a fresh 31 MB push every time.
    """
    if not OUT.exists():
        OUT.mkdir(parents=True)
        return
    for child in OUT.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child, onerror=_force_unlink)
        else:
            child.unlink()


def build():
    clear_output()

    sectors, cards = site.sector_slugs(), site.card_slugs()
    # `cards/<slug>.html` is the page and `cards/card-<slug>.html` is its stub, so a
    # slug that already began `card-` would make one file try to be both.
    for slug in sectors:
        assert not slug.startswith("sector-"), slug
    for slug in cards:
        assert not slug.startswith("card-"), slug

    written = 0

    def page(rel, response, depth, built=None):
        nonlocal written
        body = response.body.decode("utf-8")
        body = relativise(body, depth)
        if built:
            body = source_on_github(body, built)
        write(rel, body)
        written += 1

    page("index.html", site.home_page(), 0)

    page("sectors/index.html", site.resolve("/sectors/"), 1,
         built="sectors/index.html")
    for slug in sectors:
        built = "sectors/sector-%s.html" % slug
        title = site.sector_title(slug)
        # The overlay is attached unconditionally here; SEEN_JS returns on its own when
        # neither `?seen=` nor `?beacons=` is present, so a plain page is unchanged.
        page("sectors/%s.html" % slug,
             site.fragment_page(
                 ROOT / built, "sectors",
                 [(site.NAV["sectors"], "/sectors/"), (title, None)], "?raw=1",
                 head="<style>%s</style>" % site.SEEN_CSS,
                 tail="<script>%s</script>" % site.SEEN_JS),
             1, built=built)
        stub("sectors/sector-%s.html" % slug, "%s.html" % slug, title)

    page("cards/index.html", site.resolve("/cards/"), 1, built="cards/index.html")
    for slug in cards:
        built = "cards/card-%s.html" % slug
        title = site.card_title(slug)
        page("cards/%s.html" % slug,
             site.fragment_page(ROOT / built, "cards",
                                [(site.NAV["cards"], "/cards/"), (title, None)],
                                "?raw=1"),
             1, built=built)
        stub("cards/card-%s.html" % slug, "%s.html" % slug, title)

    # What the pages load at runtime. `cards/trees/` is deliberately not copied: the
    # cards name it in a provenance comment and nothing fetches it, and it is 5.8 MB.
    for rel in ("cards/runtime", "cards/data", "sectors/data"):
        shutil.copytree(ROOT / rel, OUT / rel)

    # Jekyll is what GitHub Pages runs by default; it would rebuild this and drop any
    # path with a leading underscore. `.nojekyll` publishes the tree exactly as built.
    write(".nojekyll", "")
    write("404.html", not_found())

    print("pages     %d" % written)
    print("stubs     %d" % (len(sectors) + len(cards)))
    print("out       %s" % OUT)
    return 0


def not_found():
    """404. Its links are absolute-with-prefix, not relative: GitHub Pages serves this
    one file for any missing path, so a relative link in it resolves against whatever
    the reader typed rather than against the file's own location."""
    prefix = "/" + REPO.split("/", 1)[1]
    # Written in the chrome's own root-absolute vocabulary — `/sectors/`, not
    # `/ftl-wiki/sectors/` — so the one substitution below prefixes these and the nav's
    # links together. Writing the prefix in here as well is how this page first shipped,
    # and it produced `/ftl-wiki/ftl-wiki/sectors/`.
    body = ('<div class="hm"><p class="eyebrow">404</p><h1>No such page</h1>'
            '<p class="lede">That address is not part of this site.</p>'
            '<div class="jump"><a href="/">Home</a>'
            '<a href="/sectors/">Sectors</a>'
            '<a href="/cards/">Events</a></div></div>')
    doc = site.document("Not found", body,
                        head="<style>%s</style>" % site.HOME_CSS).body.decode("utf-8")
    return ABS.sub(lambda m: m.group(1) + prefix + m.group(2) + m.group(3), doc)


# --------------------------------------------------------------------------
# Check
# --------------------------------------------------------------------------

# Same narrowness as `serve-site.py`'s ASSET: these pages build hrefs in JavaScript, and
# a pattern loose enough to match `'card-' + s.slug + '.html'` reports files that were
# never asked for and trains a reader to ignore the output.
REF_RE = re.compile(r'(?:src|href)="((?:\.\./)*[A-Za-z0-9][A-Za-z0-9._/-]*'
                    r'\.(?:js|css|json|html))"', re.I)


def check():
    """Every local reference in every built file resolves to a file that exists.

    This is the whole failure mode of a static export: the links are all relative, so a
    layout mistake shows up as a 404 and as nothing else. Absolute URLs are a failure
    too -- one that only appears once the site is under a path prefix.
    """
    if not OUT.exists():
        print("no site/ -- run tools/build-pages.py first", file=sys.stderr)
        return 1

    problems, checked, pages = [], 0, 0
    for path in sorted(OUT.rglob("*.html")):
        rel = path.relative_to(OUT).as_posix()
        if rel.startswith(".git/"):       # the deploy repo, not the site
            continue
        pages += 1
        body = path.read_text(encoding="utf-8")
        if rel != "404.html":
            for match in ABS.finditer(body):
                problems.append("%s: absolute URL %s" % (rel, match.group(2)))
        for match in REF_RE.finditer(body):
            checked += 1
            target = (path.parent / match.group(1)).resolve()
            if not target.is_file():
                problems.append("%s -> %s (missing)" % (rel, match.group(1)))

    for want in (".nojekyll", "index.html", "sectors/index.html", "cards/index.html",
                 "cards/runtime/card.js", "cards/runtime/card.css"):
        if not (OUT / want).exists():
            problems.append("missing %s" % want)

    print("files     %d html" % pages)
    print("refs      %d" % checked)
    for line in sorted(set(problems))[:40]:
        print("  " + line)
    if problems:
        print("\n%d problem(s)" % len(set(problems)), file=sys.stderr)
        return 1
    print("\nok - every reference resolves and no page carries an absolute URL")
    return 0


# --------------------------------------------------------------------------
# Deploy
# --------------------------------------------------------------------------

def deploy(remote):
    """Force-push `site/` to `gh-pages` as a single commit.

    A throwaway repository inside `site/` rather than a branch of this one: the build
    output is not history worth keeping, and force-pushing one commit means the branch
    never accumulates 33 MB of superseded HTML. `site/` is gitignored here, so its
    `.git` is invisible to the repository it sits in.
    """
    def git(*args):
        return subprocess.run(("git",) + args, cwd=str(OUT), check=True)

    # `site/` is its own repository and knows nothing of this one's remotes, so a remote
    # *name* has to be resolved to a URL here rather than passed through.
    if "/" not in remote or not re.match(r"[a-z]+://|.+@", remote):
        remote = subprocess.run(("git", "remote", "get-url", remote), cwd=str(ROOT),
                                check=True, capture_output=True,
                                text=True).stdout.strip()

    # Git discovers a repository by walking *up*, so a `site/.git` that is missing or
    # damaged silently resolves to the repository this file lives in -- and then `add -A`,
    # `commit` and `push HEAD:gh-pages` all operate on the wiki instead of on the site.
    # That is not hypothetical: a half-finished `rmtree` left `site/.git` holding nothing
    # but `objects/` and `refs/`, and the deploy committed the working tree to `main` and
    # published the repository as the website. So the toplevel is checked, not assumed.
    top = subprocess.run(("git", "rev-parse", "--show-toplevel"), cwd=str(OUT),
                         capture_output=True, text=True)
    if top.returncode or pathlib.Path(top.stdout.strip() or ".").resolve() != OUT:
        if (OUT / ".git").exists():
            shutil.rmtree(OUT / ".git", onerror=_force_unlink)
        git("init", "-q", "-b", "gh-pages")
        top = subprocess.run(("git", "rev-parse", "--show-toplevel"), cwd=str(OUT),
                             capture_output=True, text=True)
    assert pathlib.Path(top.stdout.strip()).resolve() == OUT, top.stdout

    git("add", "-A")
    subprocess.run(("git", "commit", "-q", "-m", "Build the site"),
                   cwd=str(OUT), check=False)          # nothing to commit is not a fault
    git("push", "--force", remote, "HEAD:gh-pages")
    print("pushed    %s gh-pages" % remote)
    return 0


def main():
    global REPO
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="verify site/ and exit; builds nothing")
    ap.add_argument("--deploy", action="store_true",
                    help="build, check, then force-push site/ to gh-pages")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--repo", default=REPO, help="owner/name, for the Built file links")
    args = ap.parse_args()
    REPO = args.repo

    if args.check:
        return check()
    rc = build() or check()
    if rc or not args.deploy:
        return rc
    return deploy(args.remote)


if __name__ == "__main__":
    sys.exit(main())
