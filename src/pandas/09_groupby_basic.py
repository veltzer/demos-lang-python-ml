#!/usr/bin/env python

"""Solution to exercise 10: groupby with single and multiple keys."""

import pandas as pd

df = pd.DataFrame({
    "dept": ["eng", "sales", "eng", "hr", "eng", "sales", "hr"],
    "gender": ["F", "M", "M", "F", "F", "F", "M"],
    "salary": [70000, 50000, 90000, 65000, 120000, 55000, 60000],
})

print(df.groupby("dept").size())
print(df.groupby("dept")["salary"].mean())
print(df.groupby(["dept", "gender"]).size())
