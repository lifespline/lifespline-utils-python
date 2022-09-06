"""This is the project's task runner.
"""
from invoke import task

@task
def ci(ctx, suite = '', test = 'all', host = '', database = '', port = '', user = '', password = '', lint = ''):
    """Continuous integration tools: UT, lint.

    `tasks.ci` is ran both by a human agent or by an automated agent. The human 
    agent must provide the method's parameters without persisting them in the 
    solution. The automated agent provides the parameters through the 
    pipeline's variables.

    # Args

    + ctx (_type_): _description_
    + suite (str, optional): Run unit tests. See examples below. Defaults to an empty string.
    + test (str, optional): Run unit test. See examples below. Defaults 'all'.
    + host (str, optional): _description_. Defaults to an empty string.
    + database (str, optional): _description_. Defaults to an empty string.
    + port (str, optional): _description_. Defaults to an empty string.
    + user (str, optional): _description_. Defaults to an empty string.
    + password (str, optional): _description_. Defaults to an empty string.
    + lint (str, optional): _description_. Defaults to an empty string.

    # Examples

    Running unit tests:

    ```python
    >>> inv ci --suite empower \ 
        --user <user> \ 
        --password <password> \ 
        --port <port> \ 
        --host <host> \ 
        --database <database>

    >>> inv ci --suite empower \ 
        --test invalid_user \ 
        --user <user> \ 
        --password <password>
    ```
    """

    pass
