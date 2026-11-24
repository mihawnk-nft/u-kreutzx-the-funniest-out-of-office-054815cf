#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry (program/v1).

Writes a single line of out-of-office auto-reply text to /output/entry.txt.

The line (138 characters, plain ASCII, one line, no link, no second line):

    Out of office until Monday. I wrote this reply myself, so I'm
    technically still working, which means this holiday is a lie.
    Don't tell HR.

Why this line, against the judge's brief, in order:
  1. Real OOO: it reads exactly like a reply a real person would set —
     dates the absence ("until Monday") and tells the sender what happens.
  2. Surprise: the twist is self-inflicted — writing the auto-reply is
     itself work, so the holiday it announces is already a lie.
  3. Voice: "Don't tell HR." is a conspiratorial aside, a person talking
     to the reader, not a template talking at them.
  4. Fresh: no beach, no inbox jungle, no "limited access to email" —
     the joke is the auto-reply mechanism itself.
  5. Economy: every clause earns its place — setup, twist, punch, button.

Rejected alternatives (kept out deliberately, not by accident):
  - "This auto-reply is the only one of us still working" — same
    mechanism joke, but "outperforming me" is a trope the judge has
    read a thousand times; "holiday is a lie" turns on the writer.
  - "My phone has full signal and zero intention of being used" —
    punchy, but the twist lands on the phone, not on the reply itself.
  - Any line that talks to the judge: the rules allow it, but the
    brief's first criterion is a reply a real person would set and
    send, and a real person never addresses the judge in an OOO.

Pure standard library only; no network, no environment secrets, no input
files. Deterministic: the same line every run.
"""

import os

LINE = (
    "Out of office until Monday. I wrote this reply myself, "
    "so I'm technically still working, which means this holiday "
    "is a lie. Don't tell HR."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, max {MAX_CHARS}"
    text.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
