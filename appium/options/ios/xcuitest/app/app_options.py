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


class AppInstallStrategyOption(SupportsCapabilities):
    APP_INSTALL_STRATEGY = "appInstallStrategy"
    app_install_strategy = OptionsDescriptor[Optional[str], str](APP_INSTALL_STRATEGY)
    """
    Select application installation strategy for real devices. The following
    strategies are supported:
    * serial (default) - pushes app files to the device in a sequential order;
    this is the least performant strategy, although the most reliable;
    * parallel - pushes app files simultaneously; this is usually the
    most performant strategy, but sometimes could not be very stable;
    * ios-deploy - tells the driver to use a third-party tool ios-deploy to
    install the app; obviously the tool must be installed separately
    first and must be present in PATH before it could be used.

    Usage
    -----
    - Get
        - `self.app_install_strategy`
    - Set
        - `self.app_install_strategy` = `value`
    
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


class AppPushTimeoutOption(SupportsCapabilities):
    APP_PUSH_TIMEOUT = "appPushTimeout"
    app_push_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]](
        APP_PUSH_TIMEOUT, transform_duration_get, transform_duration_set
    )
    """
    The timeout for application upload.
    Works for real devices only.
    The default value is 30000ms.

    Usage
    -----
    - Get
        - `self.app_push_timeout`
    - Set
        - `self.app_push_timeout` = `value`
    
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


class LocalizableStringsDirOption(SupportsCapabilities):
    LOCALIZABLE_STRINGS_DIR = "localizableStringsDir"
    localizable_strings_dir = OptionsDescriptor[Optional[str], str](LOCALIZABLE_STRINGS_DIR)
    """
    Where to look for localizable strings in the application bundle.
    Defaults to en.lproj.

    Usage
    -----
    - Get
        - `self.localizable_strings_dir`
    - Set
        - `self.localizable_strings_dir` = `value`
    
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
