# Exercise 00: Scatter Plot with Plotly

`plotly.express` is the high-level API — same DataFrame-and-column-names model as
seaborn, but the output is interactive HTML you can zoom, pan, and hover over.

Given:

```text
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5, 6, 7, 8],
    "y": [2, 3, 5, 4, 8, 7, 9, 11],
})
```

1. Use `px.scatter(df, x="x", y="y")` to build the figure.
2. Save it as an HTML file with `fig.write_html("/tmp/00_scatter_plot.html")`.

Note: every solution in this folder writes interactive HTML to `/tmp/` rather than
calling `fig.show()` so the script can run without a browser.
