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

# pylint: disable=abstract-method


class BaseSearchContext(object):
    """Used by each search context. Dummy find_element/s are for preventing pylint error"""

    def find_element(self, by=None, value=None):
        raise NotImplementedError

    def find_elements(self, by=None, value=None):
        raise NotImplementedError
