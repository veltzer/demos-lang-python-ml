# Exercise: Feature Engineering with Toggles

A fully-armed feature-engineering pipeline. Each transformation is gated by a boolean
flag, so you can turn knobs on and off without rewriting code. Combined with a fixed
random seed (set before everything), this lets you A/B-test feature combinations
quickly.

## The flags

```
f_embarked     # keep Embarked column (vs drop it)
f_dummies      # one-hot encode Pclass / Embarked / Title
f_drop         # drop high-cardinality columns (PassengerId, Name, Ticket, Cabin)
f_nor          # min-max normalize all columns
f_age          # impute missing Age from per-Title mean (requires f_title)
f_fare         # impute missing Fare from per-(Pclass, Embarked) mean
f_title        # extract Mr/Mrs/Miss/... from Name
f_eng_alone    # add IsAlone = (SibSp + Parch == 0)
f_turn_column_sex_into_male_female  # Sex -> 0/1 numeric
f_fillna       # fillna(0) at the start
```

## Tasks

1. Implement each transformation guarded by its `if f_xxx:` block.
2. Run with the default flag combination (provided in the solution: `f_drop`, `f_fare`,
   `f_eng_alone`, `f_turn_column_sex_into_male_female`, `f_fillna` enabled, the rest
   disabled).
3. Train a `DecisionTreeClassifier(max_depth=15)` and print
   `f"Decision Tree Train (depth=15): {score_train}, Test: {score_test}"`.
4. Toggle one flag at a time and rerun. With seed `5` set up front, the only thing that
   changes between runs is the flag you toggled, so you can isolate each effect.

This is the natural "next step" after the previous exercise, where you compared
candidates one-by-one — here you compare combinations.
