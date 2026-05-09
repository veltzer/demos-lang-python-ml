# Exercise 04: Box Plot per Category

`px.box` draws one box per value of a categorical column — quickest way to compare
distributions across groups.

Build 200 samples per group from `np.random.default_rng(0)`:

```
n = 200
rng = np.random.default_rng(0)
df = pd.DataFrame({
    "group": ["A"] * n + ["B"] * n + ["C"] * n,
    "value": np.concatenate([
        rng.normal(0, 1, n),
        rng.normal(1, 2, n),
        rng.normal(-1, 0.5, n),
    ]),
})
```

1. Draw `px.box(df, x="group", y="value")`.
2. Title `"Distribution by group"`.
3. Save to `/tmp/04_box_plot.html`.
