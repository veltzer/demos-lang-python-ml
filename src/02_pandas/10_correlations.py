#!/usr/bin/env python

"""Solution to exercise 11: encode categorical column then compute corr matrix."""

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "sex": ["male", "female", "female", "male", "female", "male"],
    "age": [22, 38, 26, 35, 27, 54],
    "fare": [7.25, 71.28, 7.92, 53.10, 8.05, 51.86],
    "survived": [0, 1, 1, 1, 0, 0],
})

df["sex_num"] = np.where(df["sex"] == "male", 0, 1)
df.drop("sex", axis=1, inplace=True)
print(df.corr())
