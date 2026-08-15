#!/usr/bin/env python

"""Solution to exercise 10: join two DataFrames on a shared key."""

import polars as pl

employees = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "dept_id": [1, 2, 2],
})
departments = pl.DataFrame({
    "dept_id": [1, 2, 3],
    "dept_name": ["eng", "sales", "hr"],
})

print(employees.join(departments, on="dept_id", how="inner"))
print(employees.join(departments, on="dept_id", how="left"))
print(departments.join(employees, on="dept_id", how="anti"))
