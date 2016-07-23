# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests

SEARCH_URL = "http://pypi.python.org/pypi/{name}/json"
SEARCH_HEADERS = {"Content-Type": "application/json"}

def search_by_name(package_name):
    """Search Python package on PyPI by package name only.

    Parameters
    ----------
    package_name : str


    Returns
    -------
    dict
        If package is found on PyPI, the metadata of all
        available versions will be returned.

    """

    url = SEARCH_URL.format(name=package_name)
    r = requests.get(url, headers=SEARCH_HEADERS)
    return r.json()
