#!/usr/bin/env python

"""
simple matplotlib demo
"""

import matplotlib.pyplot as plt
import pandas

tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)
a=tbl.hist("Age", "Survived")
plt.show()
