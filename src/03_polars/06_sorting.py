#!/usr/bin/env python

"""Solution to exercise 07: sort a DataFrame by one or more columns."""

import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "dept": ["eng", "eng", "sales", "sales"],
    "salary": [90000, 70000, 65000, 80000],
})

print(df.sort("salary"))
print(df.sort("salary", descending=True))
print(df.sort(["dept", "salary"], descending=[False, True]))
