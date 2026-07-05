#!/usr/bin/env python

"""Solution to exercise 09: aggregate with group_by and multiple expressions."""

import polars as pl

df = pl.DataFrame({
    "dept": ["eng", "eng", "sales", "sales", "sales"],
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "salary": [90000, 70000, 65000, 80000, 75000],
})

agg = df.group_by("dept").agg(
    pl.len().alias("headcount"),
    pl.col("salary").mean().alias("avg_salary"),
    pl.col("salary").max().alias("max_salary"),
).sort("dept")

print(agg)
