#!/usr/bin/env python

"""Solution to exercise 13: conditional columns with when/then/otherwise."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "score": [92, 74, 58, 85],
})

df = df.with_columns(
    pl.when(pl.col("score") >= 90)
    .then(pl.lit("A"))
    .when(pl.col("score") >= 70)
    .then(pl.lit("B"))
    .otherwise(pl.lit("C"))
    .alias("grade")
)

print(df)
