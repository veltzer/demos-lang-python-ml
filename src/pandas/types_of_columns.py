#!/usr/bin/env python

"""
This demos shows the types of columsn in a pandas table...
"""

import pandas
tbl = pandas.read_csv("data.csv")
# print(type(tbl))
print(tbl.dtypes)
print("==========================================")
for columnName, columnData in tbl.items():
    # columnData=tbl[columnName]
    print(f"{columnName} {columnData.dtype}")
    # print(f"{columnData}")
