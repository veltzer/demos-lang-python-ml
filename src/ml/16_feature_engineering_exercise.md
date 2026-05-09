# Exercise 16: Feature Engineering on Titanic

Take the Titanic dataset (`data.csv`, the same file the other `ml/` scripts in this folder
read) and the basic decision-tree training script `ml/learn.py` as your baseline.

Tasks:

1. Run the baseline once and **record your current accuracy rate** as a number.
2. Engineer at least **two new features** that you believe will help the
   `DecisionTreeClassifier`. Examples to consider — pick or invent your own:
   - `family_size = SibSp + Parch + 1`
   - `is_alone = (family_size == 1)`
   - `title` extracted from `Name` (`Mr`, `Mrs`, `Miss`, `Master`, …)
   - `age_bucket = pd.cut(Age, bins=[0, 12, 18, 35, 60, 120])`
   - `fare_per_person = Fare / family_size`
3. Re-run training and record the new accuracy.
4. Reflect: which features helped, which didn't, why? Decision trees are scale-invariant
   but care about which split values are available — features that *create cleaner splits*
   tend to help.

Bonus: post the highest accuracy you can reach.

The provided solution implements two engineered features (`family_size` and `is_alone`)
and prints both the baseline and the engineered accuracy so you can compare them in one
run.
