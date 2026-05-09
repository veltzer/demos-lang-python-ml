# Exercise: Newton-Raphson Root Finder

Implement the [Newton-Raphson
method](https://en.wikipedia.org/wiki/Newton%27s_method) to find a root of a real-valued
function `f`. The method repeats:

```
x_{n+1} = x_n - f(x_n) / f'(x_n)
```

When `f'` is not provided analytically, approximate it numerically with a centered
difference:

```
f'(x) ≈ (f(x + dx) - f(x - dx)) / (2 * dx)
```

## Tasks

1. Implement `newton_raphson(f, initial_guess=1.0, max_iterations=1000, dx=0.001,
   precision=0.001)` that:
   - returns `x` once `|f'(x)| < precision` (treated as a converged root),
   - returns `None` if `max_iterations` is exhausted without convergence.
2. Define three test functions: `square(x) = x*x`, `third(x) = x*x*x`, and
   `identity(x) = x`.
3. Call `newton_raphson(identity)` and print the result. Expected: a value very close to
   `0` (the root of `f(x) = x`).

## Notes

- The "convergence on small derivative" stopping rule is unusual — the method usually
   stops when `|f(x)| < precision`. Both work for these test cases; the derivative-based
   rule is just simpler when you don't have an analytic derivative.
- `newton_raphson(square)` will run into trouble — at the root `x = 0` the derivative is
   also `0`, so the method has to either lose convergence or stop early. Try it and see
   what happens.
