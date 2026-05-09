# Exercise: Series from Any Set of Numbers

The puzzle, written informally:

> Guess the next number in the series.
>
> ```
> 1 4 9 16 25     <- "obvious" answer is the next square: 25
> 1 4 9 16 1979   <- but I can equally claim the next number is 1979
> ```

This is the same trick as the previous exercise (`print_series`), but condensed into a
**single closed-form polynomial** that passes through *exactly three* user-chosen points.

For the three points `(1, 1)`, `(2, 4)`, `(3, 1979)`, the Lagrange polynomial is:

```
fun(x) = 1    * (x-2)(x-3) / ((1-2)(1-3))
       + 4    * (x-1)(x-3) / ((2-1)(2-3))
       + 1979 * (x-1)(x-2) / ((3-1)(3-2))
```

Simplifying the denominators:
- first  term: `(x-2)(x-3) / 2`
- second term: `(x-1)(x-3) * (-4)`
- third  term: `(x-1)(x-2) * (1979/2)`

Tasks:

1. Implement `fun(x)` exactly as the simplified Lagrange polynomial above.
2. Print `int(fun(i))` for `i` in `1..3`. The output must be `1`, `4`, `1979`.

Lesson: given any finite set of `(x, y)` points, you can always produce a polynomial of
degree `n - 1` that hits all of them. So the question "what's the next number in the
series?" has *no* unique answer in general.
