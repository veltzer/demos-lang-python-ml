#!/usr/bin/env python

"""Solution to exercise 15: reshape long data into a wide pivot table."""

import polars as pl

df = pl.DataFrame({
    "dept": ["eng", "eng", "sales", "sales"],
    "quarter": ["Q1", "Q2", "Q1", "Q2"],
    "revenue": [100, 120, 80, 95],
})

wide = df.pivot(
    on="quarter",
    index="dept",
    values="revenue",
    aggregate_function="sum",
)

print(wide)
