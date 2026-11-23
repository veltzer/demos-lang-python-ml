#!/usr/bin/env python

"""
This is an example of how to produce the correlation matrix of a table of data.
The purpose is to find columns that have a strong correlation with the result - in order
to keep them.
And two find pairs of columns which are correlated bewteen themselves - in order to drop
one of them and reduce dimensionality.
"""

import random

import pandas as pd

random.seed(0)

df = pd.read_csv("data/titanic_normalized.csv")

# y = target column
y = df["Survived"]

# X = everything except target
X = df.drop(columns="Survived")

print(df.corr())
