# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypi_search import search

import pytest

from ..base import read_response_from_file

# Scope static fixtures to `module` to avoid re-calling fixtures.
@pytest.fixture
def success_case(scope="module"):
    return read_response_from_file("large", "success.json")

def test_search_pypi_search_sample_returns_data(success_case):
    """
    Expect to get JSON response back from PyPI on
    pypi-search-sample package.

    """

    package_name = "pypi-search-sample"
    response = search.search_by_name(package_name)

    # Reset "downloads" from comparison (see issue #18)
    for tag, release in response["releases"].items():
        release[0]["downloads"] = 0
    for url in response["urls"]:
        url["downloads"] = 0

    assert response == success_case
