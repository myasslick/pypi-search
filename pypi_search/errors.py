# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

PACKAGE_NOT_FOUND_ERROR_MSG = u"Package {package_name} not found"

class PackageNotFound(Exception):
    def __init__(self, package_name):
        self.message = PACKAGE_NOT_FOUND_ERROR_MSG.format(
            package_name=package_name)
        super(PackageNotFound, self).__init__(self.message)
