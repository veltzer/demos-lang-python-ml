# Exercise 13: Measuring Memory Usage

A DataFrame's memory footprint matters when you scale up. Pandas exposes per-column memory
via `DataFrame.memory_usage`, and you can compare that against the actual process RSS
(resident set size) reported by the OS.

1. Use `psutil.Process(os.getpid()).memory_info().rss` to print the process RSS in bytes
   *before* allocating any DataFrame.
2. Build a DataFrame of shape `(890, 12)` filled with `random.random()` floats.
3. Print:
   - `df.dtypes`
   - `df.memory_usage()` (per-column memory)
   - `df.memory_usage().sum()` (total)
4. Print the process RSS again. The difference should be at least the size reported by
   `memory_usage().sum()` — usually larger because of pandas overhead.
