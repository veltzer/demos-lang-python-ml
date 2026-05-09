# Exercise 12: Pair Plot

`sns.pairplot` produces a grid of scatter plots — one for every pair of numeric columns —
with a histogram on the diagonal. Pass `hue=` to color points by a categorical column.
This is the fastest way to scan a small numeric dataset for visible relationships.

Build a synthetic 3-feature dataset with two clusters:

```
import numpy as np

rng = np.random.default_rng(0)
n = 80
df = pd.DataFrame({
    "x":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "z":     np.concatenate([rng.normal(0, 1, n), rng.normal(0, 1, n)]),
    "label": ["A"] * n + ["B"] * n,
})
```

1. Draw `sns.pairplot(df, hue="label")`. Note: `pairplot` returns a `PairGrid`, not a plain
   figure; access its underlying figure via `.figure` to save it.
2. Save to `/tmp/12_pair_plot.png`.
