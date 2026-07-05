#!/usr/bin/env python

"""Solution to exercise 17: window expressions with over() per group."""

import polars as pl

df = pl.DataFrame({
    "dept": ["eng", "eng", "sales", "sales", "sales"],
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "salary": [90000, 70000, 65000, 80000, 75000],
})

df = df.with_columns(
    pl.col("salary").mean().over("dept").alias("dept_avg"),
    (pl.col("salary") - pl.col("salary").mean().over("dept")).alias("diff_from_avg"),
    pl.col("salary").rank(descending=True).over("dept").alias("rank_in_dept"),
)

print(df.sort(["dept", "rank_in_dept"]))
