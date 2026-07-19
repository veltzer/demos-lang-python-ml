# Exercise 11: Correlation Heatmap

`sns.heatmap` is the standard way to visualize a correlation matrix. With `annot=True` it
overlays the numeric values inside each cell.

Given:

```text
df = pd.DataFrame({
    "age":      [22, 38, 26, 35, 27, 54, 14, 4, 58, 20],
    "fare":     [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 30.07, 16.7, 26.55, 8.05],
    "survived": [0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    "pclass":   [3, 1, 3, 1, 3, 1, 2, 3, 1, 3],
})
```

1. Compute `df.corr()`.
2. Pass the result to `sns.heatmap` with `annot=True`, `cmap="coolwarm"`, and
   `vmin=-1, vmax=1`.
3. Title `"Correlation matrix"`.
4. Save to `/tmp/11_heatmap.png`.
