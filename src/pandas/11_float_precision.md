# Exercise 12: Float Precision in Columns

A float column has a fixed dtype — typically `float64`, which gives you ~15-17 significant
decimal digits and a minimum positive value around `5e-324`. Anything outside those
bounds gets silently rounded.

Build a DataFrame with one column `"fare"` containing `[7.25, 71.28, 13.0, 8.05]`.

1. **Digit truncation.** Assign the Python float `1.234567890123456789` (19 digits) into
   row `0` using `.iat`. Print the stored value — only ~17 digits survive.
2. **Subnormal range.** Assign `0.1 ** 320` (~`1e-320`, a subnormal) into row `0`.
   Print the stored value — it is preserved (non-zero).
3. **Underflow.** Assign `0.1 ** 1000` into row `0`. In pure Python this expression
   already evaluates to `0.0` because float64 cannot represent it. Print it to confirm.
