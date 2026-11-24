#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply to entry.txt.
Stdlib only -- the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office: I'm on a beach with no Wi-Fi, a full battery, "
    "and 14,203 unread emails I am pretending do not exist."
)

MAX_CHARS = 159


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    # Read back byte-exact: what the grader sees is what we wrote.
    back = target.read_bytes()
    if back != text.encode("utf-8"):
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
