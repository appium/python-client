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

from typing import Dict

from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.bundle_id_option import BundleIdOption
from appium.options.common.postrun_option import PostrunOption
from appium.options.common.prerun_option import PrerunOption
from appium.options.common.system_host_option import SystemHostOption
from appium.options.common.system_port_option import SystemPortOption

from .app_path_option import AppPathOption
from .arguments_option import ArgumentsOption
from .bootstrap_root_option import BootstrapRootOption
from .environment_option import EnvironmentOption
from .server_startup_timeout_option import ServerStartupTimeoutOption
from .show_server_logs_option import ShowServerLogsOption
from .skip_app_kill_option import SkipAppKillOption
from .web_driver_agent_mac_url_option import WebDriverAgentMacUrlOption


class Mac2Options(
    AppiumOptions,
    AppPathOption,
    PrerunOption,
    PostrunOption,
    ArgumentsOption,
    BootstrapRootOption,
    BundleIdOption,
    EnvironmentOption,
    ServerStartupTimeoutOption,
    ShowServerLogsOption,
    SkipAppKillOption,
    SystemHostOption,
    SystemPortOption,
    WebDriverAgentMacUrlOption,
):
    @PrerunOption.prerun.setter  # type: ignore
    def prerun(self, value: Dict[str, str]) -> None:
        """
        A mapping containing either 'script' or 'command' key. The value of
        each key must be a valid AppleScript script or command to be
        executed after before Mac2Driver session is started. See
        https://github.com/appium/appium-mac2-driver#applescript-commands-execution
        for more details.
        """
        PrerunOption.prerun.fset(self, value)  # type: ignore

    @PostrunOption.postrun.setter  # type: ignore
    def postrun(self, value: Dict[str, str]) -> None:
        """
        A mapping containing either 'script' or 'command' key. The value of
        each key must be a valid AppleScript script or command to be
        executed after Mac2Driver session is stopped. See
        https://github.com/appium/appium-mac2-driver#applescript-commands-execution
        for more details.
        """
        PostrunOption.postrun.fset(self, value)  # type: ignore

    @SystemPortOption.system_port.setter  # type: ignore
    def system_port(self, value: int) -> None:
        """
        Set the number of the port for the internal server to listen on.
        If not provided then Mac2Driver will use the default port 10100.
        """
        SystemPortOption.system_port.fset(self, value)  # type: ignore

    @SystemHostOption.system_host.setter  # type: ignore
    def system_host(self, value: str) -> None:
        """
        Set the number of the port for the internal server to listen on.
        If not provided then Mac2Driver will use the default host
        address 127.0.0.1. You could set it to 0.0.0.0 to make the
        server listening on all available network interfaces.
        It is also possible to set the particular interface name, for example en1.
        """
        SystemHostOption.system_host.fset(self, value)  # type: ignore

    @BundleIdOption.bundle_id.setter  # type: ignore
    def bundle_id(self, value: str) -> None:
        """
        Set the bundle identifier of the application to automate, for example
        com.apple.TextEdit. This is an optional capability. If it is not provided
        then the session will be started without an application under test
        (actually, it will be Finder). If the application with the given
        identifier is not installed then an error will be thrown on session
        startup. If the application is already running then it will be moved to
        the foreground.
        """
        BundleIdOption.bundle_id.fset(self, value)  # type: ignore

    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'Mac2',
            PLATFORM_NAME: 'Mac',
        }
