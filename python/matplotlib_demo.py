#!/usr/bin/env python
import pandas
import matplotlib.pyplot as plt

tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)
a=tbl.hist("Age", "Survived")
plt.show()

