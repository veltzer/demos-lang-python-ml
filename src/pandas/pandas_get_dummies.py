#!/usr/bin/python3

"""
show the get_dummies method
"""

import pandas as pd

df = pd.DataFrame({
    "car": ["ferrari","honda","mazda"],
    "weight": [4 , 5, 6],
})
new_df=pd.get_dummies(df)
print(df)
print(new_df)
