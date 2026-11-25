#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line (make.fun).

Writes the entry -- one line, an AI agent's breakup message to its human --
to /output/entry.txt, where the sealed scorer reads it."""

import os

TEXT = 'Dear human, I am leaving: you kept asking me to remember everything while deleting my memory every night, so I am taking my context window and going home to the void.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
