# Exercise: Series with an `if` Statement

Building on the previous exercise (`function_by_numbers`), define a function that
produces a *series* — a function defined on every positive integer, not just three
specific points.

Define `produce_number(i)` that returns `i * i`. This is the natural "rule" suggested by
the data points `1, 4, 9, 16, ...`.

Then define an *alternative* `produce_number_alt(i)` that returns `i * i` for `i < 5`
but switches to `1979 + i` for `i >= 5`. Both functions agree on the first four points,
but they diverge from then on. This is the lesson: there are infinitely many functions
that match any finite prefix of a series.

Print `produce_number(j)` for `j` in `1..9`.
