# Exercise 05: Selecting Rows and Columns

Given:

```text
df = pd.DataFrame(
    {
        "name":   ["Alice", "Bob", "Charlie", "Dana", "Eve"],
        "age":    [30, 25, 35, 28, 40],
        "salary": [70000, 50000, 90000, 65000, 120000],
    },
    index=["a", "b", "c", "d", "e"],
)
```

Print:

1. just the `"name"` column
2. the row with index label `"c"` (using `.loc`)
3. the second row (using `.iloc`)
4. the `"age"` and `"salary"` columns for rows `"b"` and `"d"` (using `.loc`)
