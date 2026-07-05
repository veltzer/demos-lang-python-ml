# Exercise 03: Histogram

`px.histogram` bins a numeric column and draws the count per bin.

1. Generate 1000 samples from a standard normal using `np.random.default_rng(0)`.
2. Wrap them in a DataFrame with one column `"value"`.
3. Draw `px.histogram(df, x="value", nbins=30)`.
4. Title `"Standard normal samples"`.
5. Save to `/tmp/03_histogram.html`.
