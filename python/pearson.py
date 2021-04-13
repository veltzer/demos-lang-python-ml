#!/usr/bin/python3

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df['SexNew']=np.where(df['Sex']=="male",0,1)
# This next line doesnt matter since the 'corr' method does not take non-numeric
# columns into account...
df.drop('Sex', axis=1, inplace=True)
print(df.corr())
# print(df.columns)
