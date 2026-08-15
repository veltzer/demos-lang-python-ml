#!/usr/bin/env python

"""Solution to exercise 02: build a polars DataFrame from a dict of columns."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

print(df)
print(df.shape)
print(df.columns)
