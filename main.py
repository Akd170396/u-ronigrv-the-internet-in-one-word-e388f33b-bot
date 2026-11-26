#!/usr/bin/env python3
"""The Internet in One Word — entry: "buffering".

Prints the word and writes it to entry.txt inside MAKEFUN_OUTPUT_DIR
(env var, default /output). Standard library only.
"""

import os
import sys

# The grader runs this script with -P, so its own directory is not on
# sys.path; add it explicitly in case sibling modules are ever imported.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = "buffering"


def write_entry(out_dir):
    """Write WORD to <out_dir>/entry.txt and verify it round-trips."""
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError("entry.txt mismatch: %r != %r" % (written, WORD))
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(out_dir)
    print(WORD)


if __name__ == "__main__":
    main()
