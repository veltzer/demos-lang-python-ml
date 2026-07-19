# Exercise 02: Bar Chart

`px.bar` draws a vertical bar chart with one bar per row of the input DataFrame.

Given:

```text
df = pd.DataFrame({
    "fruit":    ["apples", "oranges", "bananas", "pears", "grapes"],
    "quantity": [23, 17, 35, 12, 28],
})
```

1. Draw `px.bar(df, x="fruit", y="quantity")`.
2. Title `"Fruit inventory"`.
3. Save to `/tmp/02_bar_chart.html`.
