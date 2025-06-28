#!/usr/bin/env python

"""
showing the 'groupby' feature of pandas
"""

import pandas

tbl = pandas.read_csv("data.csv")
tbl.fillna(0, inplace=True)
print(tbl.groupby(["Survived", "Sex"]).count())
print(tbl)
