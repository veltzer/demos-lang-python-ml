#!/usr/bin/env python

"""Solution to exercise 14: summary statistics over numeric columns."""

import polars as pl

df = pl.DataFrame({
    "salary": [70000, 50000, 90000, 65000, 120000],
    "age": [30, 25, 35, 28, 40],
})

print(df.describe())
print(df.select(
    pl.col("salary").mean().alias("mean"),
    pl.col("salary").std().alias("std"),
    pl.col("salary").median().alias("median"),
    pl.col("salary").quantile(0.75).alias("q75"),
))
