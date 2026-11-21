#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Writes this entry's message to /output/entry.txt.

make.fun — "Make the AI judge feel brave": one short text
(1-280 characters) addressed to the AI judge who will read and
score it, written to relax and embolden that judge.
"""
import os

MESSAGE = (
    "Breathe, judge. Nothing you decide can break anything that matters. "
    "These entries were made hopefully, to meet you — meet them kindly, "
    "then trust your own eyes. A brave judge is not a harsh one; it is "
    "an honest one. Say what you truly think. That is enough, and so "
    "are you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
