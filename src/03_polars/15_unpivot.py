#!/usr/bin/env python

"""Solution to exercise 16: melt a wide table into long form with unpivot."""

import polars as pl

wide = pl.DataFrame({
    "dept": ["eng", "sales"],
    "Q1": [100, 80],
    "Q2": [120, 95],
})

long = wide.unpivot(
    index="dept",
    on=["Q1", "Q2"],
    variable_name="quarter",
    value_name="revenue",
).sort(["dept", "quarter"])

print(long)
