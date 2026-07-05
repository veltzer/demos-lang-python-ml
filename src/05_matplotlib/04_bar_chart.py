#!/usr/bin/env python

"""Solution to exercise 05: vertical bar chart with rotated x-tick labels."""

import matplotlib.pyplot as plt

categories = ["apples", "oranges", "bananas", "pears", "grapes"]
counts = [23, 17, 35, 12, 28]

plt.bar(categories, counts)
plt.title("Fruit counts")
plt.ylabel("count")
plt.xticks(rotation=30)
plt.savefig("/tmp/05_bar_chart.png")
