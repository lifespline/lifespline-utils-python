"""Configuration file for the Sphinx documentation builder."""

import os
import sys

# Note
#
# An alternative to changing the sys.path variable is to create a
# pyproject.toml file and make the code installable, so it behaves like any 
# other Python library. However, the sys.path approach is simpler.
sys.path.insert(0, os.path.abspath("../src/lifespline_utils"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

PROJECT = "lifespline-utils-python"
COPYRIGHT = "2022, lifespline"
AUTHOR = "lifespline"
RELEASE = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # display docs build time
    "sphinx.ext.duration",
    # process docstrings in src
    "sphinx.ext.autodoc",
    # test code snippets
    "sphinx.ext.doctest",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

HTML_THEME = "furo"
html_static_path = ["_static"]
