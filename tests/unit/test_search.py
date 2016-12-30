# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

import pytest
import httpretty

from pypi_search import errors, search

from ..base import enable_httpretty, read_response_from_file

# Scope static fixtures to `module` to avoid re-calling fixtures.
@pytest.fixture
def success_case(scope="module"):
    package_name = "success"
    url = search.SEARCH_URL.format(name=package_name)
    status = 200
    response = read_response_from_file("unit", "success.json")
    response_serialized = json.dumps(response)
    return {
        "package_name": package_name,
        "url": url,
        "status": status,
        "response_s": response_serialized,
        "response": response
    }

@pytest.fixture
def not_found_case(scope="module"):
    package_name = "pypi-search-fake-package"
    url = search.SEARCH_URL.format(name=package_name)
    status = 404
    return {
        "package_name": package_name,
        "url": url,
        "status": status,
    }

def assert_success_case(success_case, test_response):
    assert test_response == success_case["response"]

def test_search_by_package_name_that_exists(success_case):
    """If a package exists, JSON should return."""

    httpretty.register_uri(httpretty.GET, success_case["url"],
        body=success_case["response_s"],
        status=success_case["status"]
    )

    test_response = search.search_by_name(success_case["package_name"])

def test_search_by_package_name_doesnt_exist(not_found_case):
    """If a package doesn't exist, `PackageNotFound` should be raised."""

    httpretty.register_uri(httpretty.GET, not_found_case["url"],
        status=not_found_case["status"]
    )

    with pytest.raises(errors.PackageNotFound) as e:
        search.search_by_name(not_found_case["package_name"])
