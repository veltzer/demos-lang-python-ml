# Exercise 03: Histogram

`sns.histplot` plots a histogram of one variable. Use a fixed seed so the output is
reproducible.

1. Generate 1000 samples from a normal distribution with mean `0` and std `1` using
   `np.random.default_rng(42)`.
2. Draw `sns.histplot(samples, bins=30)`.
3. Set the title to `"Standard normal samples"`.
4. Save to `/tmp/03_histogram.png`.
