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

from appium.options.android import UiAutomator2Options
from test.functional.test_helper import get_worker_info


def make_options(app: Optional[str] = None) -> UiAutomator2Options:
    """Get UiAutomator2 options configured for Android testing with parallel execution support."""
    options = UiAutomator2Options()

    # Set basic Android capabilities
    options.device_name = android_device_name()
    options.platform_name = 'Android'
    options.automation_name = 'UIAutomator2'
    options.new_command_timeout = 240
    options.uiautomator2_server_install_timeout = 120000
    options.adb_exec_timeout = 120000

    if app is not None:
        options.app = app

    return options


def android_device_name() -> str:
    """
    Get a unique device name for the current worker.
    Uses the base device name and appends the port number for uniqueness.
    """
    prefix = os.getenv('ANDROID_MODEL') or 'Android Emulator'
    worker_info = get_worker_info()

    if worker_info.is_parallel:
        # For parallel execution, we can use different device names or ports
        # This is a simplified approach - in practice you might want to use different emulators
        return f'{prefix} - Worker {worker_info.worker_id}'

    return prefix
