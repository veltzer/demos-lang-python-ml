# Exercise 11: Correlation Heatmap

`px.imshow` displays a 2-D array as a color-mapped image. Pass it the result of
`DataFrame.corr()` and you get an interactive correlation heatmap with hover tooltips
showing each cell's exact value.

Given:

```
df = pd.DataFrame({
    "age":      [22, 38, 26, 35, 27, 54, 14, 4, 58, 20],
    "fare":     [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 30.07, 16.7, 26.55, 8.05],
    "survived": [0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    "pclass":   [3, 1, 3, 1, 3, 1, 2, 3, 1, 3],
})
```

1. Compute `corr = df.corr()`.
2. Draw `px.imshow(corr, text_auto=True, color_continuous_scale="RdBu",
   zmin=-1, zmax=1)`. `text_auto=True` overlays the numeric value on each cell.
3. Title `"Correlation matrix"`.
4. Save to `/tmp/11_heatmap.html`.
