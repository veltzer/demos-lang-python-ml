# Exercise 07: Violin Plot

A violin plot is a box plot fused with a KDE — you see the median and IQR *and* the
shape of each distribution. Useful when you want to spot bimodality or skew.

Build the same DataFrame as in exercise 06 (three groups A/B/C of 200 normal samples each
with different mean and std), and:

1. Draw `sns.violinplot(data=df, x="group", y="value")`.
2. Title `"Violin plot of value by group"`.
3. Save to `/tmp/07_violin_plot.png`.
