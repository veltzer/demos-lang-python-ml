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
    "pycmdtools",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
    "pycmdtools",
    # types
    "types-termcolor",
    "types-PyYAML",
    "pandas-stubs",
    "types-psutil",
]
requires = install_requires + build_requires + test_requires
