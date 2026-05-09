#!/usr/bin/env python

"""Solution to exercise 16: walk through the pandas basics workout end-to-end."""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})

df["salary_plus_one"] = df["salary"] + 1
df = df.drop("salary_plus_one", axis=1)
df = df.rename(columns={"salary": "income"})
df = df[df["name"] != "Bob"].reset_index(drop=True)

new_row = pd.DataFrame([{"name": "Frank", "age": 33, "income": 80000}])
df = pd.concat([df, new_row], ignore_index=True)

print(df["age"].dtype)
df["age"] = df["age"].astype(float)
print(df["age"].dtype)

print(f"mean:     {df['income'].mean():.2f}")
print(f"variance: {df['income'].var():.2f}")
print(df["income"].quantile([0.25, 0.5, 0.75]))
print(df)
