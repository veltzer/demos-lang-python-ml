# Exercise 04: Series vs DataFrame

When you select a single column from a DataFrame, you get a `Series`.
When you select multiple columns, you get a `DataFrame`.

Given:

```
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie"],
    "age":    [30, 25, 35],
    "salary": [70000, 50000, 90000],
})
```

1. Print `type(df)`.
2. Select the `"age"` column and print its type. Confirm with `isinstance(..., pd.Series)`
   and print `"yes!"` if true.
3. Select the columns `["age", "salary"]` and print the result's type. Confirm it is a
   `DataFrame` and print `"yes, DataFrame!"` if true.
