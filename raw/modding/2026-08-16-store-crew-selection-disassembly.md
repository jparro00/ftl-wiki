# FTL store crew selection — recovered from the game binary

Disassembly notes, 2026-08-16. Produced by instruction under direction, by reading the
shipped executable. Source layer: do not edit.

**Target:** `D:\Steam\steamapps\common\FTL Faster Than Light\FTLGame_orig.exe`, 5,497,856
bytes — the pristine binary, *not* the 125 MB Hyperspace-patched `FTLGame.exe`.

- Machine `0x014c` (i386, 32-bit), Magic `0x010b` (PE32), ImageBase `0x00400000`,
  `.text` at VA `0x00401000`, size `0x46d808`.
- No PDB, no debug directory, no RTTI-derived names. GCC/MinGW build (`.edata`/`.CRT`/`.tls`
  sections, `lea edi,[esp+8]; and esp,-16` prologues).
- C++11 libstdc++ ABI — `std::string` is 24 bytes (ptr, len, 16-byte SSO buffer).
  Establishing this was necessary to compute struct offsets correctly.

**Tooling.** No disassembler was installed (Ghidra, IDA, Binary Ninja, radare2, `objdump`,
`dumpbin`, `nm` all absent). Analysis used `capstone` 5.0.7 + `pefile` 2024.8.26 in a
scratchpad virtualenv, driven by a purpose-written signature scanner / xref tool.

**Naming.** FTL-Hyperspace ships `FTLGameWin32.cpp`, a table of 956 ZHL byte signatures
naming vanilla Win32 functions, and `FTLGameWin32.h` with reverse-engineered class layouts.
Those supplied *names*; every behavioural claim below was then confirmed against the actual
instructions. znixian/xftl's full `doc/` tree contains no blueprint- or rarity-related
document (`grep -i rarity` over it returns nothing), so it added nothing beyond the two files
already held.

---

## 1. The algorithm

```
Store::CreateStoreBoxes(type, equip)              @ 0x004bed80
──────────────────────────────────────────────────────────────
  ae   = Settings::GetDlcEnabled()                @ 0x00597740
  span = ae ? 1 : 2
  base = ae ? 3 : 2
  switch (type) { 0:weapons 1:drones 2:augments 3:CREW 4:systems }

  case CREW:                                      @ 0x004bef00
      N = random() % span + base        // AE: exactly 3.  non-AE: 2 or 3
      repeat N times:
          box = new CrewStoreBox(shopper, worldLevel, "")   // empty type string
          vStoreBoxes.push_back(box)
      repeat (3 - N) times:
          vStoreBoxes.push_back(new CrewStoreBox())         // blank filler slot

CrewStoreBox::CrewStoreBox(ship, worldLevel, type) @ 0x0051ae20
──────────────────────────────────────────────────────────────
  if (type is empty)
      blueprint = BlueprintManager::GetRandomCrew(count=1, demo_lock=false)[0]
  else
      blueprint = GetCrewBlueprint(type)

BlueprintManager::GetRandomCrew(count, demo_lock)  @ 0x0060df30
    → shared template helper                       @ 0x00764760-family
──────────────────────────────────────────────────────────────
  cand = [dummy]                       // 1-indexed implicit binary tree
  for (name, bp) in crewBlueprints:    // std::map, in-order
      r = bp.desc.rarity
      if (r == 0) continue             // EXCLUDED
      cand.push({ name, weight = 6 - r, subtotal = 6 - r })

  for i = n down to 2:                 // build subtree sums, parent = i/2
      cand[i/2].subtotal += cand[i].subtotal

  repeat count times:
      total = cand[1].subtotal
      r     = random() % total + 1     // r in [1, total]
      node  = 1
      loop:
          if (cand[node].weight >= r) break        // selected
          r -= cand[node].weight
          node *= 2                                // left child
          if (cand[node].subtotal < r) {           // overflow -> right child
              r -= cand[node].subtotal
              node += 1
          }
      emit cand[node].name
      w = cand[node].weight            // remove, so this call can't repeat it
      cand[node].weight = 0
      for (i = node; i; i >>= 1) cand[i].subtotal -= w
```

Sector overrides, applied once on sector entry (`fn 0x005f8ca0`):

```
BlueprintManager::ResetRarities()                  @ 0x0060ba60
    for each blueprint map (crew, drones, weapons, augments, systems):
        for each blueprint: desc.rarity = desc.baseRarity     // restore base

for (name, rarity) in currentSector->description.rarities:    // <rarityList>
    BlueprintManager::SetRarity(name, rarity)      @ 0x0060b8e0
        // writes ONLY the named blueprint's desc.rarity
```

---

## 2. The weighting function — `weight = 6 − rarity`, `0` excluded

From the shared selection helper, verbatim:

```
0x00764cf0  8b939c000000   mov  edx, dword ptr [ebx + 0x9c]   ; edx = bp.desc.rarity
0x00764cf6  85d2           test edx, edx
0x00764cf8  7566           jne  0x764d60                      ; rarity != 0 -> include it
                                                              ; rarity == 0 -> falls through,
                                                              ;   0x764cfa advances to next
                                                              ;   map node (call 0x854020 =
                                                              ;   _Rb_tree_increment). SKIPPED.
...
0x00764d60  8dbd98fdffff   lea  edi, [ebp - 0x268]
0x00764d66  b806000000     mov  eax, 6                        ; <<<< the constant 6
0x00764d6b  29d0           sub  eax, edx                      ; <<<< weight = 6 - rarity
0x00764d79  898560fdffff   mov  dword ptr [ebp - 0x2a0], eax  ; stash it
...
0x00764dc2  8b8560fdffff   mov  eax, dword ptr [ebp - 0x2a0]  ; reload 6 - rarity
0x00764dcb  8985c0fdffff   mov  dword ptr [ebp - 0x240], eax  ; entry.weight   = 6 - rarity
0x00764dd1  8985c4fdffff   mov  dword ptr [ebp - 0x23c], eax  ; entry.subtotal = 6 - rarity
0x00764de0  e8eb720a00     call 0x80c0d0                      ; push entry into candidate vector
```

The candidate-entry struct is 32 bytes; `+0x18` is its own weight and `+0x1c` its subtree
total (`-0x258 + 0x18 = -0x240`, `-0x258 + 0x1c = -0x23c`, matching the two stores above).

| `rarity` | 1 | 2 | 3 | 4 | 5 | 0 |
|---|---|---|---|---|---|---|
| **weight** | 5 | 4 | 3 | 2 | 1 | **excluded** |

A linear integer weight — not a threshold roll, not repeated insertion. Each surviving
blueprint gets exactly one entry.

### That `[ebx+0x9c]` really is `desc.rarity` — two independent confirmations

**(a) From the XML parser.** `BlueprintManager::ProcessDescription` (`fn 0x00602030`) parses
the literal tag `"rarity"` (string at `0x00883e6f`):

```
0x00602315  c704246f3e8800  mov  dword ptr [esp], 0x883e6f    ; "rarity"
0x0060231c  e86f561800      call 0x787990                     ; strcmp
0x00602326  7579            jne  0x6023a1
0x0060234b  e808f21400      call 0x751558                     ; atoi(value)
0x00602350  894758          mov  dword ptr [edi + 0x58], eax  ; Description.rarity = +0x58
```

The adjacent `<bp>` tag writes `[edi+0x60]`, consistent with the declared field order. With
`TextString` = 28 bytes this gives `Description{ rarity @+0x58, baseRarity @+0x5c }`, and
`Blueprint{ vtable@0, name@+0x04 (24 bytes), desc@+0x1c }` ⇒ `desc.rarity` = blueprint+0x74.
A `std::map` node is 16 bytes of `_Rb_tree` header + a 24-byte key string ⇒ value at
node+0x28 ⇒ rarity at node+0x9c. ✔

**(b) From `SetRarity`,** which independently writes the same offset:
`mov dword ptr [eax + 0x74], edx`. ✔

---

## 3. The draw — weighted tree descent, and the RNG

Tree build (implicit binary heap, `parent = i/2`):

```
0x00764e25  8d5c01fc  lea ebx, [ecx + eax - 4]        ; &last.subtotal
0x00764e35  8b33      mov esi, dword ptr [ebx]
0x00764e3a  d1f8      sar eax, 1                      ; i/2
0x00764e3c  c1e005    shl eax, 5                      ; *32 (element stride)
0x00764e3f  0174011c  add dword ptr [ecx+eax+0x1c], esi   ; parent.subtotal += child.subtotal
```

Draw and descent:

```
0x00764e67  8b593c    mov  ebx, dword ptr [ecx + 0x3c]  ; total = cand[1].subtotal (0x20+0x1c)
0x00764e70  e87b1befff call 0x6569f0                    ; random()
0x00764e7c  f7fb      idiv ebx                          ; edx = random() % total
0x00764e83  83c201    add  edx, 1                       ; r in [1, total]
0x00764ea5  89df      mov  edi, ebx                     ; node
0x00764ead  8b7018    mov  esi, dword ptr [eax + 0x18]  ; cand[node].weight
0x00764eb0  39d6      cmp  esi, edx
0x00764eb2  7cdc      jl   0x764e90                     ; weight < r -> descend
                                                        ; else SELECT node
0x00764e90  01db      add  ebx, ebx                     ; node *= 2 (left child)
0x00764e92  29f2      sub  edx, esi                     ; r -= weight
0x00764e99  8b44011c  mov  eax, dword ptr [ecx+eax+0x1c]; left.subtotal
0x00764e9f  0f8c3b010000 jl 0x764fe0                    ; -> 0x764fe0: sub edx,eax / add ebx,1
                                                        ;    i.e. r -= left.subtotal; node |= 1
```

Removal after selection — what makes a *single call* draw without replacement:

```
0x00764ee4  c744381800000000  mov dword ptr [eax+edi+0x18], 0   ; weight = 0
0x00764ef5  2974101c          sub dword ptr [eax+edx+0x1c], esi ; ancestors -= old weight
0x00764ef9  d1fb              sar ebx, 1                        ; walk up
```

**RNG** (`0x006569f0`) is a 64-bit LCG with multiplier `0x5851f42d4c957f2d`, increment 1,
returning `(state >> 32) >> 1` — a 31-bit non-negative value. A second path
(`cmp byte ptr [0x919860],0 / jne`) calls an imported RNG thunk at `0x751680` instead, but
rejoins at the identical `cdq / idiv`, so the distribution logic is the same either way.
`random() % total` carries the usual modulo bias; at these totals it is negligible but
nonzero.

---

## 4. How many crew slots — and it depends on AE

Prologue of `Store::CreateStoreBoxes` @ `0x004bed80`:

```
0x004beda1  e89a890d00  call 0x597740          ; Settings::GetDlcEnabled() -> al
0x004beda6  3c01        cmp  al, 1
0x004beda8  19db        sbb  ebx, ebx
0x004bedaa  f7d3        not  ebx
0x004bedac  83c302      add  ebx, 2            ; ebx = ae ? 1 : 2      (modulus)
0x004bedaf  3c01        cmp  al, 1
0x004bedb4  19ff        sbb  edi, edi
0x004bedb6  83c703      add  edi, 3            ; edi = ae ? 3 : 2      (base)
0x004bedb9  83f804      cmp  eax, 4
0x004bedbc  0f872b010000 ja  0x4beeed          ; default: no boxes
0x004bedc2  ff2485a8a28700 jmp dword ptr [eax*4 + 0x87a2a8]   ; 5-way switch
```

Jump table at `0x0087a2a8`: `[0]=0x4bf340` weapons, `[1]=0x4bedd0` drones,
`[2]=0x4bf450` augments, **`[3]=0x4bef00` crew**, `[4]=0x4bf010` systems. Each case is
confirmed by which `GetRandom*` it calls.

Crew case:

```
0x004bef0d  e8de7a1900  call 0x6569f0
0x004bef1a  f7fb        idiv ebx
0x004bef1f  8d043a      lea  eax, [edx + edi]      ; N = random() % span + base
0x004bef25  894594      mov  dword ptr [ebp - 0x6c], eax
  ; loop: N iterations
0x004bef40  c7042460030000 mov dword ptr [esp], 0x360   ; sizeof(CrewStoreBox)
0x004bef55  e8966e3a00     call 0x865df0                ; operator new
0x004bef47  897dd0 / 0x004bef4a c745d400000000 / 0x004bef51 c645d800
                                                        ; local std::string = ""  (EMPTY)
0x004bef79  e8a2be0500     call 0x51ae20                ; CrewStoreBox::CrewStoreBox
0x004befaf  394594         cmp  dword ptr [ebp-0x6c], eax
0x004befb2  758c           jne  0x4bef40
  ; then pad to exactly three
0x004befb4  bb03000000     mov  ebx, 3
0x004befb9  2b5d94         sub  ebx, dword ptr [ebp - 0x6c]   ; 3 - N filler boxes
0x004befe3  e8c8bb0500     call 0x51abb0                      ; default CrewStoreBox()
```

⇒ The crew section always occupies **3 slots**. `N` are hireable; `3 − N` are blank.

- **AE on:** `span=1, base=3` ⇒ `N = 3` always.
- **AE off:** `span=2, base=2` ⇒ `N ∈ {2,3}`, uniform.

`0x00597740` is identified as `Settings::GetDlcEnabled()` by structural match against
Hyperspace's Win32 ZHL signature for that function (`0fb605????????84c075??c38d74260055b9????`
vs. ours `0fb605 ad6d9100 84c0 7505 f3c3 8d7600 55 b9 40339100` — identical semantics,
differing only in `repz ret` padding and nop-`lea` width). Behaviour read from instructions;
the *name* is derived from Hyperspace.

---

## 5. The sector `rarityList` **overlays**, it does not replace

`BlueprintManager::SetRarity` @ `0x0060b8e0`:

```
0x0060b8fb  8d7964      lea  edi, [ecx + 0x64]         ; this->crewBlueprints
0x0060b906  e805062300  call 0x83bf10                  ; map::find(name)
0x0060b911  39c1        cmp  ecx, eax                  ; == end()?
0x0060b913  742b        je   0x60b940                  ; no -> try next map (+0x34 drones, ...)
0x0060b91a  e8919c1e00  call 0x7f55b0
0x0060b925  895074      mov  dword ptr [eax + 0x74], edx   ; desc.rarity = rarity
```

It writes only the named blueprint. Nothing is cleared, so it cannot be a "replace".

Sector entry, `fn 0x005f8ca0`:

```
0x005f8f0e  b9209e9100  mov  ecx, 0x919e20      ; the global BlueprintManager
0x005f8f13  31db        xor  ebx, ebx           ; i = 0
0x005f8f15  e8462b0100  call 0x60ba60           ; ResetRarities()      <<<< FIRST
0x005f8f30  6bd31c      imul edx, ebx, 0x1c     ; stride 28 = pair<std::string,int>
0x005f8f3b  8b7018      mov  esi, dword ptr [eax + 0x18]   ; .second = rarity
0x005f8f78  e863290100  call 0x60b8e0           ; SetRarity(name, rarity)   <<<< THEN
0x005f8fae  7780        ja   0x5f8f30           ; loop over description.rarities
```

`ResetRarities` @ `0x0060ba60` — one loop per blueprint map, iterating the red-black tree:

```
0x0060baad  8b7b70          mov edi, dword ptr [ebx + 0x70]   ; map._M_header._M_left = begin()
0x0060bab8  83c068          add eax, 0x68                     ; &header = end()
0x0060bac5  8b97a0000000    mov edx, dword ptr [edi + 0xa0]   ; node+0xa0 = desc.baseRarity
0x0060bad1  8b472c          mov eax, dword ptr [edi + 0x2c]   ; node+0x2c = blueprint.name.ptr
0x0060bae8  e8c35bffff      call 0x6016b0                     ; build std::string
0x0060baf8  e8b3feffff      call 0x60b9b0                     ; SetRarity_global(name, baseRarity)
0x0060bb12  e809852400      call 0x854020                     ; _Rb_tree_increment
0x0060bb1f  75a4            jne 0x60bac5
```

`0x0060b9b0` is a constant-folded `SetRarity` bound to the global manager —
`mov ecx, 0x919e84` (= `0x919e20 + 0x64`, `crewBlueprints`), falling through to
`mov ecx, 0x919e54` (= `+0x34`, `droneBlueprints`) and so on, ending in the same
`mov dword ptr [eax + 0x74], esi`.

⇒ **Every blueprint is restored to `desc.baseRarity`, then only the sector's named entries
are overridden. An item or species absent from a sector's `rarityList` keeps its base
rarity.**

This matches Hyperspace's own reimplementation at `StarMap.cpp:328–332`, but the vanilla
instructions above are the evidence.

---

## 6. With or without replacement — a genuine asymmetry

Crew, inside `CrewStoreBox::CrewStoreBox` @ `0x0051ae20`:

```
0x0051b0bf  8b7704      mov  esi, dword ptr [edi + 4]     ; the type string
0x0051b0c2  85f6        test esi, esi
0x0051b0c4  0f8506050000 jne 0x51b5d0                     ; non-empty -> use it verbatim
0x0051b0d0  c744240800000000  mov dword ptr [esp+8], 0    ; demo_lock = false
0x0051b0d8  c744240401000000  mov dword ptr [esp+4], 1    ; count = 1     <<<<
0x0051b0e0  c70424209e9100    mov dword ptr [esp], 0x919e20
0x0051b0e7  e8442e0f00        call 0x60df30               ; GetRandomCrew
```

Weapons/drones/augments, e.g. `0x004bf340`:

```
0x004bf35e  f7fb        idiv ebx
0x004bf36a  01fa        add  edx, edi              ; N
0x004bf36c  89542404    mov  dword ptr [esp+4], edx ; count = N     <<<<
0x004bf370  e86beb1400  call 0x60dee0              ; GetRandomWeapon(N, false)
```

⇒ **Crew: `N` separate calls of `count = 1`.** Each rebuilds the candidate tree from scratch,
so the removal step never carries across boxes. **Duplicates are possible — a store genuinely
can offer three Engi.**

⇒ **Weapons, drones and augments: one call with `count = N`.** Those *are* drawn without
replacement, so one store section cannot list the same weapon twice.

---

## 7. Limits of this analysis

- **`GetDlcEnabled()` at store time.** The branch structure is read, not which side a live AE
  session takes. Internals: `if (!byte[0x916dad]) return false; return !byte[0x913340];`.
  The name is a structural signature match; what sets those globals was not traced.
- **`Store::CreateStoreBoxes` naming.** Behaviour read directly; the *name* rests on a
  near-match ZHL signature — ours `...5389ce 83ec7c 8b07 8b5704 8945a0 8955a4` vs
  Hyperspace's `...5389cb 83ec7c 8b17 8b4704 8955a0 8945a4`: same frame size, same locals,
  same operations, different register allocation. Same function, different compiler build.
- **Which of the 5 blueprint maps `ResetRarities` touches.** The loop shape and the crew and
  drone maps were confirmed explicitly; the remaining three were inferred from four
  repetitions of an identical pattern rather than read individually.
- **Section-type selection** — whether a store has a crew section at all — is `Store::OnInit`,
  not disassembled here. `2026-08-15-xftl-stores.txt` covers it.

Nothing was modified: the game install, `ftl.dat` and both executables were read only.
