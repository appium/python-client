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


class ContextOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if self.name == "AUTO_WEBVIEW_TIMEOUT":
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name == "AUTO_WEBVIEW_TIMEOUT":
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)


class AutoWebviewTimeoutOption(SupportsCapabilities):
    AUTO_WEBVIEW_TIMEOUT = 'autoWebviewTimeout'
    auto_webview_timeout = ContextOptionsDescriptor("AUTO_WEBVIEW_TIMEOUT")


class ChromeLoggingPrefsOption(SupportsCapabilities):
    CHROME_LOGGING_PREFS = 'chromeLoggingPrefs'
    chrome_logging_prefs = ContextOptionsDescriptor("CHROME_LOGGING_PREFS")


class ChromeOptionsOption(SupportsCapabilities):
    CHROME_OPTIONS = 'chromeOptions'
    chrome_options = ContextOptionsDescriptor("CHROME_OPTIONS")


class ChromedriverArgsOption(SupportsCapabilities):
    CHROMEDRIVER_ARGS = 'chromedriverArgs'
    chromedriver_args = ContextOptionsDescriptor("CHROMEDRIVER_ARGS")


class ChromedriverChromeMappingFileOption(SupportsCapabilities):
    CHROMEDRIVER_CHROME_MAPPING_FILE = 'chromedriverChromeMappingFile'
    chromedriver_chrome_mapping_file = ContextOptionsDescriptor("CHROMEDRIVER_CHROME_MAPPING_FILE")


class ChromedriverDisableBuildCheckOption(SupportsCapabilities):
    CHROMEDRIVER_DISABLE_BUILD_CHECK = 'chromedriverDisableBuildCheck'
    chromedriver_disable_build_check = ContextOptionsDescriptor("CHROMEDRIVER_DISABLE_BUILD_CHECK")


class ChromedriverExecutableDirOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE_DIR = 'chromedriverExecutableDir'
    chromedriver_executable_dir = ContextOptionsDescriptor("CHROMEDRIVER_EXECUTABLE_DIR")


class ChromedriverExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE = 'chromedriverExecutable'
    chromedriver_executable = ContextOptionsDescriptor("CHROMEDRIVER_EXECUTABLE")


class ChromedriverPortOption(SupportsCapabilities):
    CHROMEDRIVER_PORT = 'chromedriverPort'
    chromedriver_port = ContextOptionsDescriptor("CHROMEDRIVER_PORT")


class ChromedriverPortsOption(SupportsCapabilities):
    CHROMEDRIVER_PORTS = 'chromedriverPorts'
    chromedriver_ports = ContextOptionsDescriptor("CHROMEDRIVER_PORTS")


class ChromedriverUseSystemExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_USE_SYSTEM_EXECUTABLE = 'chromedriverUseSystemExecutable'
    chromedriver_use_system_executable = ContextOptionsDescriptor("CHROMEDRIVER_USE_SYSTEM_EXECUTABLE")

class EnsureWebviewsHavePagesOption(SupportsCapabilities):
    ENSURE_WEBVIEWS_HAVE_PAGES = 'ensureWebviewsHavePages'
    ensure_webviews_have_pages = ContextOptionsDescriptor("ENSURE_WEBVIEWS_HAVE_PAGES")


class ExtractChromeAndroidPackageFromContextNameOption(SupportsCapabilities):
    EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME = 'extractChromeAndroidPackageFromContextName'
    extract_chrome_android_package_from_context_name = ContextOptionsDescriptor("EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME")


class NativeWebScreenshotOption(SupportsCapabilities):
    NATIVE_WEB_SCREENSHOT = 'nativeWebScreenshot'
    native_web_screenshot = ContextOptionsDescriptor("NATIVE_WEB_SCREENSHOT")


class RecreateChromeDriverSessionsOption(SupportsCapabilities):
    RECREATE_CHROME_DRIVER_SESSIONS = 'recreateChromeDriverSessions'
    recreate_chrome_driver_sessions = ContextOptionsDescriptor("RECREATE_CHROME_DRIVER_SESSIONS")


class ShowChromedriverLogOption(SupportsCapabilities):
    SHOW_CHROMEDRIVER_LOG = 'showChromedriverLog'
    show_chromedriver_log = ContextOptionsDescriptor("SHOW_CHROMEDRIVER_LOG")


class WebviewDevtoolsPortOption(SupportsCapabilities):
    WEBVIEW_DEVTOOLS_PORT = 'webviewDevtoolsPort'
    webview_devtools_port = ContextOptionsDescriptor("WEBVIEW_DEVTOOLS_PORT")