# About #

The document contains information on how to publish the pacakge to the Azure Feed.

# Deploy the package to the Azure Feed #

`pip` needs to authenticate with PyPi feed. Create `.env/.pypirc` such that:

```yml
[distutils]
Index-servers =
  <org|feed>

[<org|feed>]
Repository = https://pkgs.dev.azure.com/<org>/<project-id>/_packaging/<org|feed>/pypi/upload/
username = __token__
password = <pat>
```

Example:

```yml
[distutils]
Index-servers =
  heartbit

[heartbit]
Repository = https://pkgs.dev.azure.com/novonordiskit/058f2dd9-7a58-4b80-a8cd-b5cf0747939d/_packaging/heartbit/pypi/upload/
username = __token__
password = <pat>

```

`pip` can now authenticate with the Azure Feed and deploy your package with `twine`.

```bash
>>> python -m twine upload -r <org|feed> --config-file .env/.pypirc dist/*
```

Example:

```bash
>>> python -m twine upload -r <org|feed> --config-file .env/.pypirc dist/*
Uploading distributions to 
https://pkgs.dev.azure.com/novonordiskit/058f2dd9-7a58-4b80-a8cd-b5cf0747939d/_packaging/heartbit/pypi/upload/
Uploading hook_utils-1.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.2/22.2 kB • 00:00 • 24.8 MB/s
Uploading hook-utils-1.1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 kB • 00:00 • 54.4 MB/s
Uploading hook_utils-1.1.0-py3.8.egg
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 25.1/25.1 kB • 00:00 • 73.4 MB/s

```

The automated agent authenticates by fetching the `pat` directly from your access tokens. The contents of `azure-pipelines.yml` must contain:


```yml
variables:
  feed_name: <org>
  dist: dist/*

steps:
- script: |
    # cmds here

- task: TwineAuthenticate@1
  inputs:
    artifactFeed: ${{ variables.feed_name }}

- script: |
    # cmds here

    python3 -m twine \
    upload -r ${{ variables.feed_name }} \
    --config-file $(PYPIRC_PATH) ${{ variables.dist }}
```

Test the deployment of the package by installing it as specified in [`README.md`]()
