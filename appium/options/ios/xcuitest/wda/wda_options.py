from typing import Optional
from datetime import timedelta

from appium.options.common.supports_capabilities import SupportsCapabilities


class WdaOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if self.name in ("WAIT_FOR_IDLE_TIMEOUT", "WDA_CONNECTION_TIMEOUT", 
                         "WDA_EVENTLOOP_IDLE_DELAY", "WDA_LAUNCH_TIMEOUT", "WDA_STARTUP_RETRY_INTERVAL"):
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(seconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        if self.name == ("WAIT_FOR_IDLE_TIMEOUT", "WDA_CONNECTION_TIMEOUT", 
                         "WDA_EVENTLOOP_IDLE_DELAY", "WDA_LAUNCH_TIMEOUT", "WDA_STARTUP_RETRY_INTERVAL"):
            getattr(obj, "set_capabilities")(self.name, value.total_seconds() if isinstance(value, timedelta) else value)  
        getattr(obj, "set_capabilities")(self.name, value)


class AllowProvisioningDeviceRegistrationOption(SupportsCapabilities):
    ALLOW_PROVISIONING_DEVICE_REGISTRATION = 'allowProvisioningDeviceRegistration'
    allow_provisioning_device_registration = WdaOptionsDescriptor("ALLOW_PROVISIONING_DEVICE_REGISTRATION")


class AutoAcceptAlertsOption(SupportsCapabilities):
    AUTO_ACCEPT_ALERTS = 'autoAcceptAlerts'
    auto_accept_alerts = WdaOptionsDescriptor("AUTO_ACCEPT_ALERTS")


class AutoDismissAlertsOption(SupportsCapabilities):
    AUTO_DISMISS_ALERTS = 'autoDismissAlerts'
    auto_dismiss_alerts = WdaOptionsDescriptor("AUTO_DISMISS_ALERTS")


class DerivedDataPathOption(SupportsCapabilities):
    DERIVED_DATA_PATH = 'derivedDataPath'
    derived_data_path = WdaOptionsDescriptor("DERIVED_DATA_PATH")


class DisableAutomaticScreenshotsOption(SupportsCapabilities):
    DISABLE_AUTOMATIC_SCREENSHOTS = 'disableAutomaticScreenshots'
    disable_automatic_screenshots = WdaOptionsDescriptor("DISABLE_AUTOMATIC_SCREENSHOTS")


class ForceAppLaunchOption(SupportsCapabilities):
    FORCE_APP_LAUNCH = 'forceAppLaunch'
    force_app_launch = WdaOptionsDescriptor("FORCE_APP_LAUNCH")


class KeychainPasswordOption(SupportsCapabilities):
    KEYCHAIN_PASSWORD = 'keychainPassword'
    keychain_password = WdaOptionsDescriptor("KEYCHAIN_PASSWORD")

class KeychainPathOption(SupportsCapabilities):
    KEYCHAIN_PATH = 'keychainPath'
    keychain_path = WdaOptionsDescriptor("KEYCHAIN_PATH")

class MaxTypingFrequencyOption(SupportsCapabilities):
    MAX_TYPING_FREQUENCY = 'maxTypingFrequency'
    max_typing_frequency = WdaOptionsDescriptor("MAX_TYPING_FREQUENCY")


class MjpegServerPortOption(SupportsCapabilities):
    MJPEG_SERVER_PORT = 'mjpegServerPort'
    mjpeg_server_port = WdaOptionsDescriptor("MJPEG_SERVER_PORT")


class ProcessArgumentsOption(SupportsCapabilities):
    PROCESS_ARGUMENTS = 'processArguments'
    process_arguments = WdaOptionsDescriptor("PROCESS_ARGUMENTS")


class ResultBundlePathOption(SupportsCapabilities):
    RESULT_BUNDLE_PATH = 'resultBundlePath'
    result_bundle_path = WdaOptionsDescriptor("RESULT_BUNDLE_PATH")


class ScreenshotQualityOption(SupportsCapabilities):
    SCREENSHOT_QUALITY = 'screenshotQuality'
    screenshot_quality = WdaOptionsDescriptor("SCREENSHOT_QUALITY")


class ShouldTerminateAppOption(SupportsCapabilities):
    SHOULD_TERMINATE_APP = 'shouldTerminateApp'
    should_terminate_app = WdaOptionsDescriptor("SHOULD_TERMINATE_APP")

class ShouldUseSingletonTestManagerOption(SupportsCapabilities):
    SHOULD_USE_SINGLETON_TEST_MANAGER = 'shouldUseSingletonTestManager'
    should_use_singleton_test_manager = WdaOptionsDescriptor("SHOULD_USE_SINGLETON_TEST_MANAGER")


class ShowXcodeLogOption(SupportsCapabilities):
    SHOW_XCODE_LOG = 'showXcodeLog'
    show_xcode_log = WdaOptionsDescriptor("SHOW_XCODE_LOG")


class SimpleIsVisibleCheckOption(SupportsCapabilities):
    SIMPLE_IS_VISIBLE_CHECK = 'simpleIsVisibleCheck'
    simple_is_visible_check = WdaOptionsDescriptor("SIMPLE_IS_VISIBLE_CHECK")

class UpdatedWdaBundleIdOption(SupportsCapabilities):
    UPDATED_WDA_BUNDLE_ID = 'updatedWDABundleId'
    updated_wda_bundle_id = WdaOptionsDescriptor("UPDATED_WDA_BUNDLE_ID")


class UseNativeCachingStrategyOption(SupportsCapabilities):
    USE_NATIVE_CACHING_STRATEGY = 'useNativeCachingStrategy'
    use_native_caching_strategy = WdaOptionsDescriptor("USE_NATIVE_CACHING_STRATEGY")


class UseNewWdaOption(SupportsCapabilities):
    USE_NEW_WDA = 'useNewWDA'
    use_new_wda = WdaOptionsDescriptor("USE_NEW_WDA")


class UsePrebuiltWdaOption(SupportsCapabilities):
    USE_PREBUILT_WDA = 'usePrebuiltWDA'
    use_prebuilt_wda = WdaOptionsDescriptor("USE_PREBUILT_WDA")


class UseSimpleBuildTestOption(SupportsCapabilities):
    USE_SIMPLE_BUILD_TEST = 'useSimpleBuildTest'
    use_simple_build_test = WdaOptionsDescriptor("USE_SIMPLE_BUILD_TEST")


class UseXctestrunFileOption(SupportsCapabilities):
    USE_XCTESTRUN_FILE = 'useXctestrunFile'
    use_xctestrun_file = WdaOptionsDescriptor("USE_XCTESTRUN_FILE")


class WaitForIdleTimeoutOption(SupportsCapabilities):
    WAIT_FOR_IDLE_TIMEOUT = 'waitForIdleTimeout'
    wait_for_idle_timeout = WdaOptionsDescriptor("WAIT_FOR_IDLE_TIMEOUT")

class WaitForQuiescenceOption(SupportsCapabilities):
    WAIT_FOR_QUIESCENCE = 'waitForQuiescence'
    wait_for_quiescence = WdaOptionsDescriptor("WAIT_FOR_QUIESCENCE")


class WdaBaseUrlOption(SupportsCapabilities):
    WDA_BASE_URL = 'wdaBaseUrl'
    wda_base_url = WdaOptionsDescriptor("WDA_BASE_URL")


class WdaConnectionTimeoutOption(SupportsCapabilities):
    WDA_CONNECTION_TIMEOUT = 'wdaConnectionTimeout'
    wda_connection_timeout = WdaOptionsDescriptor("WDA_CONNECTION_TIMEOUT")


class WdaEventloopIdleDelayOption(SupportsCapabilities):
    WDA_EVENTLOOP_IDLE_DELAY = 'wdaEventloopIdleDelay'
    wda_eventloop_idle_delay = WdaOptionsDescriptor("WDA_EVENTLOOP_IDLE_DELAY")


class WdaLaunchTimeoutOption(SupportsCapabilities):
    WDA_LAUNCH_TIMEOUT = 'wdaLaunchTimeout'
    wda_launch_timeout = WdaOptionsDescriptor("WDA_LAUNCH_TIMEOUT")

class WdaLocalPortOption(SupportsCapabilities):
    WDA_LOCAL_PORT = 'wdaLocalPort'
    wda_local_port = WdaOptionsDescriptor("WDA_LOCAL_PORT")


class WdaStartupRetriesOption(SupportsCapabilities):
    WDA_STARTUP_RETRIES = 'wdaStartupRetries'
    wda_startup_retries = WdaOptionsDescriptor("WDA_STARTUP_RETRIES")


class WdaStartupRetryIntervalOption(SupportsCapabilities):
    WDA_STARTUP_RETRY_INTERVAL = 'wdaStartupRetryInterval'
    wda_startup_retry_interval = WdaOptionsDescriptor("WDA_STARTUP_RETRY_INTERVAL")


class WebDriverAgentUrlOption(SupportsCapabilities):
    WEB_DRIVER_AGENT_URL = 'webDriverAgentUrl'
    web_driver_agent_url = WdaOptionsDescriptor("WEB_DRIVER_AGENT_URL")

class XcodeOrgIdOption(SupportsCapabilities):
    XCODE_ORG_ID = 'xcodeOrgId'
    xcode_org_id = WdaOptionsDescriptor("XCODE_ORG_ID")


class XcodeSigningIdOption(SupportsCapabilities):
    XCODE_SIGNING_ID = 'xcodeSigningId'
    xcode_signing_id = WdaOptionsDescriptor("XCODE_SIGNING_ID")