- [About](#about)
- [VSCode Python Interpreter](#vscode-python-interpreter)
- [Debugging](#debugging)
  - [Debugging Python Scripts](#debugging-python-scripts)
  - [Debugging pytest unit tests](#debugging-pytest-unit-tests)
  - [Disclaimer](#disclaimer)

# About

The document shows how to debug the project with vscode.

# VSCode Python Interpreter

The debugger needs to know the path to the libs installed in your project's virtual environment. Define the python interpreter path with:

1. `ctrl+shift+P`
1. `>Python: Select Interpreter`
1. `Entire Workspace`
1. `+Enter interpreter path...`
1. `Find...`
1. `<your-project-abs-path>/.env/bin/python3`

# Debugging

`.vscode/launch.json` contains unit test configurations for the vscode debugger.

## Debugging Python Scripts

The example below defines the configuration to debug the command `inv ci --suite utils --user <user> --password <password>`. Notice how the `invoke` module is specified. Add to `.vscode/launch.json::configurations`:

```json
{
    "name": "suite: redshift",
    "type": "python",
    "request": "launch",
    "module": "invoke",
    "python": "${workspaceFolder}/.env/bin/python3",
    "console": "integratedTerminal",
    "args": [
    "ci", "--suite", "redshift",
    "--user", "<user>",
    "--password", "<password>",
    ],
},
```


## Debugging pytest unit tests

 The example below defines the configuration for the unit test `no_args_invalid_user` of the test suite `redshift`, i.e., the `test_redshift_connection_no_args_invalid_user` unit test of the `test/test_redshift_connection.py` test suite. Add to `.vscode/launch.json::configurations`:

```json
{
    "version": "<version>",
    "configurations": [
        {
            "name": "suite: redshift, test: no_args_invalid_user",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "python": "${workspaceFolder}/.env/bin/python3",
            "console": "integratedTerminal",
            "args": [
                "test/test_redshift_connection.py::test_redshift_connection_no_args_invalid_user", "-s"
            ],
        },
    ]
}
```

 The example below defines the configuration for the unit test `invalid_user` of the test suite `redshift`. Notice how the secret values are persisted in plain test in the script. This is why `.vscode/launch.json` is ignored in `.vscode/.gitignore`.

```json
{
    "version": "<version>",
    "configurations": [
        {
            "name": "suite: empower, test: no_args_invalid_user",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "python": "${workspaceFolder}/.env/bin/python3",
            "console": "integratedTerminal",
            "args": [
                "test/test_redshift_connection.py::test_redshift_connection_no_args_invalid_user", "--user", "<user>"
                , "--password", "<password>"
            ],
        },
    ]
}
```

To debug the unit test, place you breakpoints on the desired lines of code, and debug.

## Disclaimer

+ It is recommended that the unit tests all be added manually to `.vscode/launch.json` so they can be conveniently debugged from vscode. It is FORBIDDEN to write secrets in  `.vscode/launch.json`.
+ Don't forget to specify the package's version in `.vscode/launch.json::version`.
