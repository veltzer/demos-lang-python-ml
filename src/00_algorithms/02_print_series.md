# Exercise: Generate Any Continuation You Like

The series `1, 4, 9, 16, ?` has an obvious answer: `25` (the next square). But you can
construct a polynomial of degree 4 that passes through the points `(1, 1)`, `(2, 4)`,
`(3, 9)`, `(4, 16)` and *any* fifth value you choose at `x = 5`.

This exercise demonstrates the construction explicitly using *Lagrange interpolation* —
written out by hand rather than using `numpy.polyfit`.

Tasks:

1. Define `produce_number(i)` returning `i * i` (the "obvious" answer, `f(5) = 25`).
2. Define `produce_number_alt(i)` returning `i * i` for `i < 5` and `1979 + i - 5` for
   `i >= 5` (a piecewise alternative that gives `f(5) = 1979`).
3. Define `produce_number_alt_2(i)` as a single explicit polynomial expression that
   passes through `(1, 1)`, `(2, 4)`, `(3, 9)`, `(4, 16)`, `(5, 1979)`. The Lagrange form
   for these five points is:

   ```
   f(i) = 1   * (i-2)(i-3)(i-4)(i-5) / ((1-2)(1-3)(1-4)(1-5))
        + 4   * (i-1)(i-3)(i-4)(i-5) / ((2-1)(2-3)(2-4)(2-5))
        + 9   * (i-1)(i-2)(i-4)(i-5) / ((3-1)(3-2)(3-4)(3-5))
        + 16  * (i-1)(i-2)(i-3)(i-5) / ((4-1)(4-2)(4-3)(4-5))
        + 1979* (i-1)(i-2)(i-3)(i-4) / ((5-1)(5-2)(5-3)(5-4))
   ```

   Simplify the constant denominators and write out the function.
4. Print `int(produce_number_alt_2(j))` for `j` in `1..9`.

The first four printed values must be `1, 4, 9, 16`. The fifth must be `1979`. The
remaining four are whatever the polynomial extrapolates to — and the values will be
absurdly large, demonstrating the danger of high-degree exact fits.
