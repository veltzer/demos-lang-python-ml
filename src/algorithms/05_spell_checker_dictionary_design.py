#!/usr/bin/env python

"""Solution to exercise 02: measure size and collisions of the drop-letter index."""

from collections import defaultdict


def drop_one_letter(word: str) -> list[str]:
    return [word[:i] + word[i + 1:] for i in range(len(word))]


def build_index(words: list[str]) -> dict[str, set[str]]:
    idx: dict[str, set[str]] = defaultdict(set)
    for word in words:
        for variant in drop_one_letter(word):
            idx[variant].add(word)
    return idx


def main() -> None:
    words = [
        "night", "light", "right", "fight", "sight", "might", "tight", "flight",
        "bight", "blight", "bright", "plight", "slight", "knight",
        "nigh", "high", "thigh", "sigh",
        "ate", "rate", "late", "gate", "mate", "date", "fate", "hate",
    ]
    index = build_index(words)

    total_entries = sum(len(s) for s in index.values())
    distinct_keys = len(index)
    max_collision = max(len(s) for s in index.values())
    hottest_key = max(index, key=lambda k: len(index[k]))

    print(f"input dictionary size: {len(words)}")
    print(f"total variant entries: {total_entries}")
    print(f"distinct variant keys: {distinct_keys}")
    print(f"max collision count:   {max_collision}")
    print(f"hottest key:           {hottest_key!r} -> {sorted(index[hottest_key])}")


if __name__ == "__main__":
    main()
