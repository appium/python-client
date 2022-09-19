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

from appium.options.common.app_option import AppOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.postrun_option import PostrunOption
from appium.options.common.prerun_option import PrerunOption
from appium.options.common.system_port_option import SystemPortOption

from .app_arguments_option import AppArgumentsOption
from .app_top_level_window_option import AppTopLevelWindowOption
from .app_working_dir_option import AppWorkingDirOption
from .create_session_timeout_option import CreateSessionTimeoutOption
from .expreimental_web_driver_option import ExperimentalWebDriverOption
from .wait_for_app_launch_option import WaitForAppLaunchOption


class WindowsOptions(
    AppiumOptions,
    PrerunOption,
    PostrunOption,
    AppOption,
    AppTopLevelWindowOption,
    AppWorkingDirOption,
    CreateSessionTimeoutOption,
    ExperimentalWebDriverOption,
    SystemPortOption,
    WaitForAppLaunchOption,
    AppArgumentsOption,
):
    @AppOption.app.setter  # type: ignore
    def app(self, value: str) -> None:
        """
        The name of the UWP application to test or full path to a classic app,
        for example Microsoft.WindowsCalculator_8wekyb3d8bbwe!App or
        C:\\Windows\\System32\\notepad.exe. It is also possible to set app to Root.
        In such case the session will be invoked without any explicit target application
        (actually, it will be Explorer). Either this capability or appTopLevelWindow must
        be provided on session startup.
        """
        AppOption.app.fset(self, value)  # type: ignore

    @PrerunOption.prerun.setter  # type: ignore
    def prerun(self, value: Dict[str, str]) -> None:
        """
        A mapping containing either 'script' or 'command' key. The value of
        each key must be a valid PowerShell script or command to be
        executed prior to the WinAppDriver session startup.
        See https://github.com/appium/appium-windows-driver#power-shell-commands-execution
        for more details.
        """
        PrerunOption.prerun.fset(self, value)  # type: ignore

    @PostrunOption.postrun.setter  # type: ignore
    def postrun(self, value: Dict[str, str]) -> None:
        """
        A mapping containing either 'script' or 'command' key. The value of
        each key must be a valid PowerShell script or command to be
        executed after a WinAppDriver session is finished.
        See https://github.com/appium/appium-windows-driver#power-shell-commands-execution
        for more details.
        """
        PostrunOption.postrun.fset(self, value)  # type: ignore

    @SystemPortOption.system_port.setter  # type: ignore
    def system_port(self, value: int) -> None:
        """
        The port number to execute Appium Windows Driver server listener on,
        for example 5556. The port must not be occupied. The default starting port
        number for a new Appium Windows Driver session is 4724. If this port is
        already busy then the next free port will be automatically selected.
        """
        SystemPortOption.system_port.fset(self, value)  # type: ignore

    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'Windows',
            PLATFORM_NAME: 'Windows',
        }
