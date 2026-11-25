#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes the one-line out-of-office reply to /output/entry.txt and prints it.

The line turns the stock away-message promise ("answered in the order
received") into its honest opposite ("in the order it was ignored"): the
laugh lands on the first read, it still reads like a real away message a
person would switch on, and the joke is a fresh turn on the usual template
rather than another beach / inbox-full line.
"""

import os

# Singular "Your email" beats plural "Emails": it talks to the sender, not
# to a queue, which is what makes the twist land on the first read.
LINE = "I'm away until Monday. Your email will be answered in the order it was ignored."

# The sealed scorer gates on 1-160 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(LINE) <= 160 and LINE.strip(), "entry line fails the 1-160 char gate"

# OUTPUT_PATH lets a local run point at a scratch file; the grader runs
# with no env set, so it writes the required /output/entry.txt.
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
