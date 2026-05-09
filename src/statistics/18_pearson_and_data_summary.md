# Exercise 18: Pearson Correlation and Data Summary

## Pearson correlation

The [Pearson correlation
coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) measures the
linear relationship between two numeric variables. It ranges from `-1` (perfect inverse
relationship) through `0` (uncorrelated) to `+1` (perfect direct relationship).

### Tasks (correlation)

1. Load `data.csv` (Titanic), the same file used by the `ml/` scripts.
2. For every numeric column in the data, compute its Pearson correlation with the
   `Survived` target. Print a sorted list of `column: correlation` pairs.

## Per-column data summary

Whenever you receive a new dataset, before doing anything else you should print a quick
statistical summary for each column. The provided solution prints, for every numeric
column:

- mean (expected value)
- standard deviation
- number of unique values
- median
- 25th, 50th, 75th percentiles
- min and max

For non-numeric columns it prints the value-count table.

This is the kind of one-shot script that pays for itself on day one of any new project.
