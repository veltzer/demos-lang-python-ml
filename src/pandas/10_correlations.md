# Exercise 11: Correlations

`DataFrame.corr` computes the pairwise Pearson correlation of every numeric column.
Non-numeric columns are silently dropped, so you usually want to encode categorical
columns to numeric form first.

Given:

```
df = pd.DataFrame({
    "sex":      ["male", "female", "female", "male", "female", "male"],
    "age":      [22, 38, 26, 35, 27, 54],
    "fare":     [7.25, 71.28, 7.92, 53.10, 8.05, 51.86],
    "survived": [0, 1, 1, 1, 0, 0],
})
```

1. Add a column `sex_num` that is `0` for `"male"` and `1` for `"female"`
   (use `numpy.where`).
2. Drop the original string `sex` column.
3. Print the correlation matrix of the resulting DataFrame.
