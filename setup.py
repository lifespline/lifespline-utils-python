"""[summary].
"""
import os
from typing import List

from setuptools import setup

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()


def _get_installation_requirements() -> List[str]:
    """Get dependencies for python package.

    # Returns

    `[str]`: A list of dependencies for this package
    """
    # assuming `python -m build` is run from the project root
    project_root: str = os.getcwd()
    requirements: str = f"{project_root}/requirements.txt"

    with open(requirements, mode="r", encoding="UTF-8") as deps:
        dependencies = list(deps)

        def remove_comments(token: str) -> str:
            return not token.startswith("#")

        # clean dependencies
        dependencies = list(filter(remove_comments, dependencies))
        # remove whitespace
        dependencies = list(map(str.strip, dependencies))
        # remove empty strings
        dependencies = list(filter(bool, dependencies))

        return dependencies


# published package information (migrated to feed platform doc)
host: str = "github.com"
version: str = "1.0.0"
org: str = "lifespline"
project: str = "lifespline-utils-python"
author: str = "lifespline"
email: str = "lifespline@fastmail.com"
short_description: str = "A collection of python utilities for the Lifespline project"

setup(
    python_requires=">=3.6",
    install_requires=_get_installation_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "",
        "Operating System :: OS Independent",
    ],
    # pip info:
    name=project,
    version=version,
    author=author,
    author_email=email,
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://{host}/{org}/{project}",
    # import info
    package_dir={"": "src"},
    packages=["lifespline_utils"],
)
