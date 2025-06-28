#!/usr/bin/python3


"""
Order of using functions in numpy and pandas:
- If there is a built-in function -> use it. 0.04 seconds
- If there is not built-in function prefer lambda if the function is simple. 0.3 seconds
- If the function is not simple -> prefer transform with a real function.
- Only as a last resort, change values manually.
"""


import time
# import multiprocessing
import numpy as np
# import dask.dataframe as dd
import pandas as pd


def my_absolute(x):
    return x.abs()


def main():
    num_elements=4000000
    df = pd.DataFrame({
        0: pd.Series(np.random.randn(num_elements)),
        1: pd.Series(np.random.randn(num_elements)),
        2: pd.Series(np.random.randn(num_elements)),
        3: pd.Series(np.random.randn(num_elements)),
    })
    #dd.from_pandas(df, npartitions=4*multiprocessing.cpu_count())
    #print(df)
    time_before = time.time()
    # df[0]=df[0].abs() # 0.04s
    # df[0]=df[0].transform(lambda x: x.abs()) # 0.3s
    # df[0]=df[0].transform(my_absolute) # 0.299s
    # df[0].apply(lambda x: abs(x)) # 0.9 sec
    for x in range(df.shape[0]):
        df[0][x]=abs(float(df[0][x])) #-> too much time
    time_after = time.time()
    print(f'time taken: {time_after - time_before:.3f} seconds')

    #df['one']=df['one'].transform(x.abs())
    #df['one']=df['one'].transform(my_absolute)
    #print(df)


if __name__ == "__main__":
    main()
