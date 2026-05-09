#!/usr/bin/env python

"""Solution to exercise 04: distinguish Series from DataFrame on selection."""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "salary": [70000, 50000, 90000],
})

print(type(df))

age = df["age"]
print(type(age))
if isinstance(age, pd.Series):
    print("yes!")

subset = df[["age", "salary"]]
print(type(subset))
if isinstance(subset, pd.DataFrame):
    print("yes, DataFrame!")
