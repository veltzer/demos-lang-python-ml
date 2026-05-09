# Exercise: Measure Each Engineered Feature Separately

In the previous exercise (`feature_engineering`) we added one new column and compared
before/after. But what if you have **a dozen ideas** for new features? You don't want to
add them all at once — if the score improves you won't know which feature mattered, and
if it worsens you won't know which one hurt.

This exercise measures each candidate feature in isolation: for each candidate, train
with *only that one new feature added* and compare against the baseline.

## The candidate features

```
['MartialStatus', 'LastName', 'count_lastname', 'Relatives',
 'Cabin_bool', 'Ticket_bool', 'count_Embarked', 'Cabin_first_letter',
 'ticket_num', 'ticket_letters', 'Cabin_number', 'ticket_cnt']
```

How each is computed (read the solution for the exact pandas one-liners):

- **MartialStatus**: pull `"Mr."`, `"Mrs."`, `"Miss."`, etc. out of `Name`.
- **LastName**: split `Name` on comma, take the first part.
- **count_lastname**: how many rows share each `LastName`.
- **Relatives**: `SibSp + Parch`.
- **Cabin_bool**: `1` if Cabin is recorded, else `0`.
- **Ticket_bool**: `1` if `Ticket` contains any letter, else `0`.
- **count_Embarked**: how many rows share each `Embarked`.
- **Cabin_first_letter / Cabin_number**: split the Cabin string into a letter prefix
  and a number suffix.
- **ticket_num / ticket_letters**: same idea for `Ticket`.
- **ticket_cnt**: how many rows share each `Ticket`.

## Tasks

1. Build the baseline pipeline and average the test score over `i_num = 20` runs. Print
   `f"overall score BEFORE FEATURE ENGINEERING: {round(score, 3)}"`.
2. For each candidate column `c` in the list above:
   - add **only `c`** as a new column (drop the others),
   - re-run the 20-iteration train/score loop,
   - record `score_with_c - score_baseline` and print
     `f"overall score AFTER FEATURE ENGINEERING {c}: {round(score, 3)}"`.
3. Sort the candidates by their score delta — the largest positive deltas are the
   features worth keeping.

Caveat: even with 20 averaged runs, score deltas of `±0.005` are usually within noise.
Don't over-interpret tiny improvements.
