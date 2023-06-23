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


class AppOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == "APP_PUSH_TIMEOUT":
            value = getattr(obj, "get_capability")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == "APP_PUSH_TIMEOUT":
            return getattr(obj, "set_capability")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        return getattr(obj, "set_capability")(self.name, value)


class AppInstallStrategyOption(SupportsCapabilities):
    APP_INSTALL_STRATEGY = 'appInstallStrategy'
    app_install_strategy = AppOptionsDescriptor("APP_INSTALL_STRATEGY")
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
    - `self.app_install_strategy`
    - `self.app_install_strategy` = `value`
    """


class AppPushTimeoutOption(SupportsCapabilities):
    APP_PUSH_TIMEOUT = 'appPushTimeout'
    app_push_timeout = AppOptionsDescriptor("APP_PUSH_TIMEOUT")
    """
    The timeout for application upload.
    Works for real devices only.
    The default value is 30000ms.

    Usage
    -----
    - `self.app_push_timeout`
    - `self.app_push_timeout` = `value`
    """


class LocalizableStringsDirOption(SupportsCapabilities):
    LOCALIZABLE_STRINGS_DIR = 'localizableStringsDir'
    localizable_strings_dir = AppOptionsDescriptor("LOCALIZABLE_STRINGS_DIR")
    """
    Where to look for localizable strings in the application bundle.
    Defaults to en.lproj.

    Usage
    -----
    - `self.localizable_strings_dir`
    - `self.localizable_strings_dir` = `value`
    """
