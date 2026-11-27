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

from typing import Any, TypeVar

from appium.options.common.app_option import AppOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import APPIUM_PREFIX, PLATFORM_NAME, AppiumOptions
from appium.options.common.postrun_option import PostrunOption
from appium.options.common.prerun_option import PrerunOption
from appium.options.windows.windows.app_arguments_option import AppArgumentsOption
from appium.options.windows.windows.app_top_level_window_option import APP_TOP_LEVEL_WINDOW, AppTopLevelWindowOption
from appium.options.windows.windows.app_working_dir_option import AppWorkingDirOption
from appium.options.windows.windows.wait_for_app_launch_option import WAIT_FOR_APP_LAUNCH

from .chromedriver_cdn_url_option import ChromedriverCdnUrlOption
from .chromedriver_executable_path_option import ChromedriverExecutablePathOption
from .delay_after_click_option import DelayAfterClickOption
from .delay_before_click_option import DelayBeforeClickOption
from .edgedriver_cdn_url_option import EdgedriverCdnUrlOption
from .edgedriver_executable_path_option import EdgedriverExecutablePathOption
from .ffmpeg_executable_path_option import FfmpegExecutablePathOption
from .force_quit_option import FORCE_QUIT, ForceQuitOption
from .isolated_script_execution_option import IsolatedScriptExecutionOption
from .log_file_option import LogFileOption
from .perf_metrics_option import PerfMetricsOption
from .should_close_app_option import ShouldCloseAppOption
from .smooth_pointer_move_option import SmoothPointerMoveOption
from .wait_for_app_launch_option import WaitForAppLaunchOption
from .webview_devtools_port_option import WebviewDevtoolsPortOption
from .webview_enabled_option import WebviewEnabledOption

T = TypeVar('T', bound='WincoreOptions')

_CAPABILITY_ALIASES: dict[str, str] = {
    f'{APPIUM_PREFIX}{FORCE_QUIT}': FORCE_QUIT,
    f'{APPIUM_PREFIX}{WAIT_FOR_APP_LAUNCH}': WAIT_FOR_APP_LAUNCH,
}


class WincoreOptions(
    AppiumOptions,
    PrerunOption,
    PostrunOption,
    AppOption,
    AppTopLevelWindowOption,
    AppWorkingDirOption,
    WaitForAppLaunchOption,
    AppArgumentsOption,
    ShouldCloseAppOption,
    ForceQuitOption,
    IsolatedScriptExecutionOption,
    SmoothPointerMoveOption,
    DelayBeforeClickOption,
    DelayAfterClickOption,
    LogFileOption,
    PerfMetricsOption,
    WebviewEnabledOption,
    WebviewDevtoolsPortOption,
    ChromedriverExecutablePathOption,
    EdgedriverExecutablePathOption,
    ChromedriverCdnUrlOption,
    EdgedriverCdnUrlOption,
    FfmpegExecutablePathOption,
):
    def set_capability(self: T, name: str, value: Any) -> T:  # type: ignore[override]
        return super().set_capability(_CAPABILITY_ALIASES.get(name, name), value)

    def get_capability(self, name: str) -> Any:
        return super().get_capability(_CAPABILITY_ALIASES.get(name, name))

    @property
    def app_top_level_window(self) -> str | None:
        """
        Handle of an already open top-level window to attach to, as a
        hexadecimal (``0x001A0B2C``) or decimal string.
        """
        return self.get_capability(APP_TOP_LEVEL_WINDOW)

    @app_top_level_window.setter
    def app_top_level_window(self, value: str) -> None:
        """
        Set the handle of an already open top-level window to attach to, as a
        hexadecimal (``0x001A0B2C``) or decimal string. Cannot be combined with
        ``app``; both may be omitted at startup to select a window later.
        """
        self.set_capability(APP_TOP_LEVEL_WINDOW, value)

    @property
    def default_capabilities(self) -> dict:
        return {
            AUTOMATION_NAME: 'Wincore',
            PLATFORM_NAME: 'windows',
        }
