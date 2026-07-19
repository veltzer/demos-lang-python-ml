# Exercise 10: GroupBy

Given:

```text
df = pd.DataFrame({
    "dept":     ["eng", "sales", "eng", "hr", "eng", "sales", "hr"],
    "gender":   ["F", "M", "M", "F", "F", "F", "M"],
    "salary":   [70000, 50000, 90000, 65000, 120000, 55000, 60000],
})
```

Print:

1. the count of rows in each `dept`
2. the mean salary per `dept`
3. the count of rows for each `(dept, gender)` combination (group by two columns)
