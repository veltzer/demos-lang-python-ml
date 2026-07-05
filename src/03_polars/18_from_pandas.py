#!/usr/bin/env python

"""Solution to exercise 19: convert between pandas and polars DataFrames."""

import pandas as pd
import polars as pl

pdf = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
})

pldf = pl.from_pandas(pdf)
print(pldf)
print(type(pldf))

back = pldf.to_pandas()
print(back)
print(type(back))
