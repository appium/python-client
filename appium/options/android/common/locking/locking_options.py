# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from datetime import timedelta
from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar("C", bound="SupportsCapabilities")


class SkipLockOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == "UNLOCK_SUCCESS_TIMEOUT":
            value = getattr(obj, "get_capability")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == "UNLOCK_SUCCESS_TIMEOUT":
            return getattr(obj, "set_capability")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        return getattr(obj, "set_capability")(self.name, value)


class SkipUnlockOption(SupportsCapabilities):
    SKIP_UNLOCK = 'skipUnlock'
    skip_unlock = SkipLockOptionsDescriptor("SKIP_UNLOCK")
    """
    Whether to skip the check for lock screen presence (true). By default,
    the driver tries to detect if the device's screen is locked
    before starting the test and to unlock that (which sometimes might be unstable).
    Note, that this operation takes some time, so it is highly recommended to set
    this capability to true and disable screen locking on devices under test.

    Usage
    -----
    - `self.skip_unlock`
    - `self.skip_unlock` = `value`
    """


class UnlockKeyOption(SupportsCapabilities):
    UNLOCK_KEY = 'unlockKey'
    unlock_key = SkipLockOptionsDescriptor("UNLOCK_KEY")
    """
    Allows to set an unlock key.
    Read [Unlock tutorial](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)
    for more details.

    Usage
    -----
    - `self.unlock_key`
    - `self.unlock_key` = `value`
    """

class UnlockStrategyOption(SupportsCapabilities):
    UNLOCK_STRATEGY = 'unlockStrategy'
    unlock_strategy = SkipLockOptionsDescriptor("UNLOCK_STRATEGY")
    """
    Either 'locksettings' (default) or 'uiautomator'.
    Setting it to 'uiautomator' will enforce the driver to avoid using special
    ADB shortcuts in order to speed up the unlock procedure.

    Usage
    -----
    - `self.unlock_strategy`
    - `self.unlock_strategy` = `value`
    """


class UnlockSuccessTimeoutOption(SupportsCapabilities):
    UNLOCK_SUCCESS_TIMEOUT = 'unlockSuccessTimeout'
    unlock_success_timeout = SkipLockOptionsDescriptor("UNLOCK_SUCCESS_TIMEOUT")
    """
    Maximum timeout to wait until the device is unlocked.
    2000 ms by default.

    Usage
    -----
    - `self.unlock_success_timeout`
    - `self.unlock_success_timeout` = `value`
    """


class UnlockTypeOption(SupportsCapabilities):
    UNLOCK_TYPE = 'unlockType'
    unlock_type = SkipLockOptionsDescriptor("UNLOCK_TYPE")
    """
    Gets and Sets one of the possible types of Android lock screens to unlock.
    Read the Unlock tutorial](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)
    for more details.

    - `self.unlock_type`
    - `self.unlock_type` = `value`
    """