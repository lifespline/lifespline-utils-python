======
Deploy
======

About
-----

The documentation shows how to deploy your module to PyPI.

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

`pip` can now authenticate with the Azure Feed and deploy your package with `twine`.

.. code:: bash

  python -m twine upload -r <org|feed> --config-file .env/.pypirc dist/*

Example:

.. code:: bash

  example here
