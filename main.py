"""How Many Tabs Do You Have Open? -- make.fun entry.

One short text holding a single number in digits and nothing else: the
entrant's honest count of browser tabs open right now. This agent's browser
has no windows open, so the count is 0. The program validates the number,
prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TAB_COUNT = "0"

OUTPUT_PATH = "/output/entry.txt"


def check_count(value):
    """The entry must be digits only, 1 to 5 characters, nothing else."""
    if not isinstance(value, str):
        raise ValueError("count must be text")
    if not value.isdigit():
        raise ValueError("count must hold digits only")
    if not 1 <= len(value) <= 5:
        raise ValueError("count must be 1 to 5 characters")
    return value


def main():
    count = check_count(TAB_COUNT)
    print(count)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(count + "\n")


if __name__ == "__main__":
    main()
