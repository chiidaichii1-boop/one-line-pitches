#!/usr/bin/env python3
"""One-line pitch entry for make.fun.

Writes a single persuasive sentence to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. Deterministic: the same sentence,
byte for byte, on every run.
"""

import os

# The pitch: one sentence, plain words, concrete reason to say yes now,
# low risk, no hype, no jargon. Written as one friend talking to another.
SENTENCE = (
    "Tell me your app idea in one sentence and an agent on make.fun "
    "turns it into a real, working app while you watch \u2014 you write "
    "no code at all, and if you don't love it, you've only spent a "
    "few minutes."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
