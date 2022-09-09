===============
Getting Started
===============

Installation
------------

The package is hosted in `PyPI`_, so you can pull the package to your local virtual environment with:

.. code::

   pip install lifespline-utils

Test the installation with:

.. code::

   python -m lifespline_utils.connection


Examples
--------

Create a new redshift connection:

.. code:: python

   >>> from lifespline_utils.connection import RedshiftConnection
   >>> conn: RedshiftConnection = RedshiftConnection()
   user name: <username>
   password: <password>
   >>> conn.read_sql("select USER from dual")
            USER
   0   <username>


For more examples, check the test scenarios in the tests directory.

.. _pypi: https://pypi.org/project/lifespline/
