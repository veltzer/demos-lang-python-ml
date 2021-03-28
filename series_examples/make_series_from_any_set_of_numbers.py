#!/usr/bin/python3

def fun(x):
    sum=0
    sum+=(x-2)*(x-3)/2+(x-1)*(x-3)*(-4)+(x-1)*(x-2)*(1997/2)
    return sum


for i in range(1,4):
    print(f"{int(fun(i))}")
