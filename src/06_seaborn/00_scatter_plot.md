# Exercise 01: Scatter Plot

`sns.scatterplot` is the seaborn equivalent of `plt.scatter`, designed to consume a
DataFrame directly via column names.

Given:

```text
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5, 6, 7, 8],
    "y": [2, 3, 5, 4, 8, 7, 9, 11],
})
```

1. Use `sns.scatterplot(data=df, x="x", y="y")` to draw the scatter.
2. Save the resulting figure to `/tmp/01_scatter_plot.png` using `plt.savefig`.

Note: every solution in this folder uses `plt.savefig` instead of `plt.show()` so the
script can run without a display.
