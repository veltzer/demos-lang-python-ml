""" python deps for this project """

install_requires: list[str] = [
    "scikit-learn",
    # "sklearn",
    "pyarrow",
    "pandas",
    "numpy",
    "matplotlib",
    "psutil",
    "dask",
    # deep learining
    "tensorflow",
    "keras",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
    # types
    "types-termcolor",
    "types-PyYAML",
    "types-psutil",
    "pandas-stubs",
]
requires = install_requires + build_requires + test_requires
