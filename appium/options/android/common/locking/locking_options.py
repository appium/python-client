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
from typing import Optional, Union

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.transformers import transform_duration_get, transform_duration_set


class SkipUnlockOption(SupportsCapabilities):
    SKIP_UNLOCK = "skipUnlock"
    skip_unlock = OptionsDescriptor[Optional[bool], bool](SKIP_UNLOCK)
    """
    Whether to skip the check for lock screen presence (true). By default,
    the driver tries to detect if the device's screen is locked
    before starting the test and to unlock that (which sometimes might be unstable).
    Note, that this operation takes some time, so it is highly recommended to set
    this capability to true and disable screen locking on devices under test.

    Usage
    -----
    - Get
        - `self.skip_unlock`
    - Set
        - `self.skip_unlock` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class UnlockKeyOption(SupportsCapabilities):
    UNLOCK_KEY = "unlockKey"
    unlock_key = OptionsDescriptor[Optional[str], bool](UNLOCK_KEY)
    """
    Allows to set an unlock key.
    Read [Unlock tutorial](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)
    for more details.

    Usage
    -----
    - Get
        - `self.unlock_key`
    - Set
        - `self.unlock_key` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class UnlockStrategyOption(SupportsCapabilities):
    UNLOCK_STRATEGY = "unlockStrategy"
    unlock_strategy = OptionsDescriptor[Optional[str], str](UNLOCK_STRATEGY)
    """
    Either 'locksettings' (default) or 'uiautomator'.
    Setting it to 'uiautomator' will enforce the driver to avoid using special
    ADB shortcuts in order to speed up the unlock procedure.

    Usage
    -----
    - Get
        - `self.unlock_strategy`
    - Set
        - `self.unlock_strategy` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class UnlockSuccessTimeoutOption(SupportsCapabilities):
    UNLOCK_SUCCESS_TIMEOUT = "unlockSuccessTimeout"
    unlock_success_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (UNLOCK_SUCCESS_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Maximum timeout to wait until the device is unlocked.
    2000 ms by default.

    Usage
    -----
    - Get
        - `self.unlock_success_timeout`
    - Set
        - `self.unlock_success_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


class UnlockTypeOption(SupportsCapabilities):
    UNLOCK_TYPE = "unlockType"
    unlock_type = OptionsDescriptor[Optional[str], str](UNLOCK_TYPE)
    """
    Gets and Sets one of the possible types of Android lock screens to unlock.
    Read the Unlock tutorial](https://github.com/appium/appium-android-driver/blob/master/docs/UNLOCK.md)
    for more details.

    Usage
    -----
    - Get
        - `self.unlock_type`
    - Set
        - `self.unlock_type` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """
