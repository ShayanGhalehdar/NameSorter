#!/usr/bin/env python3
"""Sort names by last name and given names, then print and save the result."""

from pathlib import Path
import sys


class Name:
    """Represents a validated individual name.

    Domain rule: Must have 1 last name and between 1 and 3 given names
    (2 to 4 tokens total).
    """

    def __init__(self, full_name: str) -> None:
        self.parts = full_name.split()

        if len(self.parts) < 2:
            raise ValueError(f"'{full_name}' must have at least 1 given name.")
        if len(self.parts) > 4:
            raise ValueError(f"'{full_name}' must have at most 3 given names.")

        self.last_name: str = self.parts[-1]
        self.given_names: list[str] = self.parts[:-1]

    def __str__(self) -> str:
        return " ".join(self.parts)

    @property
    def sort_key(self) -> tuple[str, list[str]]:
        return (self.last_name, self.given_names)


class NameSorter:
    """Sorts collections of names primarily by last name, then by given names."""

    def sort(self, raw_names: list[str]) -> list[str]:
        names = [Name(line) for line in raw_names if line.strip()]
        sorted_names = sorted(names, key=lambda n: n.sort_key)
        return [str(name) for name in sorted_names]


def main() -> None:
    """CLI orchestrator handling standard I/O and file persistence."""
    if len(sys.argv) != 2:
        print("Usage: name-sorter <file_path>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])

    try:
        if not input_path.is_file():
            raise FileNotFoundError(f"File '{input_path}' does not exist.")

        raw_text = input_path.read_text(encoding="utf-8")
        raw_names = raw_text.splitlines()

        sorter = NameSorter()
        sorted_names = sorter.sort(raw_names)
        output_text = "\n".join(sorted_names)

        print(output_text)

        output_path = Path("sorted-names-list.txt")
        output_path.write_text(output_text + "\n", encoding="utf-8")

    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()