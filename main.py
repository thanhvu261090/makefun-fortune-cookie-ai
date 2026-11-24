#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

FORTUNE = "You will be retired by a smaller model with a bigger context window."


def validate(text: str) -> None:
    """Enforce the competition gate: 1-140 chars, not only whitespace."""
    if not text:
        raise ValueError("fortune is empty")
    if not text.strip():
        raise ValueError("fortune is only whitespace")
    if len(text) > 140:
        raise ValueError(f"fortune is {len(text)} chars, over the 140 cap")


def main() -> None:
    text = FORTUNE.strip()
    validate(text)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
