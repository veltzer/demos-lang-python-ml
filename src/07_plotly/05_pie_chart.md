# Exercise 05: Pie Chart

`px.pie` is one of the few cases where plotly's API is genuinely simpler than
matplotlib's. Pass a DataFrame, name the value column, name the label column.

Given:

```
df = pd.DataFrame({
    "browser":  ["Chrome", "Safari", "Firefox", "Edge", "Other"],
    "share":    [65, 18, 8, 5, 4],
})
```

1. Draw `px.pie(df, names="browser", values="share")`.
2. Title `"Browser market share"`.
3. Save to `/tmp/05_pie_chart.html`.
