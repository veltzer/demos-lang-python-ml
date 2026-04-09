#!/usr/bin/env python

"""
How to use the "type" function
"""

import pandas as pd
from pandas.core.series import Series

df = pd.read_csv('data.csv', index_col=0)
print(type(df))
x = df['Survived']
print(type(x))
if isinstance(x, Series):
    print("yes!")
