# Exercise 07: Histogram

Histograms split a continuous variable into bins and show the count per bin. They are the
quickest way to see the distribution of a column.

Build a small DataFrame with two columns and split a histogram by group:

```
df = pd.DataFrame({
    "Age":      [22, 38, 26, 35, 27, 54, 14, 4, 58, 20, 39, 14, 55, 2, 31, 35],
    "Survived": [0,  1,  1,  1,  0,  0,  1,  1, 0,  1,  0,  0,  1,  1, 0,  0],
})
```

1. Use `df.hist(column="Age", by="Survived")` to draw two histograms side-by-side, one
   per `Survived` value.
2. Save the resulting figure to `/tmp/07_histogram.png`. Hint: `df.hist` returns an
   array of `Axes` — get the figure via `axes[0].get_figure()`.
