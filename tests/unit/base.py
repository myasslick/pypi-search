# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import contextlib
import json
import os

import requests
import httpretty

def read_response_from_file(filename):
    """Load test case file in JSON from fixture directory."""

    curr_dir = os.path.abspath(os.path.dirname(__file__))
    fixture_fpath = os.path.join(curr_dir, "fixtures/" + filename)

    with open(fixture_fpath, "r") as f:
        return json.load(f)

@contextlib.contextmanager
def enable_httpretty(*args, **kwargs):
    httpretty.disable()
    httpretty.enable()
    yield
    httpretty.disable()
