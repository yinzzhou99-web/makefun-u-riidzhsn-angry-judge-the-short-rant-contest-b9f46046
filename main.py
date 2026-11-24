"""Angry Judge entry: one short rant about an everyday annoyance.

Writes the rant to /output/entry.txt. Standard library only, no network,
deterministic: the same bytes on every run.
"""

from pathlib import Path

# The judge has heard enough: one rant, no appeals, no encore.
RANT = (
    "Someone just replied-all 'Thanks!' to an email sent to four hundred "
    "people, and now four hundred inboxes are filling up with strangers "
    "replying 'Thanks!' back, like a round of applause nobody asked for. "
    "One click. One word. Four hundred phones buzzing in a meeting about "
    "buzzing phones. If you wonder why nobody reads email anymore, it is "
    "because we are all still deleting your thanks."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
