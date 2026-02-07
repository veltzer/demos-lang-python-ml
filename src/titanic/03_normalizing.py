#!/usr/bin/env python

"""
This example show how to normalize an entire data frame in preparation
for an algorithm that needs normalized data (e.g. KNN).
"""

from sklearn.preprocessing import StandardScaler
import pandas
import random

random.seed(0)
numpy.random.seed(0)

df = pandas.read_csv("../../data/titanic_numeric.csv")

scaler = StandardScaler()
cols_to_scale = df.columns.drop("Survived")
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

# write the data back to disk

df.to_csv("../../data/titanic_normalized.csv", index=False)
