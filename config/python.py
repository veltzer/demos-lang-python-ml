""" python deps for this project """

import config.shared


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
build_requires: list[str] = config.shared.BUILD
test_requires: list[str] = config.shared.TEST
types_requires: list[str] = [
    "types-termcolor",
    "types-PyYAML",
    "types-psutil",
    "pandas-stubs",
]
requires = install_requires + build_requires + test_requires + types_requires
