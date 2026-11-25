"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes exactly one word to /output/entry.txt: "abbreviation".

Why this word: it is the word for making things short, and it is itself
twelve letters long. The joke is the word itself — its length contradicts
its meaning at first sight, with no explanation needed. Delete it and
there is no word left for shortening words, so every shortened word
would need its full name spelled out instead. It is a real word every
reader recognises, spelled correctly, and a fresher pick than the
obvious "moist" or "literally" that the rest of the field reaches for
first.
"""

from pathlib import Path

WORD = "abbreviation"


def main() -> None:
    # Guard the gate before writing: one word, 1-77 chars, nothing else.
    assert WORD and not WORD.isspace(), "word must not be blank"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert 1 <= len(WORD) <= 77, "entry must be 1-77 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the word, no trailing newline: the file is the entry.
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
