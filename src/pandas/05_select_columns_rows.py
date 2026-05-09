#!/usr/bin/env python

"""Solution to exercise 05: column / row selection with .loc and .iloc."""

import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
        "age": [30, 25, 35, 28, 40],
        "salary": [70000, 50000, 90000, 65000, 120000],
    },
    index=["a", "b", "c", "d", "e"],
)

print(df["name"])
print(df.loc["c"])
print(df.iloc[1])
print(df.loc[["b", "d"], ["age", "salary"]])
