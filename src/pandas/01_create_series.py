#!/usr/bin/env python

"""Solution to exercise 01: build a labeled Series and inspect it."""

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])

print(s)
print(s.dtype)
print(s.values)
print(s.index)
