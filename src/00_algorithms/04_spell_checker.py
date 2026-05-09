#!/usr/bin/env python

"""Solution to exercise 20: spell checker via letter-drop index."""

from collections import defaultdict


def drop_one_letter(word: str) -> list[str]:
    return [word[:i] + word[i + 1:] for i in range(len(word))]


def build_index(words: list[str]) -> dict[str, set[str]]:
    idx: dict[str, set[str]] = defaultdict(set)
    for word in words:
        for variant in drop_one_letter(word):
            idx[variant].add(word)
    return idx


def suggest(typo: str, dictionary: set[str], idx: dict[str, set[str]]) -> set[str]:
    if typo in dictionary:
        return {typo}
    candidates: set[str] = set()
    candidates |= idx.get(typo, set())
    for variant in drop_one_letter(typo):
        candidates |= idx.get(variant, set())
    return candidates


def main() -> None:
    words = ["night", "light", "right", "fight", "sight", "might", "tight", "flight"]
    dictionary = set(words)
    index = build_index(words)

    for typo in ["nigth", "liht", "rigt", "flight", "abcde"]:
        print(f"{typo:8s} -> {sorted(suggest(typo, dictionary, index))}")


if __name__ == "__main__":
    main()
