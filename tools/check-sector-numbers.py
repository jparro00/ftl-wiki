#!/usr/bin/env python3
"""Flag counts in sector copy that the sector data does not support.

    python tools/check-sector-numbers.py                 # every copy file
    python tools/check-sector-numbers.py engi-homeworlds

SECTOR-PAGE.md §5 rule 1 says every count in prose must match the data, and §10
notes the build cannot verify it: a stat tile's number is generated, but a sentence
saying "five events can kill a crew member" is just text. This closes that gap for
the two claim shapes that carry sector-wide counts:

    "<n> events …"      compared against every *_events metric
    "Label ×<n>"        compared against that gate's event count

Both are heuristics. A subset claim ("five of the eight events in this pool") is
legitimate and will be reported when its number is not a whole-sector metric, so
findings are candidates to check, not proven errors — which is why this exits 0
and prints rather than failing a build.

It exists because the extractor once missed quest-chain facts, and when that was
fixed fourteen sectors changed their counts while the pages still read the old ones.
"""

import argparse
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COPY_DIR = ROOT / "tools" / "sector-copy"
DATA_DIR = ROOT / "sectors" / "data"

WORDS = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
}

COUNT_METRICS = [
    "distinct_events", "always_fight_events", "may_fight_events", "crew_loss_events",
    "crew_gain_events", "boarder_events", "unique_events", "gated_events",
    "quest_start_events",
]

EVENT_CLAIM = re.compile(r"\b([\w-]+)\s+(?:of\s+the\s+[\w-]+\s+)?events?\b", re.IGNORECASE)
GATE_CLAIM = re.compile(r"([A-Za-z][A-Za-z \-]*?)\s*×(\d+)")


def number(word):
    word = word.lower()
    if word.isdigit():
        return int(word)
    if "-" in word:  # twenty-eight, forty-two
        parts = word.split("-")
        if len(parts) == 2 and all(p in WORDS for p in parts):
            return WORDS[parts[0]] + WORDS[parts[1]]
    return WORDS.get(word)


def strings(node, out):
    if isinstance(node, str):
        out.append(node)
    elif isinstance(node, dict):
        for key, value in node.items():
            if key != "metric":  # a metric id is not prose
                strings(value, out)
    elif isinstance(node, list):
        for value in node:
            strings(value, out)
    return out


def check(slug):
    copy_path = COPY_DIR / f"{slug}.json"
    data_path = DATA_DIR / f"{slug}.sector.json"
    if not copy_path.exists() or not data_path.exists():
        return [f"{slug}: missing copy or data file"]

    copy = json.loads(copy_path.read_text(encoding="utf-8"))
    data = json.loads(data_path.read_text(encoding="utf-8"))
    metrics = data["metrics"]
    gates = {g["label"]: len(g["events"]) for g in data["rollup"]["gates"]}
    allowed = {metrics[k] for k in COUNT_METRICS if k in metrics}

    prose = strings({k: v for k, v in copy.items() if k not in ("slug", "stats")}, [])
    findings = []
    for line in prose:
        for match in EVENT_CLAIM.finditer(line):
            value = number(match.group(1))
            if value is None or value < 2:
                continue
            if value not in allowed:
                findings.append(f'  count "{match.group(0)}" matches no sector metric '
                                f'— {line[:90]}…')
        for match in GATE_CLAIM.finditer(line):
            label, value = match.group(1).strip(), int(match.group(2))
            if label in gates and gates[label] != value:
                findings.append(f'  gate "{label} ×{value}" but the data says {gates[label]}')
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="sector slug (default: all copy files)")
    args = ap.parse_args()

    slugs = [args.slug] if args.slug else sorted(p.stem for p in COPY_DIR.glob("*.json"))
    total = 0
    for slug in slugs:
        findings = check(slug)
        if findings:
            total += len(findings)
            print(f"== {slug}")
            for finding in dict.fromkeys(findings):
                print(finding)
    print(f"\n{total} candidate(s) across {len(slugs)} sector(s). "
          "Subset claims are expected here — read each one.")


if __name__ == "__main__":
    main()
