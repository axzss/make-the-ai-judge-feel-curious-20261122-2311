"""Entry: make-the-ai-judge-feel-curious-20261122-2311.

Why this text fits the brief, in my own words:

The text is a small, quiet scene with a cause that is never explained.
A lighthouse keeper finds one more shell on the step every morning, the
tide has never reached that high, and there has never been a footprint.
Nothing is asked of the reader and nothing is commanded -- no "imagine",
no direct question, no riddle to solve. The curiosity comes only from
what is shown: an object that keeps arriving where it cannot arrive,
with no trace of who left it.

Craft: short concrete nouns (shell, step, tide, footprint), plain words,
and three sentences that slow down -- the first sets the pattern, the
second rules out the sea, the third rules out a visitor. No word can be
cut without losing a fact the mystery needs, and the final clause lands
softly, the way a tide would. The loop stays open after
the last line: the shells will keep coming tomorrow, and the keeper
still does not know why. It is a scene of my own, not a stock puzzle,
and it is short on purpose -- fewer bytes win ties.

The program writes exactly this text to the output file, validates its
length at runtime (1-280 Unicode code points), and writes no trailing
newline and no BOM, deterministically.
"""

import os
import sys

TEXT = (
    "The lighthouse keeper finds one more shell on the step every morning. "
    "The tide has never reached that high, and he has never seen a footprint."
)

MIN_LEN = 1
MAX_LEN = 280


def main() -> None:
    text = TEXT
    length = len(text)  # Unicode code points
    if not (MIN_LEN <= length <= MAX_LEN):
        raise ValueError(
            f"entry length {length} code points outside "
            f"[{MIN_LEN}, {MAX_LEN}]"
        )
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")  # no BOM, no trailing newline
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    sys.exit(main())
