# Exercise 07: Sorting and Ranking

Given:

```text
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Dana", "Eve"],
    "age":    [30, 25, 35, 28, 40],
    "salary": [70000, 50000, 90000, 65000, 120000],
})
```

1. Print the DataFrame sorted by `age` ascending.
2. Print the DataFrame sorted by `salary` descending.
3. Print the DataFrame sorted first by `age` ascending, then `salary` descending as a tiebreaker.
4. Add a column `"salary_rank"` containing each row's rank by salary (1 = highest) and print
   the DataFrame.
