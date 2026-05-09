#!/usr/bin/env python

"""Solution to exercise 15: merge two DataFrames and build a pivot_table."""

import pandas as pd

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "dept_id": [10, 20, 10, 30, 20],
})

departments = pd.DataFrame({
    "dept_id": [10, 20, 30],
    "dept_name": ["eng", "sales", "hr"],
})

sales = pd.DataFrame({
    "name": ["Alice", "Alice", "Bob", "Bob", "Eve", "Eve"],
    "quarter": ["Q1", "Q2", "Q1", "Q2", "Q1", "Q2"],
    "revenue": [100, 150, 80, 90, 200, 180],
})

merged = pd.merge(employees, departments, on="dept_id", how="inner")
print(merged)

pivot = sales.pivot_table(index="name", columns="quarter", values="revenue")
print(pivot)

pivot_with_totals = sales.pivot_table(
    index="name", columns="quarter", values="revenue", margins=True,
)
print(pivot_with_totals)
