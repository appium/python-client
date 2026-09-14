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

from typing import Any, Dict


def get_desired_capabilities() -> Dict[str, Any]:
    desired_caps: Dict[str, Any] = {'platformName': 'mac', 'automationName': 'Mac2', 'bundleId': 'com.apple.TextEdit'}

    return desired_caps
