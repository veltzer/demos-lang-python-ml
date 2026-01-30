#!/usr/bin/env python

"""
This example show how to normalize an entire data frame in preparation
for an algorithm that needs normalized data (e.g. KNN).
"""

import pandas
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pandas.read_csv("../../data/titanic_numeric.csv")

scaler = StandardScaler()
# scaler = MinMaxScaler()
df = pandas.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)

# write the data back to disk

df.to_csv("../../data/titanic_normalized.csv", index=False)
