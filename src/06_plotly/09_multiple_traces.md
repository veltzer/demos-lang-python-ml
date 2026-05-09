# Exercise 09: Multiple Traces on One Figure

Sometimes you want full control: use `plotly.graph_objects.Figure` directly and add each
trace yourself. This is what every `plotly.express` call ultimately does under the hood.

On `x = np.linspace(0, 2*np.pi, 100)`, draw three trig curves on the same axes:

- `sin(x)` as a solid blue line, label `"sin"`
- `cos(x)` as a solid red line, label `"cos"`
- `sin(x) * cos(x)` as a green dashed line, label `"sin*cos"`

Tasks:

1. Build `fig = go.Figure()`.
2. For each curve, `fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=label,
   line=dict(color=..., dash=...)))`. Use `dash="dash"` for the third curve.
3. Set `fig.update_layout(title="Trig functions", xaxis_title="x", yaxis_title="value")`.
4. Save to `/tmp/09_multiple_traces.html`.
