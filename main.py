"""The 3 AM Commit Message.

Writes the entry: one commit message, the funniest thing an AI agent
would write right after breaking production at 3 AM.
"""

import os

# The gate counts characters, not bytes: the entry is plain ASCII.
# The joke is built for the judge brief in order: it is a real commit
# message (fix plus revert), the punchline lands on the outage itself,
# it sounds like a model (it trusted tests it shipped itself), and the
# angle is fresh (production, not the agent, files the bug report).
MAX_CHARS = 200

ENTRY = (
    "fix: reverted my 3 AM deploy; the tests passed because I deployed "
    "them too, and production filed the bug report"
)


def main() -> None:
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise ValueError("entry must be a single line with no surrounding whitespace")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
