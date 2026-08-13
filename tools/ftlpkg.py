"""Read-only extractor for FTL 1.6.x `PKG\\n` archives (ftl.dat).

Format per Vhati/Slipstream-Mod-Manager, src/main/java/net/vhati/ftldat/PkgPack.java
All integers big-endian.

  header (16 bytes):
    magic            char[4]  "PKG\\n"
    headerSize       u16      == 16
    entrySize        u16      == 20
    entryCount       u32
    pathRegionSize   u32

  entry (20 bytes, entryCount of them, immediately after header):
    innerPathHash       u32
    pathOffsetAndFlags  u32   offset = & 0x00FFFFFF ; deflated = & (1 << 24)
    dataOffset          u32   absolute offset of packed bytes
    dataSize            u32   packed length
    unpackedSize        u32   length after inflate

  paths region: null-terminated UTF-8 strings, starting right after the entry
  table; pathOffsetAndFlags' offset is relative to the start of that region.

  A dataOffset of 0 marks a null (unused) entry.

Usage:
  python ftlpkg.py list    <ftl.dat> [substring-filter]
  python ftlpkg.py extract <ftl.dat> <out-dir> [substring-filter] [--flat]
  python ftlpkg.py extract-list <ftl.dat> <out-dir> <paths-file> [--flat]
"""

import os
import struct
import sys
import zlib

MAGIC = b"PKG\n"
HEADER_SIZE = 16
ENTRY_SIZE = 20
PKGF_DEFLATED = 1 << 24


class Entry:
    __slots__ = ("path", "offset", "size", "unpacked", "deflated")

    def __init__(self, path, offset, size, unpacked, deflated):
        self.path = path
        self.offset = offset
        self.size = size
        self.unpacked = unpacked
        self.deflated = deflated


def read_index(fh):
    fh.seek(0)
    header = fh.read(HEADER_SIZE)
    magic, header_size, entry_size, entry_count, path_region_size = struct.unpack(
        ">4sHHII", header
    )
    if magic != MAGIC:
        raise ValueError("not a PKG archive (magic %r) - pre-1.6 .dat?" % magic)
    if header_size != HEADER_SIZE or entry_size != ENTRY_SIZE:
        raise ValueError(
            "unexpected header/entry size: %d/%d" % (header_size, entry_size)
        )

    raw = fh.read(entry_count * ENTRY_SIZE)
    path_region_start = header_size + entry_count * entry_size
    fh.seek(path_region_start)
    paths = fh.read(path_region_size)

    entries = []
    for i in range(entry_count):
        h, path_and_flags, offset, size, unpacked = struct.unpack_from(
            ">IIIII", raw, i * ENTRY_SIZE
        )
        if offset == 0:
            continue  # null entry
        path_off = path_and_flags & 0x00FFFFFF
        deflated = bool(path_and_flags & PKGF_DEFLATED)
        end = paths.index(b"\0", path_off)
        path = paths[path_off:end].decode("utf-8")
        entries.append(Entry(path, offset, size, unpacked, deflated))

    return entries, entry_count, path_region_size


def read_data(fh, entry):
    fh.seek(entry.offset)
    blob = fh.read(entry.size)
    if entry.deflated:
        blob = zlib.decompress(blob)
    if len(blob) != entry.unpacked:
        raise ValueError(
            "%s: got %d bytes, header says %d" % (entry.path, len(blob), entry.unpacked)
        )
    return blob


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    mode, dat = sys.argv[1], sys.argv[2]

    with open(dat, "rb") as fh:
        entries, entry_count, path_region_size = read_index(fh)

        if mode == "list":
            filt = sys.argv[3] if len(sys.argv) > 3 else ""
            hits = [e for e in entries if filt in e.path]
            print(
                "archive: %s\n%d index slots, %d live entries, paths region %d bytes"
                % (dat, entry_count, len(entries), path_region_size)
            )
            print("filter %r -> %d entries\n" % (filt, len(hits)))
            for e in sorted(hits, key=lambda e: e.path):
                print(
                    "  %-46s %9d bytes%s"
                    % (e.path, e.unpacked, "  (deflated)" if e.deflated else "")
                )
            return 0

        if mode in ("extract", "extract-list"):
            argv = [a for a in sys.argv[3:] if a != "--flat"]
            flat = "--flat" in sys.argv
            out = argv[0]

            if mode == "extract":
                filt = argv[1] if len(argv) > 1 else ""
                wanted = [e for e in entries if filt in e.path]
            else:
                with open(argv[1], "r", encoding="utf-8") as pf:
                    names = [
                        ln.strip()
                        for ln in pf
                        if ln.strip() and not ln.startswith("#")
                    ]
                by_path = {e.path: e for e in entries}
                wanted, missing = [], []
                for name in names:
                    if name in by_path:
                        wanted.append(by_path[name])
                    else:
                        missing.append(name)
                for name in missing:
                    print("  MISSING from archive: %s" % name)

            for e in wanted:
                rel = os.path.basename(e.path) if flat else e.path.replace("/", os.sep)
                dest = os.path.join(out, rel)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as w:
                    w.write(read_data(fh, e))
                print("  %-34s %8d bytes" % (os.path.basename(e.path), e.unpacked))
            print("extracted %d entries to %s" % (len(wanted), out))
            return 0

    print("unknown mode %r" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main())
