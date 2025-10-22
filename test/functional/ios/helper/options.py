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
from typing import Optional

from appium.options.ios import XCUITestOptions
from test.functional.test_helper import get_wda_port, get_worker_info


def PATH(p: str) -> str:
    """Get the absolute path of a file relative to the folder where this file is located."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def make_options(app: Optional[str] = None) -> XCUITestOptions:
    """Get XCUITest options configured for iOS testing with parallel execution support."""
    options = XCUITestOptions()

    # Set basic iOS capabilities
    options.device_name = iphone_device_name()
    options.platform_version = os.getenv('IOS_VERSION') or '17.4'
    options.allow_touch_id_enroll = True
    options.wda_local_port = get_wda_port()
    options.simple_is_visible_check = True

    if app is not None:
        options.app = PATH(os.path.join('..', '..', '..', 'apps', app))

    if local_prebuilt_wda := os.getenv('LOCAL_PREBUILT_WDA'):
        options.use_preinstalled_wda = True
        options.prebuilt_wda_path = local_prebuilt_wda

    return options


def iphone_device_name() -> str:
    """
    Get a unique device name for the current worker.
    Uses the base device name and appends the port number for uniqueness.
    """
    prefix = os.getenv('IPHONE_MODEL') or 'iPhone 15 Plus'
    worker_info = get_worker_info()

    if worker_info.is_parallel:
        port = get_wda_port()
        return f'{prefix} - {port}'

    return prefix
