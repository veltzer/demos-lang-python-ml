#!/usr/bin/env python

"""Solution to exercise 06: add and derive columns with with_columns."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [70000, 50000, 90000],
})

df = df.with_columns(
    (pl.col("salary") * 1.10).round(2).alias("raised"),
    pl.col("name").str.to_uppercase().alias("upper_name"),
    (pl.col("salary") > 60000).alias("well_paid"),
)

print(df)
