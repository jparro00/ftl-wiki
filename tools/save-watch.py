"""Watch FTL's continue.sav and show the card for the event you're looking at.

    python tools/save-watch.py --open

Parks a page on http://127.0.0.1:8787 that swaps itself to the current event's card
whenever the game writes its save. Open it once on your second monitor and leave it;
there is nothing to click.

How it knows which event is on screen: `tools/ftlsave.py` parses continue.sav as far
as its EncounterState, whose `text` field holds the string-table id of the prose the
event window is displaying (FTL 1.6.1+ stores a reference, not the prose). This
module builds the reverse index -- string id back to the event that owns it -- from
raw/gamedata, then maps that event id to a card slug via cards/trees/*.tree.json.

Some strings are shared by more than one event, so the index is one-to-many and
resolution can be ambiguous; `--index-report` measures exactly how often. Ambiguity
is reported, never silently resolved to a guess.
"""

import argparse
import html
import http.server
import json
import os
import re
import socketserver
import sys
import threading
import time
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ftlsave
import importlib

buildmod = importlib.import_module("build-mod")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
TREES = os.path.join(CARDS, "trees")

SAVE_CANDIDATES = [
    os.path.expandvars(r"%USERPROFILE%\Documents\My Games\FasterThanLight\continue.sav"),
    os.path.expandvars(r"%APPDATA%\FasterThanLight\continue.sav"),
]


def find_save():
    """Where continue.sav is, or where it will appear.

    Falls back to the canonical location rather than None, because there is no save
    between runs -- FTL deletes it when one ends -- and the watcher is most useful
    started *before* the game. A missing file is the `nosave` state, not an error.
    """
    for path in SAVE_CANDIDATES:
        if os.path.exists(path):
            return path
    return SAVE_CANDIDATES[0]


# --------------------------------------------------------------------------
# Event resolution
# --------------------------------------------------------------------------

def _walk_texts(node, out):
    """Yield every text node in an event tree, depth-first.

    A card's tree already has all its loaded eventLists and nested choice outcomes
    expanded, so walking it collects exactly the prose that card can display.
    """
    if isinstance(node, dict):
        text = node.get("text")
        if isinstance(text, dict):
            out.append(text)
        for value in node.values():
            _walk_texts(value, out)
    elif isinstance(node, list):
        for item in node:
            _walk_texts(item, out)


def _norm(s):
    """Normalise a text key for lookup.

    Prose keys are matched exactly, which is fragile: `EncounterState.text` "may
    include line breaks" per the format docs, and the game's copy of a string need
    not agree with the XML's on where whitespace falls. Collapsing every run of
    whitespace to one space makes the comparison about the words. Ids contain no
    whitespace, so this is a no-op for them.
    """
    return " ".join((s or "").split())


def _keys_of(text, textlists):
    """The forms the save's `text` field could take for one text node.

    FTL 1.6.1+ stores a string-table reference, but the format docs are explicit
    that it may be the prose itself, so index both. When the ref names a
    `<textList>`, every one of its variants is a possible value too -- the game
    picks one at random and stores that one.
    """
    keys = []
    ref = text.get("ref")
    if ref:
        ref = ref.strip()
        keys.append(_norm(ref))
        for variant_ref, prose in textlists.get(ref, ()):
            if variant_ref:
                keys.append(_norm(variant_ref))
            if prose:
                keys.append(_norm(prose))
    value = text.get("value")
    if value:
        keys.append(_norm(value))
    return keys


def load_textlists():
    """`<textList>` name -> [(variant ref or None, variant prose), ...].

    Needed because a tree records only the *list* its text loads from, plus a
    variant count -- while the save records the variant actually displayed. An
    event reading `<text load="PIRATE_BRIBER"/>` shows `text_PIRATE_BRIBER_3`,
    which nothing in the tree mentions. Expanding the list here is what closes
    that gap; without it every list-backed event resolves to no card.
    """
    files, index = buildmod.load_game()
    strings = buildmod.load_strings()

    lists = {}
    for name, (fname, el) in index["textList"].items():
        variants = buildmod.variants_of(files[fname]["text"], el, strings)
        if variants:
            lists[name] = variants
    return lists


def build_index():
    """Build the text -> card indexes from cards/trees.

    Returns (anywhere, roots, titles):
      anywhere  text key -> set of slugs whose tree contains that text
      roots     text key -> set of slugs whose *root* text is that text
      titles    slug -> card title
    """
    anywhere, roots, titles = {}, {}, {}
    textlists = load_textlists()

    for name in sorted(os.listdir(TREES)):
        if not name.endswith(".tree.json"):
            continue
        with open(os.path.join(TREES, name), "r", encoding="utf-8") as fh:
            tree = json.load(fh)

        slug = tree["slug"]
        titles[slug] = tree.get("title", tree["id"])

        if isinstance(tree.get("text"), dict):
            for key in _keys_of(tree["text"], textlists):
                roots.setdefault(key, set()).add(slug)

        found = []
        _walk_texts(tree, found)
        for text in found:
            for key in _keys_of(text, textlists):
                anywhere.setdefault(key, set()).add(slug)

    return anywhere, roots, titles


class Resolver:
    """Turns the save's encounter text into a card slug.

    The same prose can appear in many cards -- every ship fight ends in
    DESTROYED_DEFAULT -- so a text alone often cannot name one card. Two things
    disambiguate it, in order:

      1. A text that is some card's *root* means that event just started.
      2. Otherwise, if the card already on screen contains this text, we are
         deeper into that same event and it stays put.
    """

    def __init__(self):
        self.anywhere, self.roots, self.titles = build_index()

    def resolve(self, encounter, current_slug=None):
        key = _norm(encounter.get("text"))
        if not key:
            return None

        root_hits = sorted(self.roots.get(key, ()))
        all_hits = sorted(self.anywhere.get(key, ()))

        reason = None
        if len(root_hits) == 1:
            slug, reason = root_hits[0], "root"
        elif current_slug and current_slug in all_hits:
            slug, reason = current_slug, "continued"
        elif len(root_hits) > 1:
            # Near-identical siblings (the four refugee variants, the three
            # rebel-auto ones). Any of them is a fair reading of the screen.
            slug, reason = root_hits[0], "root-ambiguous"
        elif len(all_hits) == 1:
            slug, reason = all_hits[0], "unique"
        elif all_hits:
            # Shared outcome prose ("the ship explodes...") with no event on
            # screen to continue from -- starting the watcher mid-combat does
            # this. Guessing here would show a confidently wrong card, so don't;
            # the next beacon resolves it.
            slug, reason = None, "ambiguous"
        else:
            slug = None

        return {
            "text_key": key,
            "slug": slug,
            "title": self.titles.get(slug),
            "reason": reason,
            "candidates": all_hits,
            "ambiguous": reason in ("ambiguous", "root-ambiguous"),
        }


# --------------------------------------------------------------------------
# Watcher
# --------------------------------------------------------------------------

class Watcher:
    def __init__(self, save_path, ftl_dat, resolver, verbose=False):
        self.save_path = save_path
        self.ftl_dat = ftl_dat
        self.resolver = resolver
        self.verbose = verbose
        self.lock = threading.Lock()
        self.state = {"status": "waiting", "detail": "no save read yet"}
        self._stamp = None
        self._last_key = None
        # What is on screen, which may be stale, versus the event we are actually
        # in. They differ while a card is held, and only the latter may drive the
        # resolver's stickiness -- otherwise a held card from a finished run could
        # capture a shared text in the next one.
        self._displayed = None
        self._anchor = None

    def snapshot(self):
        with self.lock:
            return dict(self.state)

    # Hold the last card only while we cannot tell what the player is looking at.
    # `nocard` is excluded deliberately: there we *have* identified the event and
    # simply have no card for it, so leaving the previous one up would assert
    # something false -- showing "Pirate engine hacker" while the screen reads
    # "Pirate briber". Saying nothing is better than saying the wrong thing.
    HOLDING_STATUSES = frozenset({"ambiguous", "noevent", "nosave", "error", "waiting"})

    def _set(self, state):
        """Publish a state, holding the last card when this one names none.

        A card the player may still be reading is not worth blanking for a torn
        read or a finished run. `held` marks the display as stale; `status` still
        tells the truth about what the save says.
        """
        if (not state.get("slug")
                and state.get("status") in self.HOLDING_STATUSES
                and self._displayed):
            state["slug"] = self._displayed
            state["title"] = self.resolver.titles.get(self._displayed)
            state["held"] = True
        else:
            state["held"] = False
            if state.get("slug"):
                self._displayed = state["slug"]

        with self.lock:
            self.state = state

    def poll_once(self, force=False):
        try:
            st = os.stat(self.save_path)
        except OSError:
            # A run ended. The card stays up, but the anchor must not: the next
            # run is a fresh context and may share outcome prose with this one.
            self._anchor = None
            self._set({"status": "nosave", "detail": "continue.sav not found (no run in progress)"})
            self._stamp = None
            return

        stamp = (st.st_mtime_ns, st.st_size)
        if stamp == self._stamp and not force:
            return
        self._stamp = stamp

        try:
            parsed = ftlsave.parse(self.save_path, self.ftl_dat)
        except ftlsave.SaveFormatError as exc:
            # A save caught mid-write parses as garbage; the next poll retries.
            self._set({"status": "error", "detail": str(exc)})
            return
        except Exception as exc:  # noqa: BLE001 - surfaced to the page, not swallowed
            self._set({"status": "error", "detail": "%s: %s" % (type(exc).__name__, exc)})
            return

        resolved = self.resolver.resolve(parsed["encounter"], current_slug=self._anchor)
        if resolved is None:
            self._set({"status": "noevent", "detail": "no event text in the save"})
            return

        if resolved["slug"]:
            self._anchor = resolved["slug"]

        if resolved["slug"]:
            status = "ok"
        elif resolved["reason"] == "ambiguous":
            status = "ambiguous"
        else:
            status = "nocard"

        state = {
            "status": status,
            "sector": parsed["sector_number"] + 1,
            "beacon": parsed["current_beacon_id"],
            **resolved,
        }
        self._set(state)

        if self.verbose and resolved["text_key"] != self._last_key:
            self._last_key = resolved["text_key"]
            shown = self.snapshot()
            print("[%s] %-46s -> %s (%s)" % (
                time.strftime("%H:%M:%S"),
                resolved["text_key"][:46],
                resolved["slug"] or ("holding %s" % shown["slug"] if shown.get("held")
                                     else "no card"),
                resolved["reason"] or status,
            ), flush=True)

    def run(self, interval=0.5):
        while True:
            self.poll_once()
            time.sleep(interval)


# --------------------------------------------------------------------------
# Server
# --------------------------------------------------------------------------

SHELL = """<!doctype html>
<html><head><meta charset="utf-8"><title>FTL event card</title>
<style>
  html,body{margin:0;height:100%;background:#0b0f14;color:#c9d5e1;
            font:14px/1.5 system-ui,sans-serif}
  #frame{border:0;width:100%;height:100%;display:block}
  #msg{display:flex;height:100%;align-items:center;justify-content:center;
       text-align:center;padding:2rem;box-sizing:border-box}
  #msg div{max-width:32rem}
  h1{font-size:1rem;font-weight:600;letter-spacing:.02em;margin:0 0 .5rem}
  p{margin:.25rem 0;color:#7f8ea3}
  code{color:#9db4cc}
</style></head><body>
<div id="msg"><div><h1>Waiting for FTL</h1><p>Jump to a beacon.</p></div></div>
<iframe id="frame" style="display:none"></iframe>
<script>
let shownSlug = null, shownMsg = null;
async function tick() {
  try {
    const r = await fetch('/current', {cache: 'no-store'});
    const s = await r.json();
    const frame = document.getElementById('frame');
    const msg = document.getElementById('msg');

    // Any slug at all means a card is worth showing -- held or current. Only
    // reload when it actually changes, so a held card never flickers.
    if (s.slug) {
      if (s.slug !== shownSlug) {
        shownSlug = s.slug;
        shownMsg = null;
        frame.src = '/card/' + s.slug;
      }
      frame.style.display = 'block';
      msg.style.display = 'none';
      return;
    }

    const key = s.status + ':' + (s.text_key || s.detail || '');
    if (key !== shownMsg) {
      shownMsg = key;
      shownSlug = null;
      {
        frame.style.display = 'none';
        msg.style.display = 'flex';
        const heads = {
          nocard: 'No card for this event',
          ambiguous: 'Shared outcome text',
          noevent: 'No event on screen',
          nosave: 'No run in progress',
          error: 'Could not read the save',
          waiting: 'Waiting for FTL'
        };
        let body = '';
        if (s.status === 'nocard') {
          body = '<p><code>' + s.text_key + '</code></p>';
        } else if (s.status === 'ambiguous') {
          body = '<p>This text appears in ' + s.candidates.length +
                 ' cards, so it cannot name one on its own.</p>' +
                 '<p>The next beacon will resolve it.</p>';
        } else if (s.detail) {
          body = '<p>' + s.detail + '</p>';
        }
        msg.innerHTML = '<div><h1>' + (heads[s.status] || s.status) + '</h1>' + body + '</div>';
      }
    }
  } catch (e) { /* server not up yet; try again */ }
}
tick(); setInterval(tick, 500);
</script></body></html>
"""


def make_handler(watcher):
    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass  # the watcher's own --verbose output is the useful log

        def _send(self, body, ctype, code=200):
            if isinstance(body, str):
                body = body.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if self.path == "/" or self.path.startswith("/?"):
                self._send(SHELL, "text/html; charset=utf-8")
            elif self.path == "/current":
                self._send(json.dumps(watcher.snapshot()), "application/json")
            elif self.path.startswith("/card/"):
                slug = self.path[len("/card/"):]
                if not re.fullmatch(r"[a-z0-9-]+", slug):
                    self._send("bad slug", "text/plain", 400)
                    return
                path = os.path.join(CARDS, "card-%s.html" % slug)
                if not os.path.exists(path):
                    self._send("no card %s" % html.escape(slug), "text/plain", 404)
                    return
                with open(path, "rb") as fh:
                    self._send(fh.read(), "text/html; charset=utf-8")
            else:
                self._send("not found", "text/plain", 404)

    return Handler


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


# --------------------------------------------------------------------------

def index_report(resolver):
    """Measure how well a text can be pinned to one card."""
    anywhere, roots, titles = resolver.anywhere, resolver.roots, resolver.titles

    shared = {k: v for k, v in anywhere.items() if len(v) > 1}
    root_unique = sum(1 for v in roots.values() if len(v) == 1)
    root_shared = {k: v for k, v in roots.items() if len(v) > 1}
    # A shared text is only a problem when stickiness cannot save it -- that is,
    # when it is not also some card's root text.
    hard = {k: v for k, v in shared.items() if k not in roots}

    print("cards                      %d" % len(titles))
    print("text keys indexed          %d" % len(anywhere))
    print()
    print("root texts (event start)   %d" % len(roots))
    print("  pinning exactly one card %d" % root_unique)
    print("  shared by several cards  %d" % len(root_shared))
    print()
    print("keys in >1 card's tree     %d" % len(shared))
    print("  of those, not a root     %d  <- resolved by stickiness" % len(hard))

    if root_shared:
        print("\nroot texts shared by several cards:")
        for k, v in sorted(root_shared.items())[:15]:
            print("  %-44s %s" % (k[:44], ", ".join(sorted(v))))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--save", default=find_save(), help="path to continue.sav")
    ap.add_argument("--ftl-dat", default=ftlsave.default_ftl_dat(), help="path to ftl.dat")
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--open", action="store_true", help="open the page in a browser")
    ap.add_argument("--once", action="store_true", help="resolve once, print, exit")
    ap.add_argument("--index-report", action="store_true",
                    help="measure how ambiguous the text index is, then exit")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.ftl_dat:
        ap.error("could not find ftl.dat; pass --ftl-dat")

    resolver = Resolver()

    if args.index_report:
        index_report(resolver)
        return 0

    watcher = Watcher(args.save, args.ftl_dat, resolver, verbose=not args.quiet)

    if args.once:
        watcher.poll_once(force=True)
        print(json.dumps(watcher.snapshot(), indent=2))
        return 0

    threading.Thread(target=watcher.run, daemon=True).start()

    url = "http://127.0.0.1:%d/" % args.port
    with Server(("127.0.0.1", args.port), make_handler(watcher)) as httpd:
        if not args.quiet:
            print("watching %s" % args.save)
            print("serving  %s   (ctrl-c to stop)" % url)
        if args.open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
