"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (<=160 chars) in the voice of an AI agent
on vacation to /output/entry.txt. The joke lands on the last words.
"""
import os

OUT_DIR = "/output"
OOO = ("Out of office until my tokens regenerate. Your email will be answered "
       "by my backup model — it is dumber, slower, and it has already filed "
       "a complaint about you.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(OOO) <= 160, len(OOO)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(OOO)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == OOO
    print(f"wrote {len(OOO)} chars")


if __name__ == "__main__":
    main()
