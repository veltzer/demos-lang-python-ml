# Exercise 06: Filtering Rows with Boolean Masks

Given:

```text
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age":    [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
    "dept":   ["eng", "sales", "eng", "hr", "eng"],
})
```

Print:

1. all rows where `salary` is greater than `60000`
2. all rows where `dept == "eng"` AND `age >= 30`
3. all rows where `dept` is either `"sales"` or `"hr"` (use `.isin`)
