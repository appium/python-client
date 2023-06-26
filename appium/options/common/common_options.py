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

from typing import Any, TypeVar, Generic

from .supports_capabilities import SupportsCapabilities

T = TypeVar('T')
C = TypeVar('C', bound='SupportsCapabilities')


class OptionsDescriptor(Generic[T]):
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        return obj.get_capability(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        return obj.set_capability(self.name, value)


class AppOption(SupportsCapabilities):
    APP = 'app'
    app = OptionsDescriptor('APP')
    """
    Gets and Sets String representing app location
    Set the absolute local path for the location of the App.
    The app must be located on the same machine where Appium
    server is running.
    Could also be a valid URL.

    Usage
    -----
    - `self.app`
    - `self.app` = `value`
    """


class AutoWebViewOption(SupportsCapabilities):
    AUTO_WEB_VIEW = 'autoWebView'
    auto_web_view = OptionsDescriptor('AUTO_WEB_VIEW')
    """
    Gets and Sets Whether the driver should try to automatically switch
    to a web view context after the session is started.

    Usage
    -----
    - `self.auto_web_view`
    - `self.auto_web_view` = `value`
    """


class AutomationNameOption(SupportsCapabilities):
    AUTOMATION_NAME = 'automationName'
    automation_name = OptionsDescriptor('AUTOMATION_NAME')
    """
    Gets and Sets the automation driver name to use for the given platform.

    Usage
    -----
    - `self.automation_name`
    - `self.automation_name` = `value`
     """


class BundleIdOption(SupportsCapabilities):
    BUNDLE_ID = 'bundleId'
    bundle_id = OptionsDescriptor('BUNDLE_ID')
    """
    Gets and Sets the bundle identifier of the application to automate.

    Usage
    -----
    - `self.bundle_id`
    - `self.bundle_id` = `value`
    """


class ClearSystemFilesOption(SupportsCapabilities):
    CLEAR_SYSTEM_FILES = 'clearSystemFiles'
    clear_system_files = OptionsDescriptor('CLEAR_SYSTEM_FILES')
    """
    Set whether the driver should delete generated files at the end of a session.

    Usage
    -----
    - `self.clear_system_files`
    - `self.clear_system_files` = `value`
    """


class DeviceNameOption(SupportsCapabilities):
    DEVICE_NAME = 'deviceName'
    device_name = OptionsDescriptor('DEVICE_NAME')
    """
    Gets and Sets the name of the device to be used in the test.

    Usage
    -----
    - `self.device_name` 
    - `self.device_name` = `value`
    """


class EnablePerformanceLoggingOption(SupportsCapabilities):
    ENABLE_PERFORMANCE_LOGGING = 'enablePerformanceLogging'
    enable_performance_logging = OptionsDescriptor('ENABLE_PERFORMANCE_LOGGING')
    """
    Gets and Sets whether to enable additional performance logging.

    Usage
    ----
    - `self.enable_performace_logging`
    - `self.enable_performace_logging` = `value`
    """


class EventTimingsOption(SupportsCapabilities):
    EVENT_TIMINGS = 'eventTimings'
    event_timings = OptionsDescriptor('EVENT_TIMINGS')
    """
    Get and Sets Whether the driver should to report the timings
    for various Appium-internal events.

    Usage
    -----
    - `self.event_timings`
    - `self.event_timings` = `value`
    """


class FullResetOption(SupportsCapabilities):
    FULL_RESET = 'fullReset'
    full_reset = OptionsDescriptor('FULL_RESET')
    """
    Get and Sets Whether the driver should perform a full reset.

    Usage
    -----
    - `self.full_reset`
    - `self.full_reset` = `value`
    """


class IsHeadlessOption(SupportsCapabilities):
    IS_HEADLESS = 'isHeadless'
    is_headless = OptionsDescriptor('IS_HEADLESS')
    """
    Gets and Sets Whether the driver should start emulator/simulator in headless mode.
    It is only applied if the emulator is not running before the test starts.

    Usage
    ----
    - `self.is_headless`
    - `self.is_headless` = `value`
    """


class LanguageOption(SupportsCapabilities):
    LANGUAGE = 'language'
    language = OptionsDescriptor('LANGUAGE')
    """
    Gets and Sets Language abbreviation to use in a test session

    Usage
    -----
    - `self.language`
    - `self.language` = `value`
    """


class LocaleOption(SupportsCapabilities):
    LOCALE = 'locale'
    locale = OptionsDescriptor('LOCALE')
    """
    Gets and Sets Locale abbreviation to use in a test session.

    Usage
    -----
    - `self.locale`
    - `self.locale` = `value`
    """


class NewCommandTimeoutOption(SupportsCapabilities):
    NEW_COMMAND_TIMEOUT = 'newCommandTimeout'
    new_command_timeout = OptionsDescriptor('NEW_COMMAND_TIMEOUT')
    """
    Gets and Sets the allowed time before seeing a new server command.
    The value could either be provided as timedelta instance or an integer number of seconds.

    Usage
    ----
    - `self.new_command_timeout`
    - `self.new_command_timeout` = `value`
    """


class NoResetOption(SupportsCapabilities):
    NO_RESET = 'noReset'
    no_reset = OptionsDescriptor('NO_RESET')
    """
    Gets and Sets Whether the driver should not perform a reset.

    Usage
    ----
    - `self.no_reset`
    - `self.no_reset` = `value`
    """


class OrientationOption(SupportsCapabilities):
    ORIENTATION = 'orientation'
    orientation = OptionsDescriptor('ORIENTATION')
    """
    Gets and Sets the orientation of the device's screen.
    Usually this is either 'PORTRAIT' or 'LANDSCAPE'.

    Usage
    -----
    - `self.orientation`
    - `self.orientation` = `value`
    """


class OtherAppsOption(SupportsCapabilities):
    OTHER_APPS = 'otherApps'
    other_apps = OptionsDescriptor('OTHER_APPS')
    """
    Gets and Sets Locations of apps to install before running a test.
    Each item could be separated with a single comma.

    Usage
    ----
    - `self.other_apps`
    - `self.other_apps` = `value`
    """


class PostrunOption(SupportsCapabilities):
    POSTRUN = 'postrun'
    postrun = OptionsDescriptor('POSTRUN')
    """
    Gets and Sets system script which is supposed to be executed upon
    driver session quit.

    Usage
    -----
    - `self.postrun`
    - `self.postrun` = `value`
    """


class PrerunOption(SupportsCapabilities):
    PRERUN = 'prerun'
    prerun = OptionsDescriptor('PRERUN')
    """
    Gets and Sets System script which is supposed to be executed before
    a driver session is initialised.

    Usage
    -----
    - `self.prerun`
    - `slef.prerun` = `value`
    """


class PrintPageSourceOnFindFailureOption(SupportsCapabilities):
    PRINT_PAGE_SOURCE_ON_FIND_FAILURE = 'printPageSourceOnFindFailure'
    print_page_source_on_find_failure = OptionsDescriptor('PRINT_PAGE_SOURCE_ON_FIND_FAILURE')
    """
    Gets and Sets Whether the driver should print the page source to the log
    if a find failure occurs.

    Usage
    ----
    - `self.print_page_source_on_find_failure`
    - `self.print_page_source_on_find_failure` = `value`
    """


class SkipLogCaptureOption(SupportsCapabilities):
    """
    Gets and Sets Whether the driver should not record device logs.

    Usage
    ----
    - `self.skip_log_capture`
    - `self.skip_log_capture` = `value`
    """
    SKIP_LOG_CAPTURE = 'skipLogCapture'
    skip_log_capture = OptionsDescriptor('SKIP_LOG_CAPTURE')


class SystemHostOption(SupportsCapabilities):
    SYSTEM_HOST = 'systemHost'
    system_host = OptionsDescriptor("SYSTEM_HOST")
    """
    Gets and Sets the name of the host for the internal server to listen on.

    Usage
    ----
    - `self.system_host`
    - `self.system_host` = `value`
    """


class SystemPortOption(SupportsCapabilities):
    SYSTEM_PORT = 'systemPort'
    system_port = OptionsDescriptor('SYSTEM_PORT')
    """
    Gets and Sets the number of the port for the internal server to listen on.

    Usage
    ----
    - `self.system_post`
    - `self.system_post` = `value`
    """


class UdidOption(SupportsCapabilities):
    UDID = 'udid'
    udid = OptionsDescriptor('UDID')
    """
    Gets and Sets the unique identifier of the device under test.
    
    Usage
    -----
    - `self.udid`
    - `self.udid` = `value`
    """
