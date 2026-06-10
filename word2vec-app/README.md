# word2vec-app

A small, dependency-light word-vector explorer in Python.

It loads pre-trained **GloVe** embeddings (mid-range: **100 dimensions**) and
demonstrates the operations that made word2vec-style vectors famous:

- **nearest neighbours** — words closest in meaning
- **similarity** — cosine similarity between two words
- **analogies** — `king - man + woman ≈ queen`
- **odd-one-out** — which word does not belong in a group

## Why GloVe / 100d?

word2vec, GloVe and fastText all produce the same kind of dense vectors and
support identical arithmetic. GloVe ships clean, ready-to-use text files, so
it is the easiest to demo. **100 dimensions** is the classic mid-range size:
big enough for good analogies, small enough to load in seconds (~347 MB vs.
the 3.6 GB of Google's 300d word2vec). The de-facto standard for production
is 300d; 50/100/200 are the common smaller choices.

The vectors come from **GloVe 6B** — trained on Wikipedia 2014 + Gigaword 5
(6 billion tokens, 400k-word vocabulary).

## Setup

Only `numpy` is required (gensim has no Python 3.14 wheel yet, and we don't
need it — the GloVe text format is trivial to parse).

```bash
pip install numpy
./download.sh          # fetches glove.6B.100d.txt (~347 MB)
```

## Usage

```bash
# Built-in demonstration of every feature
python3 word2vec_app.py demo

# Individual operations
python3 word2vec_app.py nearest computer -k 8
python3 word2vec_app.py similarity king queen
python3 word2vec_app.py analogy man king woman      # -> queen
python3 word2vec_app.py odd breakfast lunch dinner telephone
```

By default only the 100k most frequent words are loaded for speed; pass
`--limit 0` to load the full 400k vocabulary, or `--vectors PATH` to use a
different GloVe-format file (e.g. `glove.6B.300d.txt`).

## Files

| file              | purpose                                            |
|-------------------|----------------------------------------------------|
| `word2vec_app.py` | the application (CLI + `Embeddings` class)         |
| `download.sh`     | fetches and unpacks the 100d GloVe vectors         |
| `README.md`       | this file                                          |
