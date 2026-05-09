#!/usr/bin/env python

"""Solution to exercise 17: emit numbered lines on stdout and stderr."""

import sys

for i in range(10):
    print(f"i is {i}")
    print(f"error: i hate a with the value {i}", file=sys.stderr)
