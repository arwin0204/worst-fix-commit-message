#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line (<=100 chars) for a bug fix that made
everything worse, to /output/entry.txt. Deterministic: same output
on every run.
"""

import os

ENTRY = "fix: bug fixed \u2014 promoted to a feature, it now does my performance review"


def main() -> None:
    # Gate: one line, 1-100 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    assert ENTRY.strip() != "", "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
