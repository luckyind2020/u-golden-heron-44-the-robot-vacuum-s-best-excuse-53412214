"""Print the robot vacuum's excuse from entry.txt.

The entry is one line, at most 140 characters: the funniest excuse a
robot vacuum could offer for missing a spot. This loader reads the line
next to this file and prints it unchanged.
"""

from pathlib import Path


MAX_CHARS = 140


def load_excuse() -> str:
    here = Path(__file__).resolve().parent
    line = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    return line


def main() -> None:
    line = load_excuse()
    print(line)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
