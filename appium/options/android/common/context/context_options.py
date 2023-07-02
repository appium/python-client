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

from typing import Any, Dict, Optional, List, Union
from datetime import timedelta

from appium.options.common.supports_capabilities import SupportsCapabilities

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.transformers import transform_duration_get, transform_duration_set


class AutoWebviewTimeoutOption(SupportsCapabilities):
    AUTO_WEBVIEW_TIMEOUT = 'autoWebviewTimeout'
    auto_webview_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (AUTO_WEBVIEW_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Set the maximum timeout to wait until a web view is
    available if autoWebview capability is set to true. 2000 ms by default.

    Usage
    -----
    - Get
        - `self.auto_webview_timeout`
    - Set
        - `self.auto_webview_timeout` = `value`
    
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


class ChromeLoggingPrefsOption(SupportsCapabilities):
    CHROME_LOGGING_PREFS = 'chromeLoggingPrefs'
    chrome_logging_prefs = OptionsDescriptor[Optional[Dict[str, Any]], Dict[str, Any]](CHROME_LOGGING_PREFS)
    """
    Chrome logging preferences mapping. Basically the same as
    [goog:loggingPrefs](https://newbedev.com/
    getting-console-log-output-from-chrome-with-selenium-python-api-bindings).
    It is set to {"browser": "ALL"} by default.

    Usage
    -----
    - Get
        - `self.chrome_logging_prefs`
    - Set
        - `self.chrome_logging_prefs` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Any]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, Any]`
    - Set
        - `None`
    """


class ChromeOptionsOption(SupportsCapabilities):
    CHROME_OPTIONS = 'chromeOptions'
    chrome_options = OptionsDescriptor[Optional[Dict[str, Any]], Dict[str, Any]](CHROME_OPTIONS)
    """
    A mapping, that allows to customize chromedriver options.
    See https://chromedriver.chromium.org/capabilities for the list
    of available entries.

    Usage
    -----
    - Get
        - `self.chrome_options`
    - Set
        - `self.chrome_options` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Any]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, Any]]`
    - Set
        - `None`
    """


class ChromedriverArgsOption(SupportsCapabilities):
    CHROMEDRIVER_ARGS = 'chromedriverArgs'
    chromedriver_args = OptionsDescriptor[Optional[List[str]], List[str]](CHROMEDRIVER_ARGS)
    """
    Array of chromedriver [command line
    arguments](http://www.assertselenium.com/java/list-of-chrome-driver-command-line-arguments/).
    Note, that not all command line arguments that are available for the desktop
    browser are also available for the mobile one.

    Usage
    -----
    - Get
        - `self.chromedriver_args`
    - Set
        - `self.chromedriver_args` = `value`
    
    Parameters
    ----------
    `value`: `List[str]`

    Returns
    -------
    - Get
        - `Optional[List[str]]`
    - Set
        - `None`
    """


class ChromedriverChromeMappingFileOption(SupportsCapabilities):
    CHROMEDRIVER_CHROME_MAPPING_FILE = 'chromedriverChromeMappingFile'
    chromedriver_chrome_mapping_file = OptionsDescriptor[Optional[str], str](CHROMEDRIVER_CHROME_MAPPING_FILE)
    """
    Full path to the chromedrivers mapping file. This file is used to statically
    map webview/browser versions to the chromedriver versions that are capable
    of automating them. Read [Automatic Chromedriver Discovery](https://github.com/
    appium/appium/blob/master/docs/en/writing-running-appium/web/
    chromedriver.md#automatic-discovery-of-compatible-chromedriver)
    article for more details.

    Usage
    -----
    - Get
        - `self.chromedriver_chrome_mapping_file`
    - Set
        - `self.chromedriver_chrome_mapping_file` = `value`
    
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


class ChromedriverDisableBuildCheckOption(SupportsCapabilities):
    CHROMEDRIVER_DISABLE_BUILD_CHECK = 'chromedriverDisableBuildCheck'
    chromedriver_disable_build_check = OptionsDescriptor[Optional[bool], bool](CHROMEDRIVER_DISABLE_BUILD_CHECK)
    """
    Being set to true disables the compatibility validation between the current
    chromedriver and the destination browser/web view. Use it with care.
    `False` by default.

    Usage
    -----
    - Get
        - `self.chromedriver_disable_build_check`
    - Set
        - `self.chromedriver_disable_build_check` = `value`
    
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


class ChromedriverExecutableDirOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE_DIR = 'chromedriverExecutableDir'
    chromedriver_executable_dir = OptionsDescriptor[Optional[str], str](CHROMEDRIVER_EXECUTABLE_DIR)
    """
    Full path to the folder where chromedriver executables are located.
    This folder is used then to store the downloaded chromedriver executables
    if automatic download is enabled. Read [Automatic Chromedriver
    Discovery](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/
    web/chromedriver.md#automatic-discovery-of-compatible-chromedriver)
    article for more details.

    Usage
    -----
    - Get
        - `self.chromedriver_executable_dir`
    - Set
        - `self.chromedriver_executable_dir` = `value`
    
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


class ChromedriverExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_EXECUTABLE = 'chromedriverExecutable'
    chromedriver_executable = OptionsDescriptor[Optional[str], str](CHROMEDRIVER_EXECUTABLE)
    """
    Gets and Sets Full path to the chromedriver executable on the server file system.

    Usage
    -----
    - Get
        - `self.chromedriver_executable`
    - Set
        - `self.chromedriver_executable` = `value`
    
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


class ChromedriverPortOption(SupportsCapabilities):
    CHROMEDRIVER_PORT = 'chromedriverPort'
    chromedriver_port = OptionsDescriptor[Optional[int], int](CHROMEDRIVER_PORT)
    """
    The port number to use for Chromedriver communication.
    Any free port number is selected by default if unset.

    Usage
    -----
    - Get
        - `self.chromedriver_port`
    - Set
        - `self.chromedriver_port` = `value`
    
    Parameters
    ----------
    `value`: `int`

    Returns
    -------
    - Get
        - `Optional[int]`
    - Set
        - `None`
    """


class ChromedriverPortsOption(SupportsCapabilities):
    CHROMEDRIVER_PORTS = 'chromedriverPorts'
    chromedriver_ports = OptionsDescriptor[Optional[List[int]], List[int]](CHROMEDRIVER_PORTS)
    """
    Array of possible port numbers to assign for Chromedriver communication.
    If none of the port in this array is free then a server error is thrown.

    Usage
    -----
    - Get
        - `self.chromedriver_ports`
    - Set
        - `self.chromedriver_ports` = `value`
    
    Parameters
    ----------
    `value`: `List[int]`

    Returns
    -------
    - Get
        - `Optional[List[int]]`
    - Set
        - `None`
    """


class ChromedriverUseSystemExecutableOption(SupportsCapabilities):
    CHROMEDRIVER_USE_SYSTEM_EXECUTABLE = 'chromedriverUseSystemExecutable'
    chromedriver_use_system_executable = OptionsDescriptor[Optional[bool], bool](CHROMEDRIVER_USE_SYSTEM_EXECUTABLE)
    """
    Set it to true in order to enforce the usage of chromedriver, which gets
    downloaded by Appium automatically upon installation. This driver might not
    be compatible with the destination browser or a web view. false by default.

    Usage
    -----
    - Get
        - `self.chromedriver_use_system_executable`
    - Set
        - `self.chromedriver_use_system_executable` = `value`
    
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

class EnsureWebviewsHavePagesOption(SupportsCapabilities):
    ENSURE_WEBVIEWS_HAVE_PAGES = 'ensureWebviewsHavePages'
    ensure_webviews_have_pages = OptionsDescriptor[Optional[bool], bool](ENSURE_WEBVIEWS_HAVE_PAGES)
    """
    Whether to skip web views that have no pages from being shown in getContexts
    output. The driver uses devtools connection to retrieve the information about
    existing pages. true by default since Appium 1.19.0, false if lower than 1.19.0.

    Usage
    -----
    - Get
        - `self.ensure_webviews_have_pages`
    - Set
        - `self.ensure_webviews_have_pages` = `value`
    
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


class ExtractChromeAndroidPackageFromContextNameOption(SupportsCapabilities):
    EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME = 'extractChromeAndroidPackageFromContextName'
    extract_chrome_android_package_from_context_name = OptionsDescriptor[Optional[bool], bool]
    (EXTRACT_CHROME_ANDROID_PACKAGE_FROM_CONTEXT_NAME)
    """
    If set to true, tell chromedriver to attach to the android package we have associated
    with the context name, rather than the package of the application under test.
    false by default.

    Usage
    -----
    - Get
        - `self.extract_chrome_android_package_from_context_name`
    - Set
        - `self.extract_chrome_android_package_from_context_name` = `value`
    
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


class NativeWebScreenshotOption(SupportsCapabilities):
    NATIVE_WEB_SCREENSHOT = 'nativeWebScreenshot'
    native_web_screenshot = OptionsDescriptor[Optional[bool], bool](NATIVE_WEB_SCREENSHOT)
    """
    Gets and Sets Whether to use screenshoting endpoint provided by UiAutomator framework (true)
    rather than the one provided by chromedriver (false, the default value).
    Use it when you experience issues with the latter.

    Usage
    -----
    - Get
        - `self.native_web_screenshot`
    - Set
        - `self.native_web_screenshot` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        -  `None`
    """


class RecreateChromeDriverSessionsOption(SupportsCapabilities):
    RECREATE_CHROME_DRIVER_SESSIONS = 'recreateChromeDriverSessions'
    recreate_chrome_driver_sessions = OptionsDescriptor[Optional[bool], bool](RECREATE_CHROME_DRIVER_SESSIONS)
    """
    If this capability is set to true then chromedriver session is always going
    to be killed and then recreated instead of just suspending it on context
    switching. false by default.

    Usage
    -----
    - Get
        - `self.recreate_chrome_driver_sessions`
    - Set
        - `self.recreate_chrome_driver_sessions` = `value`
    
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


class ShowChromedriverLogOption(SupportsCapabilities):
    SHOW_CHROMEDRIVER_LOG = 'showChromedriverLog'
    show_chromedriver_log = OptionsDescriptor[Optional[bool], bool](SHOW_CHROMEDRIVER_LOG)
    """
    If set to true then all the output from chromedriver binary will be
    forwarded to the Appium server log. false by default.

    Usage
    -----
    - Get
        - `self.show_chromedriver_log`
    - Set
        - `self.show_chromedriver_log` = `value`
    
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


class WebviewDevtoolsPortOption(SupportsCapabilities):
    WEBVIEW_DEVTOOLS_PORT = 'webviewDevtoolsPort'
    webview_devtools_port = OptionsDescriptor[Optional[int], int](WEBVIEW_DEVTOOLS_PORT)
    """
    The local port number to use for devtools communication. By default, the first
    free port from 10900..11000 range is selected. Consider setting the custom
    value if you are running parallel tests.

    Usage
    -----
    - Get
        - `self.webview_devtools_port`
    - Set
        - `self.webview_devtools_port` = `value`
    
    Parameters
    ----------
    `value`: `int`

    Returns
    -------
    - Get
        - `Optional[int]`
    - Set
        - `None`
    """
