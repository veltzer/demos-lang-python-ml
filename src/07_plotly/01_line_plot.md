# Exercise 01: Line Plot with Markers

`px.line` draws a connected line. Pass `markers=True` to also show the data points.

Build a DataFrame holding monthly sales for a year:

```text
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "sales": [120, 135, 150, 160, 180, 200, 210, 205, 190, 170, 150, 140],
})
```

1. Plot it with `px.line(df, x="month", y="sales", markers=True)`.
2. Set the title to `"Monthly sales"` via `fig.update_layout(title=...)`.
3. Save to `/tmp/01_line_plot.html`.
