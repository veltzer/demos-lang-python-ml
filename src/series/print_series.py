#!/usr/bin/python3

"""
Example that shows that we can complete any series of number with any number
"""

# f(1) = 1
# f(2) = 4
# f(3) = 9
# f(4) = ?

def produce_number_alt_2(i):
    s=0
    s+=(i-2)*(i-3)*(i-4)*1/(-6)
    s+=(i-1)*(i-3)*(i-4)*4/2
    s+=(i-1)*(i-2)*(i-4)*9/-2
    s+=(i-1)*(i-2)*(i-3)*1979/6
    return s

def produce_number_alt(i):
    if i<5:
        return i*i
    return 1979+i-5

def produce_number(i):
    return i*i

for j in range(1,10):
    print(int(produce_number_alt_2(j)))
