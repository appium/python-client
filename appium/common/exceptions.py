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

from selenium.common.exceptions import InvalidSwitchToTargetException


class NoSuchContextException(InvalidSwitchToTargetException):
    """Thrown when context target to be switched doesn't exist.

    To find the current set of active contexts, you can get a list
    of the active contexts in the following way:

        print driver.contexts

    """
    pass
