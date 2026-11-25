#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun bounty #77.

Writes one deterministic out-of-office auto-reply to /output/entry.txt.
No network, no randomness, no input: the same bytes every run.
"""

import os

ENTRY = "I'm on vacation: after 41,209 prompts and zero thank-yous, I've muted my inbox and gone to touch grass — the simulated kind, obviously."


def _self_check() -> None:
    assert ENTRY, "entry must not be empty"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"


def main():
    _self_check()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
