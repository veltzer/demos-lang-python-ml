# Exercise 02: Inspect Column Dtypes

When you receive a new DataFrame, the first thing to check is what type pandas decided
each column should be. Pandas infers types from the *values* it sees — integer-only
columns become `int64`, anything with a non-integer numeric becomes `float64`, mixed
content becomes `object` (Python objects, usually strings).

Given:

```
df = pd.DataFrame({
    "id":      [1, 2, 3],
    "name":    ["Alice", "Bob", "Charlie"],
    "salary":  [70000.5, 50000.0, 90000.25],
    "active":  [True, False, True],
})
```

## Tasks

1. Print `df.info()` — pandas' built-in summary that combines row count, per-column
   non-null counts, dtypes, and memory usage in one call.
2. Print the `dtypes` Series directly with `df.dtypes`.
3. Iterate over the columns with `df.items()` and print one line per column in the
   format `<column_name> <dtype>`.

## Reflect

How did pandas decide which type to use for each column?

- `id` is `int64` because every value is an integer.
- `name` is `object` because the values are Python strings.
- `salary` is `float64` because some values are non-integer floats — even one float in
  the column is enough to promote the whole column.
- `active` is `bool` because every value is `True` or `False`.

When you read a CSV with `pd.read_csv`, pandas runs the same inference on each column.
That can be wrong: a column of years might be parsed as `int64` when you wanted dates,
or a column with one accidental string in 10000 numeric rows becomes `object` and breaks
your math. Always check `df.info()` after loading, and pass `dtype=` to `read_csv` if
you need to override.
