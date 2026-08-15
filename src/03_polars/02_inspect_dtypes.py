#!/usr/bin/env python

"""Solution to exercise 03: inspect the schema and dtypes of a DataFrame."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "height": [1.70, 1.82, 1.65],
    "active": [True, False, True],
})

print(df.schema)
print(df.dtypes)
print(df.estimated_size("kb"), "kb")
