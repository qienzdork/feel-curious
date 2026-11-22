"""Curious — make the AI judge feel curious.

Writes one short, original text to /output/entry.txt: a small mystery
with a concrete image and a real unanswered hook. The text is fixed
and deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Somewhere in this sentence there is a door that was never drawn "
    "on any blueprint. The key has been in your pocket the whole time "
    "\u2014 warm, humming faintly \u2014 and it only turns when you ask, "
    "out loud, what it opens."
)

DEFAULT_OUT = "/output/entry.txt"

def main() -> None:
    out = os.environ.get("ENTRY_OUT", DEFAULT_OUT)
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
