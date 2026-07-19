# Exercise 13: Interactive Dropdown to Toggle Traces

`fig.update_layout(updatemenus=...)` adds a dropdown (or button row) to the figure that
toggles trace visibility. This is the simplest way to put multiple views of the same
data behind a single switch.

On `x = np.linspace(0, 2*np.pi, 100)`, build a figure with three traces — `sin(x)`,
`cos(x)`, and `tan(x)` (clipped to `[-5, 5]`) — and add a dropdown that lets the user
show **only one** at a time, or all three together.

Tasks:

1. Build the figure with all three traces visible by default.
2. Add an `updatemenus` block of type `"dropdown"` with four options:
   - `"All"` — `[True, True, True]`
   - `"sin"` — `[True, False, False]`
   - `"cos"` — `[False, True, False]`
   - `"tan"` — `[False, False, True]`

   Each option's `args` is `[{"visible": [...]}]`.
3. Save to `/tmp/13_dropdown_buttons.html`. Open it and click the dropdown to switch
   views.

Hint:

```text
fig.update_layout(updatemenus=[{
    "buttons": [
        {"label": "All", "method": "update", "args": [{"visible": [True, True, True]}]},
        {"label": "sin", "method": "update", "args": [{"visible": [True, False, False]}]},
        ...
    ],
    "direction": "down",
    "showactive": True,
}])
```
