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

# Returns abs path relative to this file and not cwd


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


BUNDLE_ID = 'com.example.apple-samplecode.UICatalog'


def get_desired_capabilities(app):
    desired_caps = {
        'deviceName': iphone_device_name(),
        'platformName': 'iOS',
        'platformVersion': '10.3',
        'app': PATH('../../apps/' + app),
        'automationName': 'XCUITest',
        'allowTouchIdEnroll': True,
        'wdaLocalPort': wda_port(),
    }

    return desired_caps

# If you run tests with pytest-xdist, you can run tests in parallel.


def wda_port():
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 8101

    return 8100

# Before running tests, you must have iOS simulators named 'iPhone 6s - 8100' and 'iPhone 6s - 8101'


def iphone_device_name():
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return 'iPhone 6s - 8100'
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 'iPhone 6s - 8101'

    return 'iPhone 6s'
