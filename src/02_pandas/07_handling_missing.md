# Exercise 08: Handling Missing Values

Given:

```
import numpy as np

df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Dana"],
    "age":    [30, np.nan, 35, np.nan],
    "salary": [70000, 50000, np.nan, 65000],
})
```

1. Print a boolean DataFrame showing where the NaNs are (`isna`).
2. Print the count of NaNs in each column.
3. Print the DataFrame after filling NaN `age` values with the mean age and NaN `salary`
   values with `0`.
4. Print the DataFrame after dropping any row that has at least one NaN.
