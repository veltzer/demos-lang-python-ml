#!/usr/bin/env python

"""Solution to exercise 06: boolean filtering with &, |, and isin."""

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age": [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
    "dept": ["eng", "sales", "eng", "hr", "eng"],
})

print(df[df["salary"] > 60000])
print(df[(df["dept"] == "eng") & (df["age"] >= 30)])
print(df[df["dept"].isin(["sales", "hr"])])
