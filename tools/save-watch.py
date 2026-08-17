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

Under Hyperspace there is a better channel and the watcher prefers it: the engine logs
`Creating event: <ID>` to FTL_HS.log as each event is instantiated. That names the event
outright, and names it when it appears -- where the save is not rewritten at all for an
event a hidden choice chains into, so it can be a whole event behind. SAVE-WATCH.md 4b.
"""

import argparse
import http.server
import json
import os
import re
import socketserver
import sys
import threading
import time
import urllib.request
import webbrowser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ftlsave
import importlib

buildmod = importlib.import_module("build-mod")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
TREES = os.path.join(CARDS, "trees")
SECTOR_PAGES = os.path.join(ROOT, "sectors")
SECTOR_DATA = os.path.join(SECTOR_PAGES, "data")

SAVE_DIRS = [
    os.path.expandvars(r"%USERPROFILE%\Documents\My Games\FasterThanLight"),
    os.path.expandvars(r"%APPDATA%\FasterThanLight"),
]

# Hyperspace redirects the game's file access through its own prefix, so a modded
# install writes hs_continue.sav and never touches continue.sav. Both are watched, and
# the most recently written one wins -- which is what makes the watcher follow the
# player across an install, an uninstall, or a downgrade without being told.
SAVE_NAMES = ["continue.sav", "hs_continue.sav"]

SAVE_CANDIDATES = [os.path.join(d, n) for d in SAVE_DIRS for n in SAVE_NAMES]


def find_save():
    """The live save, or where one will appear.

    Falls back to the canonical location rather than None, because there is no save
    between runs -- FTL deletes it when one ends -- and the watcher is most useful
    started *before* the game. A missing file is the `nosave` state, not an error.
    """
    existing = [p for p in SAVE_CANDIDATES if os.path.exists(p)]
    if existing:
        return max(existing, key=lambda p: os.stat(p).st_mtime_ns)
    return SAVE_CANDIDATES[0]


# --------------------------------------------------------------------------
# Which sector — from Hyperspace's log, because the save cannot say
# --------------------------------------------------------------------------

# Hyperspace prints one of these before the beacon lines of every generation.
SECTOR_LINE = re.compile(r"^Sector:\s*([A-Z0-9_]+)\s*$", re.M)

# And one of these as each event is instantiated -- on arrival at a beacon, and again
# for every event a choice chains into. `Creating ShipEvent:` lines are ship spawns and
# deliberately not matched.
CREATED_EVENT = re.compile(r"^Creating event: ([A-Za-z0-9_]+)", re.M)

# The same line, but only where **nothing follows the name** -- which is what separates
# arriving at a beacon from creating an event inside one. Measured on a real log
# (2026-08-17, MANTIS_SECTOR, 8 lines, entirely consistent):
#
#   Creating event: NOTHING_MANTIS              <- arrival
#   Creating event: AUTO_ASTEROID               <- arrival
#   Creating event: DESTROYED_DEFAULT 287       <- its outcome
#   Creating event: DISTRESS_TRAPPED_MINER      <- arrival
#   Creating event: DISTRESS_TRAPPED_MINER_LOOT 99
#   Creating event: REBEL_TRANSPORT             <- arrival
#   Creating event: REBEL_TRANSPORT 851         <- and its own child, same name
#
# The pool filter (§4c) already drops the children whose names differ from any pool
# event. **The last pair is why this pattern has to exist:** a child sharing its
# parent's name is in the pool by definition, so nothing but the trailing number
# distinguishes it, and counting it made one visit to the exit beacon read as two.
#
# `CREATED_EVENT` deliberately still matches both, because *which event is on screen*
# is answered by the most recent line of either kind -- `REBEL_TRANSPORT 851` being
# last is exactly how we know we are in REBEL_TRANSPORT.
#
# Known risk, stated because the evidence is one sector wide: if a genuine arrival ever
# carries a trailing number, it is missed, and the symptom is an undercount rather than
# a wrong count.
#
# **A real newline, not `$`.** In MULTILINE, `$` also matches at the end of the string,
# so a log caught mid-write matches its own truncated final line -- and the game appends
# to this file constantly while the watcher polls twice a second. Two ways that lies,
# both silent:
#
#   `Creating event: REBEL_CHECKPOINT` cut short reads as an arrival at `REBEL`, which is
#   a real event in the pool, so nothing downstream can tell it was never there.
#   `Creating event: REBEL_TRANSPORT 851` read before ` 851` lands looks bare, and
#   inflates that beacon's count by one.
#
# The lookahead costs only the genuine last line of a file with no trailing newline,
# which is the ambiguous case anyway -- the next poll picks it up once the newline is
# written.
ARRIVED_EVENT = re.compile(r"^Creating event: ([A-Za-z0-9_]+)[ \t]*(?=\r?\n)", re.M)

# And the `map-signal` mod (tools/build-map-signal-mod.py) prints one of these each
# time the star map opens or closes. Only the two state words match: the mod's
# `loaded` and its error lines share the prefix and must not read as transitions.
#
# Hyperspace stamps its own tag on anything a script logs, so what lands in the file is
# `[Lua]: map-signal: open sector 2` -- the optional group is that tag, and leaving it
# out was the one thing the synthetic test could not catch, because the test wrote the
# lines the mod emits rather than the lines the log receives.
MAP_SIGNAL = re.compile(r"^(?:\[[^\]]*\]:\s*)?map-signal:\s+(open|closed)\b", re.M)

# The same mod reports the *sector* map — the screen that offers the next sectors — and
# names what is on offer, which is the one thing neither the save nor the engine's own
# log holds before the jump is taken:
#
#   map-signal: choosing 4 column -> Rock Homeworlds | Slug Home Nebula
#   map-signal: chosen
#
# `column` before the arrow is load-bearing: it says the names are the sectors in the
# next column of the map, which is a *superset* of the ones this sector connects to.
# Hyperspace exposes three members on a Sector -- description, level, visited -- so the
# engine's own adjacency cannot be read, and naming a subset would mean re-deriving
# xftl's linking rules and risking the wrong two. See SAVE-WATCH.md §5d.
SECTOR_CHOICE = re.compile(
    r"^(?:\[[^\]]*\]:\s*)?map-signal:\s+(choosing|chosen)\b([^\n]*)", re.M)
CHOICE_SPLIT = " | "
CHOICE_APPROX = "column"

# Only the tail matters and the log is small (a few KB per sector), but a long
# session appends, so the read is bounded rather than trusting that.
LOG_TAIL_BYTES = 256 * 1024

# Where the pages are served from (`tools/LOCAL-SITE.md`). The watcher builds URLs
# against this origin and serves no pages of its own; `--site` points it elsewhere,
# which is the whole change needed to drive a hosted copy.
DEFAULT_SITE = "http://127.0.0.1:8080"


def default_hs_log(ftl_dat):
    """Hyperspace writes FTL_HS.log beside the game, so ftl.dat locates it."""
    return os.path.join(os.path.dirname(os.path.abspath(ftl_dat)), "FTL_HS.log")


def _pool_of(data):
    """Every event id a beacon of this sector can hold — all three sources.

    **All three, because the sector page draws a box for each of them**, and a box is
    what `?seen=` marks. Taking only `entries` is the mistake this function exists to
    have made once: the fill-in list is 20 events in the Mantis sector and 18 of them
    are nowhere in `entries`, so more than a third of that sector's beacons could never
    be marked, silently.

      entries[].events        the allocation table's own lists
      generation.fallback_events   the fill-in row (`SECTOR-PAGE.md` §4.1b-2)
      entries[].override.added     the Advanced Edition delta (§4.4)
    """
    pool = set()
    for entry in data.get("entries") or []:
        for event in entry.get("events") or []:
            if event.get("id"):
                pool.add(event["id"])
        for event in ((entry.get("override") or {}).get("added") or []):
            if event.get("id"):
                pool.add(event["id"])
    for event in ((data.get("generation") or {}).get("fallback_events") or []):
        if event.get("id"):
            pool.add(event["id"])
    return pool


class HyperspaceLog:
    """What `FTL_HS.log` knows that the save does not: the sector, the screen, the event.

    The save cannot answer this. A vanilla parse yields a sector *number*; the
    Hyperspace scan yields not even that; and neither yields the sector *type*,
    which is what names a page — the type is regenerated from `sectorTreeSeed` and
    never stored (`SAVE-WATCH.md` §3). Hyperspace prints it: every sector
    generation logs `Sector: CIVILIAN_SECTOR`, and `sectors/data/*.sector.json`
    carries that same id. So this costs no mod and is read, not inferred.

    The star map being *open* is `starMap.bOpen`, which only a Hyperspace script can
    read. The `map-signal` mod logs its transitions to the same file, so when that mod
    is installed this class reports the real screen and the watcher drops its
    heuristic. When it is not, `map_open` stays None and nothing pretends otherwise.

    And the **event on screen** — which the save does hold, but late. `Creating event:
    <ID>` is written the instant an event is instantiated, including one a hidden
    choice chains into, where the save is not rewritten at all (§4b). The id is also
    better evidence than the text: it names the event outright, where prose shared by
    sixty cards cannot.
    """

    def __init__(self, log_path, by_id=None):
        self.log_path = log_path
        (self.index, self.start_slugs, self.by_display_name,
         self.pools) = self._load_index()
        # Event id -> card slug, from the same trees the text index is built from.
        self.by_id = by_id or {}
        self._id = None
        self._since = None          # monotonic stamp of the last arrival, if known
        self._seen = False          # whether any sector has been read yet
        self._stamp = None          # (mtime_ns, size) of the last read
        self._map_open = None       # None = the map-signal mod is not installed
        self._event = None          # (event id, slug) of the last event with a card
        self._choosing = None       # slugs on offer at the sector map, or None
        self._choosing_approx = False   # ...and whether that is the column, not the offer
        self._visits = []           # [(event id, times)] visited in this sector, in order

    @staticmethod
    def _load_index():
        """Engine sector id -> page slug, and the entry-beacon cards, off the profiles.

        The start-beacon set is read from each sector's `<startEvent>` rather than
        listed here, so a sector whose entry event changes needs no edit. The Last
        Stand drops out on its own: its `startEvent` is `BOSS_NEUTRAL`, a list rather
        than an event, so it has no card slug — and its members are real fights that
        must keep showing their own cards.

        The **pool** — every event id a beacon of that sector can hold — comes from the
        same files, and is what filters the log's `Creating event:` stream down to
        beacon arrivals (§4c). Nothing else distinguishes a beacon from a sub-event.
        """
        out, starts, by_name, pools = {}, set(), {}, {}
        try:
            names = sorted(os.listdir(SECTOR_DATA))
        except OSError:
            return out, starts, by_name, pools
        for name in names:
            if not name.endswith(".sector.json"):
                continue
            try:
                with open(os.path.join(SECTOR_DATA, name), encoding="utf-8") as fh:
                    data = json.load(fh)
            except (OSError, ValueError):
                continue
            if data.get("id") and data.get("slug"):
                out[data["id"]] = data["slug"]
            # The sector-choice screen can only give the *display* name — that is what
            # the engine hands Lua — so the name is a second key into the same pages.
            for key in ("display_name", "title", "short_name"):
                if data.get(key) and data.get("slug"):
                    by_name.setdefault(data[key].strip().lower(), data["slug"])
            if data.get("id"):
                pools[data["id"]] = _pool_of(data)
            start = data.get("start_event") or {}
            if start.get("slug") and str(start.get("id", "")).startswith("START_BEACON"):
                starts.add(start["slug"])
        return out, starts, by_name, pools

    def poll(self):
        try:
            st = os.stat(self.log_path)
        except OSError:
            return
        stamp = (st.st_mtime_ns, st.st_size)
        if stamp == self._stamp:
            return
        # A shrinking file is the game restarting: Hyperspace truncates its log at
        # launch. Everything read from it belongs to the previous session and must go,
        # or a fresh menu keeps reporting the sector the last run ended in. Measured:
        # a watcher left running across a relaunch reported ENGI_HOME at the main menu.
        if self._stamp and st.st_size < self._stamp[1]:
            self._id, self._since, self._seen = None, None, False
            self._map_open, self._event, self._choosing = None, None, None
            self._choosing_approx = False
            self._visits = []
        self._stamp = stamp
        try:
            with open(self.log_path, "rb") as fh:
                if st.st_size > LOG_TAIL_BYTES:
                    fh.seek(-LOG_TAIL_BYTES, os.SEEK_END)
                text = fh.read().decode("utf-8", "replace")
        except OSError:
            return
        # The last transition is the current screen. Absent entirely means the mod is
        # not installed, which is a different state from "closed" and stays None.
        signals = MAP_SIGNAL.findall(text)
        self._map_open = (signals[-1] == "open") if signals else None

        # Sector choice, from the last `choosing`/`chosen` pair. Names are resolved
        # against the profiles; one that resolves to nothing is dropped rather than
        # guessed at, so a renamed sector shows as a short offer, never a wrong one.
        choices = SECTOR_CHOICE.findall(text)
        if not choices or choices[-1][0] == "chosen":
            self._choosing = None
            self._choosing_approx = False
        else:
            _, tail = choices[-1]
            head, _, offered = tail.partition("->")
            self._choosing_approx = CHOICE_APPROX in head
            slugs = []
            for name in offered.split(CHOICE_SPLIT):
                slug = self.by_display_name.get(name.strip().lower())
                if slug and slug not in slugs:
                    slugs.append(slug)
            self._choosing = slugs

        # The most recent created event that has a card. Scanning back past the ones
        # that do not is what makes this work without any tree of sub-events: an
        # outcome node (DESTROYED_DEFAULT, LANIUS_TRADER_LIST) has no card of its own,
        # and the card that should be on screen is its parent -- the last id before it
        # that does. Which is exactly what the text index's stickiness computes the
        # long way round.
        for eid in reversed(CREATED_EVENT.findall(text)):
            if eid in self.by_id:
                self._event = (eid, self.by_id[eid])
                break

        hits = SECTOR_LINE.findall(text)

        # Which beacons this sector has been to. Recomputed from the log on every read
        # rather than accumulated, which is what makes the reset exact and free: a new
        # `Sector:` line moves the anchor, and everything before it stops counting.
        # Nothing to remember, so nothing to forget at the wrong moment.
        anchor = 0
        last = None
        for match in SECTOR_LINE.finditer(text):
            anchor, last = match.end(), match.group(1)
        # No `Sector:` line in the tail means the whole tail lies inside one sector's
        # block -- a line between two blocks would be in it. So anchor 0 is right, not
        # a fallback.
        pool = self.pools.get(last if last else self._id) or set()
        order, times = [], {}
        # ARRIVED_EVENT, not CREATED_EVENT: only a line with nothing after the name is a
        # beacon arrival. A child event created inside one carries a trailing number, and
        # where it shares its parent's name the pool cannot tell them apart.
        for match in ARRIVED_EVENT.finditer(text, anchor):
            eid = match.group(1)
            # And only events this sector's pool can place. The log also carries the
            # entry beacon, ship spawns, and the out-of-fuel event -- none of which is a
            # beacon the budget allocated, and the pool is what states the difference.
            if eid not in pool:
                continue
            if eid not in times:
                times[eid] = 0
                order.append(eid)
            times[eid] += 1
        self._visits = [(eid, times[eid]) for eid in order]

        if not hits:
            return
        # The last generation block is the current sector; earlier ones are history.
        if hits[-1] != self._id:
            first = self._id is None and not self._seen
            self._id = hits[-1]
            self._seen = True
            # Starting the watcher is not arriving anywhere. On the first read the
            # sector is known but its age is not, so it counts as no arrival at all --
            # otherwise every restart would seize the screen for the hold window,
            # mid-event, on the strength of a log line written an hour ago.
            self._since = None if first else time.monotonic()

    def current(self):
        return {
            "id": self._id,
            "slug": self.index.get(self._id) if self._id else None,
            "age": None if self._since is None else time.monotonic() - self._since,
            "map_open": self._map_open,
            "event": self._event,
            "choosing": self._choosing,
            "choosing_approx": self._choosing_approx,
            "visits": list(self._visits),
        }


# --------------------------------------------------------------------------
# Staleness
# --------------------------------------------------------------------------

# Python reads these files once, at import, and the watcher is meant to be left
# running for hours. So an edit to the script does not reach a watcher already up --
# it keeps serving the old code while looking perfectly healthy. That is not
# hypothetical: on 2026-08-15 a watcher started at 11:46 was still following
# continue.sav at 16:50, because SAVE_NAMES learned about hs_continue.sav at 15:44
# and nobody restarted it. The symptom was "the watcher stopped picking up events",
# which points at the game, the save, or the index -- anywhere but the real cause.
_SOURCES = [os.path.abspath(__file__), os.path.abspath(ftlsave.__file__)]
_STARTED = time.time()
_source_warned = False


def _source_mtimes():
    out = {}
    for path in _SOURCES:
        try:
            out[path] = os.stat(path).st_mtime_ns
        except OSError:
            pass  # a source that cannot be stat'd simply is not compared
    return out


_SOURCE_MTIMES = _source_mtimes()


def _warn_if_source_changed():
    """Say so, once, if the code on disk no longer matches the code running."""
    global _source_warned
    if _source_warned:
        return
    changed = [p for p, m in _source_mtimes().items() if _SOURCE_MTIMES.get(p) != m]
    if not changed:
        return
    _source_warned = True
    names = ", ".join(os.path.basename(p) for p in changed)
    # flush: the watcher is normally launched in the background with stdout to a
    # file, where an unflushed warning sits in the buffer and never gets read.
    print("[stale] %s changed on disk since this watcher started at %s."
          % (names, time.strftime("%H:%M", time.localtime(_STARTED))), flush=True)
    print("[stale] This process is still running the old code -- restart it.", flush=True)


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

    Returns (anywhere, roots, titles, by_id):
      anywhere  text key -> set of slugs whose tree contains that text
      roots     text key -> set of slugs whose *root* text is that text
      titles    slug -> card title
      by_id     in-game event id -> slug, for the log channel (§4b), where the
                event is named outright and no text matching is needed
    """
    anywhere, roots, titles, by_id = {}, {}, {}, {}
    textlists = load_textlists()

    for name in sorted(os.listdir(TREES)):
        if not name.endswith(".tree.json"):
            continue
        with open(os.path.join(TREES, name), "r", encoding="utf-8") as fh:
            tree = json.load(fh)

        slug = tree["slug"]
        titles[slug] = tree.get("title", tree["id"])
        if tree.get("id"):
            by_id[tree["id"]] = slug

        if isinstance(tree.get("text"), dict):
            for key in _keys_of(tree["text"], textlists):
                roots.setdefault(key, set()).add(slug)

        found = []
        _walk_texts(tree, found)
        for text in found:
            for key in _keys_of(text, textlists):
                anywhere.setdefault(key, set()).add(slug)

    return anywhere, roots, titles, by_id


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
        self.anywhere, self.roots, self.titles, self.by_id = build_index()

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
    def __init__(self, save_path, ftl_dat, resolver, verbose=False, pinned_save=False,
                 hs_log=None, sector_hold=40.0, site=DEFAULT_SITE):
        self.save_path = save_path
        self.ftl_dat = ftl_dat
        self.resolver = resolver
        self.verbose = verbose
        # Where the pages live. The watcher builds URLs against this and serves none
        # itself; point it at a hosted site and nothing else changes.
        self.site = site.rstrip("/")
        # Optional: the sector page takes the screen when there is no card to show,
        # and for `sector_hold` seconds after arriving somewhere new.
        self.hs_log = hs_log
        self.sector_hold = sector_hold
        # An explicit --save is obeyed; an auto-detected one is re-resolved each poll
        # so the watcher follows the game between continue.sav and hs_continue.sav.
        self._pinned_save = pinned_save
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
        self._log_event = None

    def _scan_encounter(self):
        """An encounter-shaped dict from a content scan, or None.

        Only `text` is recovered, which is all `Resolver.resolve` reads. The *last*
        candidate in file order is taken: the encounter block sits after the ship and
        the star map, so anything else of this shape appears before it.
        """
        try:
            hits = ftlsave.scan_encounter_text(self.save_path)
        except OSError:
            return None
        if not hits:
            return None
        return {"text": hits[-1][1]}

    def snapshot(self):
        with self.lock:
            state = dict(self.state)
        # Decided per request, not per save write: the hold window expires on the
        # clock, and the save is silent exactly while it is running down.
        self._decorate_sector(state)
        state["site"] = self.site
        return state

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

    def _decorate_sector(self, state):
        """Attach the sector, and decide which of the two pages to show.

        Where the sector profile is the better answer:

        0. **The star map is open** — but only when the `map-signal` mod is installed
           to say so (§5c). This is the exact answer, and when it is available it
           replaces the timed guess in 3 entirely: an open map means the profile, a
           closed one means the card, and no window is invented around either.
        1. **The entry beacon.** A `START_BEACON_*` card says "you jump in" and
           nothing else, and it is on screen at exactly the moment the question is
           *what is this sector*. It also stays the last resolved event for as long
           as the player sits on the map planning the route, which is why this alone
           gets most of the way without the mod.
        2. There is no card to show at all.
        3. The player has just arrived somewhere new — the timed window, and the one
           heuristic in the watcher. Dropped the moment the signal exists.
        """
        if not self.hs_log:
            state["view"] = "card"
            state["url"] = self._url(state)
            return
        info = self.hs_log.current()
        state["sector_id"] = info["id"]
        state["sector_slug"] = info["slug"]
        state["sector_age"] = None if info["age"] is None else round(info["age"], 1)
        state["map_open"] = info["map_open"]
        state["next_sectors"] = info["choosing"]
        state["next_sectors_approx"] = info["choosing_approx"]
        state["seen"] = [eid if n == 1 else "%s:%d" % (eid, n)
                         for eid, n in info["visits"]]
        start = state.get("slug") in self.hs_log.start_slugs
        state["at_start_beacon"] = start

        # The sector map outranks everything: the player is choosing where to fly, and
        # the chooser is the page for that question, with the offer already pinned.
        # An empty list still means that screen is up — the offer could not be named,
        # which is a reason to show the chooser unpinned, not to show a card.
        if info["choosing"] is not None:
            state["view"] = "choose"
            state["url"] = self._url(state)
            return
        # A guess is only worth making where nothing is being reported.
        fresh = (info["map_open"] is None
                 and info["age"] is not None and info["age"] <= self.sector_hold)
        want = info["map_open"] or start or fresh or not state.get("slug")
        state["view"] = "sector" if info["slug"] and want else "card"
        state["url"] = self._url(state)

    @staticmethod
    def _url(state):
        """The site URL this state should be showing — path and query, no origin.

        The watcher decides the whole URL rather than handing the page a slug and a
        `view` to reassemble, because the URL *is* the interface to the site
        (`LOCAL-SITE.md` §5c). Once the site is hosted, the address is the only channel
        the watcher has left, and a shell that built its own would be a second place
        where the two could disagree.
        """
        if state.get("view") == "choose":
            query = "?pick=" + ",".join(state.get("next_sectors") or [])
            if state.get("next_sectors_approx"):
                query += "&column=1"
            return "/sectors/" + query
        if state.get("view") == "sector" and state.get("sector_slug"):
            url = "/sectors/" + state["sector_slug"]
            # Only this sector's beacons, and only on this sector's page. Carrying them
            # onto a card would mark nothing and lengthen every URL.
            if state.get("seen"):
                url += "?seen=" + ",".join(state["seen"])
            return url
        if state.get("slug"):
            return "/cards/" + state["slug"]
        return None

    def poll_once(self, force=False):
        # Before the early return below: the log moves on its own schedule, and both
        # a sector change and a new event are worth seeing on a poll where the save
        # has not moved -- which is precisely the case the log exists to cover.
        log_event = None
        if self.hs_log:
            self.hs_log.poll()
            log_event = self.hs_log.current()["event"]
        # Which file is live can change under us: installing Hyperspace moves the run
        # save to hs_continue.sav, uninstalling moves it back. Re-resolving each poll
        # costs two stats and means neither transition needs a restart.
        if not self._pinned_save:
            self.save_path = find_save()

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
        if stamp == self._stamp and log_event == self._log_event and not force:
            return
        self._stamp = stamp
        self._log_event = log_event

        source = "parse"
        try:
            parsed = ftlsave.parse(self.save_path, self.ftl_dat)
            encounter = parsed["encounter"]
        except Exception as exc:  # noqa: BLE001 - surfaced to the page, not swallowed
            # The structured walk needs FTL's exact ship layout. A Hyperspace save is
            # not that shape, and a save caught mid-write is not either. Both land
            # here, and the scan tells them apart: a torn read yields nothing.
            encounter = self._scan_encounter()
            source = "scan"
            if encounter is None:
                detail = str(exc) if isinstance(exc, ftlsave.SaveFormatError) \
                    else "%s: %s" % (type(exc).__name__, exc)
                self._set({"status": "error", "detail": detail})
                return

        resolved = self.resolver.resolve(encounter, current_slug=self._anchor)

        # The log names the event outright, and names it sooner. FTL does not rewrite
        # the save when a hidden choice chains into the rolled event -- measured at the
        # exit beacon, where the save sat on FINISH_BEACON while the screen showed the
        # event it rolled (§4b) -- so the save can be a whole event behind. An id also
        # beats prose sixty cards share. Where the log has an answer, it wins.
        if log_event:
            eid, slug = log_event
            resolved = dict(resolved or {"text_key": None, "candidates": []},
                            slug=slug, title=self.resolver.titles.get(slug),
                            reason="logged", event_id=eid)
            source = "log"
        elif resolved is None:
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
            # The scan recovers the event and nothing else -- no sector or beacon
            # number -- so those are null rather than guessed. `source` says which
            # path produced this, since the two differ in what they can know.
            "source": source,
            "save": os.path.basename(self.save_path),
            "sector": parsed["sector_number"] + 1 if source == "parse" else None,
            "beacon": parsed["current_beacon_id"] if source == "parse" else None,
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
            _warn_if_source_changed()
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
let shownSrc = null, shownMsg = null;
async function tick() {
  try {
    const r = await fetch('/current', {cache: 'no-store'});
    const s = await r.json();
    const frame = document.getElementById('frame');
    const msg = document.getElementById('msg');

    // One frame, and the watcher has already decided what belongs in it: `url` is a
    // complete site URL, chosen in Python (`Watcher._url`), and `site` is where the
    // site is served from. The shell composes and nothing more -- rebuilding the URL
    // here would be a second place for the two to disagree, and the hosted case makes
    // the address the only channel the watcher has.
    const want = s.url ? (s.site || '') + s.url : null;
    if (want) {
      if (want !== shownSrc) {
        shownSrc = want;
        shownMsg = null;
        frame.src = want;
      }
      frame.style.display = 'block';
      msg.style.display = 'none';
      return;
    }

    const key = s.status + ':' + (s.text_key || s.detail || '');
    if (key !== shownMsg) {
      shownMsg = key;
      shownSrc = null;
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
            else:
                # **This watcher no longer serves pages — the site does**
                # (`tools/LOCAL-SITE.md`). One owner for page serving, and it is the one
                # with the URLs, the chrome and the `?seen=` overlay. The old shapes are
                # kept as redirects so a link or a bookmark from before still lands in
                # the right place.
                match = re.fullmatch(r"/(card|sector)/([a-z0-9-]+)", self.path)
                if match:
                    kind, slug = match.groups()
                    self._redirect("%s/%ss/%s" % (watcher.site, kind, slug))
                elif self.path.startswith(("/cards", "/sectors")):
                    self._redirect(watcher.site + self.path)
                else:
                    self._send("not found -- pages are served by %s" % watcher.site,
                               "text/plain", 404)

        def _redirect(self, to):
            self.send_response(302)
            self.send_header("Location", to)
            self.send_header("Content-Length", "0")
            self.end_headers()

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


def probe_site(base, timeout=1.5):
    """One-line verdict on whether the site is answering. Never raises."""
    try:
        with urllib.request.urlopen(base + "/sectors/", timeout=timeout) as fh:
            return "reachable" if fh.status == 200 else "responded %s" % fh.status
    except Exception as exc:                              # any failure is the same news
        return ("not reachable (%s) -- start it with tools/serve-site.py"
                % type(exc).__name__)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--save", default=None,
                    help="path to the run save; auto-detects continue.sav / "
                         "hs_continue.sav (Hyperspace) and follows the newer one")
    ap.add_argument("--ftl-dat", default=ftlsave.default_ftl_dat(), help="path to ftl.dat")
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--open", action="store_true", help="open the page in a browser")
    ap.add_argument("--once", action="store_true", help="resolve once, print, exit")
    ap.add_argument("--index-report", action="store_true",
                    help="measure how ambiguous the text index is, then exit")
    ap.add_argument("--hs-log", default=None,
                    help="Hyperspace's FTL_HS.log; defaults to beside ftl.dat. It is "
                         "where the current sector comes from — the save does not hold it")
    ap.add_argument("--sector-hold", type=float, default=40.0, metavar="SECONDS",
                    help="show the sector profile for this long after arriving in a new "
                         "sector (default 40; 0 shows it only when no card resolves)")
    ap.add_argument("--no-sector", action="store_true",
                    help="cards only; never show a sector profile")
    ap.add_argument("--site", default=DEFAULT_SITE, metavar="URL",
                    help="where the pages are served from (default %(default)s). The "
                         "watcher builds URLs against this and serves no pages itself, "
                         "so a hosted site needs only this flag. Start it with "
                         "tools/serve-site.py")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.ftl_dat:
        ap.error("could not find ftl.dat; pass --ftl-dat")

    resolver = Resolver()

    if args.index_report:
        index_report(resolver)
        return 0

    hs_log = None
    if not args.no_sector:
        hs_log = HyperspaceLog(args.hs_log or default_hs_log(args.ftl_dat),
                               by_id=resolver.by_id)
        hs_log.poll()      # so startup can report what it found, not what it will find

    watcher = Watcher(args.save or find_save(), args.ftl_dat, resolver,
                      verbose=not args.quiet, pinned_save=bool(args.save),
                      hs_log=hs_log, sector_hold=args.sector_hold, site=args.site)

    if args.once:
        watcher.poll_once(force=True)
        print(json.dumps(watcher.snapshot(), indent=2))
        return 0

    threading.Thread(target=watcher.run, daemon=True).start()

    url = "http://127.0.0.1:%d/" % args.port
    with Server(("127.0.0.1", args.port), make_handler(watcher)) as httpd:
        if not args.quiet:
            # args.save is None unless pinned, which printed "watching None" for the
            # ordinary case. Name the file that was actually resolved -- under
            # Hyperspace that is hs_continue.sav, and seeing which one it picked is
            # the first thing worth knowing when it reports nothing.
            print("watching %s%s" % (watcher.save_path,
                                     "" if args.save else "   (auto, re-resolved each poll)"),
                  flush=True)
            print("serving  %s   (ctrl-c to stop)" % url, flush=True)
            # The pages come from somewhere else now, so whether that somewhere is up
            # is worth one probe at startup. Getting this wrong shows up as a blank
            # frame with no explanation anywhere -- the watcher would look broken while
            # reporting perfectly good state on /current.
            print("site     %s   (%s)" % (watcher.site, probe_site(watcher.site)),
                  flush=True)
            if hs_log:
                found = hs_log.current()["id"]
                print("sectors  %s   (%s)" % (
                    hs_log.log_path,
                    "reading %s" % found if found else
                    "no Sector: line yet — needs Hyperspace, and a sector generated "
                    "since the log was last truncated"), flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
