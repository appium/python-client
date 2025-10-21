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
from dataclasses import dataclass
from typing import Optional

from appium.options.ios import XCUITestOptions

# Returns abs path relative to this file and not cwd


def PATH(p: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def make_options(app: Optional[str] = None) -> XCUITestOptions:
    """Get XCUITest options configured for iOS testing with parallel execution support."""
    options = XCUITestOptions()

    # Set basic iOS capabilities
    options.device_name = iphone_device_name()
    options.platform_version = os.getenv('IOS_VERSION') or '17.4'
    options.allow_touch_id_enroll = True
    options.wda_local_port = wda_port()
    options.simple_is_visible_check = True

    if app is not None:
        options.app = PATH(os.path.join('../../..', 'apps', app))

    local_prebuilt_wda = os.getenv('LOCAL_PREBUILT_WDA')
    if local_prebuilt_wda:
        options.use_preinstalled_wda = True
        options.prebuilt_wda_path = local_prebuilt_wda

    return options


@dataclass
class WorkerInfo:
    """Information about the current test worker in parallel execution."""

    worker_number: Optional[int]
    total_workers: Optional[int]

    @property
    def is_parallel(self) -> bool:
        """Check if running in parallel mode."""
        return self.worker_number is not None and self.total_workers is not None


def _get_worker_info() -> WorkerInfo:
    """
    Get current worker number and total worker count from pytest-xdist environment variables.

    Returns:
        WorkerInfo: Worker information or None values if not running in parallel
    """
    worker_number = os.getenv('PYTEST_XDIST_WORKER')
    worker_count = os.getenv('PYTEST_XDIST_WORKER_COUNT')

    if worker_number and worker_count:
        # Extract number from worker string like 'gw0', 'gw1', etc.
        try:
            worker_num = int(worker_number.replace('gw', ''))
            total_workers = int(worker_count)
            return WorkerInfo(worker_number=worker_num, total_workers=total_workers)
        except (ValueError, AttributeError):
            pass

    return WorkerInfo(worker_number=None, total_workers=None)


def wda_port() -> int:
    """
    Get a unique WDA port for the current worker.
    Uses base port 8100 and increments by worker number.
    """
    worker_info = _get_worker_info()
    return 8100 + (worker_info.worker_number or 0)


def iphone_device_name() -> str:
    """
    Get a unique device name for the current worker.
    Uses the base device name and appends the port number for uniqueness.
    """
    prefix = os.getenv('IPHONE_MODEL') or 'iPhone 15 Plus'
    worker_info = _get_worker_info()

    if worker_info.is_parallel:
        port = wda_port()
        return f'{prefix} - {port}'

    return prefix
