#!/usr/bin/env python

"""
This example shows how to clean data in machine learning.
The data is the Titanic data.
"""

import pandas

df = pandas.read_csv("../../data/titanic.csv")

print(f"total number of rows is {df.shape[0]}...")
print(df.isna().sum()[df.isna().sum() > 0])
print(df["Embarked"].value_counts())


"""
I ran the lines above to check what is out non available data.
This is what we got:

total number of rows is 891...
Age         177
Cabin       687
Embarked      2
dtype: int64
Embarked
S    644
C    168
Q     77
Name: count, dtype: int64

I then decided to:
- remove the 177 lines with no age, age is important
- remove the Cabin column completely, as it is almost empty
- only two lines with embarked missing - remove them, not a big loss.
"""
df = df.dropna(subset=["Age", "Embarked"])
print(df.shape)
df = df.drop(columns="Cabin")
print(df.shape)
df.to_csv("../../data/titanic_clean.csv", index=False)
