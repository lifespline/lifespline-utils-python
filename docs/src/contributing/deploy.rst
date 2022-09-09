======
Deploy
======

About
-----

The documentation shows how to deploy your module to PyPI.

``pip`` needs to authenticate with the PyPi registry. Create ``.env/.pypirc`` such that:

.. code-block:: yml

  [distutils]
  Index-servers =
    <org|feed>

  [<org|feed>]
  Repository = https://pypi.org/project/lifespline/
  username = __token__
  password = <pat>


`pip` can now authenticate with the Azure Feed and deploy your package with `twine`.

.. code:: bash

  python -m twine upload -r <org|feed> --config-file .env/.pypirc dist/*

Example:

.. code:: bash

  example here
