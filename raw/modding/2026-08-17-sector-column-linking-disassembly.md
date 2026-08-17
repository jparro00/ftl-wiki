# FTL sector-map column linking — recovered from the game binary

Disassembly notes, 2026-08-17. Produced by instruction under direction, by reading the
shipped executable. Source layer: do not edit.

**Target:** `D:\Steam\steamapps\common\FTL Faster Than Light\FTLGame.exe`, 125,087,845
bytes — the **Hyperspace-patched** binary, which is the one this install actually runs.

- Machine `0x014c` (i386, 32-bit), PE32, ImageBase `0x00400000`, `.text` at VA `0x00401000`.
- Chosen over the pristine `FTLGame_orig.exe` deliberately: Hyperspace's own signature for
  `StarMap::AddSectorColumn` (`.578d7c240883e4f0ff77fc5589e557565389cebb`) **does not occur**
  in `FTLGame_orig.exe` at all, but occurs twice in `FTLGame.exe`. The two are different
  builds — the folder holds a `downgrade.bat` — so the patched one is both the running code
  and the one Hyperspace's signatures were cut against.

**Tooling.** `capstone` 5.0.7 + `pefile` 2024.8.26 in a scratchpad virtualenv. No
disassembler installed.

**Locating the function.** `zhl.log` in the game directory is ZHL's own resolution log and
names vanilla functions with the addresses it found them at — but those are *runtime*
addresses. The module loads 0xB90000 above its ImageBase, so:

| Function | `zhl.log` | file VA | confirmed by |
|---|---|---|---|
| `StarMap::AddSectorColumn` | `0x0115a680` | **`0x005ca680`** | signature hit |
| `StarMap::PushSectorColumn` | `0x0115b4e0` | `0x005cb4e0` | exact signature hit |
| `StarMap::GenerateSectorMap` | `0x0115b6f0` | `0x005cb6f0` | offset agreement |

`AddSectorColumn` runs `0x005ca680`–`0x005cb13d`. It is called from exactly two sites:
`0x005cb5a2` (inside `PushSectorColumn`) and `0x005cb9e5` (inside `GenerateSectorMap`).

---

## 1. How many sectors the next column has

At the top of the function, `esi = this`:

```
005ca69e  mov eax, [ecx+0x8ac]      ; last column vector: end
005ca6a4  sub eax, [ecx+0x8a8]      ;                     begin
005ca6aa  sar eax, 2                ; eax = prevCount
005ca6ad  mov [ebp-0x110], eax
005ca6b3  mov edi, eax
005ca6b5  jmp 0x5ca6de
005ca6c0  call 0x71e728             ; rand
005ca6c9  imul ebx                  ; ebx = 0x55555556  -> signed / 3
005ca6d5  sub ecx, eax              ; ecx = rand() % 3
005ca6d7  add ecx, 2                ; ecx = 2 + (rand() % 3)   -> 2..4
005ca6da  cmp ecx, edi
005ca6dc  jne 0x5ca6f0              ; accept when != prevCount, else roll again
```

**The re-roll excludes equality and nothing else.** Every ordered pair of unequal sizes
drawn from {2,3,4} therefore occurs: 2→3, 2→4, 3→2, 3→4, 4→2, 4→3. There is no constraint
that would make 3→4 or 4→3 impossible.

`[ebp-0x114]` holds the new count from here on. `[ebp-0x110]` holds the previous count.

## 2. The three paths

```
005ca6f0  cmp [ebp-0x110], 1
005ca6fd  je  0x5cabeb              ; prevCount == 1: leaving the first sector
005ca70f  cmp ecx, 2 ; sete bl      ; bl = (newCount == 2)
005ca781  cmp ecx, 4                ; ecx recomputed = prevCount
005ca784  jne 0x5ca78e
005ca786  test bl, bl
005ca788  jne 0x5cac04              ; prevCount == 4 && newCount == 2  -> special
005ca78e  cmp ecx, 2
005ca791  jne 0x5ca7a0
005ca793  cmp [ebp-0x114], 4
005ca79a  je  0x5cb1de              ; prevCount == 2 && newCount == 4  -> special
005ca7a8  mov ecx, [ebp-0x110]
005ca7ae  cmp [ebp-0x114], ecx
005ca7c6  setle [ebp-0x118]         ; flag = (newCount <= prevCount)
005ca7cd  xor edi, edi              ; peer index
005ca7cf  jmp 0x5ca975              ; the general loop
```

Because the two size-2 gaps are special-cased and equality is impossible, **the general
loop only ever runs with `|newCount − prevCount| == 1`.**

## 3. The general loop

A `Sector` carries its connection vector at `+8` (begin) / `+0xc` (end) / `+0x10` (cap);
`this+0x8a8` is the previous column, `this+0x6fc` every sector. `ebx` carries the
last-created sector across iterations, and starts null (`[ebp-0xf8] = 0` at `0x5ca725`).

```
005ca975  test ebx, ebx
005ca977  je   0x5ca9a3
005ca979  mov  edx, [edx+edi*4]     ; peer = prev[edi]
005ca97c..94                        ; peer.connections.push_back(ebx)
005ca9a3  sar eax,2 ; sub eax,1     ; eax = prevCount - 1
005ca9ab  cmp eax, edi
005ca9ad  jne 0x5ca9bc
005ca9af  cmp byte [ebp-0x118], 0
005ca9b6  jne 0x5caf46              ; last peer AND newCount <= prevCount -> done
          ... roll sector type, operator new(0xd0), init ...
005ca8fe  mov ecx, [eax+edx]        ; peer = prev[edi]
005ca904  add ecx, 8
005ca907  call 0x7dbec0             ; peer.connections.push_back(newSector)
005ca90c..29                        ; newColumn.push_back / allSectors.push_back
005ca849  mov edx, [ebp-0x110]
005ca84f  cmp [ebp-0x114], edx
005ca855  jle 0x5ca931              ; only when the column is growing...
005ca85b  test edi, edi
005ca85d  jne 0x5ca931              ; ...and only at peer 0
005ca863..92e                       ; create a SECOND sector, also linked to prev[0]
005ca931  mov eax, [edx+eax]        ; peer = prev[edi]
005ca944  mov ecx, [eax+8]
005ca947  mov eax, [eax+0xc]
005ca94f  mov ebx, [ecx+eax*4-4]    ; ebx = last of peer.connections
005ca93e  add edi, 1
005ca96d  cmp edi, ecx
005ca96f  jae 0x5caf46              ; peers exhausted
```

Reconstructed, with 1-based indices:

```
for p in 1 .. prevCount:
    if prev_new: reach[p] += prev_new         # peer inherits the last new sector
    if p == prevCount and newCount <= prevCount: break
    made += 1; reach[p] += made               # its own new sector
    if newCount > prevCount and p == 1:
        made += 1; reach[1] += made           # the extra one, hung off peer 1
    prev_new = made
```

`made == newCount` on exit in both directions, and every new sector is reachable by
somebody — no orphan column entries.

## 4. The two special cases

**`prevCount == 4, newCount == 2`** at `0x5cac04`. With `k = [ebp-0x104]`:

```
005cac98  mov eax, [ebp-0x104]      ; k
005cac9e  lea ebx, [eax+2]          ; k+2
005caca1  mov edi, eax
005cacba  mov edx, [eax+edi*4]      ; prev[k]        <- push new sector
005cacde  mov eax, [ebp-0x104]
005cace4  add eax, 1
005cace7  cmp eax, ebx
005cace9  jge 0x5cad1c
005cacf7  mov edx, [eax+esi+4]      ; prev[k+1]      <- push the same new sector
```

`k = 2j` for the *j*th new sector, so **new *j* hangs off prev 2*j* and 2*j*+1** — the 1st
new sector off the previous 1st/2nd, the 2nd off the 3rd/4th.

**`prevCount == 2, newCount == 4`** at `0x5cb1de`, the mirror: new 1st/2nd hang off the
previous 1st, new 3rd/4th off the previous 2nd.

Both agree with the prose in `raw/modding/2026-08-15-xftl-sector-map.txt`, which states
these two and only these two outright.

## 5. Column order

New sectors are appended to `this+0x6fc` (every sector) in creation order, and the y
coordinate `[ebp-0xf0]` is advanced by `0x32` per creation (`0x5ca959`, `0x5ca865`). So
**iterating `starMap.sectors` filtered by level yields the column top to bottom**, which is
also the order the game's own "1." / "2." choice labels count in. Confirmed on screen: a
2-wide column into a 4-wide one, ship in the 1st, offered the first two of the four.

## 6. The full table

`m` = sectors in the current column, `n` = in the next, position 1-based from the top.

| m → n | pos 1 | pos 2 | pos 3 | pos 4 | path |
|---|---|---|---|---|---|
| 1 → n | all | | | | forced |
| 2 → 3 | 1,2 | 2,3 | | | general (grow) |
| 3 → 4 | 1,2 | 2,3 | 3,4 | | general (grow) |
| 3 → 2 | 1 | 1,2 | 2 | | general (shrink) |
| 4 → 3 | 1 | 1,2 | 2,3 | 3 | general (shrink) |
| 2 → 4 | 1,2 | 3,4 | | | special |
| 4 → 2 | 1 | 1 | 2 | 2 | special |

Note 2→4 differs from the general grow rule at position 2 (3,4 rather than 2,3) — which is
precisely why the binary special-cases it.
