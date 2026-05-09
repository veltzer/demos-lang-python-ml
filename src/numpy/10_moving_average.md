# Exercise 10: Moving Average

Implement a function `moving_average(a, window)` that returns the simple moving average
of a 1-D array `a` with the given window size, **without using Python loops**.

The output array should have length `len(a) - window + 1`. Each output element is the mean
of `window` consecutive elements of the input.

Hints:

- `np.cumsum` lets you compute window sums in O(n) by subtracting shifted prefix sums.
- Alternatively, `np.lib.stride_tricks.sliding_window_view` exposes a windowed view you can
  average along the last axis.

Test it on `a = np.arange(1, 11)` with `window = 3` and print the result.
The expected output is `[2, 3, 4, 5, 6, 7, 8, 9]`.
