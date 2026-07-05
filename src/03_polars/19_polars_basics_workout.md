# Exercise 20: Polars Basics Workout

Walk through a full polars workout on a small people `DataFrame`:

1. add a derived `raised` column, then drop it
2. rename `salary` to `income`
3. filter out one person by name
4. append a new person with `pl.concat`
5. cast `age` to float and confirm the dtype
6. group by `dept` and report head count and average income
7. compute the overall mean and variance of `income`
8. sort by `income` descending
