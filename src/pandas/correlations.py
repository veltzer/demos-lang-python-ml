#!/usr/bin/python3

"""
Showing how to calculate correlations using pandas
"""

import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
df['SexNew']=np.where(df['Sex']=="male",0,1)
# This next line doesnt matter since the 'corr' method does not take non-numeric
# columns into account...
df.drop('Sex', axis=1, inplace=True)
print(df.corr())
# print(df.columns)
