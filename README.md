# Python Kata

## Initialize dev environment

1. Install `Poetry` for package management using [this site](https://python-poetry.org/)
2. Run `poetry install` to install package dependencies.
3. Launch virtual env using `poetry shell`
4. Run tests with `pytest`

Run single test file:

`python -m pytest tests/array_comparison_test.py`

Run specific test:

`python -m pytest tests/array_comparison_test.py::test_with_none_input`

