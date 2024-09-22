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
from typing import Any, Dict


def get_desired_capabilities(platform_name: str) -> Dict[str, Any]:
    desired_caps: Dict[str, Any] = {}
    if platform_name == 'android':
        desired_caps.update(
            {
                'platformName': 'Android',
                'deviceName': 'Android Emulator',
                'newCommandTimeout': 120,
                'uiautomator2ServerInstallTimeout': 120000,
                'adbExecTimeout': 120000,
                'app': os.getenv('FLUTTER_ANDROID_APP'),
                'autoGrantPermissions': True
            }
        )
    else:
        desired_caps.update(
            {
                'deviceName': os.getenv('IPHONE_MODEL'),
                'platformName': 'iOS',
                'platformVersion': os.getenv('IOS_VERSION'),
                'allowTouchIdEnroll': True,
                'wdaLaunchTimeout': 240000,
                'wdaLocalPort': 8100,
                'eventTimings': True,
                'app': os.getenv('FLUTTER_IOS_APP'),
            }
        )

    return desired_caps
