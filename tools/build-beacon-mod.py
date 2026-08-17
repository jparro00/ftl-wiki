#!/usr/bin/env python3
"""Build the `beacon-reveal` FTL mod: name every beacon on the sector map.

    python tools/build-beacon-mod.py           # generate mods/beacon-reveal/src/
    python tools/build-beacon-mod.py --pack    # ... and zip it to beacon-reveal.ftl
    python tools/build-beacon-mod.py --verify  # re-check an already-generated tree

Requires FTL Hyperspace: the sector map is drawn by compiled code, so no vanilla
data mod can put text above a beacon. Hyperspace exposes `StarMap.locations` and each
`Location.event` to Lua, and `Location.event` reads fine on a beacon the player has
never visited -- which is the whole cheat. See
`raw/modding/2026-08-15-beacon-name-labels-mod.md` for the research this rests on.

Labels are the card titles from `cards/trees/*.tree.json`, the same source
`build-mod.py` uses for the in-event labels, so the map, the card and the event text
all say the same string. Nothing is hand-written per event.

The script is registered by editing Hyperspace's own `<scripts>` element in place with
Slipstream's Advanced XML rather than appending a second `<scripts>` block, because
hyperspace.xml documents that "only one `<scripts>` is allowed".
"""

import argparse
import json
import os
import pathlib
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TREES = ROOT / "cards" / "trees"
SECTORS = ROOT / "sectors" / "data"
TEMPLATE = ROOT / "tools" / "beacon-reveal.lua.tmpl"
MOD = ROOT / "mods" / "beacon-reveal"
SRC = MOD / "src"
# The only two values here that are about *this machine* rather than about the mod.
# Environment first, then a `--slipstream` / `--game` flag, then the paths this repo was
# built on -- so nothing changes for the machine it was written on and a clone needs no
# source edit. `FTL_DIR` is the name `mods/fullscreen-no-minimize/launch-ftl.cmd` already
# reads: one variable for the game directory, rather than two that can disagree.
#
# Only `--install` uses them. Building, packing and verifying touch neither, which is why
# a bare clone can build this mod (SETUP.md §0) and only fails at the point it would write
# to somebody's game.
DEFAULT_SLIPSTREAM = r"C:\Users\jparr\Documents\Slipstream"
DEFAULT_GAME = r"D:\Steam\steamapps\common\FTL Faster Than Light"

SLIPSTREAM = pathlib.Path(os.environ.get("SLIPSTREAM_DIR") or DEFAULT_SLIPSTREAM)
GAME = pathlib.Path(os.environ.get("FTL_DIR") or DEFAULT_GAME)

# Hyperspace must be patched first -- this mod adds a <script> to the <scripts>
# element Hyperspace itself defines, so that element has to exist already.
#
# `map-signal.ftl` rides along because --patch applies exactly what it is given and
# reverts everything else: omitting it here would silently uninstall it, and the only
# symptom would be the save watcher quietly going back to guessing which screen the
# player is on (SAVE-WATCH.md §5c).
PATCH_ORDER = ["Hyperspace.ftl", "event-labels.ftl", "map-signal.ftl", "beacon-reveal.ftl"]

LUA_NAME = "beacon-reveal.lua"

# Rendering constants, substituted into the template. ORIGIN is where beacon
# coordinate 0,0 is drawn; RISE lifts the label clear of the beacon icon.
#
# ORIGIN was *measured*, not taken from documentation. `starMap.position` is not
# exposed to Lua, and the xftl notes' 45,40 is wrong for this build -- it put every
# label 337 px left and 90 px above its beacon. The value below comes from pairing
# three beacons against their drawn labels on screen (exit beacon, abandoned station,
# giant alien spiders); all three agreed to within 1 px, which also proves the mapping
# is a pure translation with no scaling. See tools/BEACON-REVEAL.md §3.2.
# FONT is a font *id* from fonts.png in the Hyperspace zip, not a point size.
# 10 was too large for a map label -- its text overflowed the box. 6 is the small
# size the game's own STORE / EXIT tags are drawn at. GLYPH_H is only a fallback:
# the Lua measures the real line height from the font at runtime.
FONT, ORIGIN_X, ORIGIN_Y, RISE, GLYPH_H = 6, 382, 116, 14, 8

# The shared list that fills any beacon left over once a sector's table is exhausted
# (`OVERRIDE_NEUTRAL` under AE). Labelled by the generic name, which is what
# sector_data.xml, the sector pages and FTL_HS.log's own "Getting Event: NEUTRAL" all
# call it. Its section matches what section_of() gives every other NEUTRAL* pool, so
# fallback beacons are outlined like the neutral lines they resemble.
FALLBACK_POOL, FALLBACK_SECTION = "NEUTRAL", "neutral"

METADATA = """<?xml version="1.0" encoding="UTF-8"?>
<metadata>
\t<title><![CDATA[ Beacon Reveal ]]></title>
\t<threadUrl><![CDATA[ https://subsetgames.com/ftl_mods.html ]]></threadUrl>
\t<author><![CDATA[ generated from an FTL event wiki ]]></author>
\t<version><![CDATA[ 1.0 ]]></version>
\t<description>
<![CDATA[
Prints the name of every event on the sector map, above its beacon, whether or not
the beacon has been explored. A map spoiler, on purpose.

Requires FTL Hyperspace. Draws only - no event, choice, reward, ship or probability
is changed, and nothing is written to the save.

%d events are named, from the same card titles the Event Labels mod uses. An event
with no card shows its raw id rather than an invented name.
]]>
\t</description>
</metadata>
"""

# Advanced XML: add one <script> child to Hyperspace's existing <scripts> element.
APPEND = """<mod:findLike type="scripts">
\t<mod-append:script>data/%s</mod-append:script>
</mod:findLike>
""" % LUA_NAME


def ascii_fold(s):
    """FTL's bitmap fonts have no glyph for typographic punctuation."""
    swaps = {"—": "-", "–": "-", "‘": "'", "’": "'",
             "“": '"', "”": '"', "…": "...", " ": " "}
    s = "".join(swaps.get(c, c) for c in s)
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if ord(c) < 127)


def lua_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def load_labels():
    """event id -> card title, from the trees. Sorted, so builds are deterministic."""
    labels = {}
    for path in sorted(TREES.glob("*.tree.json")):
        tree = json.loads(path.read_text(encoding="utf-8"))
        eid, title = tree.get("id"), tree.get("title")
        if not eid or not title:
            continue
        folded = ascii_fold(title).strip()
        if not folded:
            continue
        if eid in labels and labels[eid] != folded:
            raise SystemExit("two titles for %s: %r vs %r" % (eid, labels[eid], folded))
        labels[eid] = folded
    if not labels:
        raise SystemExit("no labels found in %s" % TREES)
    return labels


def load_categories():
    """Per-sector event -> pool, from the sector-profile pipeline's own output.

    `sectors/data/*.sector.json` already expands each sector's `sector_data.xml`
    entries into their concrete events, so the category table is a projection of work
    `extract-sector.py` has done rather than a second parse of the game files.

    Three rules decide which pool an event is labelled with, in this order:

    1. **The nested list wins over the list that contains it.** A sector list can load
       another list wholesale -- `NEUTRAL_CIVILIAN` contains `<event load=
       "DISTRESS_BEACON"/>` -- and flattening makes every distress event a member of
       both. Ranking by sector order alone made `DISTRESS_BEACON` unreachable in
       Civilian Sector and Federation Space: all 14 of its events drew
       `NEUTRAL_CIVILIAN`, so an allocation line that genuinely rolls could never be
       named. `extract-sector.py` records the inner list as `via`, and that is
       preferred whenever it is itself one of *this* sector's allocation lines --
       which keeps every label inside the vocabulary of the sector page's budget
       table instead of inventing pool names the player has never seen.
    2. **AE additions count.** `entry["override"]["added"]` holds the events an
       `OVERRIDE_X` list adds to `X`. FTL_HS.log shows a Civilian Sector `ITEMS`
       allocation producing `STORE_REBELSIDE`, which exists only in `OVERRIDE_ITEMS`
       -- so AE does substitute, and an unmerged delta is a beacon the map cannot name.
    3. **Otherwise first pool in sector order wins.** Genuine cross-pool overlap that
       is not nesting stays ambiguous; the count is reported at build time so the
       number cannot drift unnoticed.

    The shared `NEUTRAL` fallback is appended last, after every real line, since a
    beacon only reaches it once the table is exhausted.
    """
    by_sector, sections, ambiguous, nested, ae_added = {}, {}, 0, 0, 0
    for path in sorted(SECTORS.glob("*.sector.json")):
        profile = json.loads(path.read_text(encoding="utf-8"))
        table = {}
        # Only this sector's own allocation lines are eligible as a `via` target.
        lines = {entry["name"] for entry in profile["entries"]}

        def put(eid, pool):
            nonlocal ambiguous
            if eid in table:
                if table[eid] != pool:
                    ambiguous += 1
                return                      # first pool in sector order wins
            table[eid] = pool

        for entry in profile["entries"]:
            pool = entry["name"]
            if entry.get("section"):
                sections[pool] = entry["section"]
            for event in entry["events"]:
                via = event.get("via")
                if via in lines and via != pool:
                    nested += 1
                    put(event["id"], via)
                else:
                    put(event["id"], pool)
            for event in entry.get("override", {}).get("added", []):
                ae_added += 1
                put(event["id"], pool)

        # The fallback list every sector reaches but almost none names. Last, so it
        # can never take an event away from a line that was actually allocated.
        fallback = profile["generation"].get("fallback_events") or []
        if fallback:
            sections.setdefault(FALLBACK_POOL, FALLBACK_SECTION)
            for event in fallback:
                put(event["id"], FALLBACK_POOL)

        by_sector[profile["display_name"]] = table

    # An event keeps a global category only where every sector agrees on it.
    seen = {}
    for table in by_sector.values():
        for eid, pool in table.items():
            if seen.setdefault(eid, pool) != pool:
                seen[eid] = None
    any_sector = {e: p for e, p in seen.items() if p}
    return by_sector, any_sector, sections, (ambiguous, nested, ae_added)


def render(labels, by_sector, any_sector, sections):
    template = TEMPLATE.read_text(encoding="utf-8")

    names = "\n".join(
        '    ["%s"] = "%s",' % (lua_escape(eid), lua_escape(title))
        for eid, title in sorted(labels.items()))

    sector_rows = []
    for sector, table in sorted(by_sector.items()):
        pairs = " ".join('["%s"]="%s",' % (lua_escape(e), lua_escape(p))
                         for e, p in sorted(table.items()))
        sector_rows.append('    ["%s"] = { %s },' % (lua_escape(sector), pairs))

    any_rows = "\n".join('    ["%s"] = "%s",' % (lua_escape(e), lua_escape(p))
                         for e, p in sorted(any_sector.items()))
    section_rows = "\n".join('    ["%s"] = "%s",' % (lua_escape(p), lua_escape(s))
                             for p, s in sorted(sections.items()))

    out = (template
           .replace("--%%NAMES%%", names)
           .replace("--%%BY_SECTOR%%", "\n".join(sector_rows))
           .replace("--%%ANY_SECTOR%%", any_rows)
           .replace("--%%SECTION%%", section_rows))
    for token, value in (("%%FONT%%", FONT), ("%%ORIGIN_X%%", ORIGIN_X),
                         ("%%ORIGIN_Y%%", ORIGIN_Y), ("%%RISE%%", RISE),
                         ("%%GLYPH_H%%", GLYPH_H), ("%%COUNT%%", len(labels)),
                         ("%%POOLS%%", len(any_sector))):
        out = out.replace(token, str(value))
    if "%%" in out:
        raise SystemExit("unsubstituted placeholder left in the rendered Lua")
    return out


def build():
    labels = load_labels()
    by_sector, any_sector, sections, (ambiguous, nested, ae_added) = load_categories()
    print("categories %d sectors, %d events with an unambiguous global pool, "
          "%d sector/event pairs in more than one pool (first wins)"
          % (len(by_sector), len(any_sector), ambiguous))
    print("           %d resolved to a nested list over its container, "
          "%d Advanced Edition additions merged" % (nested, ae_added))
    (SRC / "data").mkdir(parents=True, exist_ok=True)
    (SRC / "mod-appendix").mkdir(parents=True, exist_ok=True)
    (SRC / "data" / LUA_NAME).write_text(
        render(labels, by_sector, any_sector, sections), encoding="utf-8", newline="\n")
    (SRC / "data" / "hyperspace.xml.append").write_text(APPEND, encoding="utf-8", newline="\n")
    (SRC / "mod-appendix" / "metadata.xml").write_text(
        METADATA % len(labels), encoding="utf-8", newline="\n")
    return labels


def verify(labels):
    """Every check that can be made without launching the game."""
    problems = []
    lua = (SRC / "data" / LUA_NAME).read_text(encoding="utf-8")
    append = (SRC / "data" / "hyperspace.xml.append").read_text(encoding="utf-8")
    meta = (SRC / "mod-appendix" / "metadata.xml").read_text(encoding="utf-8")

    # A glyph the game cannot render, anywhere in the Lua.
    for i, ch in enumerate(lua):
        if ord(ch) > 0x7E:
            problems.append("non-ASCII byte %r at offset %d of the Lua" % (ch, i))
            break

    # Every label actually reached the file.
    missing = [e for e in labels if '["%s"]' % lua_escape(e) not in lua]
    if missing:
        problems.append("%d labels missing from the Lua, e.g. %s" % (len(missing), missing[:3]))

    # Balanced table and one registration.
    if lua.count("script.on_render_event") != 1:
        problems.append("expected exactly one render-event registration")
    if "%%" in lua:
        problems.append("unsubstituted placeholder in the Lua")

    # The category tables must actually be populated, and every sector present.
    by_sector, any_sector, sections, _ = load_categories()
    for sector in by_sector:
        if '["%s"] = {' % lua_escape(sector) not in lua:
            problems.append("sector %r missing from BY_SECTOR" % sector)
    if not any_sector or not sections:
        problems.append("category tables are empty")

    # No allocation line may be unreachable. A line whose every event resolves to some
    # other pool is a category that can never be drawn however the sector rolls -- the
    # map then silently reports a line that did roll under another line's name. That
    # was true of DISTRESS_BEACON in Civilian Sector and Federation Space (14 of 14
    # events drawn as NEUTRAL_CIVILIAN) and nothing in the build said so.
    for path in sorted(SECTORS.glob("*.sector.json")):
        profile = json.loads(path.read_text(encoding="utf-8"))
        drawn = set(by_sector[profile["display_name"]].values())
        for entry in profile["entries"]:
            if entry["events"] and entry["name"] not in drawn:
                problems.append(
                    "%s: allocation line %s can never be drawn -- all %d of its events "
                    "resolve to another pool"
                    % (profile["display_name"], entry["name"], len(entry["events"])))

    # A category must be a real pool name, never a card title -- the two are easy to
    # cross-wire in the template and the mix-up would only show on the map.
    titles = set(labels.values())
    for pool in sections:
        if pool in titles:
            problems.append("pool %r collides with a card title" % pool)

    # Drawing primitives the boxes depend on.
    for call in ("GL_DrawRect", "GL_DrawRectOutline", "easy_measureWidth"):
        if call not in lua:
            problems.append("missing %s -- the boxed label cannot render" % call)

    # The append must parse, must carry no <FTL> wrapper, and must edit <scripts>
    # in place rather than declare a second one.
    if "<FTL" in append:
        problems.append("append carries its own <FTL> wrapper; Slipstream adds it")
    if re.search(r"<scripts[ >/]", append):
        problems.append("append declares its own <scripts>; hyperspace.xml allows only one")
    if "mod-append:script" not in append or "mod:findLike" not in append:
        problems.append("append does not add a <script> to the existing <scripts>")
    try:
        ET.fromstring(
            '<wrap xmlns:mod="urn:mod" xmlns:mod-append="urn:mod-append">%s</wrap>' % append)
    except ET.ParseError as exc:
        problems.append("append is not well-formed XML: %s" % exc)

    # Slipstream's metadata reader is strict: five elements, none empty, or the mod
    # is rejected outright and never appears in the list.
    try:
        root = ET.fromstring(meta)
        for tag in ("title", "threadUrl", "author", "version", "description"):
            el = root.find(tag)
            if el is None or not (el.text or "").strip():
                problems.append("metadata.xml: <%s> missing or empty" % tag)
    except ET.ParseError as exc:
        problems.append("metadata.xml is not well-formed: %s" % exc)

    return problems


def pack():
    MOD.mkdir(parents=True, exist_ok=True)
    out = MOD / "beacon-reveal.ftl"
    files = sorted(p for p in SRC.rglob("*") if p.is_file())
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for path in files:
            # Fixed timestamps keep the archive byte-identical between builds.
            info = zipfile.ZipInfo(str(path.relative_to(SRC)).replace("\\", "/"),
                                   date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, path.read_bytes())
    return out


def check_paths():
    """Both machine paths, checked before anything is copied or patched.

    Checked by a file that has to be *inside* each directory rather than by the directory
    existing: a plausible-but-wrong path is the likely mistake, and `cwd=SLIPSTREAM` on a
    directory with no `modman.jar` fails several steps later as a Java error about a
    missing jar, which reads as a broken toolchain rather than as a wrong path.

    The message names the environment variable, because that is the fix that survives the
    next `git pull`.
    """
    problems = []
    if not (SLIPSTREAM / "modman.jar").is_file():
        problems.append("no modman.jar in %s\n"
                        "  set SLIPSTREAM_DIR, or pass --slipstream <dir>" % SLIPSTREAM)
    if not (GAME / "ftl.dat").is_file():
        problems.append("no ftl.dat in %s\n"
                        "  set FTL_DIR, or pass --game <dir>" % GAME)
    if problems:
        raise SystemExit("\n".join(problems))


def install():
    """Copy the .ftl to Slipstream and patch it into the game.

    This exists because a rebuilt .ftl that is never patched in is invisible: the game
    keeps running the previous build, and the only symptom is that the fix "didn't
    work". Packing and installing in one command removes the gap. Requires FTL closed;
    Slipstream cannot rewrite ftl.dat safely underneath a running game.
    """
    import shutil
    import subprocess

    ftl = MOD / "beacon-reveal.ftl"
    if not ftl.exists():
        raise SystemExit("no beacon-reveal.ftl -- run with --pack first")
    check_paths()
    shutil.copy2(ftl, SLIPSTREAM / "mods" / ftl.name)

    result = subprocess.run(
        ["java", "-jar", "modman.jar", "--patch"] + PATCH_ORDER,
        cwd=SLIPSTREAM, capture_output=True, text=True)
    tail = (result.stdout + result.stderr).strip().splitlines()[-3:]
    for line in tail:
        print("         %s" % line.strip())
    if result.returncode != 0:
        raise SystemExit("slipstream patch failed (exit %d)" % result.returncode)
    dat = GAME / "ftl.dat"
    print("patched  %s at %s"
          % (dat, __import__("datetime").datetime.fromtimestamp(
              dat.stat().st_mtime).strftime("%H:%M:%S")))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pack", action="store_true", help="zip src/ into beacon-reveal.ftl")
    ap.add_argument("--verify", action="store_true", help="check an existing tree, no rebuild")
    ap.add_argument("--install", action="store_true",
                    help="--pack, then copy to Slipstream and patch the game (FTL must be closed)")
    ap.add_argument("--slipstream", metavar="DIR",
                    help="Slipstream Mod Manager directory, the one holding modman.jar "
                         "(default: $SLIPSTREAM_DIR, else %s)" % DEFAULT_SLIPSTREAM)
    ap.add_argument("--game", metavar="DIR",
                    help="FTL install directory, the one holding ftl.dat "
                         "(default: $FTL_DIR, else %s)" % DEFAULT_GAME)
    args = ap.parse_args()

    global SLIPSTREAM, GAME
    if args.slipstream:
        SLIPSTREAM = pathlib.Path(args.slipstream)
    if args.game:
        GAME = pathlib.Path(args.game)
    if args.install:
        args.pack = True

    labels = load_labels()
    if not args.verify:
        build()
        print("built    %s  (%d labels)" % (SRC, len(labels)))

    problems = verify(labels)
    for p in problems:
        print("FAIL     %s" % p)
    if problems:
        return 1
    print("verified %d labels, metadata, and the hyperspace.xml patch" % len(labels))

    if args.pack:
        out = pack()
        print("packed   %s  (%d bytes)" % (out, out.stat().st_size))
    if args.install:
        install()
    return 0


if __name__ == "__main__":
    sys.exit(main())
