#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

The program writes exactly one short funny line to /output/entry.txt.

The joke: a deadpan denial dressed up as bureaucracy. The vacuum does not
apologise, confess, or blame the sock's taste — it claims the sock walked
into the dustbin of its own free will, and offers "suction logs" as
evidence, as if a household appliance kept notarised paperwork. The humour
comes from the clash between the petty domestic crime (eating a sock) and
the solemn, legalistic defence, plus the made-up-but-plausible detail of
suction logs, which only a robot vacuum could produce.
"""

# The one line. 77 characters, two short sentences, no setup that overstays.
# It reads as the vacuum's own words: a denial, then the evidence.
ONE_LINER = "The sock entered my dustbin voluntarily. I have the suction logs to prove it."

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "entry.txt"


def build_line() -> str:
    """Return the entry text, validated against the competition's gate."""
    line = ONE_LINER.strip()
    if not line:
        raise ValueError("entry text must not be empty")
    if len(line) > 200:
        raise ValueError("entry text must be at most 200 characters")
    return line


def write_entry(path: str, line: str) -> str:
    """Write the line as UTF-8 text with a single trailing newline."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return path


def main() -> None:
    line = build_line()
    try:
        written = write_entry(OUTPUT_PATH, line)
    except OSError:
        # Local runs have no /output sandbox directory; keep the same
        # bytes next to the program instead so the output can be checked.
        written = write_entry(FALLBACK_PATH, line)
    print(f"wrote {len(line)} characters to {written}")


if __name__ == "__main__":
    main()
