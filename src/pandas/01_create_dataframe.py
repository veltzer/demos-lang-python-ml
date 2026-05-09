#!/usr/bin/env python

"""Solution to exercise 02: build a DataFrame from a dict and inspect it."""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "age": [30, 25, 35, 28],
    "salary": [70000, 50000, 90000, 65000],
})

print(df)
print(df.shape)
print(df.columns)
print(df.head(2))
