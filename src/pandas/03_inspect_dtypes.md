# Exercise 03: Inspect Column Dtypes

Given the DataFrame:

```
df = pd.DataFrame({
    "id":      [1, 2, 3],
    "name":    ["Alice", "Bob", "Charlie"],
    "salary":  [70000.5, 50000.0, 90000.25],
    "active":  [True, False, True],
})
```

1. Print the `dtypes` of every column.
2. Iterate over the columns with `df.items()` and print one line per column in the format
   `<column_name> <dtype>`.
