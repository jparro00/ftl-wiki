# Setup — for the agent

You are setting this repository up on a machine that is not the one it was written on.
This file tells you what already works, what does not, and exactly which facts are baked
into the source as somebody else's paths.

Read this before `README.md`. `README.md` is an operator's guide and assumes the
environment already exists; this is how the environment comes to exist.

**The short version:** the wiki, the 386 event cards, the 19 sector profiles, the local
site and the save watcher all work from a bare `git clone` with **nothing installed**.
Everything that does not work needs one of exactly three things — the game's own data
files, Hyperspace, or Slipstream — and this file says which.

---

## 0. What you get from a bare clone

Verified by cloning the public repo into an empty directory and running each command.
No installs, no configuration, no edits:

```bash
python tools/serve-site.py --check       # routes 418 · sectors 19 · cards 386 → ok
python tools/build-pages.py              # 408 pages, 405 stubs, 4528 refs → ok
python tools/build-map-signal-mod.py     # built + verified
python tools/save-watch.py --once        # resolved a live event
python tools/save-watch.py --index-report  # 386 cards, 3448 text keys
```

That is the whole read-and-serve half of the project. **Nothing here is generated at
setup time** — `cards/`, `sectors/`, `cards/trees/` and `sectors/data/` are committed
build output, which is why a clone has a working site before it has a game.

> ⚠️ **One caveat on that last pair.** `save-watch.py` was verified on a machine that
> already had FTL installed, Hyperspace running, and a live save on disk. The *clone*
> needed no setup; the *game* was already there. §3 is about getting the game there.

### Python

Stdlib only. Every `tools/*.py` imports nothing outside the standard library — no
`requirements.txt`, no virtualenv, nothing to `pip install`. Developed against
**Python 3.10**.

Two optional extras, each used by one verification tool and nothing else:

| Needed by | Install | Without it |
|---|---|---|
| `tools/smoke-inline.py` | `pip install playwright && python -m playwright install firefox` | that one smoke test exits with the install line; everything else is unaffected |
| `tools/smoke-card.js` | Node (developed against v24) | same |

---

## 1. Work out what the user actually wants

Do this before installing anything. The four tiers are independent and each is useful
alone. Do not walk the user through Hyperspace because they asked to read a sector page.

| They want | Tier | Needs |
|---|---|---|
| Read the cards and sector profiles, ask questions of the wiki | **1** | nothing |
| The watcher opening cards by itself while they play | **2** | FTL installed |
| Sector names, `?seen=`, `?beacons=`, the star-map signal | **3** | Hyperspace + Slipstream |
| Rebuild a card, a sector profile, or an event-labels mod | **4** | `raw/gamedata/*.xml` |

Tier 4 is orthogonal — it is about *changing* content, not running anything. A user who
only reads never needs it.

---

## 2. Tier 1 — the pages

Two ways to read them. **The first needs nothing running at all**, which also makes it the
simplest thing to point the watcher at (§3).

### Hosted — nothing to start

<https://jparro00.github.io/ftl-wiki/>

This repository's own output, published to GitHub Pages. All 19 sector profiles, all 386
cards, both indexes, and the beacon boxes still open onto cards in place.

It is frozen at whenever somebody last deployed, so a card you rebuild locally will not
appear there until it is republished. To publish your own copy:

```bash
python tools/build-pages.py --deploy     # → the gh-pages branch of your origin remote
```

`owner/name` is read from `git remote get-url origin`, so a fork publishes to its own Pages
URL with no edit (§6). Spec: `tools/LOCAL-SITE.md` §10.

### Local — the same pages, live

```bash
python tools/serve-site.py --check       # resolves every route in-process, starts nothing
python tools/serve-site.py --open        # http://127.0.0.1:8080
```

**`serve-site.py` without `--check` or `--routes` never returns.** Launch it backgrounded.
A foreground call blocks until your tool times out and tells you nothing.

Worth the extra process when you are *changing* content: pages are read from disk per
request, so a rebuilt card shows up on the next reload with no restart. Spec:
`tools/LOCAL-SITE.md`.

---

## 3. Tier 2 — the save watcher

The watcher reads the game's save and works out which event is on screen.

```bash
python tools/save-watch.py --once        # parse once, print JSON, exit — always start here

# then one of:
python tools/save-watch.py --site https://jparro00.github.io/ftl-wiki   # hosted: nothing else to run
python tools/save-watch.py --site http://127.0.0.1:8080                 # local: start serve-site.py first
```

`--once` is the diagnostic: it starts no server and tells you whether the whole resolution
chain works on this machine. Only start the server after it answers.

**Nothing needs configuring if FTL is installed normally.** The watcher discovers
everything:

| | how |
|---|---|
| the save | `%USERPROFILE%\Documents\My Games\FasterThanLight` and `%APPDATA%\FasterThanLight`, trying `continue.sav` and `hs_continue.sav`, newest wins |
| `ftl.dat` | a candidate list including the Steam default and `C:\Program Files (x86)\...` |
| `FTL_HS.log` | derived — Hyperspace writes it beside `ftl.dat` |

Override any of them with `--save`, `--ftl-dat`, `--hs-log` if the install is somewhere
unusual. Prefer the flags to editing source.

**The watcher serves no pages.** It computes a URL and points an iframe at whatever
`--site` names. It probes that at startup and prints `reachable`, or says it is not:

```
serving  http://127.0.0.1:8787/   (ctrl-c to stop)
site     https://jparro00.github.io/ftl-wiki   (reachable)
```

### Pointing it at the hosted site

**Nothing in the watcher needs changing for this** — verified end to end against the live
Pages site. It works because the watcher never *resolves* URLs, it concatenates them:
`_url()` returns a path, `--site` keeps whatever you gave it including a `/<repo>` prefix,
and the shell composes `site + url`. The prefix survives.

```
site:      https://jparro00.github.io/ftl-wiki
url:       /cards/pirate-engine-hacker
composed:  https://jparro00.github.io/ftl-wiki/cards/pirate-engine-hacker   → 200
```

Every shape it builds resolves, including `?seen=` and `?beacons=` on a sector profile and
`?pick=` on the chooser. Two things that had to be true and are: `github.io` sends **no
`X-Frame-Options`** and no `frame-ancestors` CSP on Pages content, so the shell can frame
it; and Pages tries the `.html` extension for an extensionless path, so the watcher's
`/sectors/<slug>` resolves without it having to know about the export's filenames.

Two consequences, neither fatal:

- **Latency.** Every swap is a round trip to GitHub instead of to localhost, and each card
  payload is fetched per box. Fine on a second monitor; worse than local.
- **It goes stale.** The hosted copy is whatever was last deployed. Rebuild a card and the
  watcher keeps showing the old one until `build-pages.py --deploy` runs, plus ~30 seconds
  for the Pages build.

So: **hosted for playing, local for working.** If you are only reading, the hosted site
means one process instead of two.

Ports, neither started automatically: **8787** is the watcher, always. **8080** is the local
site, and is only needed if `--site` points at it. If a page will not load, check what
`--site` names is actually up before looking anywhere else.

Spec: `tools/SAVE-WATCH.md`. `nosave`, `ambiguous` and `nocard` are defined outcomes, not
faults; only a persistent `error` is worth investigating.

---

## 4. Tier 3 — Hyperspace and Slipstream

Only needed for what the save file cannot answer. Without them the watcher still resolves
events from the save; it loses the sector, `?seen=`, `?beacons=`, and the star-map signal,
and can run an event behind on events a hidden choice chains into.

### What each piece is

| | what | where it comes from |
|---|---|---|
| **Hyperspace** | a mod engine that adds Lua scripting and writes `FTL_HS.log` | <https://ftl-hyperspace.github.io/FTL-Hyperspace/> — **not in this repo**, ~10 MB |
| **Slipstream** | the mod manager that patches `.ftl` files into the game | Vhati's Slipstream Mod Manager; needs **Java** (developed against Slipstream 1.9.1 + Java 8) |

**Hyperspace runs on FTL 1.6.9 only**, and its installer downgrades 1.6.14 for you.
Install it per its own guide — this repo does not automate it and you should not try to.
Note that *uninstalling* Hyperspace requires deleting `Hyperspace.dll`; removing the mod
in Slipstream is not enough.

### The two mods here that need it

`mods/map-signal/` and `mods/beacon-reveal/` are Lua mods — full source is in this repo,
the engine they run on is not. `mods/event-labels/` is plain XML and needs Slipstream but
not Hyperspace. `mods/fullscreen-no-minimize/` needs neither.

```bash
python tools/build-map-signal-mod.py            # build + verify   — works with nothing installed
python tools/build-map-signal-mod.py --pack     # ... zip to map-signal.ftl
python tools/build-map-signal-mod.py --install  # ... copy to Slipstream and patch (FTL must be closed)
```

Building and verifying work on a bare clone. **`--install` does not** — see §6.

> ⚠️ **A Slipstream `--patch` applies exactly what it is given, so a mod missing from the
> list is a mod uninstalled.** `build-beacon-mod.py` carries a longer `PATCH_ORDER` than
> `build-map-signal-mod.py` for that reason: installing beacon-reveal keeps map-signal,
> but installing map-signal drops beacon-reveal. Read the list before running either.

Check what is actually loaded rather than assuming:

```bash
grep "Loading Lua file" "<game dir>/FTL_HS.log"
```

### Launching the game

Never start `FTLGame.exe` from a tool call. Use `mods\fullscreen-no-minimize\launch-ftl.cmd`,
which puts `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0` into the game's process environment — an
agent's own shell does not have it, and without it the game minimizes every time the user
clicks the other monitor, with nothing about the launch looking wrong. That script reads
`%FTL_DIR%` and falls back to a hardcoded path, so **set `FTL_DIR`** rather than editing it.

Also: the game may be holding an unsaved run. Under Hyperspace the run save is
`hs_continue.sav`; if that file does not exist, killing `FTLGame.exe` destroys the run.
Check before restarting the game, and ask.

---

## 5. Tier 4 — `raw/gamedata`, and why it is absent

The 33 game XML files are **not in this repository and never were** — they were stripped
from every commit, not just deleted at the tip. They are Subset Games' copyrighted files
and this repo is public. `raw/gamedata/_PROVENANCE.md` and `raw/gamedata/README.md` are
still here and explain the format and the fit between files.

Everything already generated *from* them is committed, which is why Tiers 1–3 work without
them. What fails is regeneration. The failure is clean and names the cause:

```
$ python tools/extract-event.py GIANT_ALIEN_SPIDERS
GIANT_ALIEN_SPIDERS: no <event name="…"> with that name in raw/gamedata
```

### Re-extracting from the user's own install

`tools/ftlpkg.py` is a read-only parser for FTL's `PKG\n` archive. It does not modify the
game.

```bash
python tools/ftlpkg.py list "<game dir>/ftl.dat" ".xml"
python tools/ftlpkg.py extract-list "<game dir>/ftl.dat" raw/gamedata tools/gamedata-files.txt --flat
```

`tools/gamedata-files.txt` is the exact list — 33 files — so this reproduces what the wiki
was built from rather than a judgement call about what to pull.

**Only do this from a copy the user owns.** `.gitignore` already has `raw/gamedata/*.xml`,
so re-extracted files stay untracked; do not remove that line.

Which tools need them: `extract-event.py`, `extract-sector.py`, `build-mod.py`. The
watcher and `ftlsave.py` reference them but degrade rather than fail.

---

## 6. Machine-specific values — two environment variables

**Nothing in this repo needs a source edit to run on another machine.** Everything that is
about a specific computer reads an environment variable, with the original machine's paths
as the fallback so that machine keeps working unchanged.

| Variable | Names | Read by |
|---|---|---|
| `FTL_DIR` | the FTL install directory, the one holding `ftl.dat` | both mod builders, `launch-ftl.cmd`, and `ftlsave.py` — so the watcher finds a non-standard install too |
| `SLIPSTREAM_DIR` | the Slipstream directory, the one holding `modman.jar` | both mod builders |

```bash
export FTL_DIR="/path/to/FTL Faster Than Light"
export SLIPSTREAM_DIR="/path/to/Slipstream"
```

`FTL_DIR` is one variable for one directory — `launch-ftl.cmd` already used that name, so
the builders read it too rather than inventing a second that can disagree.

Per-invocation flags override the environment:

```bash
python tools/build-map-signal-mod.py --install --slipstream <dir> --game <dir>
python tools/build-beacon-mod.py     --install --slipstream <dir> --game <dir>
```

**Only `--install` reads either.** Build, `--pack` and `--verify` touch neither, which is
why a bare clone builds every mod (§0) and fails only where it would write to somebody's
game. When it does fail, it names the variable and reports both paths at once:

```
$ python tools/build-map-signal-mod.py --install
no modman.jar in C:\nope
  set SLIPSTREAM_DIR, or pass --slipstream <dir>
no ftl.dat in C:\also-nope
  set FTL_DIR, or pass --game <dir>
```

Each is checked by a file that must be *inside* it, not by the directory existing — a
plausible-but-wrong path is the likely mistake, and `modman.jar` missing surfaces several
steps later as a Java error that reads like a broken toolchain.

### Everything else derives itself

| | derived from |
|---|---|
| `build-pages.py` `REPO` | `git remote get-url origin`. A fork's `Built file` links and its 404's path prefix follow the fork. `--repo owner/name` overrides; a repo named `<owner>.github.io` is treated as a user site and gets no prefix |
| `pull-fandom.ps1` output | `$PSScriptRoot`'s parent — wherever the repo is cloned |
| `pull-fandom.ps1` User-Agent contact | `git config user.email` |
| the save, `ftl.dat`, `FTL_HS.log` | probed (§3) |

### One thing still to read carefully

Prose in `mods/*/README.md`, `tools/BEACON-REVEAL.md` and `tools/EVENT-LABELS.md` records
what was installed on the machine this was written on — Slipstream 1.9.1, Java 8,
Hyperspace 1.22.2, at that machine's paths. Those lines are marked as records rather than
instructions, but they are still descriptions of somebody else's computer. Do not read
"Hyperspace 1.22.2 is in the game folder" as a statement about yours.

---

## 7. Verify, in this order

Each line is independent and each starts nothing.

```bash
python tools/serve-site.py --check                   # every route + every asset it asks for
python tools/build-card-index.py --verify            # the event index
python tools/build-sector-index.py --verify          # the sector chooser
python tools/build-pages.py --check                  # the static export, if you built one
python tools/save-watch.py --once                    # the whole watcher chain, one shot
python tools/save-watch.py --index-report            # how ambiguous the text index is
python tools/build-map-signal-mod.py --verify        # a generated mod tree
```

With playwright, and with a site actually running:

```bash
python tools/smoke-inline.py --all                                   # over file://
python tools/smoke-inline.py --all --base http://127.0.0.1:8080      # over the served site
```

> ⚠️ `--all` globs `sector-*.html`, which picks up the `-review` copies. `serve-site.py`
> serves those because its route checks the file; a hosted export does not carry them, so
> against a hosted `--base` it 404s and times out 30 seconds later with a traceback rather
> than a verdict. Name pages individually against a hosted base.

---

## 8. What "not working" looks like

| Symptom | Cause |
|---|---|
| `no <event name="…"> … in raw/gamedata` | Tier 4 — §5 |
| watcher `status: error` that persists | both channels failed; `--once` prints why. A single `error` between polls is not one |
| watcher `sector_id: null`, empty `seen` | Hyperspace not installed, or `FTL_HS.log` not where it is expected — `--hs-log` |
| `seen` identical across polls 20s apart | the poll thread is dead while the HTTP server keeps serving the last state. Restart; `SAVE-WATCH.md` has the signature |
| a page 404s in the browser | check what `--site` names is up — 8080 only matters if `--site` points there. Against the hosted site, check the watcher printed `reachable` |
| the watcher shows a card you know you rebuilt as the old version | it is pointed at the hosted copy, which is frozen at the last `build-pages.py --deploy` (§2) |
| an edit to `tools/*.py` has no effect | Python reads source at import — restart the server. Page *content* is read per request and needs no restart |
| `--install` fails on a path | §6 |
| a second watcher "starts clean" but serves old code | on Windows `allow_reuse_address` lets it bind a port that is already listening. Kill by port and **confirm the port is clear** |

---

## 9. Not in this repository

- **The game.** FTL itself, `ftl.dat`, and the 33 extracted XML files (§5).
- **Hyperspace.** ~10 MB, its own project, its own installer (§4).
- **Slipstream**, and the Java it runs on (§4).
- **Packed mod archives.** `mods/*/*.ftl` is gitignored — `--pack` regenerates them.
- **The static site export.** `site/` is gitignored; `build-pages.py` regenerates it.

Everything else — the wiki, the tools, all four mods' source, all 386 cards, all 19 sector
profiles, and the specs for every pipeline — is here.
