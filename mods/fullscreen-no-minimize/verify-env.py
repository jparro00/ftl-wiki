"""Check whether a running FTLGame.exe actually received SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS.

The variable is read from the process environment by SIL's should_minimize_fullscreen()
(see README.md). It is fixed at process creation, so what matters is not what is set at
user scope but what the *running game* inherited from whoever launched it. Those two
differ whenever the launching process started before the variable was installed --- which
is exactly how this fix silently stopped working.

    python verify-env.py            # find FTLGame.exe and report
    python verify-env.py --pid 1234 # a specific process
    python verify-env.py --dump     # print its whole environment

Exit code 0 = the running game will not minimize on focus loss.
Exit code 1 = it will (or no game is running / the check failed).

Windows only. Reads PEB -> RTL_USER_PROCESS_PARAMETERS -> Environment out of the target
with ReadProcessMemory; handles both 32-bit (WOW64) and 64-bit targets. Read-only: it
never writes to the game or its memory.
"""
import argparse
import ctypes as C
import subprocess
import sys

VAR = "SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS"
OFF_VALUES = {"0", "false"}  # SIL: strcmp(...,"0") && stricmp(...,"false")

ntdll = C.WinDLL("ntdll")
k32 = C.WinDLL("kernel32", use_last_error=True)

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
ProcessBasicInformation = 0
ProcessWow64Information = 26


class PROCESS_BASIC_INFORMATION(C.Structure):
    _fields_ = [
        ("Reserved1", C.c_void_p),
        ("PebBaseAddress", C.c_void_p),
        ("Reserved2", C.c_void_p * 2),
        ("UniqueProcessId", C.c_void_p),
        ("Reserved3", C.c_void_p),
    ]


def _read(h, addr, size):
    buf = (C.c_char * size)()
    got = C.c_size_t(0)
    if not k32.ReadProcessMemory(h, C.c_void_p(addr), buf, size, C.byref(got)):
        raise OSError(f"ReadProcessMemory({addr:#x}, {size}) failed: {C.get_last_error()}")
    return bytes(buf[: got.value])


def _ptr(h, addr, width):
    return int.from_bytes(_read(h, addr, width), "little")


def process_environment(pid):
    """Return (bits, {NAME: VALUE}) for another process."""
    h = k32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not h:
        raise OSError(f"OpenProcess({pid}) failed: {C.get_last_error()}")
    try:
        wow64_peb = C.c_void_p(0)
        st = ntdll.NtQueryInformationProcess(
            h, ProcessWow64Information, C.byref(wow64_peb), C.sizeof(wow64_peb), None
        )
        if st != 0:
            raise OSError(f"NtQueryInformationProcess(Wow64Information) status {st:#x}")

        if wow64_peb.value:
            # 32-bit target: PEB32.ProcessParameters +0x10, params32.Environment +0x48
            bits = 32
            params = _ptr(h, wow64_peb.value + 0x10, 4)
            env_addr = _ptr(h, params + 0x48, 4)
        else:
            pbi = PROCESS_BASIC_INFORMATION()
            st = ntdll.NtQueryInformationProcess(
                h, ProcessBasicInformation, C.byref(pbi), C.sizeof(pbi), None
            )
            if st != 0:
                raise OSError(f"NtQueryInformationProcess(BasicInformation) status {st:#x}")
            # 64-bit target: PEB.ProcessParameters +0x20, params64.Environment +0x80
            bits = 64
            params = _ptr(h, pbi.PebBaseAddress + 0x20, 8)
            env_addr = _ptr(h, params + 0x80, 8)

        raw = b""
        while len(raw) < (1 << 20):  # environment blocks are far smaller; this is a backstop
            try:
                raw += _read(h, env_addr + len(raw), 4096)
            except OSError:
                break
            if b"\x00\x00\x00\x00" in raw:
                break

        env = {}
        for entry in raw.decode("utf-16-le", errors="replace").split("\x00"):
            if "=" in entry[1:]:  # skip the "=C:=..." drive entries' leading '='
                name, _, value = entry.partition("=")
                env[name.upper()] = value
        return bits, env
    finally:
        k32.CloseHandle(h)


def find_ftl():
    """PIDs of running FTLGame.exe, newest first, via tasklist (no extra dependencies)."""
    out = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq FTLGame.exe", "/FO", "CSV", "/NH"],
        capture_output=True, text=True,
    ).stdout
    pids = []
    for line in out.splitlines():
        parts = [p.strip('" ') for p in line.split('","')]
        if len(parts) >= 2 and parts[0].lower() == "ftlgame.exe":
            pids.append(int(parts[1]))
    return pids


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pid", type=int, help="process to inspect (default: find FTLGame.exe)")
    ap.add_argument("--dump", action="store_true", help="print the whole environment")
    args = ap.parse_args()

    pids = [args.pid] if args.pid else find_ftl()
    if not pids:
        print("FTLGame.exe is not running -- nothing to check.")
        print("Launch it with launch-ftl.cmd, then run this again.")
        return 1

    ok = True
    for pid in pids:
        try:
            bits, env = process_environment(pid)
        except OSError as e:
            print(f"pid {pid}: could not read environment: {e}")
            ok = False
            continue

        value = env.get(VAR)
        print(f"pid {pid}  ({bits}-bit, {len(env)} environment entries)")

        if value is None:
            ok = False
            print(f"  FAIL  {VAR} is not in this process's environment.")
            print("        It will minimize when you click the other monitor.")
            # Name the launcher, since that is what determines the answer.
            hint = next((k for k in ("CLAUDECODE", "AI_AGENT", "MSYSTEM") if k in env), None)
            if hint:
                print(f"        Launched from a shell, not from Steam ({hint} is set in it).")
                print("        Use launch-ftl.cmd, which sets the variable itself.")
            elif "STEAMAPPID" not in env:
                print("        Not launched by Steam either; whoever launched it had a")
                print("        stale environment. Use launch-ftl.cmd.")
            else:
                print("        Launched by Steam, but Steam itself lacks the variable ---")
                print("        restart Steam so it picks up the user-scope setting.")
        elif value.lower() in OFF_VALUES:
            print(f"  PASS  {VAR}={value}")
            print("        SIL will skip the minimize on focus loss.")
        else:
            ok = False
            print(f"  FAIL  {VAR}={value} -- any value other than 0/false means minimize.")

        if args.dump:
            for k in sorted(env):
                print(f"        {k}={env[k]}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
