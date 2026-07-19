# Setting Up a Python Virtual Environment for ML

ML libraries are big and conflict often (different projects pinning different versions
of `numpy`, `scikit-learn`, `pandas`). Always work inside a per-project virtual
environment so each project has its own isolated set of installed packages.

## The packages we need

| package         | what for             |
| --------------- | -------------------- |
| `numpy`         | numeric arrays       |
| `pandas`        | DataFrames           |
| `matplotlib`    | static plots         |
| `seaborn`       | statistical plots    |
| `plotly`        | interactive plots    |
| `scikit-learn`  | ML algorithms        |
| `psutil`        | memory measurements  |

## Linux

```text
# install python3 and the venv module if you don't already have them
sudo apt install python3 python3-venv python3-pip   # Debian/Ubuntu
sudo dnf install python3 python3-pip                 # Fedora

# create a venv next to the project
cd ~/projects/demos-lang-python-ml
python3 -m venv .venv

# enter the venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn plotly scikit-learn psutil

# leave the venv when done
deactivate
```

## macOS

Same as Linux once you have a recent Python. The system Python on macOS is old and
should not be used for ML work — install one of:

- **Homebrew Python** (recommended): `brew install python` — gives you `python3` and
  `pip3`.
- **The python.org installer**: download the latest macOS `.pkg` from
  [python.org/downloads](https://www.python.org/downloads/).
- **pyenv**: `brew install pyenv` then `pyenv install 3.13` if you want to manage
  multiple Python versions.

After that, the venv steps are identical to Linux:

```text
cd ~/projects/demos-lang-python-ml
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn plotly scikit-learn psutil
```

## Windows

```text
:: install Python from python.org/downloads/windows/ (check "Add Python to PATH" in
:: the installer)

:: create a venv
cd C:\projects\demos-lang-python-ml
python -m venv .venv

:: enter the venv (cmd.exe)
.venv\Scripts\activate.bat

:: ...or PowerShell
.venv\Scripts\Activate.ps1

:: install dependencies
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn plotly scikit-learn psutil

:: leave the venv
deactivate
```

If PowerShell refuses to run the activate script with an execution-policy error, run
once as admin:

```text
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Sanity check

After activation, this should print version numbers without error:

```text
python -c "import numpy, pandas, matplotlib, seaborn, plotly, sklearn; \
           print(numpy.__version__, pandas.__version__, sklearn.__version__)"
```

## Pinning versions for reproducibility

Once a project works, freeze the exact versions to a file so others (and future-you) get
the same setup:

```text
pip freeze > requirements.txt          # write
pip install -r requirements.txt        # reinstall later
```

## Alternative: `uv`

[uv](https://github.com/astral-sh/uv) is a much faster modern replacement for `pip` +
`venv`. If you're starting fresh, consider it:

```text
curl -LsSf https://astral.sh/uv/install.sh | sh   # Linux/macOS
uv venv
source .venv/bin/activate
uv pip install numpy pandas matplotlib seaborn plotly scikit-learn psutil
```

It does the same job in a fraction of the time.
