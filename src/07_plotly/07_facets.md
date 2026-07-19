# Exercise 07: Faceting

Pass `facet_row=` and/or `facet_col=` to any `plotly.express` plotting function and you
get a grid of subplots — one per value of the facet column. Same idea as seaborn's
`FacetGrid` but with a one-line API.

Build a synthetic dataset with two grouping columns:

```text
import numpy as np

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x":     np.tile(np.arange(n), 4),
    "y":     np.concatenate([
        rng.normal(0, 1, n),
        rng.normal(2, 1, n),
        rng.normal(0, 1, n) + 5,
        rng.normal(2, 1, n) + 5,
    ]),
    "day":   ["Mon"] * (2 * n) + ["Tue"] * (2 * n),
    "group": (["A"] * n + ["B"] * n) * 2,
})
```

1. Draw `px.scatter(df, x="x", y="y", facet_row="group", facet_col="day")` — a 2x2
   grid of subplots.
2. Save to `/tmp/07_facets.html`.
