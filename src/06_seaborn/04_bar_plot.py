#!/usr/bin/env python

"""Solution to exercise 05: barplot of mean salary by department."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "dept": ["eng", "eng", "eng", "sales", "sales", "sales", "hr", "hr", "hr"],
    "salary": [70000, 90000, 120000, 50000, 55000, 60000, 65000, 60000, 62000],
})

sns.barplot(data=df, x="dept", y="salary")
plt.title("Mean salary by department")
plt.savefig("/tmp/05_bar_plot.png")
