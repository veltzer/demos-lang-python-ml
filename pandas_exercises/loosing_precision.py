#!/usr/bin/python3

"""
This demos shows the types of columsn in a pandas table...
"""

import pandas
tbl = pandas.read_csv("data.csv")
fare=0.1**1000;
print(tbl["Fare"][0])
# print(tbl.dtypes)
tbl.iat[9, 0]=fare
print(tbl["Fare"][0])
