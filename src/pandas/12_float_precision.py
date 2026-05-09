#!/usr/bin/env python

"""Solution to exercise 12: digit truncation, subnormals, and underflow."""

import pandas as pd

df = pd.DataFrame({"fare": [7.25, 71.28, 13.0, 8.05]})

df.iat[0, 0] = 1.234567890123456789
print(df["fare"][0])

df.iat[0, 0] = 0.1 ** 320
print(df["fare"][0])

df.iat[0, 0] = 0.1 ** 1000
print(df["fare"][0])
