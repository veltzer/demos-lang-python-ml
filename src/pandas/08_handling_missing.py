#!/usr/bin/env python

"""Solution to exercise 08: detect, fill, and drop missing values."""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana"],
    "age": [30, np.nan, 35, np.nan],
    "salary": [70000, 50000, np.nan, 65000],
})

print(df.isna())
print(df.isna().sum())

filled = df.copy()
filled["age"] = filled["age"].fillna(filled["age"].mean())
filled["salary"] = filled["salary"].fillna(0)
print(filled)

print(df.dropna())
