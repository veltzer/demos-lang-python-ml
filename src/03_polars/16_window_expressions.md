# Exercise 17: Window Expressions

Given a `DataFrame` with `dept` and `salary` columns, use `over("dept")` to add:

1. a `dept_avg` column: the average salary within each department
2. a `diff_from_avg` column: how far each salary is from its department average
3. a `rank_in_dept` column: the salary rank within each department
