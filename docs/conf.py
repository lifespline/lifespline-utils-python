# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Note
#
# An alternative to changing the sys.path variable is to create a pyproject.toml
# file and make the code installable, so it behaves like any other Python library.
# However, the sys.path approach is simpler.
import os
import sys
# extract documentation from the module
sys.path.insert(0, os.path.abspath('../src/lifespline_utils'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lifespline-utils-python'
copyright = '2022, lifespline'
author = 'lifespline'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # display docs build time
    'sphinx.ext.duration',

    # process docstrings in src
    'sphinx.ext.autodoc',

    # test code snippets
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
