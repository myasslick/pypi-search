#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import setup, find_packages

setup(
    name="pypi-search",
    version="0.1",
    description="CLI utility for looking up packages on PyPI",
    author="John Yeuk Hon Wong",
    author_email="yeukhon@acm.org",
    packages=find_packages(exclude=["tests*"]),
)
