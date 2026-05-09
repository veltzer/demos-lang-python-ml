#!/usr/bin/env python

"""Solution to exercise 02: inspect column dtypes with info(), dtypes, and items()."""

import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [70000.5, 50000.0, 90000.25],
    "active": [True, False, True],
})

df.info()
print("==========================================")
print(df.dtypes)
print("==========================================")
for column_name, column_data in df.items():
    print(f"{column_name} {column_data.dtype}")
