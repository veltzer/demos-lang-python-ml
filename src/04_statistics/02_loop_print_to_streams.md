# Exercise 17: Print to stdout and stderr

Write a single script that produces both of the following outputs.

On **stdout** (10 lines):

```text
i is 0
i is 1
i is 2
i is 3
i is 4
i is 5
i is 6
i is 7
i is 8
i is 9
```

On **stderr** (10 lines):

```text
error: i hate a with the value 0
error: i hate a with the value 1
error: i hate a with the value 2
error: i hate a with the value 3
error: i hate a with the value 4
error: i hate a with the value 5
error: i hate a with the value 6
error: i hate a with the value 7
error: i hate a with the value 8
error: i hate a with the value 9
```

Use `print(...)` for stdout and `print(..., file=sys.stderr)` for stderr.

Verify by redirecting them separately:

```text
python3 17_loop_print_to_streams.py >data.txt 2>errors.txt
```
