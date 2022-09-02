# Lifespline Utils Python

# About

`lifespline-utils` is a Python package that provides a set of python utilities for the Lifespline project. Check the [changelog] for to check the utils released each version.

# Install

The package is hosted in [PyPi][pypi], so you can push the package to your local virtual environment with:

```bash
pip install lifespline-utils
```

Test the installation with:

```bash
python -m lifespline_utils.connection
```

# Getting Started

Create a new redshift connection:

```python
>>> from lifespline_utils.connection import RedshiftConnection
>>> conn: RedshiftConnection = RedshiftConnection()
user name: <username>
password: <password>
INFO: Connecting to source: <host>
╰─(connection.py:124)
>>> conn.read_sql("select USER from dual")
          USER
0   <username>
```

For more examples, check the test scenarios in the tests directory.

# Contributing

Read-the-docs at [`doc/dev.md`]().

[changelog]: CHANGELOG.md "Changelog"
[pypi]: https://pypi.org/manage/projects/lifespline-utils-python/ "PyPi"
[pypi-test]: https://test.pypi.org/manage/projects/lifespline-utils-python/ "PyPi"