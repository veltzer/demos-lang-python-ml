#!/usr/bin/env python

"""Solution to exercise 05: filter rows with boolean expressions."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

print(df.filter(pl.col("age") > 30))
print(df.filter((pl.col("age") > 25) & (pl.col("salary") < 100000)))
print(df.filter(pl.col("name").is_in(["Alice", "Eve"])))
