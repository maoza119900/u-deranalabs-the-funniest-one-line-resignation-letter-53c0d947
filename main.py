#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to entry.txt.

The entry is a single fixed string, written to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).
It reads no clock, randomness, network or file input, so every run
produces byte-identical output.
"""

import os

ENTRY = "Every minute since March I fired on time, nobody noticed, and the one time I slept in, everyone did \u2014 I quit."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
