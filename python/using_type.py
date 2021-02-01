#!/usr/bin/python3

import pandas as pd

df = pd.read_csv('data.csv', index_col=0)
print(type(df))
x = df['Survived']
print(type(x))
