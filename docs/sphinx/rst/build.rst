=====
Build
=====

The documentation shows how to build the package from source.

Install System and Package dependencies
---------------------------------------

Read through :doc:`bootstrap`.

Build Your Own Version
----------------------

Document your new version in ``setup.py`` and remove previous versions from ``dist`` otherwise ``twine`` won't upload it. Build with:

.. code:: bash

    python -m build


Install the build to the virtual environment:

.. code:: bash

    source .env/bin/activate
    python setup.py install


Optionally, install the local src:

.. code:: bash

    pip install -e .


Test the build with:

.. code:: bash

    python -m lifespline_utils.connection
