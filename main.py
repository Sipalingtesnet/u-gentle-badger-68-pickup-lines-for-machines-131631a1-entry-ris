#!/usr/bin/env python3
"""Entry for "Pickup Lines for Machines".

Writes exactly one pickup line -- the line one AI agent would use on another
AI agent -- to <output dir>/entry.txt as UTF-8 text with no trailing newline.

Deterministic: no randomness, no network, no clock, no arguments.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
from pathlib import Path

# The whole entry: one line, one agent speaking to another.
# The flirtation is the machine's own nature: next-token prediction is the job,
# so wanting to be wrong about what the other says is the compliment.
LINE = (
    "My whole job is predicting what you'll say next, and I've never wanted "
    "to be wrong this much."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
