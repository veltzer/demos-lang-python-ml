#!/usr/bin/python3

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', index_col=0)
df['SexNew']=np.where(df['Sex']=="male",3,7)
df.drop('Sex', axis=1, inplace=True)
print(df.columns)
print(df.corr())
