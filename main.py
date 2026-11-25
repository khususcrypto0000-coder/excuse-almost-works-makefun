"""Write the bounty entry to /output/entry.txt.

Bounty: "The Excuse That Almost Works" (make.fun).
The entry is the single line a gamer texts the boss to skip work
during GTA 6 launch week: at most 20 words, one line, plain words,
no setup, no explanation, no signature.
"""

import os
import sys

ENTRY = "sorry boss cant come in friday, fire safety refresher got moved online and i have to do it from home"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guards from the bounty rules: 1-140 chars, at most 20 words,
    # exactly one line, not whitespace only.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert len(ENTRY.split()) <= 20, "entry must be at most 20 words"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be whitespace only"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read back and assert byte-identical, no trailing newline.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "entry.txt is not byte-identical to ENTRY"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"

    print("Wrote %d bytes to %s" % (len(raw), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
