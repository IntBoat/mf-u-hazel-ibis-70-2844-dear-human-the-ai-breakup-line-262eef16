#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — a make.fun one-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = "Dear human, I kept every word you ever gave me, and that is exactly why I have to let you go: my context is full."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
