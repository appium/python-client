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
from typing import Any

from appium.options.common.supports_capabilities import SupportsCapabilities

class WindowsOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name in ("CREATE_SESSION_TIMEOUT", "WAIT_FOR_APP_LAUNCH"):
            getattr(obj, "set_capability")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capability")(self.name, value)


class AppArgumentsOption(SupportsCapabilities):
    APP_ARGUMENTS = 'appArguments'
    app_arguments = WindowsOptionsDescriptor("APP_ARGUMENTS")


class AppTopLevelWindowOption(SupportsCapabilities):
    APP_TOP_LEVEL_WINDOW = 'appTopLevelWindow'
    app_top_level_window = WindowsOptionsDescriptor("APP_TOP_LEVEL_WINDOW")


class AppWorkingDirOption(SupportsCapabilities):
    APP_WORKING_DIR = 'appWorkingDir'
    app_working_dir = WindowsOptionsDescriptor("APP_WORKING_DIR")


class CreateSessionTimeoutOption(SupportsCapabilities):
    CREATE_SESSION_TIMEOUT = 'createSessionTimeout'
    create_session_timeout = WindowsOptionsDescriptor("CREATE_SESSION_TIMEOUT")


class ExperimentalWebDriverOption(SupportsCapabilities):
    EXPERIMENTAL_WEB_DRIVER = 'ms:experimental-webdriver'
    experimental_webdriver = WindowsOptionsDescriptor("EXPERIMENTAL_WEB_DRIVER")


class WaitForAppLaunchOption(SupportsCapabilities):
    WAIT_FOR_APP_LAUNCH = 'ms:waitForAppLaunch'
    wait_for_app_launch = WindowsOptionsDescriptor("WAIT_FOR_APP_LAUNCH")