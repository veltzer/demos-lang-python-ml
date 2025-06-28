#!/usr/bin/python3

"""
An example of how to make a function from every series of numbers,
even such that doesn't make sense
"""


def fun(x):
    return (x-2)*(x-3)/2+(x-1)*(x-3)*(-4)+(x-1)*(x-2)*(1979/2)


for i in range(1,4):
    print(f"{int(fun(i))}")
