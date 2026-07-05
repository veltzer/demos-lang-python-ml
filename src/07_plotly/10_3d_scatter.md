# Exercise 10: 3-D Scatter Plot

`px.scatter_3d` is one of plotly's biggest wins — interactive 3-D rotation in the
browser, no separate library needed.

Generate 300 points from three Gaussian clusters in 3-D:

```
import numpy as np

rng = np.random.default_rng(0)
n = 100
df = pd.DataFrame({
    "x":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "y":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "z":     np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n), rng.normal(-3, 1, n)]),
    "label": ["A"] * n + ["B"] * n + ["C"] * n,
})
```

1. Draw `px.scatter_3d(df, x="x", y="y", z="z", color="label")`.
2. Save to `/tmp/10_3d_scatter.html`.
3. Open the HTML and click-drag to rotate the cube.
