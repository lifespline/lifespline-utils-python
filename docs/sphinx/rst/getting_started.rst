===============
Getting Started
===============

Installation
------------

The package is hosted in `PyPI`_, so you can pull the package to your local virtual environment with:

.. code::

   pip install lifespline-utils==1.0.0

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
   INFO: Connecting to source: <host>
   ╰─(connection.py:124)
   >>> conn.read_sql("select USER from dual")
            USER
   0   <username>


For more examples, check the test scenarios in the tests directory.

.. _pypi: https://pypi.org/project/lifespline/
