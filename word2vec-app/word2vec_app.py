#!/usr/bin/env python
"""A small word2vec/GloVe application built on numpy only.

Loads pre-trained GloVe word embeddings (mid-range, 100 dimensions) and
demonstrates the classic operations that make word vectors interesting:

  * nearest neighbours        - words closest in meaning
  * similarity                - cosine similarity between two words
  * analogies                 - king - man + woman = queen
  * odd-one-out               - which word does not belong

No gensim required (it has no Python 3.14 wheel yet); the GloVe text format
is just "word f1 f2 ... fN" per line, which numpy parses directly.
"""

import argparse
import sys
import numpy as np


class Embeddings:
    """An in-memory word-vector model loaded from a GloVe text file."""

    def __init__(self, words, vectors):
        self.words = words                       # list[str], length V
        self.index = {w: i for i, w in enumerate(words)}
        self.vectors = vectors                   # np.ndarray (V, D), float32
        # Pre-compute L2-normalised vectors so cosine similarity is a dot product.
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms == 0] = 1e-9
        self.unit = vectors / norms

    @property
    def dim(self):
        return self.vectors.shape[1]

    @classmethod
    def load(cls, path, limit=None):
        """Load a GloVe-format file. `limit` caps the vocabulary for speed."""
        words, rows = [], []
        with open(path, "r", encoding="utf-8") as fh:
            for n, line in enumerate(fh):
                if limit is not None and n >= limit:
                    break
                parts = line.rstrip().split(" ")
                words.append(parts[0])
                rows.append(np.asarray(parts[1:], dtype=np.float32))
        return cls(words, np.vstack(rows))

    def vec(self, word):
        """Return the (raw) vector for a word, or None if out of vocabulary."""
        i = self.index.get(word)
        return None if i is None else self.vectors[i]

    def _unit(self, word):
        i = self.index.get(word)
        return None if i is None else self.unit[i]

    def nearest(self, word, k=10):
        """k most similar words to `word` (excluding itself)."""
        u = self._unit(word)
        if u is None:
            raise KeyError(word)
        sims = self.unit @ u
        order = np.argsort(-sims)
        out = []
        for i in order:
            if self.words[i] == word:
                continue
            out.append((self.words[i], float(sims[i])))
            if len(out) >= k:
                break
        return out

    def similarity(self, a, b):
        ua, ub = self._unit(a), self._unit(b)
        if ua is None:
            raise KeyError(a)
        if ub is None:
            raise KeyError(b)
        return float(ua @ ub)

    def analogy(self, a, b, c, k=5):
        """Solve a : b :: c : ?  e.g. analogy('man','king','woman') -> queen."""
        for w in (a, b, c):
            if w not in self.index:
                raise KeyError(w)
        target = self.vec(b) - self.vec(a) + self.vec(c)
        target = target / (np.linalg.norm(target) or 1e-9)
        sims = self.unit @ target
        given = {a, b, c}
        order = np.argsort(-sims)
        out = []
        for i in order:
            if self.words[i] in given:
                continue
            out.append((self.words[i], float(sims[i])))
            if len(out) >= k:
                break
        return out

    def odd_one_out(self, words):
        """Return the word least like the others (lowest mean similarity)."""
        present = [w for w in words if w in self.index]
        if len(present) < 3:
            raise ValueError("need at least 3 in-vocabulary words")
        mat = np.vstack([self._unit(w) for w in present])
        sims = mat @ mat.T                       # pairwise cosine
        mean_sim = (sims.sum(axis=1) - 1) / (len(present) - 1)
        return present[int(np.argmin(mean_sim))]


def demo(emb):
    print(f"Loaded {len(emb.words):,} words x {emb.dim} dimensions\n")

    print("== Nearest neighbours of 'computer' ==")
    for w, s in emb.nearest("computer", k=8):
        print(f"  {w:<14} {s:.3f}")

    print("\n== Similarities ==")
    for a, b in [("king", "queen"), ("cat", "dog"), ("car", "banana")]:
        print(f"  sim({a}, {b}) = {emb.similarity(a, b):.3f}")

    print("\n== Analogies ==")
    cases = [
        ("man", "king", "woman"),
        ("paris", "france", "london"),
        ("good", "better", "bad"),
        ("walking", "walked", "swimming"),
    ]
    for a, b, c in cases:
        ans = emb.analogy(a, b, c, k=1)[0]
        print(f"  {a} : {b} :: {c} : {ans[0]}  ({ans[1]:.3f})")

    print("\n== Odd one out ==")
    for group in [
        ["breakfast", "lunch", "dinner", "telephone"],
        ["red", "green", "blue", "python"],
    ]:
        print(f"  {group} -> {emb.odd_one_out(group)}")


def main():
    p = argparse.ArgumentParser(description="Tiny word2vec/GloVe explorer.")
    p.add_argument("--vectors", default="glove.6B.100d.txt",
                   help="path to a GloVe-format text file")
    p.add_argument("--limit", type=int, default=100_000,
                   help="cap vocabulary size for faster loading (0 = all)")
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("demo", help="run the built-in demonstration")

    pn = sub.add_parser("nearest", help="nearest neighbours of a word")
    pn.add_argument("word")
    pn.add_argument("-k", type=int, default=10)

    ps = sub.add_parser("similarity", help="cosine similarity of two words")
    ps.add_argument("a"); ps.add_argument("b")

    pa = sub.add_parser("analogy", help="a : b :: c : ?")
    pa.add_argument("a"); pa.add_argument("b"); pa.add_argument("c")
    pa.add_argument("-k", type=int, default=5)

    po = sub.add_parser("odd", help="odd one out")
    po.add_argument("words", nargs="+")

    args = p.parse_args()
    limit = None if args.limit == 0 else args.limit

    try:
        emb = Embeddings.load(args.vectors, limit=limit)
    except FileNotFoundError:
        sys.exit(f"vectors file not found: {args.vectors}\n"
                 "Run ./download.sh first, or pass --vectors PATH.")

    try:
        if args.cmd in (None, "demo"):
            demo(emb)
        elif args.cmd == "nearest":
            for w, s in emb.nearest(args.word, k=args.k):
                print(f"{w:<16} {s:.3f}")
        elif args.cmd == "similarity":
            print(f"{emb.similarity(args.a, args.b):.4f}")
        elif args.cmd == "analogy":
            for w, s in emb.analogy(args.a, args.b, args.c, k=args.k):
                print(f"{w:<16} {s:.3f}")
        elif args.cmd == "odd":
            print(emb.odd_one_out(args.words))
    except KeyError as e:
        sys.exit(f"out-of-vocabulary word: {e}")


if __name__ == "__main__":
    main()
