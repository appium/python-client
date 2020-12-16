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
from typing import Any, Dict, Optional

# Returns abs path relative to this file and not cwd


def PATH(p: str) -> str: return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


BUNDLE_ID = 'com.example.apple-samplecode.UICatalog'


def get_desired_capabilities(app: Optional[str] = None) -> Dict[str, Any]:
    desired_caps: Dict[str, Any] = {
        'deviceName': iphone_device_name(),
        'platformName': 'iOS',
        'platformVersion': '13.6',
        'automationName': 'XCUITest',
        'allowTouchIdEnroll': True,
        'wdaLocalPort': wda_port(),
        'simpleIsVisibleCheck': True
    }

    if app is not None:
        desired_caps['app'] = PATH(os.path.join('../../..', 'apps', app))

    return desired_caps


class PytestXdistWorker:
    NUMBER: Optional[str] = os.getenv('PYTEST_XDIST_WORKER')
    COUNT: Optional[str] = os.getenv('PYTEST_XDIST_WORKER_COUNT')  # Return 2 if `-n 2` is passed

    @staticmethod
    def gw(number: int) -> str:
        if PytestXdistWorker.COUNT is None:
            return '0'

        if number >= int(PytestXdistWorker.COUNT):
            return 'gw0'

        return f'gw{number}'

# If you run tests with pytest-xdist, you can run tests in parallel.


def wda_port() -> int:
    if PytestXdistWorker.NUMBER == PytestXdistWorker.gw(1):
        return 8101

    return 8100


# Before running tests, you must have iOS simulators named 'iPhone 8 - 8100' and 'iPhone 8 - 8101'


def iphone_device_name() -> str:
    if PytestXdistWorker.NUMBER == PytestXdistWorker.gw(0):
        return 'iPhone 8 - 8100'
    elif PytestXdistWorker.NUMBER == PytestXdistWorker.gw(1):
        return 'iPhone 8 - 8101'

    return 'iPhone 8'
