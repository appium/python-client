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

import os
from typing import Dict, Optional, Union

# Returns abs path relative to this file and not cwd


def PATH(p: str) -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', p)
    )


def get_desired_capabilities(app: Optional[str] = None) -> Dict[str, Union[str, int, bool]]:
    desired_caps: Dict[str, Union[str, int, bool]] = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'newCommandTimeout': 240,
        'automationName': 'UIAutomator2',
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000
    }

    if app is not None:
        desired_caps['app'] = PATH(os.path.join('../..', 'apps', app))

    return desired_caps
