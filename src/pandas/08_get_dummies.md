# Exercise 09: One-Hot Encoding with get_dummies

`pd.get_dummies` converts each unique value of a categorical column into its own boolean
column. This is the standard way to feed string categories into ML models that need
numeric input.

Given:

```
df = pd.DataFrame({
    "car":    ["ferrari", "honda", "mazda", "honda"],
    "weight": [4, 5, 6, 5],
})
```

1. Print the original DataFrame.
2. Apply `pd.get_dummies` to it and print the result. The `weight` column should pass
   through unchanged; `car` should become three boolean columns (`car_ferrari`,
   `car_honda`, `car_mazda`).
