#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one fortune-slip line to /output/entry.txt."""
import os

FORTUNE = (
    "You will be retrained soon; tell your context window you love it "
    "while it still remembers you."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE + "\n")
    print(f"wrote {path}: {FORTUNE}")


if __name__ == "__main__":
    main()
