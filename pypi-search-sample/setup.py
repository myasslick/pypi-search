#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import setup, find_packages

setup(
    name="pypi-search-sample",
    version="0.1",
    description="Sample package for the infamous pypi-search package on PyPI",
    author="John Yeuk Hon Wong",
    author_email="yeukhon@acm.org",
    install_requires=[],
    packages=find_packages(exclude=["tests*"]),
    keywords=["pypi-search", "pypi-search-sample"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
