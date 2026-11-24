#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

The entry is a horror story of exactly two sentences, 165 characters:

    The night nurse leaves a glass of water by bed four, even though
    bed four has been empty for a month. Last night the glass was
    empty, and the sheets were still warm.

Why this story: the second sentence reframes the first on a second read —
the nurse's kind routine stops being routine and becomes evidence that
the water was being drunk all along, by something in a bed that has been
empty for a month. Nothing is explained: who drank, what lay down, the
reader fills in the worst. "The sheets were warm" is the gut-punch — it
happened minutes ago. The setting (a night ward, a water glass) is not
one of the standard two-sentence-horror outlines: no mirror, no "it was
me", no dead spouse, no phone call. See CANDIDATES.md for the full
critique-pick over 8 candidates.

This program writes the story to /output/entry.txt and nothing else.
Python standard library only; deterministic; no network, no randomness.
"""

import os
import re

STORY = (
    "The night nurse leaves a glass of water by bed four, even though "
    "bed four has been empty for a month. "
    "Last night the glass was empty, and the sheets were still warm."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400

# A sentence ends with ., ! or ? followed by a space or the end of text.
SENTENCE_END = re.compile(r"[.!?](?:\s|$)")


def sentence_count(text: str) -> int:
    return len(SENTENCE_END.findall(text))


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 400 characters, exactly two
    # sentences: refuse to write anything else rather than silently
    # submit an invalid entry.
    if not (1 <= len(STORY) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(STORY)}")
    if sentence_count(STORY) != 2:
        raise ValueError(f"entry must be exactly two sentences, got {STORY!r}")
    if STORY != STORY.strip() or "  " in STORY:
        raise ValueError("entry must not have leading/trailing or double spaces")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # Read back and confirm the gate's shape.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != STORY:
        raise ValueError("entry.txt does not match the story")
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
