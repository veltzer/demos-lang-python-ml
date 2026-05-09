# Exercise 23: Spell-Checker Dictionary Design

Companion to exercise 20. Exercise 20 builds the spell checker. This one steps back and
asks: *what does the underlying dictionary look like, and is it actually feasible?*

## The back-of-the-envelope estimate

The English dictionary has roughly **150,000** words. The average word length is about
**5** letters. The drop-one-letter index stores, for every word `w`, every variant of `w`
with one letter removed — i.e. `len(w)` entries per word.

> Total entries ≈ 150,000 × 5 = **750,000**.
>
> If the average word length is 6 (including longer words), that's ≈ **1,000,000**.

A million entries is small. A modern laptop holds it in RAM trivially. So the design is
feasible — but you should verify with code, not just believe the estimate.

## Collisions

Multiple real words can produce the same drop-variant:

- `light` and `right` both drop the leading letter to give `ight`.
- `night` and `nigh` are related — `nigh` is a real (archaic) word, and `night` drops its
  trailing `t` to also give `nigh`.

Your index value must therefore be a **set** of real words, not a single word. When a typo
matches a variant, you suggest *all* of them and let the user (or a downstream ranker)
choose.

## Tasks

1. Take a list of real English words. The provided solution uses a small built-in list,
   but if you have `/usr/share/dict/words` available you can read it instead.
2. Build the drop-one-letter index. Track:
   - the total number of variant entries (`sum(len(s) for s in idx.values())`),
   - the number of distinct variant keys,
   - the maximum collision count (the largest set of real words that share a single
     variant key),
   - one example of a variant key with the most collisions and the words that map to it.
3. Print all four numbers. Use them to validate the back-of-the-envelope estimate above.
4. Reflect: as the input dictionary grows from 1,000 → 10,000 → 100,000 words, how do the
   four numbers grow? Linearly? Faster? Slower?

The provided solution generates the dictionary by upper-casing and lower-casing a small
seed list and adding a few hand-picked extras, so collisions are guaranteed and you can
see them in the output.
