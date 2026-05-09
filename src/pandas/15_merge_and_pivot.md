# Exercise 15: Merge and Pivot

The two essential reshaping tools:

- `pd.merge` joins two DataFrames on a shared key (like a SQL JOIN).
- `DataFrame.pivot_table` reshapes long-format data into a 2-D summary, with one axis
  per grouping column and one cell per aggregated value.

Given:

```
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name":   ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "dept_id": [10, 20, 10, 30, 20],
})

departments = pd.DataFrame({
    "dept_id":   [10, 20, 30],
    "dept_name": ["eng", "sales", "hr"],
})

sales = pd.DataFrame({
    "name":    ["Alice", "Alice", "Bob", "Bob",  "Eve",  "Eve"],
    "quarter": ["Q1",    "Q2",    "Q1",  "Q2",   "Q1",   "Q2"],
    "revenue": [100,     150,     80,    90,     200,    180],
})
```

1. Inner-merge `employees` with `departments` on `dept_id` and print the result.
2. From `sales`, build a pivot table with `name` on the rows, `quarter` on the columns,
   and `revenue` as the values. Print it.
3. Add `margins=True` to that same pivot to include a totals row and column. Print it.
