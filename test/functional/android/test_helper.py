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

import sys


def is_py2():
    """
    Return bool if python2 is executed

    :return: True if python2 is executed
    :rtype: bool
    """
    return sys.version_info.major == 2


def is_py3():
    """
    Return bool if python3 is executed

    :return: True if python3 is executed
    :rtype: bool
    """
    return sys.version_info.major == 3
