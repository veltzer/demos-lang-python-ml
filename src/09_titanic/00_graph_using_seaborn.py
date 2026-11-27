#!/usr/bin/env python

"""
basic learning example
"""

import random

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

random.seed(0)

df = pd.read_csv("data/titanic.csv")

# seaborn.regplot(x=df['Age'], y=df['Survived'])  # noqa: ERA001  teaching: kept in the comment for the reader
# plt.show()  # noqa: ERA001  teaching: kept in the comment for the reader

# seaborn.histplot(df['Age'], bins=16)  # noqa: ERA001  teaching: kept in the comment for the reader
# plt.show()  # noqa: ERA001  teaching: kept in the comment for the reader

# seaborn.histplot(df, x='Age', hue='Sex', multiple='dodge')  # noqa: ERA001  teaching: kept in the comment for the reader
# plt.show()  # noqa: ERA001  teaching: kept in the comment for the reader

df['Survived_Sex'] = df['Survived'].astype(str) + '_' + df['Sex']
sns.histplot(df, x='Age', hue='Survived_Sex', multiple='dodge')
plt.show()
