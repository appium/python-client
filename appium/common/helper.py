#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import OrderedDict

from appium import version as appium_version


def appium_bytes(value, encoding):
    """Return a bytes-like object

    Has _appium_ prefix to avoid overriding built-in bytes.

    Args:
        value (str): A value to convert
        encoding (str): A encoding which will convert to

    Returns:
        str: A bytes-like object
    """

    try:
        return bytes(value, encoding)  # Python 3
    except TypeError:
        return value  # Python 2


def extract_const_attributes(cls):
    """Return dict with constants attributes and values in the class(e.g. {'VAL1': 1, 'VAL2': 2})

    Args:
        cls (type): Class to be extracted constants

    Returns:
        OrderedDict: dict with constants attributes and values in the class
    """
    return OrderedDict(
        [(attr, value) for attr, value in vars(cls).items() if not callable(getattr(cls, attr)) and attr.isupper()])


def library_version():
    """Return a version of this python library
    """

    return appium_version.version
