#!/usr/bin/env python

"""
basic learning example
"""

import pandas
import seaborn
import matplotlib.pyplot as plt

df = pandas.read_csv("../data/titanic.csv")

# seaborn.regplot(x=df['Age'], y=df['Survived'])
# plt.show()

# seaborn.histplot(df['Age'], bins=16)
# plt.show()

# seaborn.histplot(df, x='Age', hue='Sex', multiple='dodge')
# plt.show()

df['Survived_Sex'] = df['Survived'].astype(str) + '_' + df['Sex']
seaborn.histplot(df, x='Age', hue='Survived_Sex', multiple='dodge')
plt.show()
