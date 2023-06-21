from .supports_capabilities import SupportsCapabilities

class OptionsDescriptor:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, obj, cls):
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        getattr(obj, "set_capabilities")(self.name, value)


class AppOption(SupportsCapabilities):
    """
    Set the absolute local path for the location of the App.
    The app must be located on the same machine where Appium
    server is running.
    Could also be a valid URL.
    """
    APP = 'app'
    # Create a descriptor object (Indirectly we are creating a getter and setter here)
    app = OptionsDescriptor("APP")


class AutoWebViewOption(SupportsCapabilities):
        """
        Set whether the driver should try to automatically switch
        a web view context after the session is started.
        """
        AUTO_WEB_VIEW = 'autoWebView'
        auto_web_view = OptionsDescriptor("AUTO_WEB_VIEW")


class AutomationNameOption(SupportsCapabilities):
       """Gets and Sets the automation driver name to use for the given platform."""
       AUTOMATION_NAME = 'automationName'
       automation_name = OptionsDescriptor("AUTOMATION_NAME")


class BundleIdOption(SupportsCapabilities):
       """Gets and Sets the bundle identifier of the application to automate."""
       BUNDLE_ID = 'bundleId'
       bundle_id = OptionsDescriptor("BUNDLE_ID")

class ClearSystemFilesOption(SupportsCapabilities):
       """ Set whether the driver should delete generated files at the end of a session."""
       CLEAR_SYSTEM_FILES = 'clearSystemFiles'
       clear_system_files = OptionsDescriptor("CLEAR_SYSTEM_FILES")


class DeviceNameOption(SupportsCapabilities):
    """Gets and Sets the name of the device to be used in the test."""
    DEVICE_NAME = 'deviceName'
    device_name = OptionsDescriptor("DEVICE_NAME")


class EnablePerformanceLoggingOption(SupportsCapabilities):
    """Gets and Sets whether to enable additional performance logging."""
    ENABLE_PERFORMANCE_LOGGING = 'enablePerformanceLogging'
    enable_performance_logging = OptionsDescriptor("ENABLE_PERFORMANCE_LOGGING")

class EventTimingsOption(SupportsCapabilities):
    """
    Get Whether the driver should to report the timings
    for various Appium-internal events.

    Set whether the driver should to report the timings
    for various Appium-internal events.
        """
    EVENT_TIMINGS = 'eventTimings'
    event_timings = OptionsDescriptor("EVENT_TIMINGS")

class FullResetOption(SupportsCapabilities):
    """
    Get Whether the driver should perform a full reset.
    Set whether the driver should perform a full reset.
    """
    FULL_RESET = 'fullReset'
    full_reset = OptionsDescriptor("FULL_RESET")

class IsHeadlessOption(SupportsCapabilities):
    """
    Whether the driver should start emulator/simulator in headless mode.
    Set emulator/simulator to start in headless mode (e.g. no UI is shown).
    It is only applied if the emulator is not running before the test starts.
    """
    IS_HEADLESS = 'isHeadless'
    is_headless = OptionsDescriptor("IS_HEADLESS")

class LanguageOption(SupportsCapabilities):
    """
    Gets Language abbreviation to use in a test session
    Set language abbreviation to use in a test session.
    """
    LANGUAGE = 'language'
    language = OptionsDescriptor("LANGUAGE")

class LocaleOption(SupportsCapabilities):
    """
    Gets Locale abbreviation to use in a test session.
    Set locale abbreviation to use in a test session.
    """
    LOCALE = 'locale'
    locale = OptionsDescriptor("LOCALE")

class NewCommandTimeoutOption(SupportsCapabilities):
    """
    The allowed time before seeing a new server command.
    Set the allowed time before seeing a new server command.
    The value could either be provided as timedelta instance or an integer number of seconds.
    """
    NEW_COMMAND_TIMEOUT = 'newCommandTimeout'
    new_command_timeout = OptionsDescriptor("NEW_COMMAND_TIMEOUT")


class NoResetOption(SupportsCapabilities):
    """
    Whether the driver should not perform a reset.
    Set whether the driver should not perform a reset.
    """
    NO_RESET = 'noReset'
    no_reset = OptionsDescriptor("NO_RESET")


class OrientationOption(SupportsCapabilities):
    """
    Gets The orientation of the device's screen.
    Usually this is either 'PORTRAIT' or 'LANDSCAPE'.
       
    Set the orientation of the device's screen.
    Usually this is either 'PORTRAIT' or 'LANDSCAPE'.
    """
    ORIENTATION = 'orientation'
    orientation = OptionsDescriptor("ORIENTATION")


class OtherAppsOption(SupportsCapabilities):
    """
    Gets Locations of apps to install before running a test.
    Sets locations of apps to install before running a test.
    Each item could be separated with a single comma.
    """
    OTHER_APPS = 'otherApps'
    other_apps = OptionsDescriptor("OTHER_APPS")


class PostrunOption(SupportsCapabilities):
    """
    Gets System script which is supposed to be executed upon
    driver session quit.
    Sets a system script to execute upon driver session quit.
    """
    POSTRUN = 'postrun'
    postrun = OptionsDescriptor("POSTRUN")


class PrerunOption(SupportsCapabilities):
    """
    Gets System script which is supposed to be executed before
    a driver session is initialised.

    Sets a system script which is supposed to be executed before
    a driver session is initialised.
    """
    PRERUN = 'prerun'
    prerun = OptionsDescriptor("PRERUN")


class PrintPageSourceOnFindFailureOption(SupportsCapabilities):
    """
    Gets Whether the driver should print the page source to the log
    if a find failure occurs.

    Sets whether the driver should print the page source to the log
    if a find failure occurs.
    """
    PRINT_PAGE_SOURCE_ON_FIND_FAILURE = 'printPageSourceOnFindFailure'
    print_page_source_on_find_failure = OptionsDescriptor("PRINT_PAGE_SOURCE_ON_FIND_FAILURE")


class SkipLogCaptureOption(SupportsCapabilities):
    """
    Whether the driver should not record device logs.
    Set whether the driver should not record device logs.
    """
    SKIP_LOG_CAPTURE = 'skipLogCapture'
    skip_log_capture = OptionsDescriptor("SKIP_LOG_CAPTURE")

class SystemHostOption(SupportsCapabilities):
    """
    Gets The name of the host for the internal server to listen on.
    Sets the name of the host for the internal server to listen on.
    """
    SYSTEM_HOST = 'systemHost'
    system_host = OptionsDescriptor("SYSTEM_HOST")

class SystemPortOption(SupportsCapabilities):
    """
    Gets The number of the port for the internal server to listen on.
    Sets the number of the port for the internal server to listen on.
    """
    SYSTEM_PORT = 'systemPort'
    system_port = OptionsDescriptor("SYSTEM_PORT")

class UdidOption(SupportsCapabilities):
    """
    The unique identifier of the device under test.
    Set the unique identifier of the device under test.
    """
    UDID = 'udid'
    udid = OptionsDescriptor("UDID")
