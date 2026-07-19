# Exercise 08: Count Plot

`sns.countplot` is `barplot` for the special case of "just count the occurrences of each
category" — like `value_counts` rendered as a chart.

Given:

```text
df = pd.DataFrame({
    "color": ["red", "blue", "red", "green", "blue", "blue", "red", "red",
              "green", "blue", "red", "blue"],
})
```

1. Draw `sns.countplot(data=df, x="color")`.
2. Set the title to `"Color frequencies"`.
3. Save to `/tmp/08_count_plot.png`.
