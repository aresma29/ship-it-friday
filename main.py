from pathlib import Path
import sys


def main():
    entry = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry.read_text(encoding="utf-8"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
