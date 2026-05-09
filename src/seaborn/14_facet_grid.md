# Exercise 14: Facet Grid

A facet grid splits a single dataset into a grid of subplots according to one or two
categorical columns, with the same plot drawn on each facet. This is the canonical way
to ask "is the relationship between x and y the same across each subgroup?".

Build a synthetic dataset with two grouping columns:

```
import numpy as np

rng = np.random.default_rng(0)
n = 60
df = pd.DataFrame({
    "x":   np.tile(np.arange(n), 4),
    "y":   np.concatenate([
        rng.normal(0, 1, n),     # day=Mon, group=A
        rng.normal(2, 1, n),     # day=Mon, group=B
        rng.normal(0, 1, n) + 5, # day=Tue, group=A
        rng.normal(2, 1, n) + 5, # day=Tue, group=B
    ]),
    "day":   ["Mon"] * (2 * n) + ["Tue"] * (2 * n),
    "group": (["A"] * n + ["B"] * n) * 2,
})
```

1. Build the grid: `g = sns.FacetGrid(df, col="day", row="group")`.
2. Draw a scatter on every facet: `g.map_dataframe(sns.scatterplot, x="x", y="y")`.
3. Save to `/tmp/14_facet_grid.png` via `g.figure.savefig`.
