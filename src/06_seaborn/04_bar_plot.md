# Exercise 05: Bar Plot

`sns.barplot` shows the mean of a numeric column for each value of a categorical column,
along with a confidence interval drawn as an error bar.

Given:

```text
df = pd.DataFrame({
    "dept":   ["eng", "eng", "eng", "sales", "sales", "sales", "hr", "hr", "hr"],
    "salary": [70000, 90000, 120000, 50000, 55000, 60000, 65000, 60000, 62000],
})
```

1. Draw `sns.barplot(data=df, x="dept", y="salary")`.
2. Set the title to `"Mean salary by department"`.
3. Save to `/tmp/05_bar_plot.png`.
