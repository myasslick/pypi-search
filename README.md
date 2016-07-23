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
python setup.py [install|develop}
```
