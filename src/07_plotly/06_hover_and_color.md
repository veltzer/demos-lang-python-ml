# Exercise 06: Color by Column and Custom Hover

The big advantage of plotly over matplotlib is *interactivity*. You can color points by a
categorical column with `color=`, and you can control exactly what shows in the
hover-tooltip with `hover_data=`.

Build:

```
import numpy as np

rng = np.random.default_rng(0)
n = 50
df = pd.DataFrame({
    "x":         np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "y":         np.concatenate([rng.normal(0, 1, n), rng.normal(3, 1, n)]),
    "label":     ["A"] * n + ["B"] * n,
    "weight":    rng.uniform(1, 10, 2 * n),
})
```

1. Draw `px.scatter(df, x="x", y="y", color="label", size="weight",
   hover_data=["weight"])`.
2. Open the resulting HTML and hover over points to verify each tooltip shows `x`, `y`,
   `label`, and `weight`.
3. Save to `/tmp/06_hover_and_color.html`.
