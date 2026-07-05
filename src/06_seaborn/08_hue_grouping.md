# Exercise 09: Splitting by `hue`

`hue=` is seaborn's way of adding a third dimension to almost any plot: each value of the
`hue` column gets its own color, and the points/bars are grouped accordingly. No looping.

Given a synthetic 3-feature dataset:

```
import numpy as np

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "label": ["A"] * n + ["B"] * n,
})
```

1. Draw `sns.scatterplot(data=df, x="x", y="y", hue="label")` — points should be colored
   by `label`.
2. Title `"Two clusters"`.
3. Save to `/tmp/09_hue_grouping.png`.
