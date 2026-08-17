---
id: source-sector-column-linking-disassembly
type: source
source_kind: research
raw: raw/modding/2026-08-17-sector-column-linking-disassembly.md
game_version: both
date: 2026-08-17
ingested: 2026-08-17
reliability: high
tags: [sector-map, generation, engine-internals, reverse-engineering, disassembly]
---

# Sector-map column linking, read out of `FTLGame.exe`

## Summary
Which sectors the map actually offers you at a jump, recovered instruction by instruction
from `StarMap::AddSectorColumn` in the shipped binary. It settles what
[[source-xftl-sector-map]] describes only as prose: the exact link map for **all six**
column transitions, the fact that a column's size is re-rolled only while equal to the
previous one, and that `starMap.sectors` yields a column in top-to-bottom order.

`reliability: high` despite `source_kind: research`, on the precedent of
[[source-store-crew-selection-disassembly]]: reading the shipped machine code is a primary
reading of the game itself, not a synthesis of sources this repo does not hold.

## Key Takeaways

- **A column holds 2–4 sectors, re-rolled only while equal to the previous column.**
  `2 + (rand() % 3)`, compared against the previous count, `jne` to accept. So every
  ordered unequal pair occurs — **3→4 and 4→3 included**. Nothing forbids them.
- **Therefore the general path only ever runs with `|n − m| == 1`**, because the two
  size-2 gaps (2→4, 4→2) are special-cased and equality cannot happen.
- **The general loop** walks the previous column's sectors in order. Each is linked to the
  sector the previous one created, then creates one of its own; a growing column makes one
  extra sector at position 1; a shrinking column breaks before the last position creates
  anything.
- **The two special cases** match the prose in [[source-xftl-sector-map]] exactly — new
  *j* hangs off previous 2*j* / 2*j*+1 when 4→2, and the mirror when 2→4.
- **2→4 is not the general grow rule.** From position 2 it reaches the 3rd and 4th, where
  the general rule would say 2nd and 3rd. That difference is why the binary branches.
- **Column order is creation order**, appended to the all-sectors vector with the y
  coordinate advancing by a fixed step — so the *n*th sector at a level is the *n*th from
  the top, and the game's own "1." / "2." labels count the same way.

## The table

`m` = sectors in the current column, `n` = in the next, position 1-based from the top.

| m → n | pos 1 | pos 2 | pos 3 | pos 4 |
|---|---|---|---|---|
| 1 → n | all | | | |
| 2 → 3 | 1,2 | 2,3 | | |
| 3 → 4 | 1,2 | 2,3 | 3,4 | |
| 3 → 2 | 1 | 1,2 | 2 | |
| 4 → 3 | 1 | 1,2 | 2,3 | 3 |
| 2 → 4 | 1,2 | 3,4 | | |
| 4 → 2 | 1 | 1 | 2 | 2 |

## Contradictions Flagged

> ⚠️ **CONTRADICTION:** [[source-xftl-sector-map]] describes the non-special transitions as
> "find its 'peer', the sector with the corresponding index in the previous column… If this
> column has more sectors than the last column, add a new column in the 2nd position to keep
> the connections right." Read literally that is not implementable — a loop building one
> column cannot add a column — and "corresponding index" has no meaning when the new column
> is larger. The binary shows what is really happening: an **extra sector** (not a column) is
> created at **position 1** (not the 2nd) when the column grows. Trusting the binary; the
> prose is a good-faith summary its own author calls hard to read.

Not a version difference: the prose and the binary describe the same routine, and the prose
is an informal account of it.

## Other Pages Touched
- [[source-xftl-sector-map]] — its linking bullet now carries the contradiction above.

Nothing else. The link map is consumed by tooling (`tools/build-map-signal-mod.py`), not yet
by any wiki page; a `[[concept-sector-map-generation]]` gathering the column sizes, the
type roll and the linking in one place is worth creating and does not exist.

## Links
- `raw/modding/2026-08-17-sector-column-linking-disassembly.md` — the disassembly
- [[source-xftl-sector-map]] — the prose account this corrects and completes
- [[source-store-crew-selection-disassembly]] — the same method, applied to stores
- [[source-beacon-name-labels-mod]] — what Hyperspace does and does not expose to Lua
