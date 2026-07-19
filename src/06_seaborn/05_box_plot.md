# Exercise 06: Box Plot

A box plot shows the median, the inter-quartile range (IQR), and outliers — making it
easy to compare the spread of a numeric column across categories.

Build a DataFrame with 200 samples per group from `np.random.default_rng(0)`:

```text
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

1. Draw `sns.boxplot(data=df, x="group", y="value")`.
2. Title `"Distribution of value by group"`.
3. Save to `/tmp/06_box_plot.png`.
