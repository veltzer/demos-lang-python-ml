#!/usr/bin/env python

"""Solution to exercise 11: build a lazy query and collect it."""

import polars as pl

lf = pl.LazyFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "dept": ["eng", "eng", "sales", "sales", "sales"],
    "salary": [90000, 70000, 65000, 80000, 75000],
})

query = (
    lf.filter(pl.col("salary") > 60000)
    .group_by("dept")
    .agg(pl.col("salary").mean().alias("avg_salary"))
    .sort("dept")
)

print(query.explain())
print(query.collect())
