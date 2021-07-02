#!/usr/bin/python3

import sys

for i in range(10):
    print(f"i is {i}")
    print(f"error: i hate a with the value {i}", file=sys.stderr)
