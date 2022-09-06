# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# extract documentation from the module
sys.path.insert(0, os.path.abspath('../../src/lifespline_utils'))

# extract documentation from the task-runner
sys.path.insert(0, os.path.abspath('../..'))

# extract documenation from the module utils
sys.path.insert(0, os.path.abspath('../../utils'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lifespline-utils'
copyright = '2022, lifespline'
author = 'lifespline'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    # test docstring
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    # reference other pages
    'sphinx.ext.autosectionlabel',
]
autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
# html_static_path = ['_static']

intersphinx_mapping = {'numpy': ('https://numpy.org/doc/stable', None)}
