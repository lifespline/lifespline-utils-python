""":doc:`tasks.py <../../tasks.py>` is the project's task-runner.
"""
import os
from invoke import task
from utils import utils


@task
def docs(ctx):
    """Build the documentation with sphinx.

    :param ctx: A session on the host OS
    :type ctx: invoke.Context
    """
    cmds = [
        "cd docs",
        "make html",
        "cp -a _build/html/. static/",
        "make clean",
        "echo && echo Your static documentation pages can be found at 'docs/debug/static' && echo",
    ]

    ctx.run(";".join(cmds))

@task
def lint(ctx, src="py", format=True):
    """Lint and format the project's src files.

    :param ctx: A session on the host OS
    :type ctx: invoke.Context
    :param src: Lint files of extension :param lint:, defaults to 'py'
    :type src: str, optional
    :param format: Format files, defaults to 'True'
    :type format: bool, optional
    """
    if src in ["yml", "yaml"]:
        utils.lint_yml(ctx)
    elif src in "python":
        utils.lint_python(ctx, format)


@task
def test(
    ctx, suite="", test="all", host="", database="", port="", user="", password=""
):
    """Run unit tests.

    .. warning::

        Whichever operations that require secrets should never have those secrets persisted in the repo, but in some secrets manager.

    Args
    ----

    :param ctx: A session on the host OS
    :type ctx: invoke.Context
    :param suite: Run this suite of unit tests, defaults to ''
    :type suite: str, optional
    :param test: Run unit tests, defaults to 'all'
    :type test: str, optional
    :param host: The database host, defaults to ''
    :type host: str, optional
    :param database: The database name, defaults to ''
    :type database: str, optional
    :param port: The database port, defaults to ''
    :type port: str, optional
    :param user: The database user, defaults to ''
    :type user: str, optional
    :param password: The database password, defaults to ''
    :type password: str, optional

    Examples
    --------

    .. code:: python

        >>> inv ci --suite redshift \
        --user <user> \
        --password <password> \
        --port <port> \
        --host <host> \

        >>> --database <database>
        inv ci --suite redshift \
        --test invalid_user \
        --user <user> \
        --password <password>

    """
    if suite == "oracle":
        utils.unit_test_oracle(ctx, test, host, database, port, user, password)

    elif suite == "redshift":
        utils.unit_test_redshift(ctx, test, host, database, port, user, password)

    elif suite == "mssql":
        utils.unit_test_mssql(ctx, test, host, database, port, user, password)
