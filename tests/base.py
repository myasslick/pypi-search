# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import contextlib

import json
import os

import requests
import httpretty

def read_response_from_file(directory, filename):
    """
    Load test case file in JSON from fixture directory.

    Parameters
    ----------
    directory : str
        Kind of tests. Valid choices are ["unit", "large"].

    filename : str
        Name of the test case file in JSON.

    Returns
    -------
    dict
        JSON read from the file ``filename``.

    """

    curr_dir = os.path.abspath(os.path.dirname(__file__))
    fixture_dir = os.path.join(curr_dir, "fixtures/" + directory)
    fixture_fpath = os.path.join(fixture_dir, filename)

    with open(fixture_fpath, "r") as f:
        return json.load(f)

@contextlib.contextmanager
def enable_httpretty(*args, **kwargs):
    """Requests/HTTP mock decorator."""
    httpretty.disable()
    httpretty.enable()
    yield
    httpretty.disable()
