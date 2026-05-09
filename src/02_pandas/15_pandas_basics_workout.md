# Exercise 16: Pandas Basics Workout

Practice the most common DataFrame manipulations in one go. Start from:

```
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age":    [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})
```

Tasks:

1. **Add a column** `salary_plus_one` that equals `salary + 1`.
2. **Remove a column** — drop `salary_plus_one` you just added.
3. **Rename a column** — rename `salary` to `income`.
4. **Remove a row** — drop the row with `name == "Bob"`.
5. **Add a row** — append a new row for `("Frank", 33, 80000)`.
6. **Inspect a column type** — print `df["age"].dtype`.
7. **Change a column type** — convert `age` from `int64` to `float64`.
8. **Summary stats** — for the `income` column print:
   - mean
   - variance
   - 25th, 50th, 75th percentiles (use `.quantile([0.25, 0.5, 0.75])`)

Bonus: invent two more transformations and add them.
