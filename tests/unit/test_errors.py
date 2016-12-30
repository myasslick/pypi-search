# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

import pytest
import httpretty

from pypi_search import errors


TEST_PACKAGE_NAME = u"pypi-search-fake-package"

def test_package_not_found_error_message():
    """Check PackageNotFound error message."""
    error_msg = errors.PACKAGE_NOT_FOUND_ERROR_MSG.format(
        package_name=TEST_PACKAGE_NAME)

    with pytest.raises(errors.PackageNotFound) as e:
        raise errors.PackageNotFound(TEST_PACKAGE_NAME)

    assert e.value.message == error_msg
