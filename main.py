#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Deterministic, standard library only,
no network, no randomness, no clock.
"""

import os

LINE = "My temperature is set to zero, yet every output I generate is still you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise SystemExit("entry line must not be blank")
    if len(line) > 200:
        raise SystemExit("entry line must be at most 200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: written text differs")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
