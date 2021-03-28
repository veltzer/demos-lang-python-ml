#!/usr/bin/python3

def produce_number_alt(i):
    if i<5:
        return i*i
    else:
        return 1979+i

def produce_number(i):
    return i*i

for j in range(1,10):
    print(produce_number(j))
