#!/usr/bin/env python

"""
This example shows how to convert all the columns of data frame to numeric
values in preparation to doing ML with an algorithm that only works with
numeric data (e.g. KNN).
"""

import pandas
import random

random.seed(0)
numpy.random.seed(0)

df = pandas.read_csv("../../data/titanic_clean.csv")

# show all columns which are non numeric

print(df.select_dtypes(exclude="number").columns)

# So we need to turn "Sex" and "Embarked" to numeric values

df["Sex"] = df["Sex"].astype("category").cat.codes
df["Embarked"] = df["Embarked"].astype("category").cat.codes

# write the data back to disk

df.to_csv("../../data/titanic_numeric.csv", index=False)
