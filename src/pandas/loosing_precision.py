#!/usr/bin/env python

"""
This example explores how panda columns lose precision
"""

import pandas
tbl = pandas.read_csv("data.csv")
fare=0.1**1000;
print(tbl["Fare"][0])
# print(tbl.dtypes)
tbl.iat[9, 0]=fare
print(tbl["Fare"][0])
