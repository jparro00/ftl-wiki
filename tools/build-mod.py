#!/usr/bin/env python3
"""Build the `event-labels` FTL mod: stamp every carded event with its card title.

    python tools/build-mod.py            # generate mods/event-labels/src/
    python tools/build-mod.py --pack     # ... and zip it to event-labels.ftl
    python tools/build-mod.py --verify   # re-check an already-generated tree

Input is `cards/trees/*.tree.json` — the `title` field is the label, and `id` +
`source` locate the event's definition in `raw/gamedata/`. Nothing is hand-written
per event; see `tools/EVENT-LABELS.md` for the contract.

Two emission mechanisms, chosen per event to keep the footprint minimal. Both rest
only on the plain append convention ("reuse an identical tag name, last one counts");
neither uses Slipstream's Advanced XML.

  STRING   the event's text resolves to a `<text name=…>` used by exactly one event,
           so relabelling the string relabels only that event. Emitted into
           `text_events.xml.append`. Touches no structure — this is the common case.

  EVENT    anything else (shared string, shared textList, or prose inlined in the
           event). The event definition is copied verbatim from the vanilla file and
           re-emitted with only its own `<text>` element rewritten. A shared textList
           becomes a new per-event list under a namespaced name, so the vanilla list
           is left alone and the other events using it keep their own labels.
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
GAMEDATA = ROOT / "raw" / "gamedata"
MOD = ROOT / "mods" / "event-labels"
SRC = MOD / "src"

# Event-bearing files. text_*.xml hold strings, not definitions, and are handled
# separately; events_imageList.xml holds background art pools only.
EVENT_FILES = [
    "events.xml", "newEvents.xml", "events_boss.xml", "events_crystal.xml",
    "events_engi.xml", "events_fuel.xml", "events_mantis.xml", "events_nebula.xml",
    "events_pirate.xml", "events_rebel.xml", "events_rock.xml", "events_ships.xml",
    "events_slug.xml", "events_zoltan.xml", "dlcEvents.xml", "dlcEvents_anaerobic.xml",
    "dlcEventsOverwrite.xml", "nameEvents.xml", "bosses.xml",
]
TEXT_FILES = ["text_events.xml", "text_misc.xml"]

LABEL_OPEN, LABEL_CLOSE, LABEL_GAP = "[ ", " ]", "\n\n"
NAMESPACE = "EVLBL_"          # prefix for every name this mod introduces

TAG_RE = re.compile(
    r"<!--.*?-->|<\?.*?\?>|<!\[CDATA\[.*?\]\]>"
    r"|<(/?)([A-Za-z_][\w:.-]*)((?:'[^']*'|\"[^\"]*\"|[^'\">])*?)(/?)>",
    re.S,
)
ATTR_RE = re.compile(r"([\w:.-]+)\s*=\s*(?:\"([^\"]*)\"|'([^']*)')")
BARE_AMP_RE = re.compile(r"&(?!(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z][\w.-]*);)")


# --------------------------------------------------------------------------- XML

def attrs_of(blob):
    out = {}
    for m in ATTR_RE.finditer(blob or ""):
        out[m.group(1)] = m.group(2) if m.group(2) is not None else m.group(3)
    return out


def elements(text):
    """Every element in `text`, with source spans. Depth 0 is the outermost tag.

    Hand-rolled rather than ET-based because these files are only nearly-XML (bare
    ampersands, stray declarations) and because the spans have to be exact: an event
    is re-emitted by copying its own bytes, not by re-serializing a parse tree.
    """
    out, stack = [], []
    for m in TAG_RE.finditer(text):
        if m.group(2) is None:          # comment / PI / CDATA
            continue
        closing, tag, blob, selfclose = m.groups()
        if closing:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i]["tag"] == tag:
                    el = stack[i]
                    del stack[i:]
                    el["inner_end"], el["end"] = m.start(), m.end()
                    out.append(el)
                    break
        elif selfclose:
            out.append({"tag": tag, "attrs": attrs_of(blob), "depth": len(stack),
                        "start": m.start(), "end": m.end(),
                        "inner_start": None, "inner_end": None})
        else:
            stack.append({"tag": tag, "attrs": attrs_of(blob), "depth": len(stack),
                          "start": m.start(), "inner_start": m.end()})
    out.extend(el for el in stack if el.setdefault("end", None))   # unclosed: dropped
    return out


def root_depth(els):
    """Definitions sit inside the files' own <FTL> wrapper where one is present."""
    return 1 if any(e["tag"] == "FTL" and e["depth"] == 0 for e in els) else 0


def inner(text, el):
    if el["inner_start"] is None:
        return ""
    return text[el["inner_start"]:el["inner_end"]]


def esc_text(s):
    """Escape for element content, preserving entities the vanilla files already use."""
    return BARE_AMP_RE.sub("&amp;", s).replace("<", "&lt;").replace(">", "&gt;")


def esc_attr(s):
    return esc_text(s).replace('"', "&quot;")


def ascii_fold(s):
    """FTL's bitmap fonts have no glyph for typographic punctuation."""
    swaps = {"—": "-", "–": "-", "‘": "'", "’": "'",
             "“": '"', "”": '"', "…": "...", " ": " "}
    s = "".join(swaps.get(c, c) for c in s)
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if ord(c) < 127)


# ------------------------------------------------------------------------ loading

def load_game():
    files, index = {}, {"event": {}, "textList": {}}
    for name in EVENT_FILES:
        path = GAMEDATA / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        els = elements(text)
        rd = root_depth(els)
        files[name] = {"text": text, "elements": els, "root_depth": rd}
        for el in els:
            if el["tag"] in index and el["depth"] == rd and "name" in el["attrs"]:
                # A <event name=…/> inside an <eventList> is a reference, not a
                # definition; the depth test is what separates the two. Later
                # definitions in the same file win, matching the engine.
                index[el["tag"]][el["attrs"]["name"]] = (name, el)
    return files, index


def load_strings():
    """name -> (file, verbatim inner content) for every <text name=…> string."""
    table = {}
    for name in TEXT_FILES:
        path = GAMEDATA / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for el in elements(text):
            if el["tag"] == "text" and "name" in el["attrs"]:
                table[el["attrs"]["name"]] = (name, inner(text, el))
    return table


def load_labels():
    labels = []
    for path in sorted(TREES.glob("*.tree.json")):
        tree = json.loads(path.read_text(encoding="utf-8"))
        labels.append({"id": tree["id"], "title": ascii_fold(tree["title"]),
                       "source": os.path.basename(tree["source"])})
    return labels


def count_refs(files):
    """How many places reference each text id / textList name, game-wide."""
    ids, loads = {}, {}
    for f in files.values():
        for el in f["elements"]:
            if el["tag"] != "text":
                continue
            if "id" in el["attrs"]:
                ids[el["attrs"]["id"]] = ids.get(el["attrs"]["id"], 0) + 1
            if "load" in el["attrs"]:
                loads[el["attrs"]["load"]] = loads.get(el["attrs"]["load"], 0) + 1
    return ids, loads


# -------------------------------------------------------------------------- build

class Build:
    def __init__(self):
        self.appends = {}                    # filename -> [chunk, ...]
        self.stats = {"string": 0, "event": 0, "skipped": 0}
        self.skipped, self.notes = [], []

    def add(self, filename, chunk):
        self.appends.setdefault(filename, []).append(chunk)


def own_text_element(text, ev_el):
    """The event's own <text>, not one belonging to a nested <choice>."""
    slice_ = text[ev_el["start"]:ev_el["end"]]
    for el in sorted(elements(slice_), key=lambda e: e["start"]):
        if el["tag"] == "text" and el["depth"] == 1:
            return slice_, el
    return slice_, None


def variants_of(list_text, list_el, strings):
    """Resolve a <textList>'s children to (ref-or-None, verbatim string) pairs."""
    out = []
    slice_ = list_text[list_el["start"]:list_el["end"]]
    for el in sorted(elements(slice_), key=lambda e: e["start"]):
        if el["tag"] != "text" or el["depth"] != 1:
            continue
        ref = el["attrs"].get("id")
        if ref:
            if ref not in strings:
                return None
            out.append((ref, strings[ref][1]))
        else:
            out.append((None, inner(slice_, el)))
    return out or None


def build():
    files, index = load_game()
    strings = load_strings()
    labels = load_labels()
    id_refs, load_refs = count_refs(files)
    b = Build()

    for rec in labels:
        eid, title, source = rec["id"], rec["title"], rec["source"]
        prefix = LABEL_OPEN + esc_text(title) + LABEL_CLOSE + LABEL_GAP

        if eid not in index["event"]:
            b.skipped.append((eid, "no top-level definition found")); b.stats["skipped"] += 1
            continue
        ev_file, ev_el = index["event"][eid]
        ev_text = files[ev_file]["text"]
        slice_, text_el = own_text_element(ev_text, ev_el)
        if text_el is None:
            b.skipped.append((eid, "event has no text element")); b.stats["skipped"] += 1
            continue

        ref, load = text_el["attrs"].get("id"), text_el["attrs"].get("load")

        # --- STRING: a string only this event can reach ------------------------
        if ref and id_refs.get(ref, 0) == 1 and ref in strings:
            sfile, body = strings[ref]
            b.add(sfile, '<text name="%s">%s%s</text>' % (esc_attr(ref), prefix, body))
            b.stats["string"] += 1
            continue

        if load and load_refs.get(load, 0) == 1 and load in index["textList"]:
            lfile, list_el = index["textList"][load]
            parts = variants_of(files[lfile]["text"], list_el, strings)
            if parts and all(r and id_refs.get(r, 0) == 1 for r, _ in parts):
                for vref, body in parts:
                    sfile = strings[vref][0]
                    b.add(sfile,
                          '<text name="%s">%s%s</text>' % (esc_attr(vref), prefix, body))
                b.stats["string"] += 1
                continue

        # --- EVENT: redefine, rewriting only this event's own <text> -----------
        replacement = None
        if load and load in index["textList"]:
            lfile, list_el = index["textList"][load]
            parts = variants_of(files[lfile]["text"], list_el, strings)
            if parts:
                new_name = NAMESPACE + eid
                attrs = dict(index["textList"][load][1]["attrs"])
                extra = "".join(' %s="%s"' % (k, esc_attr(v))
                                for k, v in sorted(attrs.items()) if k != "name")
                body = "".join("\n\t<text>%s%s</text>" % (prefix, v) for _, v in parts)
                b.add(ev_file, '<textList name="%s"%s>%s\n</textList>'
                               % (esc_attr(new_name), extra, body))
                replacement = '<text load="%s"/>' % esc_attr(new_name)
        if replacement is None:
            if ref:
                if ref not in strings:
                    b.skipped.append((eid, "unresolved text id %s" % ref))
                    b.stats["skipped"] += 1
                    continue
                body = strings[ref][1]
            else:
                body = inner(slice_, text_el)
            replacement = "<text>%s%s</text>" % (prefix, body)

        rewritten = (slice_[:text_el["start"]] + replacement + slice_[text_el["end"]:])
        b.add(ev_file, BARE_AMP_RE.sub("&amp;", rewritten))
        b.stats["event"] += 1

    return b, labels


HEADER = (
    "<!-- event-labels: generated by tools/build-mod.py from cards/trees/*.tree.json.\n"
    "     Do not hand-edit. Appended to vanilla {name}; last definition wins. -->\n"
)


def write_tree(b):
    data = SRC / "data"
    if SRC.exists():
        for path in sorted(SRC.rglob("*"), reverse=True):
            path.unlink() if path.is_file() else path.rmdir()
    data.mkdir(parents=True, exist_ok=True)

    for name in sorted(b.appends):
        out = data / (name + ".append")
        out.write_text(HEADER.format(name=name) + "\n"
                       + "\n\n".join(b.appends[name]) + "\n", encoding="utf-8")

    appendix = SRC / "mod-appendix"
    appendix.mkdir(parents=True, exist_ok=True)
    # Slipstream parses this strictly and rejects the mod outright on a missing or
    # empty element — threadUrl included, even though no forum thread exists for a
    # locally built mod. CDATA matches the format of the example mods it ships with.
    (appendix / "metadata.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<metadata>\n"
        "\t<title><![CDATA[ Event Labels ]]></title>\n"
        "\t<threadUrl><![CDATA[ https://subsetgames.com/ftl_mods.html ]]></threadUrl>\n"
        "\t<author><![CDATA[ generated from an FTL event wiki ]]></author>\n"
        "\t<version><![CDATA[ 1.0 ]]></version>\n"
        "\t<description>\n<![CDATA[\n"
        "Prints the name of each event above its text, so you always know which\n"
        "encounter you are looking at. 386 events are labelled.\n\n"
        "Text only - no choice, requirement, reward, ship or probability is changed.\n\n"
        "Compatibility:\n"
        "- Built against FTL 1.6.x data.\n"
        "- 351 events are relabelled by replacing a string only that event uses, which\n"
        "  leaves every event definition untouched.\n"
        "- 35 events are redefined outright, and will clobber another mod that redefines\n"
        "  the same event (or be clobbered by it, depending on patch order).\n"
        "]]>\n\t</description>\n"
        "</metadata>\n", encoding="utf-8")


# ------------------------------------------------------------------------- verify

def verify(labels):
    """Parse every append and prove the labels landed, once each, ASCII-only."""
    problems, seen = [], {}
    data = SRC / "data"
    if not data.exists():
        return ["no generated tree at %s" % data]

    for path in sorted(data.glob("*.append")):
        raw = path.read_text(encoding="utf-8")
        vanilla = GAMEDATA / path.name[: -len(".append")]
        if not vanilla.exists():
            problems.append("%s appends to a file not in raw/gamedata/" % path.name)
        try:
            ET.fromstring("<FTL>" + raw + "</FTL>")
        except ET.ParseError as exc:
            problems.append("%s does not parse: %s" % (path.name, exc))
        for i, ch in enumerate(raw):
            if ord(ch) > 126:
                problems.append("%s: non-ASCII %r at offset %d" % (path.name, ch, i))
                break
        if "<FTL>" in raw:
            problems.append("%s carries an <FTL> wrapper (Slipstream adds it)" % path.name)
        for m in re.finditer(re.escape(LABEL_OPEN) + r"(.*?)" + re.escape(LABEL_CLOSE), raw):
            seen[m.group(1)] = seen.get(m.group(1), 0) + 1

    for rec in labels:
        if rec["title"] not in seen:
            problems.append("label never emitted: %s (%s)" % (rec["title"], rec["id"]))

    problems += verify_redefinitions()
    problems += verify_single_label()
    problems += verify_metadata()

    # Every name this mod defines must either exist in vanilla (a deliberate
    # override) or carry the mod's namespace (a deliberate addition).
    vanilla_names = set()
    for name in EVENT_FILES + TEXT_FILES:
        path = GAMEDATA / name
        if path.exists():
            vanilla_names |= set(re.findall(r'name="([^"]+)"',
                                            path.read_text(encoding="utf-8", errors="replace")))
    for path in sorted(data.glob("*.append")):
        for name in re.findall(r'name="([^"]+)"', path.read_text(encoding="utf-8")):
            if name not in vanilla_names and not name.startswith(NAMESPACE):
                problems.append("%s: defines unknown name %s" % (path.name, name))
    return problems


def verify_metadata():
    """Slipstream's JDOMModMetadataReader parses this strictly and refuses to list
    the mod if any element is missing or empty — `Missing threadUrl.` is what an
    empty <threadUrl/> earns you, and the mod silently never appears."""
    path = SRC / "mod-appendix" / "metadata.xml"
    if not path.exists():
        return ["mod-appendix/metadata.xml is missing"]
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        return ["metadata.xml does not parse: %s" % exc]
    problems = []
    for field in ("title", "threadUrl", "author", "version", "description"):
        el = root.find(field)
        if el is None:
            problems.append("metadata.xml: missing <%s>" % field)
        elif not (el.text or "").strip():
            problems.append("metadata.xml: <%s> is empty" % field)
    return problems


def verify_redefinitions():
    """A redefined event must match its vanilla definition byte for byte, apart
    from its own <text> element. This is the check that guards the risky path:
    a copy that silently loses a <choice> would still parse and still show the
    label, and would only surface as a missing option mid-run."""
    problems = []
    files, index = load_game()
    for path in sorted((SRC / "data").glob("*.append")):
        raw = path.read_text(encoding="utf-8")
        for el in elements(raw):
            if el["tag"] != "event" or "name" not in el["attrs"]:
                continue
            name = el["attrs"]["name"]
            if name not in index["event"]:
                problems.append("%s: redefines unknown event %s" % (path.name, name))
                continue
            ev_file, ev_el = index["event"][name]
            vanilla = files[ev_file]["text"][ev_el["start"]:ev_el["end"]]
            mine = raw[el["start"]:el["end"]]
            stripped = []
            for blob in (vanilla, mine):
                _, text_el = own_text_element(blob, {"start": 0, "end": len(blob)})
                if text_el is None:
                    stripped.append(None)
                else:
                    stripped.append(blob[:text_el["start"]] + blob[text_el["end"]:])
            van, got = stripped
            if van is None or got is None:
                problems.append("%s: %s lost its text element" % (path.name, name))
            elif BARE_AMP_RE.sub("&amp;", van) != got:
                problems.append("%s: %s differs from vanilla outside its <text>"
                                % (path.name, name))
    return problems


def verify_single_label():
    """No string may carry two labels — the symptom of a double-prefixed rebuild."""
    problems = []
    marker = re.escape(LABEL_OPEN) + r".*?" + re.escape(LABEL_CLOSE)
    for path in sorted((SRC / "data").glob("*.append")):
        raw = path.read_text(encoding="utf-8")
        for el in elements(raw):
            if el["tag"] != "text":
                continue
            body = inner(raw, el)
            if len(re.findall(marker, body, re.S)) > 1:
                problems.append("%s: %s carries more than one label"
                                % (path.name, el["attrs"].get("name", "?")))
    return problems


def pack():
    """A .ftl is a renamed .zip. Written with zipfile, not Compress-Archive, which
    can emit backslash separators that Slipstream (Java) reads as flat filenames."""
    target = MOD / "event-labels.ftl"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SRC.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(SRC).as_posix())
    return target


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", action="store_true", help="also zip to .ftl")
    ap.add_argument("--verify", action="store_true", help="verify only, do not rebuild")
    args = ap.parse_args()

    labels = load_labels()
    if not args.verify:
        b, labels = build()
        write_tree(b)
        print("labelled %d events: %d via string override, %d via event redefinition"
              % (b.stats["string"] + b.stats["event"], b.stats["string"], b.stats["event"]))
        if b.skipped:
            print("skipped %d:" % len(b.skipped))
            for eid, why in b.skipped:
                print("   %-34s %s" % (eid, why))
        for name in sorted(b.appends):
            print("   data/%s.append  (%d chunks)" % (name, len(b.appends[name])))

    problems = verify(labels)
    if problems:
        print("\nVERIFY FAILED (%d)" % len(problems))
        for p in problems[:40]:
            print("   " + p)
        return 1
    print("\nverify ok: %d labels, all appends parse, ASCII only, no stray names"
          % len(labels))

    if args.pack:
        target = pack()
        print("packed %s (%d bytes)" % (target.relative_to(ROOT), target.stat().st_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
