# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `notes/virtualenv.md:35` - the install command (repeated at lines 60 and 81) leaves out `polars`, which `pyproject.toml` declares and all of `src/03_polars/` imports, so students following the note cannot run the polars exercises; add `polars` (or point to `uv sync`).
- `notes/dev_environment.md:46` - tells the reader to `pip install -r requirements.txt`, but the repo has no `requirements.txt` (dependencies are in `pyproject.toml` / `uv.lock`); replace with `uv sync` or the package list from `notes/virtualenv.md`.
- `rsconstruct.toml:32` - ruff and mypy (line 36) only cover `src`, so `word2vec-app/word2vec_app.py` and `data/titanic_*.py` are never linted; `ruff check word2vec-app data` currently reports 4 errors. Add those directories to `src_dirs` and fix the findings.

## Low

- `pyproject.toml:40` - the mypy `ignore_missing_imports` list includes `pandas.*` and `psutil.*` (line 42) although the dev group installs `pandas-stubs` and `types-psutil`, and `matplotlib.*` (line 39) ships its own type information; drop the stale entries so a missing stub is reported instead of silenced.
- `pyproject.toml:32` - `mypy_path = "src:python:scripts"` names `python` and `scripts` directories that do not exist; reduce to `src`.
- `src/08_ml/13_naive_bayes_mushrooms.py:3` - docstring says "Solution to exercise 19" and the matching `.md` is titled "Exercise 19", while the file is exercise 13 of `08_ml`; renumbering leftover, fix the number.
