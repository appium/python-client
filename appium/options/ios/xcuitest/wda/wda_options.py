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

from appium.options.transformers import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities

class AllowProvisioningDeviceRegistrationOption(SupportsCapabilities):
    ALLOW_PROVISIONING_DEVICE_REGISTRATION = 'allowProvisioningDeviceRegistration'
    allow_provisioning_device_registration = OptionsDescriptor('ALLOW_PROVISIONING_DEVICE_REGISTRATION')
    """
    Allow xcodebuild to register your destination device on the developer portal
    if necessary. Requires a developer account to have been added in Xcode's Accounts
    preference pane. Defaults to false.

    Usage
    -----
    - Get
        - `self.allow_provisioning_device_registration`
    - Set
        - `self.allow_provisioning_device_registration` = `value`
    
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


class AutoAcceptAlertsOption(SupportsCapabilities):
    AUTO_ACCEPT_ALERTS = 'autoAcceptAlerts'
    auto_accept_alerts = OptionsDescriptor('AUTO_ACCEPT_ALERTS')
    """
    Accept all iOS alerts automatically if they pop up. This includes privacy
    access permission alerts (e.g., location, contacts, photos). Default is false.

    Usage
    -----
    - Get
        - `self.auto_accept_alerts`
    - Set
        - `self.auto_accept_alerts` = `value`
    
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


class AutoDismissAlertsOption(SupportsCapabilities):
    AUTO_DISMISS_ALERTS = 'autoDismissAlerts'
    auto_dismiss_alerts = OptionsDescriptor('AUTO_DISMISS_ALERTS')
    """
    Dismiss all iOS alerts automatically if they pop up. This includes privacy
    access permission alerts (e.g., location, contacts, photos). Default is false.

    Usage
    -----
    - Get
        - `self.auto_dismiss_alerts`
    - Set
        - `self.auto_dismiss_alerts` = `value`
    
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


class DerivedDataPathOption(SupportsCapabilities):
    DERIVED_DATA_PATH = 'derivedDataPath'
    derived_data_path = OptionsDescriptor('DERIVED_DATA_PATH')
    """
    Use along with usePrebuiltWDA capability and choose where to search for the existing WDA app.
    If the capability is not set then Xcode will store the derived data in the default root
    taken from preferences.It also makes sense to choose different folders for parallel WDA sessions.

    Usage
    -----
    - Get
        - `self.derived_data_path`
    - Set
        - `self.derived_data_path` = `value`
    
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


class DisableAutomaticScreenshotsOption(SupportsCapabilities):
    DISABLE_AUTOMATIC_SCREENSHOTS = 'disableAutomaticScreenshots'
    disable_automatic_screenshots = OptionsDescriptor('DISABLE_AUTOMATIC_SCREENSHOTS')
    """
    Disable automatic screenshots taken by XCTest at every interaction.
    Default is up to WebDriverAgent's config to decide, which currently
    defaults to true.

    Usage
    -----
    - Get
        - `self.disable_automatic_screenshots`
    - Set
        - `self.disable_automatic_screenshots` = `value`

    Parameters
    ----------
    `value` = `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class ForceAppLaunchOption(SupportsCapabilities):
    FORCE_APP_LAUNCH = 'forceAppLaunch'
    force_app_launch = OptionsDescriptor('FORCE_APP_LAUNCH')
    """
    Specify if the app should be forcefully restarted if it is already
    running on session startup. This capability only has an effect if an
    application identifier has been passed to the test session (either
    explicitly, by setting bundleId, or implicitly, by providing app).
    Default is true unless noReset capability is set to true.

    Usage
    -----
    - Get
        - `self.force_app_launch`
    - Set
        - `self.force_app_launch` = `value`
    
    Parameters
    ---------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class KeychainPasswordOption(SupportsCapabilities):
    KEYCHAIN_PASSWORD = 'keychainPassword'
    keychain_password = OptionsDescriptor('KEYCHAIN_PASSWORD')
    """
    Custom keychain password. The keychain is expected to
    contain the private development key.

    Usage
    -----
    - Get
        - `self.keychain_password`
    - Set
        - `self.keychain_password` = `value`
    
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

class KeychainPathOption(SupportsCapabilities):
    KEYCHAIN_PATH = 'keychainPath'
    keychain_path = OptionsDescriptor('KEYCHAIN_PATH')
    """
    Path to a custom keychain, which
    contains the private development key.

    Usage
    -----
    - Get
        - `self.keychain_path`
    - Set
        - `self.keychain_path` = `value`
    
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

class MaxTypingFrequencyOption(SupportsCapabilities):
    MAX_TYPING_FREQUENCY = 'maxTypingFrequency'
    max_typing_frequency = OptionsDescriptor('MAX_TYPING_FREQUENCY')
    """
    Maximum frequency of keystrokes for typing and clear. If your tests
    are failing because of typing errors, you may want to adjust this.
    Defaults to 60 keystrokes per minute.

    Usage
    -----
    - Get
        - `self.max_typing_frequency`
    - Set
        - `self.max_typing_frequency` = `value`
    
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


class MjpegServerPortOption(SupportsCapabilities):
    MJPEG_SERVER_PORT = 'mjpegServerPort'
    mjpeg_server_port = OptionsDescriptor('MJPEG_SERVER_PORT')
    """
     Port number on which WDA broadcasts screenshots stream encoded into MJPEG
    format from the device under test. It might be necessary to change this value
    if the default port is busy because of other tests running in parallel.
    Default value: 9100.

    Usage
    -----
    - Get
        - `self.mjpeg_server_port`
    - Set
        - `self.mjpeg_server_port` = `value`
    
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


class ProcessArgumentsOption(SupportsCapabilities):
    PROCESS_ARGUMENTS = 'processArguments'
    process_arguments = OptionsDescriptor('PROCESS_ARGUMENTS')
    """
    Provides process arguments and environment which will be sent
    to the WebDriverAgent server. Acceptable dictionary keys are 'env'
    and 'args'. The value of 'args' should be a list of app command line
    arguments represented as strings and the value of 'env' is expected to
    be a dictionary of environment variable names and their values (also strings).

    Usage
    -----
    - Get
        - `self.process_arguments`
    - Set
        - `self.process_arguments` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Union[List[str], Dict[str, str]]]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, Union[List[str], Dict[str, str]]]]`
    - Set
        - `None`
    """


class ResultBundlePathOption(SupportsCapabilities):
    RESULT_BUNDLE_PATH = 'resultBundlePath'
    result_bundle_path = OptionsDescriptor('RESULT_BUNDLE_PATH')
    """
    Specify the path to the result bundle path as xcodebuild argument for
    WebDriverAgent build under a security flag. WebDriverAgent process must
    start/stop every time to pick up changed value of this property.
    Specifying useNewWDA to true may help there. Please read 'man xcodebuild'
    for more details.

    Usage
    -----
    - Get
        - `self.result_bundle_path`
    - Set
        - `self.result_bundle_path` = `value`
    
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


class ScreenshotQualityOption(SupportsCapabilities):
    SCREENSHOT_QUALITY = 'screenshotQuality'
    screenshot_quality = OptionsDescriptor('SCREENSHOT_QUALITY')
    """
     Changes the quality of phone display screenshots following
    xctest/xctimagequality Default value is 1. 0 is the highest and
    2 is the lowest quality. You can also change it via settings
    command. 0 might cause OutOfMemory crash on high-resolution
    devices like iPad Pro.

    Usage
    -----
    - Get
        - `self.screenshot_quality`
    - Set
        - `self.screenshot_quality` = `value`
    
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


class ShouldTerminateAppOption(SupportsCapabilities):
    SHOULD_TERMINATE_APP = 'shouldTerminateApp'
    should_terminate_app = OptionsDescriptor('SHOULD_TERMINATE_APP')
    """
    Specify if the app should be terminated on session end.
    This capability only has an effect if an application identifier
    has been passed to the test session (either explicitly,
    by setting bundleId, or implicitly, by providing app).
    Default is true unless noReset capability is set to true.

    Usage
    -----
    - Get
        - `self.should_terminate_app`
    - Set
        - `self.should_terminate_app` = `value`
    
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

class ShouldUseSingletonTestManagerOption(SupportsCapabilities):
    SHOULD_USE_SINGLETON_TEST_MANAGER = 'shouldUseSingletonTestManager'
    should_use_singleton_test_manager = OptionsDescriptor('SHOULD_USE_SINGLETON_TEST_MANAGER')
    """
    Use default proxy for test management within WebDriverAgent. Setting this to false
    sometimes helps with socket hangup problems. Defaults to true.

    Usage
    -----
    - Get
        - `self.should_use_singleton_test_manager`
    - Set
        - `self.should_use_singleton_test_manager` = `value`
    
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


class ShowXcodeLogOption(SupportsCapabilities):
    SHOW_XCODE_LOG = 'showXcodeLog'
    show_xcode_log = OptionsDescriptor('SHOW_XCODE_LOG')
    """
     Whether to display the output of the Xcode command used to run the tests in
    server logs. If this is true, there will be lots of extra logging at startup.
    Defaults to false.

    Usage
    -----
    - Get
        - `self.show_xcode_log`
    - Set
        - `self.show_xcode_log` = `value`
    
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


class SimpleIsVisibleCheckOption(SupportsCapabilities):
    SIMPLE_IS_VISIBLE_CHECK = 'simpleIsVisibleCheck'
    simple_is_visible_check = OptionsDescriptor('SIMPLE_IS_VISIBLE_CHECK')
    """
    Use native methods for determining visibility of elements.
    In some cases this takes a long time. Setting this capability to false will
    cause the system to use the position and size of elements to make sure they
    are visible on the screen. This can, however, lead to false results in some
    situations. Defaults to false, except iOS 9.3, where it defaults to true.

    Usage
    -----
    - Get
        - `self.simple_is_visible_check`
    - Set
        - `self.simple_is_visible_check` = `value`
    
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

class UpdatedWdaBundleIdOption(SupportsCapabilities):
    UPDATED_WDA_BUNDLE_ID = 'updatedWDABundleId'
    updated_wda_bundle_id = OptionsDescriptor('UPDATED_WDA_BUNDLE_ID')
    """
    Bundle id to update WDA to before building and launching on real devices.
    This bundle id must be associated with a valid provisioning profile.

    Usage
    -----
    - Get
        - `self.updated_wda_bundle_id`
    - Set
        - `self.updated_wda_bundle_id` = `value`
    
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


class UseNativeCachingStrategyOption(SupportsCapabilities):
    USE_NATIVE_CACHING_STRATEGY = 'useNativeCachingStrategy'
    use_native_caching_strategy = OptionsDescriptor('USE_NATIVE_CACHING_STRATEGY')
    """
    Set this capability to false in order to use the custom elements caching
    strategy. This might help to avoid stale element exception on property
    change. By default, the native XCTest cache resolution is used (true)
    for all native locators (e.g. all, but xpath).

    Usage
    -----
    - Get
        - `self.use_native_caching_strategy`
    - Set
        - `self.use_native_caching_strategy` = `value`
    
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


class UseNewWdaOption(SupportsCapabilities):
    USE_NEW_WDA = 'useNewWDA'
    use_new_wda = OptionsDescriptor('USE_NEW_WDA')
    """
    If true, forces uninstall of any existing WebDriverAgent app on device.
    Set it to true if you want to apply different startup options for WebDriverAgent
    for each session. Although, it is only guaranteed to work stable on Simulator.
    Real devices require WebDriverAgent client to run for as long as possible without
    reinstall/restart to avoid issues like
    https://github.com/facebook/WebDriverAgent/issues/507. The false value
    (the default behaviour since driver version 2.35.0) will try to
    detect currently running WDA listener executed by previous testing session(s)
    and reuse it if possible, which is highly recommended for real device testing
    and to speed up suites of multiple tests in general. A new WDA session will be
    triggered at the default URL (http://localhost:8100) if WDA is not listening and
    webDriverAgentUrl capability is not set. The negative/unset value of useNewWDA
    capability has no effect prior to xcuitest driver version 2.35.0.

    Usage
    -----
    - Get
        - `self.use_new_wda`
    - Set
        - `self.use_new_wda` = `value`
    
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


class UsePrebuiltWdaOption(SupportsCapabilities):
    USE_PREBUILT_WDA = 'usePrebuiltWDA'
    use_prebuilt_wda = OptionsDescriptor('USE_PREBUILT_WDA')
    """
    Skips the build phase of running the WDA app. Building is then the responsibility
    of the user. Only works for Xcode 8+. Defaults to `False`.

    Usage
    -----
    - Get
        - `self.use_prebuilt_wda`
    - Set
        - `self.use_prebuilt_wda` = `value`
    
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


class UseSimpleBuildTestOption(SupportsCapabilities):
    USE_SIMPLE_BUILD_TEST = 'useSimpleBuildTest'
    use_simple_build_test = OptionsDescriptor('USE_SIMPLE_BUILD_TEST')
    """
    Build with 'build' and run test with 'test' in xcodebuild for all Xcode versions if
    this is true, or build with 'build-for-testing' and run tests with
    'test-without-building' for over Xcode 8 if this is false. Defaults to `False`.

    Usage
    -----
    - Get
        - `self.use_simple_build_test`
    - Set
        - `self.use_simple_build_test` = `value`
    
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


class UseXctestrunFileOption(SupportsCapabilities):
    USE_XCTESTRUN_FILE = 'useXctestrunFile'
    use_xctestrun_file = OptionsDescriptor('USE_XCTESTRUN_FILE')
    """
    Use Xctestrun file to launch WDA. It will search for such file in bootstrapPath.
    Expected name of file is WebDriverAgentRunner_iphoneos&lt;sdkVersion&gt;-arm64.xctestrun for
    real device and WebDriverAgentRunner_iphonesimulator&lt;sdkVersion&gt;-x86_64.xctestrun for
    simulator. One can do build-for-testing for WebDriverAgent project for simulator and
    real device and then you will see Product Folder like this and you need to copy content
    of this folder at bootstrapPath location. Since this capability expects that you have
    already built WDA project, it neither checks whether you have necessary dependencies to
    build WDA nor will it try to build project. Defaults to false. Tips: Xcodebuild builds for the
    target platform version. We'd recommend you to build with minimal OS version which you'd
    like to run as the original WDA module. e.g. If you build WDA for 12.2, the module cannot
    run on iOS 11.4 because of loading some module error on simulator. A module built with 11.4
    can work on iOS 12.2. (This is xcodebuild's expected behaviour.)

    Usage
    -----
    - Get
        - `self.use_xctestrun_file`
    - Set
        - `self.use_xctestrun_file` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Result
    ------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class WaitForIdleTimeoutOption(SupportsCapabilities):
    WAIT_FOR_IDLE_TIMEOUT = 'waitForIdleTimeout'

    def transform_get(self, value):
        return None if value is None else timedelta(seconds=value)

    def transform_set(self, value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    wait_for_idle_timeout = OptionsDescriptor('WAIT_FOR_IDLE_TIMEOUT', transform_get, transform_set)
    """
     The time to wait until the application under test is idling.
    XCTest requires the app's main thread to be idling in order to execute any action on it,
    so WDA might not even start/freeze if the app under test is constantly hogging the main
    thread. The default value is 10 (seconds). Setting it to zero disables idling checks completely
    (not recommended) and has the same effect as setting waitForQuiescence to false.
    Available since Appium 1.20.0.

    Usage
    -----
    - Get
        - `self.wait_for_idle_timeout`
    - Set
        - `self.wait_for_idle_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, float]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """

class WaitForQuiescenceOption(SupportsCapabilities):
    WAIT_FOR_QUIESCENCE = 'waitForQuiescence'
    wait_for_quiescence = OptionsDescriptor('WAIT_FOR_QUIESCENCE')
    """
    It allows to turn on/off waiting for application quiescence in WebDriverAgent,
    while performing queries. The default value is true. You can avoid this kind
    of issues if you turn it off. Consider using waitForIdleTimeout capability
    instead for this purpose since Appium 1.20.0.

    Usage
    -----
    - Get
        - `self.wait_for_quiescence`
    - Set
        - `self.wait_for_quiescence` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, float]`

    Results
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class WdaBaseUrlOption(SupportsCapabilities):
    WDA_BASE_URL = 'wdaBaseUrl'
    wda_base_url = OptionsDescriptor('WDA_BASE_URL')
    """
    This value, if specified, will be used as a prefix to build a custom
    WebDriverAgent url. It is different from webDriverAgentUrl, because
    if the latter is set then it expects WebDriverAgent to be already
    listening and skips the building phase. Defaults to http://localhost.

    Usage
    -----
    - Get
        - `self.wda_base_url`
    - Set
        - `self.wda_base_url` = `value`
    
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


class WdaConnectionTimeoutOption(SupportsCapabilities):
    WDA_CONNECTION_TIMEOUT = 'wdaConnectionTimeout'

    def transform_get(self, value):
        return None if value is None else timedelta(seconds=value)

    def transform_set(self, value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    wda_connection_timeout = OptionsDescriptor('WDA_CONNECTION_TIMEOUT', transform_get, transform_set)
    """
    Connection timeout to wait for a response from WebDriverAgent.
    Defaults to 240000ms.

    Usage
    -----
    - Get
        - `self.wda_connection_timeout`
    - Set
        - `self.wda_connection_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Results
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


class WdaEventloopIdleDelayOption(SupportsCapabilities):
    WDA_EVENTLOOP_IDLE_DELAY = 'wdaEventloopIdleDelay'
    
    def transform_get(self, value):
        return None if value is None else timedelta(seconds=value)

    def transform_set(self, value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    wda_eventloop_idle_delay = OptionsDescriptor('WDA_EVENTLOOP_IDLE_DELAY', transform_get, transform_set)
    """
    Delays the invocation of -[XCUIApplicationProcess setEventLoopHasIdled:] by the
    duration specified with this capability. This can help quiescence apps
    that fail to do so for no obvious reason (and creating a session fails for
    that reason). This increases the time for session creation
    because -[XCUIApplicationProcess setEventLoopHasIdled:] is called multiple times.
    If you enable this capability start with at least 3 seconds and try increasing it,
    if creating the session still fails. Defaults to 0.

    Usage
    -----
    - Get
        - `self.wda_eventloop_idle_delay`
    - Set
        - `self.wda_eventloop_idle_delay` = `value`
    
    Parameters
    ----------
    `value`: `Union[timedelta, float]`

    Results
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


class WdaLaunchTimeoutOption(SupportsCapabilities):
    WDA_LAUNCH_TIMEOUT = 'wdaLaunchTimeout'

    def transform_get(self, value):
        return None if value is None else timedelta(seconds=value)

    def transform_set(self, value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    wda_launch_timeout = OptionsDescriptor('WDA_LAUNCH_TIMEOUT', transform_get, transform_set)
    """
    Timeout to wait for WebDriverAgent to be pingable,
    after its building is finished. Defaults to 60000ms.

    Usage
    -----
    - Get
        - `self.wda_launch_timeout`
    - Set
        - `self.wda_launch_timeout` = `value`
    
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

class WdaLocalPortOption(SupportsCapabilities):
    WDA_LOCAL_PORT = 'wdaLocalPort'
    wda_local_port = OptionsDescriptor('WDA_LOCAL_PORT')
    """
    This value, if specified, will be used to forward traffic from
    Mac host to real ios devices over USB.
    Default value is the same as the port number used by WDA on
    the device under test (8100).

    Usage
    -----
    - Get
        - `self.wda_local_port`
    - Set
        - `self.wda_local_port` = `value`
    
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


class WdaStartupRetriesOption(SupportsCapabilities):
    WDA_STARTUP_RETRIES = 'wdaStartupRetries'
    wda_startup_retries = OptionsDescriptor('WDA_STARTUP_RETRIES')
    """
    Number of times to try to build and launch WebDriverAgent onto the device.
    Defaults to 2.

    Usage
    -----
    - Get
        - `self.wda_startup_retries`
    - Set
        - `self.wda_startup_retries` = `value`
    
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


class WdaStartupRetryIntervalOption(SupportsCapabilities):
    WDA_STARTUP_RETRY_INTERVAL = 'wdaStartupRetryInterval'

    def transform_get(self, value):
        return None if value is None else timedelta(seconds=value)

    def transform_set(self, value):
        return value.total_seconds() if isinstance(value, timedelta) else value

    wda_startup_retry_interval = OptionsDescriptor('WDA_STARTUP_RETRY_INTERVAL', transform_get, transform_set)
    """
    Time interval to wait between tries to build and launch WebDriverAgent.
    Defaults to 10000ms.

    Usage
    -----
    - Get
        - `self.wda_startup_retry_interval`
    - Set
        - `self.wda_startup_retry_interval` = `value`
    
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


class WebDriverAgentUrlOption(SupportsCapabilities):
    WEB_DRIVER_AGENT_URL = 'webDriverAgentUrl'
    web_driver_agent_url = OptionsDescriptor('WEB_DRIVER_AGENT_URL')
    """
    If provided, Appium will connect to an existing WebDriverAgent
    instance at this URL instead of starting a new one.

    Usage
    -----
    - Get
        - `self.web_driver_agent_url`
    - Set
        - `self.web_driver_agent_url` = `value`
    
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

class XcodeOrgIdOption(SupportsCapabilities):
    XCODE_ORG_ID = 'xcodeOrgId'
    xcode_org_id = OptionsDescriptor('XCODE_ORG_ID')
    """
    Provides a signing certificate organization id for WebDriverAgent compilation.
    If signing id is not provided then it defaults to "iPhone Developer"

    Usage
    -----
    - Get
        - `self.xcode_org_id`
    - Set
        - `self.xcode_org_id` = `value`
    
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


class XcodeSigningIdOption(SupportsCapabilities):
    XCODE_SIGNING_ID = 'xcodeSigningId'
    xcode_signing_id = OptionsDescriptor('XCODE_SIGNING_ID')
    """
    Provides a signing certificate for WebDriverAgent compilation.
    If signing id is not provided then it defaults to "iPhone Developer"

    Usage
    -----
    - Get
        - `self.xcode_signing_id`
    - Set
        - `self.xcode_signing_id` = `value`
    
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