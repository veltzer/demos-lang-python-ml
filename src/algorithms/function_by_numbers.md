# Exercise: A Function That Doesn't Follow a Rule

You can implement *any* mapping from a finite set of inputs to outputs as a Python
function — the function does not have to follow any mathematical rule. A long chain of
`if` statements is a valid way to express a function whose values are pure assertions.

Implement `my_function(x)` such that:

- `my_function(1) == 1`
- `my_function(2) == 4`
- `my_function(3) == 1979`

For any other input it returns `0`.

Then call it for `x` in `1, 2, 3` and print each value.

This exercise is the warm-up for the next ones, where we build the *same* function with
progressively more interesting techniques (control flow, polynomial fits) and discover
that any finite scatter of points can be produced by infinitely many functions.
