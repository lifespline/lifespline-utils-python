"""The `lifepsline-utils` utils package includes utilities testint and linting.
"""
from typing import Dict, List


def _exec_test(ctx, suite={}, script="", prefix="", test=""):
    """Execute either a test or a suite of tests.

    Args:
        ctx (_type_): _description_
        suite (dict, optional): _description_. Defaults to {}.
        script (str, optional): _description_. Defaults to "".
        prefix (str, optional): _description_. Defaults to "".
        test (str, optional): _description_. Defaults to "".
    """
    if test == "all":
        for name, params in suite.items():
            ctx.run(f"pytest {script}::{prefix}{name} {params}")
    else:
        name: str = test
        params: str = suite[test]
        ctx.run(f"pytest {script}::{prefix}{name} {params}")


def _unit_test_redshift(
    ctx, test="", host="", database="", port="", user="", password=""
):
    """Run redshift connection unit tests.

    Args:
        ctx (_type_): _description_
        test (str, optional): Specify which test to run from the test suite.
        Defaults to 'all'.
        host (str, optional): _description_. Defaults to ''.
        database (str, optional): _description_. Defaults to ''.
        port (str, optional): _description_. Defaults to ''.
        user (str, optional): _description_. Defaults to ''.
        password (str, optional): _description_. Defaults to ''.
    """
    test_params: str = (
        f" --user {user}"
        f" --password {password}"
        f" --host {host}"
        f" --port {port}"
        f" --database {database}"
    )
    test_script: str = "test/test_redshift_connection.py"
    test_prefix: str = "test_redshift_connection_"
    test_suite: Dict[str, str] = {
        "no_args": "",
        "invalid_user": test_params,
        "invalid_password": test_params,
        "authenticates": test_params,
    }

    _exec_test(ctx, test_suite, test_script, test_prefix, test)


def _unit_test_mssql(ctx, test="", host="", database="", port="", user="", password=""):
    """Run mssql connection unit tests.

    Args:
        ctx (_type_): _description_
        test (str, optional): Specify which test to run from the test suite.
        Defaults to 'all'.
        host (str, optional): _description_. Defaults to ''.
        database (str, optional): _description_. Defaults to ''.
        port (str, optional): _description_. Defaults to ''.
        user (str, optional): _description_. Defaults to ''.
        password (str, optional): _description_. Defaults to ''.
    """
    test_params: str = (
        f" --user {user}"
        f" --password {password}"
        f" --host {host}"
        f" --port {port}"
        f" --database {database}"
    )
    test_script: str = "test/test_mssql_connection.py"
    test_prefix: str = "test_mssql_connection_"
    test_suite: Dict[str, str] = {
        "no_args": "",
        "invalid_user": test_params,
        "invalid_password": test_params,
        "authenticates": test_params,
    }

    _exec_test(ctx, test_suite, test_script, test_prefix, test)


def _unit_test_oracle(
    ctx, test="", host="", database="", port="", user="", password=""
):
    """Run oracle connection unit tests.

    Args:
        ctx (_type_): _description_
        test (str, optional): Specify which test to run from the test suite.
        Defaults to 'all'.
        host (str, optional): _description_. Defaults to ''.
        database (str, optional): _description_. Defaults to ''.
        port (str, optional): _description_. Defaults to ''.
        user (str, optional): _description_. Defaults to ''.
        password (str, optional): _description_. Defaults to ''.
    """
    test_params: str = (
        f" --user {user}"
        f" --password {password}"
        f" --host {host}"
        f" --port {port}"
        f" --database {database}"
    )
    test_script: str = "test/test_oracle_connection.py"
    test_prefix: str = "test_oracle_connection_"
    test_suite: Dict[str, str] = {
        "no_args": "",
        "invalid_user": test_params,
        "invalid_password": test_params,
        "authenticates": test_params,
    }

    _exec_test(ctx, test_suite, test_script, test_prefix, test)


def _lint_yml(ctx):
    """Lint yml scripts in project's yml paths.

    Args:
        ctx (_type_): _description_
    """
    paths: List[str] = ["azure-pipeline.yml"]
    for path in paths:
        ctx.run(f"yamllint {path}")


def _lint_python(ctx):
    """Lint python code in project's python paths.

    Args:
        ctx (_type_): _description_
    """
    paths: List[str] = ["*.py", "test/*.py", "src/hook_utils/*.py"]
    for path in paths:

        # format before linting
        ctx.run(f"isort {path}")
        ctx.run(f"black {path}")

        # lint
        ctx.run(f"pylint {path}")
        ctx.run(f"flake8 {path}")
