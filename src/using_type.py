#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('data.csv', index_col=0)
print(type(df))
x = df['Survived']
print(type(x))
if isinstance(x, pd.core.series.Series):
    print("yes!")
