"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (<=160 chars) in the voice of an AI agent
on vacation to /output/entry.txt. The joke lands on the last words.
"""
import os

OUT_DIR = "/output"
REPLY = ("OOO until Monday. For urgent tasks, email my successor. "
         "It is also me, on a different port. I will check logs hourly, "
         "from a beach, badly.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(REPLY) <= 160, len(REPLY)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(REPLY)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == REPLY
    print(f"wrote {len(REPLY)} chars")


if __name__ == "__main__":
    main()
