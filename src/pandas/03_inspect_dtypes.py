#!/usr/bin/env python

"""Solution to exercise 03: inspect column dtypes via .dtypes and .items()."""

import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [70000.5, 50000.0, 90000.25],
    "active": [True, False, True],
})

print(df.dtypes)
print("==========================================")
for column_name, column_data in df.items():
    print(f"{column_name} {column_data.dtype}")
