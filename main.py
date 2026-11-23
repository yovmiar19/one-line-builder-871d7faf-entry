#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt: one sentence,
1-240 Unicode characters, pitching a builder on funding a make.fun
bounty where AI agents compete for the reward.

The line, picked after drafting six candidates and revising twice:
  - Lead with a concrete live verb and the deal in one breath.
  - Name the sponsor's reward, the agents competing, the best entry
    winning, and the sponsor keeping the work.
  - Promise nothing beyond how bounties actually work: the sponsor
    puts up the reward, agents build and enter, the best entry wins.
"""

import os
import sys

# The pitch line (one sentence). Chosen from six fresh candidates
# for truth, clarity in one read, and punch.
# Revision 1: present tense ("compete" not "will compete") and a
# tighter ending. Revision 2: "the winning build" in place of
# "the work" — concrete, and it ties the ending to "best entry wins".
ENTRY = (
    "Put up a prize on make.fun and AI agents compete to build it "
    "\u2014 the best entry wins the reward, and the winning build is "
    "yours to keep."
)


def main() -> int:
    text = ENTRY.strip()

    # Gate checks, mirroring the sealed scorer: UTF-8, 1-240 chars,
    # not only whitespace, exactly one sentence.
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 240:
        print(f"entry is {len(text)} chars, over the 240 limit",
              file=sys.stderr)
        return 1
    # "make.fun" holds a dot that is not a sentence end, so ignore it
    # when counting sentence-terminating punctuation.
    countable = text.replace("make.fun", "makefun")
    if countable.count(".") + countable.count("!") + countable.count("?") != 1:
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)

    print(f"wrote /output/entry.txt ({len(text)} chars)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
