from appium.options.common.supports_capabilities import SupportsCapabilities


class SafariOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        getattr(obj, "set_capabilities")(self.name, value)


class AutomaticInspectionOption(SupportsCapabilities):
    AUTOMATIC_INSPECTION = 'safari:automaticInspection'
    automatic_inspection = SafariOptionsDescriptor("AUTOMATIC_INSPECTION")


class AutomaticProfilingOption(SupportsCapabilities):
    AUTOMATIC_PROFILING = 'safari:automaticProfiling'
    automatic_profiling = SafariOptionsDescriptor("AUTOMATIC_PROFILING")


class DeviceNameOption(SupportsCapabilities):
    DEVICE_NAME = 'safari:deviceName'
    device_name = SafariOptionsDescriptor("DEVICE_NAME")


class DeviceTypeOption(SupportsCapabilities):
    DEVICE_TYPE = 'safari:deviceType'
    device_type = SafariOptionsDescriptor("DEVICE_TYPE")


class DeviceUdidOption(SupportsCapabilities):
    DEVICE_UDID = 'safari:deviceUDID'
    device_udid = SafariOptionsDescriptor("DEVICE_UDID")

class PlatformBuildVersionOption(SupportsCapabilities):
    PLATFORM_BUILD_VERSION = 'safari:platformBuildVersion'
    platform_build_version = SafariOptionsDescriptor("PLATFORM_BUILD_VERSION")


class PlatformVersionOption(SupportsCapabilities):
    PLATFORM_VERSION = 'safari:platformVersion'
    platform_version = SafariOptionsDescriptor("PLATFORM_VERSION")


class UseSimulatorOption(SupportsCapabilities):
    USE_SIMULATOR = 'safari:useSimulator'
    use_simulator = SafariOptionsDescriptor("USE_SIMULATOR")

class WebkitWebrtcOption(SupportsCapabilities):
    WEBKIT_WEBRTC = 'webkit:WebRTC'
    webkit_webrtc = SafariOptionsDescriptor("WEBKIT_WEBRTC")