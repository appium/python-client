from datetime import timedelta
import json
from typing import Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities


class SimulatorOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if self.name == "PERMISSIONS":
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else json.loads(value)
        if self.name == "SIMULATOR_STARTUP_TIMEOUT":
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        if self.name == "PERMISSIONS":
            getattr(obj, "set_capabilities")(self.name, json.dumps(value, ensure_ascii=False))
        if self.name == "SIMULATOR_STARTUP_TIMEOUT":
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)      
        getattr(obj, "set_capabilities")(self.name, value)


class CalendarAccessAuthorizedOption(SupportsCapabilities):
    CALENDAR_ACCESS_AUTHORIZED = 'calendarAccessAuthorized'
    calendar_access_authorized = SimulatorOptionsDescriptor("CALENDAR_ACCESS_AUTHORIZED")


class CalendarFormatOption(SupportsCapabilities):
    CALENDAR_FORMAT = 'calendarFormat'
    calendar_format = SimulatorOptionsDescriptor("CALENDAR_FORMAT")


class ConnectHardwareKeyboardOption(SupportsCapabilities):
    CONNECT_HARDWARE_KEYBOARD = 'connectHardwareKeyboard'
    connect_hardware_keyboard = SimulatorOptionsDescriptor("CONNECT_HARDWARE_KEYBOARD")


class CustomSslCertOption(SupportsCapabilities):
    CUSTOM_SSL_CERT = 'customSSLCert'
    custom_ssl_cert = SimulatorOptionsDescriptor("CUSTOM_SSL_CERT")


class EnforceFreshSimulatorCreationOption(SupportsCapabilities):
    ENFORCE_FRESH_SIMULATOR_CREATION = 'enforceFreshSimulatorCreation'
    enforce_fresh_simulator_creation = SimulatorOptionsDescriptor("ENFORCE_FRESH_SIMULATOR_CREATION")


class ForceSimulatorSoftwareKeyboardPresenceOption(SupportsCapabilities):
    FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE = 'forceSimulatorSoftwareKeyboardPresence'
    force_simulator_software_keyboard_presence = SimulatorOptionsDescriptor("FORCE_SIMULATOR_SOFTWARE_KEYBOARD_PRESENCE")


class IosSimulatorLogsPredicateOption(SupportsCapabilities):
    IOS_SIMULATOR_LOGS_PREDICATE = 'iosSimulatorLogsPredicate'
    ios_simulator_logs_predicate = SimulatorOptionsDescriptor("IOS_SIMULATOR_LOGS_PREDICATE")


class KeepKeyChainsOption(SupportsCapabilities):
    KEEP_KEY_CHAINS = 'keepKeyChains'
    keep_key_chains = SimulatorOptionsDescriptor("KEEP_KEY_CHAINS")


class KeychainsExcludePatternsOption(SupportsCapabilities):
    KEYCHAINS_EXCLUDE_PATTERNS = 'keychainsExcludePatterns'
    keychains_exclude_patterns = SimulatorOptionsDescriptor("KEYCHAINS_EXCLUDE_PATTERNS")


class PermissionsOption(SupportsCapabilities):
    PERMISSIONS = 'permissions'
    permissions = SimulatorOptionsDescriptor("PERMISSIONS")


class ReduceMotionOption(SupportsCapabilities):
    REDUCE_MOTION = 'reduceMotion'
    reduce_motion = SimulatorOptionsDescriptor("REDUCE_MOTION")


class ResetOnSessionStartOnlyOption(SupportsCapabilities):
    RESET_ON_SESSION_START_ONLY = 'resetOnSessionStartOnly'
    reset_on_session_start_only = SimulatorOptionsDescriptor("RESET_ON_SESSION_START_ONLY")


class ScaleFactorOption(SupportsCapabilities):
    SCALE_FACTOR = 'scaleFactor'
    scale_factor = SimulatorOptionsDescriptor("SCALE_FACTOR")


class ShutdownOtherSimulatorsOption(SupportsCapabilities):
    SHUTDOWN_OTHER_SIMULATORS = 'shutdownOtherSimulators'
    shutdown_other_simulators = SimulatorOptionsDescriptor("SHUTDOWN_OTHER_SIMULATORS")


class SimulatorDevicesSetPathOption(SupportsCapabilities):
    SIMULATOR_DEVICES_SET_PATH = 'simulatorDevicesSetPath'
    simulator_devices_set_path = SimulatorOptionsDescriptor("SIMULATOR_DEVICES_SET_PATH")


class SimulatorPasteboardAutomaticSyncOption(SupportsCapabilities):
    SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC = 'simulatorPasteboardAutomaticSync'
    simulator_pasteboard_automatic_sync = SimulatorOptionsDescriptor("SIMULATOR_PASTEBOARD_AUTOMATIC_SYNC")


class SimulatorStartupTimeoutOption(SupportsCapabilities):
    SIMULATOR_STARTUP_TIMEOUT = 'simulatorStartupTimeout'
    simulator_startup_timeout = SimulatorOptionsDescriptor("SIMULATOR_STARTUP_TIMEOUT")


class SimulatorTracePointerOption(SupportsCapabilities):
    SIMULATOR_TRACE_POINTER = 'simulatorTracePointer'
    simulator_trace_pointer = SimulatorOptionsDescriptor("SIMULATOR_TRACE_POINTER")

class SimulatorWindowCenterOption(SupportsCapabilities):
    SIMULATOR_WINDOW_CENTER = 'simulatorWindowCenter'
    simulator_window_center = SimulatorOptionsDescriptor("SIMULATOR_WINDOW_CENTER")