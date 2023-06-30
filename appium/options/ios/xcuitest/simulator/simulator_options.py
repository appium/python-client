from datetime import timedelta
import json
from typing import Any, TypeVar, Generic

from appium.options.common.supports_capabilities import SupportsCapabilities

T = TypeVar('T')
C = TypeVar('C', bound='SupportsCapabilities')


class SimulatorOptionsDescriptor(Generic[T]):
    def __init__(self, name):
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == 'PERMISSIONS':
            value = getattr(obj, 'get_capability')(self.name)
            return None if value is None else json.loads(value)
        if self.name == 'SIMULATOR_STARTUP_TIMEOUT':
            value = getattr(obj, 'get_capability')(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, 'get_capability')(self.name)

    def __set__(self, obj: C, value: Any) -> None:
        if self.name == 'PERMISSIONS':
            getattr(obj, 'set_capability')(self.name, json.dumps(value, ensure_ascii=False))
        if self.name == 'SIMULATOR_STARTUP_TIMEOUT':
            getattr(obj, 'set_capability')(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)      
        getattr(obj, 'set_capability')(self.name, value)


class CalendarAccessAuthorizedOption(SupportsCapabilities):
    CALENDAR_ACCESS_AUTHORIZED = 'calendarAccessAuthorized'
    calendar_access_authorized = SimulatorOptionsDescriptor('CALENDAR_ACCESS_AUTHORIZED')
    """
    Set this to true if you want to enable calendar access on IOS Simulator
    with given bundleId. Set to false, if you want to disable calendar access
    on IOS Simulator with given bundleId. If not set, the calendar
    authorization status will not be set.

    Usage
    -----
    - Get
        - `self.calendar_access_authorized`
    - Set
        - `self.calendar_access_authorized` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Ser
        - `None`
    """


class CalendarFormatOption(SupportsCapabilities):
    CALENDAR_FORMAT = 'calendarFormat'
    calendar_format = SimulatorOptionsDescriptor('CALENDAR_FORMAT')
    """
    Gets and Sets calendar format for the iOS Simulator.

    Usage
    -----
    - Get
        - `self.calendar_format`
    - Set
        - `self.calendar_format` = `value`
    
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


class ConnectHardwareKeyboardOption(SupportsCapabilities):
    CONNECT_HARDWARE_KEYBOARD = 'connectHardwareKeyboard'
    connect_hardware_keyboard = SimulatorOptionsDescriptor('CONNECT_HARDWARE_KEYBOARD')
    """
    Set this option to true in order to enable hardware keyboard in Simulator.
    The preference works only when Appium launches a simulator instance with
    this value. It is set to false by default, because this helps to workaround
    some XCTest bugs. connectHardwareKeyboard: true makes
    forceSimulatorSoftwareKeyboardPresence: false if no explicit value is set
    for forceSimulatorSoftwareKeyboardPresence capability since Appium 1.22.0.

    Usage
    -----
    - Get
        - `self.connect_hardware_keyboard`
    - Set
        - `self.connect_hardware_keyboard` = `value`
    
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


class CustomSslCertOption(SupportsCapabilities):
    CUSTOM_SSL_CERT = 'customSSLCert'
    custom_ssl_cert = SimulatorOptionsDescriptor('CUSTOM_SSL_CERT')
    """
    Adds a root SSL certificate to IOS Simulator.
    The certificate content must be provided in PEM format.

    Usage
    -----
    - Get
        - `self.custom_ssl_cert`
    - Set
        - `self.custom_ssl_cert` = `value`
    
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


class EnforceFreshSimulatorCreationOption(SupportsCapabilities):
    ENFORCE_FRESH_SIMULATOR_CREATION = 'enforceFreshSimulatorCreation'
    enforce_fresh_simulator_creation = SimulatorOptionsDescriptor('ENFORCE_FRESH_SIMULATOR_CREATION')
    """
    Creates a new simulator in session creation and deletes it in session deletion.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.enforce_fresh_simulator_creation`
    - Set
        - `self.enforce_fresh_simulator_creation` = `value`
    
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


class ForceSimulatorSoftwareKeyboardPresenceOption(SupportsCapabilities):
    FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE = 'forceSimulatorSoftwareKeyboardPresence'
    force_simulator_software_keyboard_presence = SimulatorOptionsDescriptor('FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE')
    """
    Set this option to true in order to turn software keyboard on and turn
    hardware keyboard off in Simulator since Appium 1.22.0. This option helps
    to avoid Keyboard is not present error. It is set to true by default.
    Appium respects preset simulator software/hardware keyboard preference
    when this value is false, so connectHardwareKeyboard: false and
    forceSimulatorSoftwareKeyboardPresence: false means for Appium to keep
    the current Simulator keyboard preferences. This option has priority
    over connectHardwareKeyboard.

    Usage
    -----
    - Get
        - `self.force_simulator_software_keyboard_presence`
    - Set
        - `self.force_simulator_software_keyboard_presence` = `value`
    
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


class IosSimulatorLogsPredicateOption(SupportsCapabilities):
    IOS_SIMULATOR_LOGS_PREDICATE = 'iosSimulatorLogsPredicate'
    ios_simulator_logs_predicate = SimulatorOptionsDescriptor('IOS_SIMULATOR_LOGS_PREDICATE')
    """
    Gets and Sets the --predicate flag in the ios simulator logs.

    Usage
    -----
    - Get
        - `self.ios_simulator_logs_predicate`
    - Set
        - `self.ios_simulator_logs_predicate` = `value`
    
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


class KeepKeyChainsOption(SupportsCapabilities):
    KEEP_KEY_CHAINS = 'keepKeyChains'
    keep_key_chains = SimulatorOptionsDescriptor('KEEP_KEY_CHAINS')
    """
    Gets and Sets the capability to true in order to preserve Simulator keychains folder after
    full reset. This feature has no effect on real devices. Defaults to false.

    Usage
    -----
    - Get
        - `self.keep_key_chains`
    - Set
        - `self.keep_key_chains` = `value`
    
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


class KeychainsExcludePatternsOption(SupportsCapabilities):
    KEYCHAINS_EXCLUDE_PATTERNS = 'keychainsExcludePatterns'
    keychains_exclude_patterns = SimulatorOptionsDescriptor('KEYCHAINS_EXCLUDE_PATTERNS')
    """
    This capability accepts comma-separated path patterns,
    which are going to be excluded from keychains restore while
    full reset is being performed on Simulator. It might be
    useful if you want to exclude only particular keychain types
    from being restored, like the applications keychain. This
    feature has no effect on real devices. E.g. "*keychain*.db*"
    to exclude applications keychain from being restored

    Usage
    -----
    - Get
        - `self.keychains_exclude_patterns`
    - Set
        - `self.keychains_exclude_patterns` = `value`
    
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


class PermissionsOption(SupportsCapabilities):
    PERMISSIONS = 'permissions'
    permissions = SimulatorOptionsDescriptor('PERMISSIONS')
    """
    Since Xcode SDK 11.4 Apple provides native APIs to interact with
    application settings. Check the output of `xcrun simctl privacy booted`
    command to get the list of available permission names. Use yes, no
    and unset as values in order to grant, revoke or reset the corresponding
    permission. Below Xcode SDK 11.4 it is required that applesimutils package
    is installed and available in PATH. The list of available service names
    and statuses can be found at https://github.com/wix/AppleSimulatorUtils.
    For example: {"com.apple.mobilecal": {"calendar": "YES"}}

    Usage
    -----
    - Get
        - `self.permissions`
    - Set
        - `self.permissions` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Dict[str, str]]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, Dict[str, str]]]`
    - Set
        - `None`
    """


class ReduceMotionOption(SupportsCapabilities):
    REDUCE_MOTION = 'reduceMotion'
    reduce_motion = SimulatorOptionsDescriptor('REDUCE_MOTION')
    """
    Allows to turn on/off reduce motion accessibility preference.
    Setting reduceMotion on helps to reduce flakiness during tests.
    Only on simulators.

    Usage
    -----
    - Get
        - `self.reduce_motion`
    - Set
        - `self.reduce_motion` = `value`
    
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


class ResetOnSessionStartOnlyOption(SupportsCapabilities):
    RESET_ON_SESSION_START_ONLY = 'resetOnSessionStartOnly'
    reset_on_session_start_only = SimulatorOptionsDescriptor('RESET_ON_SESSION_START_ONLY')
    """
     Whether to perform reset on test session finish (false) or not (true).
    Keeping this variable set to true and Simulator running (the default
    behaviour since version 1.6.4) may significantly shorten the duration of
    test session initialization.

    Usage
    -----
    - Get
        - `self.reset_on_session_start_only`
    - Set
        - `self.reset_on_session_start_only` = `value`
    
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


class ScaleFactorOption(SupportsCapabilities):
    SCALE_FACTOR = 'scaleFactor'
    scale_factor = SimulatorOptionsDescriptor('SCALE_FACTOR')
    """
    Simulator scale factor. This is useful to have if the default resolution
    of simulated device is greater than the actual display resolution.
    So you can scale the simulator to see the whole device screen without scrolling.
    Acceptable values for simulators running Xcode SDK 8 and older are: '1.0',
    '0.75', '0.5', '0.33' and '0.25', where '1.0' means 100% scale.
    For simulators running Xcode SDK 9 and above the value could be any valid
    positive float number.

    Usage
    -----
    - Get
        - `self.scale_factor`
    - Set
        - `self.scale_factor` = `value`
    
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


class ShutdownOtherSimulatorsOption(SupportsCapabilities):
    SHUTDOWN_OTHER_SIMULATORS = 'shutdownOtherSimulators'
    shutdown_other_simulators = SimulatorOptionsDescriptor('SHUTDOWN_OTHER_SIMULATORS')
    """
    If this capability set to true and the current device under test is an iOS
    Simulator then Appium will try to shut down all the other running Simulators
    before to start a new session. This might be useful while executing webview
    tests on different devices, since only one device can be debugged remotely
    at once due to an Apple bug. The capability only has an effect if
    --relaxed-security command line argument is provided to the server.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.shutdown_other_simulators`
    - Set
        - `self.shutdown_other_simulators` = `value`
    
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


class SimulatorDevicesSetPathOption(SupportsCapabilities):
    SIMULATOR_DEVICES_SET_PATH = 'simulatorDevicesSetPath'
    simulator_devices_set_path = SimulatorOptionsDescriptor('SIMULATOR_DEVICES_SET_PATH')
    """
    This capability allows to set an alternative path to the simulator devices
    set in case you have multiple sets deployed on your local system. Such
    feature could be useful if you, for example, would like to save disk space
    on the main system volume.

    Usage
    -----
    - Get
        - `self.simulator_devices_set_path`
    - Set
        - `self.simulator_devices_set_path` = `value`
    
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


class SimulatorPasteboardAutomaticSyncOption(SupportsCapabilities):
    SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC = 'simulatorPasteboardAutomaticSync'
    simulator_pasteboard_automatic_sync = SimulatorOptionsDescriptor('SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC')
    """
    Handle the -PasteboardAutomaticSync flag when simulator process launches.
    It could improve launching simulator performance not to sync pasteboard with
    the system when this value is off. on forces the flag enabled. system does
    not provide the flag to the launching command. on, off, or system is available.
    They are case-insensitive. Defaults to off.

    Usage
    -----
    - Get
        - `self.simulator_pasteboard_automatic_sync`
    - Set
        - `self.simulator_pasteboard_automatic_sync` = `value`
    
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


class SimulatorStartupTimeoutOption(SupportsCapabilities):
    SIMULATOR_STARTUP_TIMEOUT = 'simulatorStartupTimeout'
    simulator_startup_timeout = SimulatorOptionsDescriptor('SIMULATOR_STARTUP_TIMEOUT')
    """
     Allows to change the default timeout for Simulator startup.
    By default, this value is set to 120000ms (2 minutes),
    although the startup could take longer on a weak hardware
    or if other concurrent processes use much system resources
    during the boot up procedure.

    Usage
    -----
    - Get
        - `self.simulator_startup_timeout`
    - Set
        - `self.simulator_startup_timeout` = `value`
    
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


class SimulatorTracePointerOption(SupportsCapabilities):
    SIMULATOR_TRACE_POINTER = 'simulatorTracePointer'
    simulator_trace_pointer = SimulatorOptionsDescriptor('SIMULATOR_TRACE_POINTER')
    """
     Set whether to highlight pointer moves in the Simulator window.
    The Simulator UI client must be shut down before the session
    startup in order for this capability to be applied properly.
    false by default.

    Usage
    -----
    - Get
        - `self.simulator_trace_pointer`
    - Set
        - `self.simulator_trace_pointer` = `value`
    
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

class SimulatorWindowCenterOption(SupportsCapabilities):
    SIMULATOR_WINDOW_CENTER = 'simulatorWindowCenter'
    simulator_window_center = SimulatorOptionsDescriptor('SIMULATOR_WINDOW_CENTER')
    """
    Allows to explicitly set the coordinates of Simulator window center
    for Xcode9+ SDK. This capability only has an effect if Simulator
    window has not been opened yet for the current session before it started.
    e.g. "{-100.0,100.0}" or "{500,500}", spaces are not allowed

    Usage
    -----
    - Get
        - `self.simulator_window_center`
    - Set
        - `self.simulator_window_center` = `value`
    
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