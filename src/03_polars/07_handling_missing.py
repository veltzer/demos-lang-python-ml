#!/usr/bin/env python

"""Solution to exercise 08: detect and fill missing (null) values."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "age": [30, None, 35, None],
    "salary": [70000, 50000, None, 65000],
})

print(df.null_count())
print(df.drop_nulls())
print(df.with_columns(
    pl.col("age").fill_null(strategy="mean"),
    pl.col("salary").fill_null(0),
))
