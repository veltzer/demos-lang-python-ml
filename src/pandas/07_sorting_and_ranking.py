#!/usr/bin/env python

"""Solution to exercise 07: sort_values single + multi-key, and rank."""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

print(df.sort_values("age"))
print(df.sort_values("salary", ascending=False))
print(df.sort_values(["age", "salary"], ascending=[True, False]))

df["salary_rank"] = df["salary"].rank(method="min", ascending=False).astype(int)
print(df)
