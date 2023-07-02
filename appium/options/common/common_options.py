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

from appium.options.base_options_descriptor import OptionsDescriptor
from .supports_capabilities import SupportsCapabilities


class AppOption(SupportsCapabilities):
    APP = 'app'
    app = OptionsDescriptor(APP)
    """
    Gets and Sets String representing app location
    Set the absolute local path for the location of the App.
    The app must be located on the same machine where Appium
    server is running.
    Could also be a valid URL.

    Usage
    -----
    - Get
        - `self.app`
    - Set
        - `self.app` = `value`
    
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


class AutoWebViewOption(SupportsCapabilities):
    AUTO_WEB_VIEW = 'autoWebView'
    auto_web_view = OptionsDescriptor(AUTO_WEB_VIEW)
    """
    Gets and Sets Whether the driver should try to automatically switch
    to a web view context after the session is started.

    Usage
    -----
    - Get
        - `self.auto_web_view`
    - Set
        - `self.auto_web_view` = `value`
    
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


class AutomationNameOption(SupportsCapabilities):
    AUTOMATION_NAME = 'automationName'
    automation_name = OptionsDescriptor(AUTOMATION_NAME)
    """
    Gets and Sets the automation driver name to use for the given platform.

    Usage
    -----
    - Get
        - `self.automation_name`
    - Set
        - `self.automation_name` = `value`
    
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


class BundleIdOption(SupportsCapabilities):
    BUNDLE_ID = 'bundleId'
    bundle_id = OptionsDescriptor(BUNDLE_ID)
    """
    Gets and Sets the bundle identifier of the application to automate.

    Usage
    -----
    - Get
        - `self.bundle_id`
    - Set
        - `self.bundle_id` = `value`
    
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


class ClearSystemFilesOption(SupportsCapabilities):
    CLEAR_SYSTEM_FILES = 'clearSystemFiles'
    clear_system_files = OptionsDescriptor(CLEAR_SYSTEM_FILES)
    """
    Set whether the driver should delete generated files at the end of a session.

    Usage
    -----
    - Get
        - `self.clear_system_files`
    - Set
        - `self.clear_system_files` = `value`
    
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


class DeviceNameOption(SupportsCapabilities):
    DEVICE_NAME = 'deviceName'
    device_name = OptionsDescriptor(DEVICE_NAME)
    """
    Gets and Sets the name of the device to be used in the test.

    Usage
    -----
    - Get
        - `self.device_name` 
    - Set
        - `self.device_name` = `value`
    
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


class EnablePerformanceLoggingOption(SupportsCapabilities):
    ENABLE_PERFORMANCE_LOGGING = 'enablePerformanceLogging'
    enable_performance_logging = OptionsDescriptor(ENABLE_PERFORMANCE_LOGGING)
    """
    Gets and Sets whether to enable additional performance logging.

    Usage
    -----
    - Get
        - `self.enable_performace_logging`
    - Set
        - `self.enable_performace_logging` = `value`
    
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


class EventTimingsOption(SupportsCapabilities):
    EVENT_TIMINGS = 'eventTimings'
    event_timings = OptionsDescriptor(EVENT_TIMINGS)
    """
    Get and Sets Whether the driver should to report the timings
    for various Appium-internal events.

    Usage
    -----
    - Get
        - `self.event_timings`
    - Set
        - `self.event_timings` = `value`
    
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


class FullResetOption(SupportsCapabilities):
    FULL_RESET = 'fullReset'
    full_reset = OptionsDescriptor(FULL_RESET)
    """
    Get and Sets Whether the driver should perform a full reset.

    Usage
    -----
    - Get
        - `self.full_reset`
    - Set
        - `self.full_reset` = `value`
    
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


class IsHeadlessOption(SupportsCapabilities):
    IS_HEADLESS = 'isHeadless'
    is_headless = OptionsDescriptor(IS_HEADLESS)
    """
    Gets and Sets Whether the driver should start emulator/simulator in headless mode.
    It is only applied if the emulator is not running before the test starts.

    Usage
    -----
    - Get
        - `self.is_headless`
    - Set
        - `self.is_headless` = `value`
    
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


class LanguageOption(SupportsCapabilities):
    LANGUAGE = 'language'
    language = OptionsDescriptor(LANGUAGE)
    """
    Gets and Sets Language abbreviation to use in a test session

    Usage
    -----
    - Get
        - `self.language`
    - Set
        - `self.language` = `value`
    
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


class LocaleOption(SupportsCapabilities):
    LOCALE = 'locale'
    locale = OptionsDescriptor(LOCALE)
    """
    Gets and Sets Locale abbreviation to use in a test session.

    Usage
    -----
    - Get
        - `self.locale`
    - Set
        - `self.locale` = `value`
    
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


class NewCommandTimeoutOption(SupportsCapabilities):
    NEW_COMMAND_TIMEOUT = 'newCommandTimeout'

    @staticmethod
    def transform_command_timeout_get(value):
        return None if value is None else timedelta(seconds=value)
    
    @staticmethod
    def transfrom_command_timeout_set(value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    new_command_timeout = OptionsDescriptor(
        NEW_COMMAND_TIMEOUT, 
        transform_command_timeout_get, 
        transfrom_command_timeout_set
    )
    """
    Gets and Sets the allowed time before seeing a new server command.
    The value could either be provided as timedelta instance or an integer number of seconds.

    Usage
    -----
    - Get
        - `self.new_command_timeout`
    - Set
        - `self.new_command_timeout` = `value`
    
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


class NoResetOption(SupportsCapabilities):
    NO_RESET = 'noReset'
    no_reset = OptionsDescriptor(NO_RESET)
    """
    Gets and Sets Whether the driver should not perform a reset.

    Usage
    -----
    - Get
        - `self.no_reset`
    - Set
        - `self.no_reset` = `value`
    
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


class OrientationOption(SupportsCapabilities):
    ORIENTATION = 'orientation'
    orientation = OptionsDescriptor(ORIENTATION)
    """
    Gets and Sets the orientation of the device's screen.
    Usually this is either 'PORTRAIT' or 'LANDSCAPE'.

    Usage
    -----
    - Get
        - `self.orientation`
    - Set
        - `self.orientation` = `value`
    
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


class OtherAppsOption(SupportsCapabilities):
    OTHER_APPS = 'otherApps'
    other_apps = OptionsDescriptor(OTHER_APPS)
    """
    Gets and Sets Locations of apps to install before running a test.
    Each item could be separated with a single comma.

    Usage
    ----
    - Get
        - `self.other_apps`
    - Set
        - `self.other_apps` = `value`
    
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


class PostrunOption(SupportsCapabilities):
    POSTRUN = 'postrun'
    postrun = OptionsDescriptor(POSTRUN)
    """
    Gets and Sets system script which is supposed to be executed upon
    driver session quit.

    Usage
    -----
    - Get
        - `self.postrun`
    - Set
        - `self.postrun` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, str]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, str]`
    - Set
        - `None`
    """


class PrerunOption(SupportsCapabilities):
    PRERUN = 'prerun'
    prerun = OptionsDescriptor(PRERUN)
    """
    Gets and Sets System script which is supposed to be executed before
    a driver session is initialised.

    Usage
    -----
    - Get
        - `self.prerun`
    - Set
        - `self.prerun` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, str]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, str]`
    - Set
        - `None`
    """


class PrintPageSourceOnFindFailureOption(SupportsCapabilities):
    PRINT_PAGE_SOURCE_ON_FIND_FAILURE = 'printPageSourceOnFindFailure'
    print_page_source_on_find_failure = OptionsDescriptor(PRINT_PAGE_SOURCE_ON_FIND_FAILURE)
    """
    Gets and Sets Whether the driver should print the page source to the log
    if a find failure occurs.

    Usage
    -----
    - Get
        - `self.print_page_source_on_find_failure`
    - Set
        - `self.print_page_source_on_find_failure` = `value`
    
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


class SkipLogCaptureOption(SupportsCapabilities):
    """
    Gets and Sets Whether the driver should not record device logs.

    Usage
    -----
    - Get
        - `self.skip_log_capture`
    - Set
        - `self.skip_log_capture` = `value`
    
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
    SKIP_LOG_CAPTURE = 'skipLogCapture'
    skip_log_capture = OptionsDescriptor(SKIP_LOG_CAPTURE)


class SystemHostOption(SupportsCapabilities):
    SYSTEM_HOST = 'systemHost'
    system_host = OptionsDescriptor(SYSTEM_HOST)
    """
    Gets and Sets the name of the host for the internal server to listen on.

    Usage
    -----
    - Get
        - `self.system_host`
    - Set
        - `self.system_host` = `value`
    
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


class SystemPortOption(SupportsCapabilities):
    SYSTEM_PORT = 'systemPort'
    system_port = OptionsDescriptor(SYSTEM_PORT)
    """
    Gets and Sets the number of the port for the internal server to listen on.

    Usage
    -----
    - Get
        - `self.system_post`
    - Set
        - `self.system_post` = `value`
    
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


class UdidOption(SupportsCapabilities):
    UDID = 'udid'
    udid = OptionsDescriptor(UDID)
    """
    Gets and Sets the unique identifier of the device under test.
    
    Usage
    -----
    - Get
        - `self.udid`
    - Set
        - `self.udid` = `value`
    
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