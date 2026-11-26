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

from datetime import timedelta
from os import PathLike, fspath
from typing import Any, TypeVar

from appium.options.common.app_option import AppOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import APPIUM_PREFIX, PLATFORM_NAME, AppiumOptions
from appium.options.common.postrun_option import PostrunOption
from appium.options.common.prerun_option import PrerunOption
from appium.options.windows.windows.app_arguments_option import AppArgumentsOption
from appium.options.windows.windows.app_top_level_window_option import APP_TOP_LEVEL_WINDOW, AppTopLevelWindowOption
from appium.options.windows.windows.app_working_dir_option import AppWorkingDirOption
from appium.options.windows.windows.wait_for_app_launch_option import WAIT_FOR_APP_LAUNCH, WaitForAppLaunchOption

SHOULD_CLOSE_APP = 'shouldCloseApp'
FORCE_QUIT = 'ms:forcequit'
ISOLATED_SCRIPT_EXECUTION = 'isolatedScriptExecution'
SMOOTH_POINTER_MOVE = 'smoothPointerMove'
DELAY_BEFORE_CLICK = 'delayBeforeClick'
DELAY_AFTER_CLICK = 'delayAfterClick'
LOG_FILE = 'logFile'
PERF_METRICS = 'perfMetrics'
WEBVIEW_ENABLED = 'webviewEnabled'
WEBVIEW_DEVTOOLS_PORT = 'webviewDevtoolsPort'
CHROMEDRIVER_EXECUTABLE_PATH = 'chromedriverExecutablePath'
EDGEDRIVER_EXECUTABLE_PATH = 'edgedriverExecutablePath'
CHROMEDRIVER_CDN_URL = 'chromedriverCdnUrl'
EDGEDRIVER_CDN_URL = 'edgedriverCdnUrl'
FFMPEG_EXECUTABLE_PATH = 'ffmpegExecutablePath'

MAX_WAIT_FOR_APP_LAUNCH_SECONDS = 120

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
    def wait_for_app_launch(self) -> timedelta | None:
        """
        Maximum wait duration for the application window to appear after launch.
        Values up to 120 are interpreted as seconds by Wincore; larger values are
        interpreted as milliseconds.
        """
        value = self.get_capability(WAIT_FOR_APP_LAUNCH)
        if value is None:
            return None
        if value > MAX_WAIT_FOR_APP_LAUNCH_SECONDS:
            return timedelta(milliseconds=value)
        return timedelta(seconds=value)

    @wait_for_app_launch.setter
    def wait_for_app_launch(self, value: timedelta | int | float) -> None:
        """
        Set how long to wait for the application window (or main window after a splash
        screen) to appear after launch. Numeric values up to 120 are read as seconds and
        larger values as milliseconds. ``timedelta`` values longer than 120 seconds are
        serialized in milliseconds.
        """
        if isinstance(value, timedelta):
            seconds = value.total_seconds()
            serialized: int | float = round(seconds * 1000) if seconds > MAX_WAIT_FOR_APP_LAUNCH_SECONDS else seconds
        else:
            serialized = value
        self.set_capability(WAIT_FOR_APP_LAUNCH, serialized)

    @property
    def should_close_app(self) -> bool | None:
        """
        Whether to close the application window when the session ends.
        """
        return self.get_capability(SHOULD_CLOSE_APP)

    @should_close_app.setter
    def should_close_app(self, value: bool) -> None:
        """
        Set whether to close the application window when the session ends.
        Defaults to True on the driver side; has no effect in Root sessions.
        """
        self.set_capability(SHOULD_CLOSE_APP, value)

    @property
    def force_quit(self) -> bool | None:
        """
        Whether to kill the application process instead of closing its window on session end.
        """
        return self.get_capability(FORCE_QUIT)

    @force_quit.setter
    def force_quit(self, value: bool) -> None:
        """
        Set whether to terminate the application process instead of closing its window
        when the application is closed at the end of the session.
        """
        self.set_capability(FORCE_QUIT, value)

    @property
    def isolated_script_execution(self) -> bool | None:
        """
        Whether PowerShell scripts run without loading the user profile.
        """
        return self.get_capability(ISOLATED_SCRIPT_EXECUTION)

    @isolated_script_execution.setter
    def isolated_script_execution(self, value: bool) -> None:
        """
        Set whether PowerShell scripts (windows: powerShell, prerun, postrun) run
        without loading the user profile.
        """
        self.set_capability(ISOLATED_SCRIPT_EXECUTION, value)

    @property
    def smooth_pointer_move(self) -> str | None:
        """
        Easing curve used for mouse pointer moves.
        """
        return self.get_capability(SMOOTH_POINTER_MOVE)

    @smooth_pointer_move.setter
    def smooth_pointer_move(self, value: str) -> None:
        """
        Set the easing curve for mouse pointer moves, such as 'linear', 'ease',
        'ease-in', 'ease-out', 'ease-in-out', or 'cubic-bezier(x1,y1,x2,y2)'.
        """
        self.set_capability(SMOOTH_POINTER_MOVE, value)

    @property
    def delay_before_click(self) -> timedelta | None:
        """
        Duration of the pointer move to an element before clicking it.
        """
        value = self.get_capability(DELAY_BEFORE_CLICK)
        return None if value is None else timedelta(milliseconds=value)

    @delay_before_click.setter
    def delay_before_click(self, value: timedelta | int) -> None:
        """
        Set the duration of the pointer move to an element before clicking it,
        either as a timedelta or an integer number of milliseconds.
        """
        self.set_capability(DELAY_BEFORE_CLICK, round(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)

    @property
    def delay_after_click(self) -> timedelta | None:
        """
        Duration to wait after each click.
        """
        value = self.get_capability(DELAY_AFTER_CLICK)
        return None if value is None else timedelta(milliseconds=value)

    @delay_after_click.setter
    def delay_after_click(self, value: timedelta | int) -> None:
        """
        Set the duration to wait after each click, either as a timedelta or
        an integer number of milliseconds.
        """
        self.set_capability(DELAY_AFTER_CLICK, round(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)

    @property
    def log_file(self) -> str | bool | None:
        """
        File path or boolean flag controlling session log mirroring.
        """
        return self.get_capability(LOG_FILE)

    @log_file.setter
    def log_file(self, value: str | PathLike[str] | bool) -> None:
        """
        Mirror the driver session log to a file. Pass True for a timestamped default
        path, a directory path ending in a separator, or an explicit file path.
        """
        self.set_capability(LOG_FILE, value if isinstance(value, bool) else fspath(value))

    @property
    def perf_metrics(self) -> bool | None:
        """
        Whether per-session performance counters are enabled.
        """
        return self.get_capability(PERF_METRICS)

    @perf_metrics.setter
    def perf_metrics(self, value: bool) -> None:
        """
        Enable or disable per-session performance counters for driver calls.
        """
        self.set_capability(PERF_METRICS, value)

    @property
    def webview_enabled(self) -> bool | None:
        """
        Whether automation of WebView2, Chrome, and Edge content over CDP is enabled.
        """
        return self.get_capability(WEBVIEW_ENABLED)

    @webview_enabled.setter
    def webview_enabled(self, value: bool) -> None:
        """
        Enable or disable automation of WebView2, Chrome, and Edge content over
        the Chrome DevTools Protocol.
        """
        self.set_capability(WEBVIEW_ENABLED, value)

    @property
    def webview_devtools_port(self) -> int | None:
        """
        Remote debugging port used to connect to WebView2 or browser CDP.
        """
        return self.get_capability(WEBVIEW_DEVTOOLS_PORT)

    @webview_devtools_port.setter
    def webview_devtools_port(self, value: int) -> None:
        """
        Set the remote debugging port to connect to for WebView2 or browser automation.
        """
        self.set_capability(WEBVIEW_DEVTOOLS_PORT, value)

    @property
    def chromedriver_executable_path(self) -> str | None:
        """
        Path to a local Chromedriver binary.
        """
        return self.get_capability(CHROMEDRIVER_EXECUTABLE_PATH)

    @chromedriver_executable_path.setter
    def chromedriver_executable_path(self, value: str | PathLike[str]) -> None:
        """
        Set the path to a local Chromedriver binary to use instead of downloading one.
        """
        self.set_capability(CHROMEDRIVER_EXECUTABLE_PATH, fspath(value))

    @property
    def edgedriver_executable_path(self) -> str | None:
        """
        Path to a local Microsoft Edge WebDriver binary.
        """
        return self.get_capability(EDGEDRIVER_EXECUTABLE_PATH)

    @edgedriver_executable_path.setter
    def edgedriver_executable_path(self, value: str | PathLike[str]) -> None:
        """
        Set the path to a local Microsoft Edge WebDriver (msedgedriver) binary
        to use instead of downloading one.
        """
        self.set_capability(EDGEDRIVER_EXECUTABLE_PATH, fspath(value))

    @property
    def chromedriver_cdn_url(self) -> str | None:
        """
        Custom CDN URL used to download Chromedriver.
        """
        return self.get_capability(CHROMEDRIVER_CDN_URL)

    @chromedriver_cdn_url.setter
    def chromedriver_cdn_url(self, value: str) -> None:
        """
        Set a custom CDN URL to download Chromedriver from.
        """
        self.set_capability(CHROMEDRIVER_CDN_URL, value)

    @property
    def edgedriver_cdn_url(self) -> str | None:
        """
        Custom CDN URL used to download Microsoft Edge WebDriver.
        """
        return self.get_capability(EDGEDRIVER_CDN_URL)

    @edgedriver_cdn_url.setter
    def edgedriver_cdn_url(self, value: str) -> None:
        """
        Set a custom CDN URL to download Microsoft Edge WebDriver from.
        """
        self.set_capability(EDGEDRIVER_CDN_URL, value)

    @property
    def ffmpeg_executable_path(self) -> str | None:
        """
        Path to a local FFmpeg binary used for screen recording.
        """
        return self.get_capability(FFMPEG_EXECUTABLE_PATH)

    @ffmpeg_executable_path.setter
    def ffmpeg_executable_path(self, value: str | PathLike[str]) -> None:
        """
        Set the path to a local FFmpeg binary used by screen recording.
        """
        self.set_capability(FFMPEG_EXECUTABLE_PATH, fspath(value))

    @property
    def default_capabilities(self) -> dict:
        return {
            AUTOMATION_NAME: 'Wincore',
            PLATFORM_NAME: 'windows',
        }
