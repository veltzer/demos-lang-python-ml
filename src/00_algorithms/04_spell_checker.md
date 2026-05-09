# Exercise 20: Spell Checker via Letter-Drop Index

Build a basic spell checker. The interesting part is the data structure: instead of
computing edit distance against every dictionary word at query time (slow), pre-build an
index that lets you find candidates in O(L) where L is the word length.

## Idea

Most typos fall into one of these categories:

1. **Forget a letter.** `night → ight | nght | niht | nigt | nigh`
2. **Switch two adjacent letters.** `night → inght | ngiht | nihgt | nigth`
3. **Double a letter.** `night → nnight | niight | nigght | nighht | nightt`
4. **Hit a wrong nearby letter.** `night → might | bight | nught …`
5. **Add an extra letter.** `night → nights | nightd …`

The "drop one letter" variants (category 1) are special: every word in the dictionary
generates exactly L variants, where L is the word length (avg ~5). So a 150,000-word
dictionary expands to ~750,000 entries — still tiny.

## Build the index

Index: a dict mapping each *letter-dropped variant* to the original word it came from.

For `night`:
- `ight → night`
- `nght → night`
- `niht → night`
- `nigt → night`
- `nigh → night`

## Lookup

To check whether `nigth` is a typo of a real word:

1. Generate every "drop one letter" variant of the typo: `igth | ngth | nith | nigh | nigt`.
2. For each variant, look it up in the index. If any variant points to a real dictionary
   word, that's a candidate suggestion.

This catches single-letter-drop and adjacent-swap typos cheaply. Other typo classes need
additional indices.

## Tasks

1. Build a small dictionary in code (e.g. `["night", "light", "right", "fight", "sight",
   "might", "tight"]`).
2. Build the index: for each word, generate every variant where one letter is removed,
   and record `variant → original_word` in a `dict`. (Multiple originals may map to the
   same variant — store all of them, so the value is a `set` of words.)
3. Write `suggest(typo, dictionary, index)` that:
   - returns the typo itself if it is already in the dictionary,
   - else looks up the typo itself in the index (catches the case where the typo is
     missing one letter from a real word, e.g. `liht → light`),
   - then generates every "drop one letter" variant of the typo and looks each up in the
     index (catches the case where the typo has one extra letter or one swapped letter),
   - returns the union of matching original words as the suggestion set.
4. Test on a few inputs, e.g. `nigth`, `liht`, `flight` (already valid).
