# Exercise: Newton-Raphson — Roots and Minima

Implement the [Newton-Raphson
method](https://en.wikipedia.org/wiki/Newton%27s_method) and apply it to two related
problems.

## Part 1: Find a root of `f`

The classic Newton-Raphson update for finding `x` such that `f(x) = 0`:

```
x_{n+1} = x_n - f(x_n) / f'(x_n)
```

When `f'` is not provided analytically, approximate it with a centered difference:

```
f'(x) ≈ (f(x + dx) - f(x - dx)) / (2 * dx)
```

Stop when `|f(x)| < precision`.

### Tasks

1. Implement `newton_raphson_root(f, initial_guess=1.0, max_iterations=1000, dx=0.001,
   precision=0.001)`. Return the converged `x`, or `None` if `max_iterations` was
   exhausted.
2. Test on `cube(x) = x*x*x - 8`. The root is `x = 2`.

## Part 2: Find a minimum of `f`

A minimum (or maximum) of `f` is a root of its **derivative**. So you can find a minimum
of `f` by running Newton-Raphson **on `f'`** instead of `f`. This requires the second
derivative `f''` (or, again, a numerical approximation).

The update becomes:

```
x_{n+1} = x_n - f'(x_n) / f''(x_n)
```

Stop when `|f'(x)| < precision`.

### Tasks

1. Implement `newton_raphson_min(f, initial_guess=1.0, max_iterations=1000, dx=0.001,
   precision=0.001)` using numerical first and second derivatives.
2. Test on `square(x) = x*x`. The minimum is at `x = 0`. (You'll see N-R converge in one
   step here because `square` is exactly quadratic.)
3. Test on `quartic(x) = (x - 3) ** 4 + 5`. The minimum is at `x = 3`.

## Reflection

- Newton-Raphson converges very fast (quadratically) when it converges, but it can
  diverge if the initial guess is far from the answer or if the function is poorly
  behaved.
- Pure-derivative stopping (`|f'(x)| < precision`) finds *any* extremum — minimum,
  maximum, or saddle. To verify you actually have a minimum, also check that
  `f''(x) > 0`.
