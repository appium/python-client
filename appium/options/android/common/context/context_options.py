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

C = TypeVar('C', bound='SupportsCapabilities')


class ContextOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == 'AUTO_WEBVIEW_TIMEOUT':
            value = getattr(obj, "get_capability")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, 'get_capability')(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == 'AUTO_WEBVIEW_TIMEOUT':
            return getattr(obj, 'set_capability')(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        return getattr(obj, 'set_capability')(self.name, value)


class AutoWebviewTimeoutOption(SupportsCapabilities):
    AUTO_WEBVIEW_TIMEOUT = 'autoWebviewTimeout'
    auto_webview_timeout = ContextOptionsDescriptor('AUTO_WEBVIEW_TIMEOUT')
    """
    Set the maximum timeout to wait until a web view is
    available if autoWebview capability is set to true. 2000 ms by default.

    Usage
    -----
    - `self.auto_webview_timeout`
    - `self.auto_webview_timeout` = `value`
    """


class ChromeLoggingPrefsOption(SupportsCapabilities):
    CHROME_LOGGING_PREFS = 'chromeLoggingPrefs'
    chrome_logging_prefs = ContextOptionsDescriptor('CHROME_LOGGING_PREFS')
    """
    Chrome logging preferences mapping. Basically the same as
    [goog:loggingPrefs](https://newbedev.com/
    getting-console-log-output-from-chrome-with-selenium-python-api-bindings).
    It is set to {"browser": "ALL"} by default.

    Usage
    -----
    - `self.chrome_logging_prefs`
    - `self.chrome_logging_prefs` = `value`
    """


class ChromeOptionsOption(SupportsCapabilities):
    CHROME_OPTIONS = 'chromeOptions'
    chrome_options = ContextOptionsDescriptor('CHROME_OPTIONS')
    """
    A mapping, that allows to customize chromedriver options.
    See https://chromedriver.chromium.org/capabilities for the list
    of available entries.

    Usage
    -----
    - `self.chrome_options`
    - `self.chrome_options` = `value`
    """


class ChromedriverArgsOption(SupportsCapabilities):
    CHROMEDRIVER_ARGS = 'chromedriverArgs'
    chromedriver_args = ContextOptionsDescriptor('CHROMEDRIVER_ARGS')
    """
    Array of chromedriver [command line
    arguments](http://www.assertselenium.com/java/list-of-chrome-driver-command-line-arguments/).
    Note, that not all command line arguments that are available for the desktop
    browser are also available for the mobile one.

    Usage
    -----
    - `self.chromedriver_args`
    - `self.chromedriver_args` = `value`
    """


class ChromedriverChromeMappingFileOption(SupportsCapabilities):
    CHROMEDRIVER_CHROME_MAPPING_FILE = 'chromedriverChromeMappingFile'
    chromedriver_chrome_mapping_file = ContextOptionsDescriptor('CHROMEDRIVER_CHROME_MAPPING_FILE')
    """
    Full path to the chromedrivers mapping file. This file is used to statically
    map webview/browser versions to the chromedriver versions that are capable
    of automating them. Read [Automatic Chromedriver Discovery](https://github.com/
    appium/appium/blob/master/docs/en/writing-running-appium/web/
    chromedriver.md#automatic-discovery-of-compatible-chromedriver)
    article for more details.

    Usage
    - `self.chromedriver_chrome_mapping_file`
    - `self.chromedriver_chrome_mapping_file` = `value`
    """


class ChromedriverDisableBuildCheckOption(SupportsCapabilities):
    CHROMEDRIVER_DISABLE_BUILD_CHECK = 'chromedriverDisableBuildCheck'
    chromedriver_disable_build_check = ContextOptionsDescriptor('CHROMEDRIVER_DISABLE_BUILD_CHECK')
    """
    Being set to true disables the compatibility validation between the current
    chromedriver and the destination browser/web view. Use it with care.
    `False` by default.

    Usage
    -----
    - `self.chromedriver_disable_build_check`
    - `self.chromedriver_disable_build_check` = `value`
    """


class ChromedriverExecutableDirOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE_DIR = 'chromedriverExecutableDir'
    chromedriver_executable_dir = ContextOptionsDescriptor('CHROMEDRIVER_EXECUTABLE_DIR')
    """
    Full path to the folder where chromedriver executables are located.
    This folder is used then to store the downloaded chromedriver executables
    if automatic download is enabled. Read [Automatic Chromedriver
    Discovery](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/
    web/chromedriver.md#automatic-discovery-of-compatible-chromedriver)
    article for more details.

    Usage
    -----
    - `self.chromedriver_executable_dir`
    - `self.chromedriver_executable_dir` = `value`
    """


class ChromedriverExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE = 'chromedriverExecutable'
    chromedriver_executable = ContextOptionsDescriptor('CHROMEDRIVER_EXECUTABLE')
    """
    Gets and Sets Full path to the chromedriver executable on the server file system.

    Usage
    -----
    - `self.chromedriver_executable`
    - `self.chromedriver_executable` = `value`
    """


class ChromedriverPortOption(SupportsCapabilities):
    CHROMEDRIVER_PORT = 'chromedriverPort'
    chromedriver_port = ContextOptionsDescriptor('CHROMEDRIVER_PORT')
    """
    The port number to use for Chromedriver communication.
    Any free port number is selected by default if unset.

    Usage
    -----
    - `self.chromedriver_port`
    - `self.chromedriver_port` = `value`
    """


class ChromedriverPortsOption(SupportsCapabilities):
    CHROMEDRIVER_PORTS = 'chromedriverPorts'
    chromedriver_ports = ContextOptionsDescriptor('CHROMEDRIVER_PORTS')
    """
    Array of possible port numbers to assign for Chromedriver communication.
    If none of the port in this array is free then a server error is thrown.

    Usage
    -----
    - `self.chromedriver_ports`
    - `self.chromedriver_ports` = `value`
    """


class ChromedriverUseSystemExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_USE_SYSTEM_EXECUTABLE = 'chromedriverUseSystemExecutable'
    chromedriver_use_system_executable = ContextOptionsDescriptor('CHROMEDRIVER_USE_SYSTEM_EXECUTABLE')
    """
    Set it to true in order to enforce the usage of chromedriver, which gets
    downloaded by Appium automatically upon installation. This driver might not
    be compatible with the destination browser or a web view. false by default.

    Usage
    -----
    - `self.chromedriver_use_system_executable`
    - `self.chromedriver_use_system_executable` = `value`
    """

class EnsureWebviewsHavePagesOption(SupportsCapabilities):
    ENSURE_WEBVIEWS_HAVE_PAGES = 'ensureWebviewsHavePages'
    ensure_webviews_have_pages = ContextOptionsDescriptor('ENSURE_WEBVIEWS_HAVE_PAGES')
    """
    Whether to skip web views that have no pages from being shown in getContexts
    output. The driver uses devtools connection to retrieve the information about
    existing pages. true by default since Appium 1.19.0, false if lower than 1.19.0.

    Usage
    -----
    - `self.ensure_webviews_have_pages`
    - `self.ensure_webviews_have_pages` = `value`
    """


class ExtractChromeAndroidPackageFromContextNameOption(SupportsCapabilities):
    EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME = 'extractChromeAndroidPackageFromContextName'
    extract_chrome_android_package_from_context_name = ContextOptionsDescriptor('EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME')
    """
    If set to true, tell chromedriver to attach to the android package we have associated
    with the context name, rather than the package of the application under test.
    false by default.

    Usage
    -----
    - `self.extract_chrome_android_package_from_context_name`
    - `self.extract_chrome_android_package_from_context_name` = `value`
    """


class NativeWebScreenshotOption(SupportsCapabilities):
    NATIVE_WEB_SCREENSHOT = 'nativeWebScreenshot'
    native_web_screenshot = ContextOptionsDescriptor('NATIVE_WEB_SCREENSHOT')


class RecreateChromeDriverSessionsOption(SupportsCapabilities):
    RECREATE_CHROME_DRIVER_SESSIONS = 'recreateChromeDriverSessions'
    recreate_chrome_driver_sessions = ContextOptionsDescriptor('RECREATE_CHROME_DRIVER_SESSIONS')
    """
    If this capability is set to true then chromedriver session is always going
    to be killed and then recreated instead of just suspending it on context
    switching. false by default.

    Usage
    -----
    - `self.recreate_chrome_driver_sessions`
    - `self.recreate_chrome_driver_sessions` = `value`
    """


class ShowChromedriverLogOption(SupportsCapabilities):
    SHOW_CHROMEDRIVER_LOG = 'showChromedriverLog'
    show_chromedriver_log = ContextOptionsDescriptor('SHOW_CHROMEDRIVER_LOG')
    """
    If set to true then all the output from chromedriver binary will be
    forwarded to the Appium server log. false by default.

    Usage
    -----
    - `self.show_chromedriver_log`
    - `self.show_chromedriver_log` = `value`
    """


class WebviewDevtoolsPortOption(SupportsCapabilities):
    WEBVIEW_DEVTOOLS_PORT = 'webviewDevtoolsPort'
    webview_devtools_port = ContextOptionsDescriptor('WEBVIEW_DEVTOOLS_PORT')
    """
    The local port number to use for devtools communication. By default, the first
    free port from 10900..11000 range is selected. Consider setting the custom
    value if you are running parallel tests.

    Usage
    -----
    - `self.webview_devtools_port`
    - `self.webview_devtools_port` = `value`
    """