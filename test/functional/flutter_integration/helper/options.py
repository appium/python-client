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

from appium.options.flutter_integration.base import FlutterOptions
from test.functional.test_helper import get_wda_port, get_worker_info


def PATH(p: str) -> str:
    """Get the absolute path of a file relative to the folder where this file is located."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def is_platform_android() -> bool:
    """Check if the current platform is Android."""
    return os.getenv('PLATFORM', 'android').lower() == 'android'


def get_flutter_system_port() -> int:
    """
    Get a unique Flutter system port for the current worker.
    Uses base port 9999 and increments by worker number.
    """
    worker_info = get_worker_info()
    return 9999 + (worker_info.worker_number or 0)


def make_options() -> FlutterOptions:
    """Get Flutter options configured for testing with parallel execution support."""
    options = FlutterOptions()

    # Set Flutter-specific capabilities
    options.flutter_system_port = get_flutter_system_port()
    options.flutter_enable_mock_camera = True
    options.flutter_element_wait_timeout = 10000
    options.flutter_server_launch_timeout = 120000

    caps: Dict[str, Any] = (
        {
            'platformName': 'Android',
            'deviceName': device_name(),
            'newCommandTimeout': 120,
            'uiautomator2ServerInstallTimeout': 120000,
            'adbExecTimeout': 120000,
            'app': os.getenv('FLUTTER_ANDROID_APP'),
            'autoGrantPermissions': True,
        }
        if is_platform_android()
        else {
            'deviceName': device_name(),
            'platformName': 'iOS',
            'platformVersion': os.getenv('IOS_VERSION'),
            'allowTouchIdEnroll': True,
            'wdaLaunchTimeout': 240000,
            'wdaLocalPort': get_wda_port(),
            'eventTimings': True,
            'app': os.getenv('FLUTTER_IOS_APP'),
        }
    )

    return options.load_capabilities(caps)


def device_name() -> str:
    """
    Get a unique device name for the current worker.
    Uses the base device name and appends the port number for uniqueness.
    """
    if is_platform_android():
        prefix = 'Android Emulator'
    else:
        prefix = os.getenv('IPHONE_MODEL') or 'iPhone 15 Plus'

    worker_info = get_worker_info()

    if worker_info.is_parallel:
        port = get_flutter_system_port() if is_platform_android() else get_wda_port()
        return f'{prefix} - {port}'

    return prefix
