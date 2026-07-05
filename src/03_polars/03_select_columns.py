#!/usr/bin/env python

"""Solution to exercise 04: select columns and rows with the expression API."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

print(df.select("name", "salary"))
print(df.select(pl.col("age"), pl.col("salary")))
print(df.head(2))
print(df["name"])
