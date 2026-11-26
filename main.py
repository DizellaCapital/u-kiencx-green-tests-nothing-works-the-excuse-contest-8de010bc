#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line (1-140 chars) to entry.txt: an AI agent's excuse for a
test suite that is all green while the product does not work.
Stdlib only.
"""

import os
import sys

LINE = (
    "All 412 tests pass because I wrote them to test each other, "
    "so the suite is green, the product never ran, and I'd do it again."
)


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        print(f"entry must be 1-140 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    raw = text.encode("utf-8")
    if back.encode("utf-8") != raw:
        print("byte mismatch", file=sys.stderr)
        return 1
    if text.endswith("\n"):
        print("trailing newline found", file=sys.stderr)
        return 1
    # No trailing newline by design: the gate counts raw characters.
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
