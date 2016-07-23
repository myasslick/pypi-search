# pypi-search
I don't know. I heard pip search command only returns the latest version, not all.

# Usage

First, clone this repository.

```!bash
git clone https://github.com/yeukhon/pypi-search
```

Next, install the dependencies:

```!bash
# For contributor / development only
pip install -r requirements/development.txt

# For user, run this only
pip install -r requirements/requirements.txt
```

Then, run this to install Python package.

```!bash
# use `develop` if you are developing.
python setup.py [install|develop]
```

# Maintain pypi-search-sample

In order to support our functional tests
[pypi-search-sample](https://pypi.python.org/pypi/pypi-search-sample) was created on PyPI.
To push package to PyPI, follow the instructions below:

```!bash
# Go into sample directory
cd pypi-search-sample

# Build wheel package
python setup.py bdist_wheel

# Upload project to PyPI
twine upload dist/*
```

Use [Packaging and Distributing Projects](https://packaging.python.org/distributing/#install-requires)
for reference.
