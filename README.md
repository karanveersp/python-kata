# Python Kata

Create a virtual environment folder in root directory

`python -m venv venv`

Activate the virtual environment

`.\venv\Scripts\Activate.ps1`

Install requirements:

`pip install -r requirements.txt`

Run all tests:

`python -m pytest`

Run single test file:

`python -m pytest tests/array_comparison_test.py`

Run specific test:

`python -m pytest tests/array_comparison_test.py::test_with_none_input`

