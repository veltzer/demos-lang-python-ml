# Exercise: Feature Engineering — Last-Name Counts

Feature engineering means inventing new columns out of existing ones, in the hope that
the new columns make the classifier's job easier.

This exercise tries one specific idea: the **last name** of each passenger. If two
passengers share a last name, they're likely related; the *count* of passengers per last
name is a rough proxy for "how many family members were on board". Family ties were a
real predictor of survival on the Titanic.

## Tasks

1. Load `data.csv` and do basic preparation:
   - fill `Embarked` NaNs with `'S'` (the most common value),
   - replace `Sex` `'male'/'female'` with `0/1`,
   - fill remaining NaNs with `0`,
   - drop `PassengerId` and `Name` from the working copy `tbl`.
2. Define a helper `run_it(title)` that, given the global `X` and `Y`:
   - loops 40 times,
   - on each iteration trains a `DecisionTreeClassifier()` on a fresh train/test split
     and accumulates the test score,
   - prints `f"avg {title} is {score / 40}"` so the comparison is apples-to-apples.
3. Call `run_it("before fe")` to get the baseline score.
4. Engineer a new column on `o_tbl` (the original loaded DataFrame): extract the last
   name from the comma-separated `Name` column. (`o_tbl["Name"].str.split(",").str[0]`.)
5. Call `run_it("after fe")` to score the augmented feature set.

Reflect on whether the new feature actually helped. (On Titanic, the last-name *count*
helps more than the last name itself, but feel free to try both.)
