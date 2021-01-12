#!/usr/bin/python3
import pandas as pd
import numpy as np
import time
import dask.dataframe as dd
import multiprocessing


"""
Order of using functions in numpy and pandas:
- If there is a built-in function -> use it. 0.04 seconds
- If there is not built-in function prefer lambda if the function is simple. 0.3 seconds
- If the function is not simple -> prefer transform with a real function.
- Only as a last resort, change values manually.
"""


def my_absolute(x):
    return x.abs()

num_elements=40000000
df = pd.DataFrame({
    0: pd.Series(np.random.randn(num_elements)),
    1: pd.Series(np.random.randn(num_elements)),
    2: pd.Series(np.random.randn(num_elements)),
    3: pd.Series(np.random.randn(num_elements)),
})
dd.from_pandas(df, npartitions=4*multiprocessing.cpu_count()) 
#print(df)
time_before = time.time()
#df[0].apply(lambda x: abs(x))
#df[0]=df[0].abs() # 0.04s
df[0]=df[0].transform(lambda x: x.abs()) # 0.3s
#df[0]=df[0].transform(my_absolute) # 0.299s
###for x in range(df.shape[0]):
###  df[0][x]=abs(float(df[0][x])) #-> too much time
time_after = time.time()
print('time taken: {0:.3f} seconds'.format(time_after - time_before))

#df['one']=df['one'].transform(x.abs())
#df['one']=df['one'].transform(my_absolute)
#print(df)
