#!/usr/bin/python3

def fun(x):
    return (x-2)*(x-3)/2+(x-1)*(x-3)*(-4)+(x-1)*(x-2)*(1979/2)


for i in range(1,4):
    print(f"{int(fun(i))}")
