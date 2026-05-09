# Exercise 14: Vectorization Speed

The same operation can be many orders of magnitude slower depending on how you express it
in pandas. Rule of thumb:

1. If a built-in vectorized method exists (`.abs()`, `.sum()`, `+`, `*`, …) — use it. Fastest.
2. Otherwise prefer `Series.transform` or `Series.apply` with a function.
3. Iterating row-by-row in Python is the slowest option by far — avoid it.

Build a DataFrame of `1_000_000` random floats in a single column, then time each of these
ways to take the absolute value of the column. Print one timing line per approach:

1. `df[0].abs()` — vectorized built-in
2. `df[0].apply(abs)` — Python `abs` per element
3. A Python `for` loop over `range(len(df))` writing back to `df.iat[i, 0]` — full iteration

Use `time.perf_counter` and print each timing in seconds.

Expect approach 1 to be ~100x faster than approach 2, and approach 2 to be much faster
than approach 3.
