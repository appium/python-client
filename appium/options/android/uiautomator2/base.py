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

from typing import Dict

from appium.options.android.common.adb.adb_exec_timeout_option import AdbExecTimeoutOption
from appium.options.android.common.adb.adb_port_option import AdbPortOption
from appium.options.android.common.adb.allow_delay_adb_option import AllowDelayAdbOption
from appium.options.android.common.adb.build_tools_version_option import BuildToolsVersionOption
from appium.options.android.common.adb.clear_device_logs_on_start_option import ClearDeviceLogsOnStartOption
from appium.options.android.common.adb.ignore_hidden_api_policy_error_option import IgnoreHiddenApiPolicyErrorOption
from appium.options.android.common.adb.logcat_filter_specs_option import LogcatFilterSpecsOption
from appium.options.android.common.adb.logcat_format_option import LogcatFormatOption
from appium.options.android.common.adb.mock_location_app_option import MockLocationAppOption
from appium.options.android.common.adb.remote_adb_host_option import RemoteAdbHostOption
from appium.options.android.common.adb.skip_logcat_capture_option import SkipLogcatCaptureOption
from appium.options.android.common.adb.suppress_kill_server_option import SuppressKillServerOption
from appium.options.android.common.app.allow_test_packages_option import AllowTestPackagesOption
from appium.options.android.common.app.android_install_timeout_option import AndroidInstallTimeoutOption
from appium.options.android.common.app.app_activity_option import AppActivityOption
from appium.options.android.common.app.app_package_option import AppPackageOption
from appium.options.android.common.app.app_wait_activity_option import AppWaitActivityOption
from appium.options.android.common.app.app_wait_duration_option import AppWaitDurationOption
from appium.options.android.common.app.app_wait_for_launch_option import AppWaitForLaunchOption
from appium.options.android.common.app.app_wait_package_option import AppWaitPackageOption
from appium.options.android.common.app.auto_grant_premissions_option import AutoGrantPermissionsOption
from appium.options.android.common.app.enforce_app_install_option import EnforceAppInstallOption
from appium.options.android.common.app.intent_action_option import IntentActionOption
from appium.options.android.common.app.intent_category_option import IntentCategoryOption
from appium.options.android.common.app.intent_flags_option import IntentFlagsOption
from appium.options.android.common.app.optional_intent_arguments_option import OptionalIntentArgumentsOption
from appium.options.android.common.app.remote_apps_cache_limit_option import RemoteAppsCacheLimitOption
from appium.options.android.common.app.uninstall_other_packages_option import UninstallOtherPackagesOption
from appium.options.android.common.avd.avd_args_option import AvdArgsOption
from appium.options.android.common.avd.avd_env_option import AvdEnvOption
from appium.options.android.common.avd.avd_launch_timeout_option import AvdLaunchTimeoutOption
from appium.options.android.common.avd.avd_option import AvdOption
from appium.options.android.common.avd.avd_ready_timeout_option import AvdReadyTimeoutOption
from appium.options.android.common.avd.gps_enabled_option import GpsEnabledOption
from appium.options.android.common.avd.network_speed_option import NetworkSpeedOption
from appium.options.android.common.context.auto_webview_timeout_option import AutoWebviewTimeoutOption
from appium.options.android.common.context.chrome_logging_prefs_option import ChromeLoggingPrefsOption
from appium.options.android.common.context.chrome_options_option import ChromeOptionsOption
from appium.options.android.common.context.chromedriver_args_option import ChromedriverArgsOption
from appium.options.android.common.context.chromedriver_chrome_mapping_file_option import (
    ChromedriverChromeMappingFileOption,
)
from appium.options.android.common.context.chromedriver_disable_build_check_option import (
    ChromedriverDisableBuildCheckOption,
)
from appium.options.android.common.context.chromedriver_executable_dir_option import ChromedriverExecutableDirOption
from appium.options.android.common.context.chromedriver_executable_option import ChromedriverExecutableOption
from appium.options.android.common.context.chromedriver_port_option import ChromedriverPortOption
from appium.options.android.common.context.chromedriver_ports_option import ChromedriverPortsOption
from appium.options.android.common.context.chromedriver_use_system_executable_option import (
    ChromedriverUseSystemExecutableOption,
)
from appium.options.android.common.context.ensure_webviews_have_pages_option import EnsureWebviewsHavePagesOption
from appium.options.android.common.context.extract_chrome_android_package_from_context_name_option import (
    ExtractChromeAndroidPackageFromContextNameOption,
)
from appium.options.android.common.context.native_web_screenshot_option import NativeWebScreenshotOption
from appium.options.android.common.context.recreate_chrome_driver_sessions_option import (
    RecreateChromeDriverSessionsOption,
)
from appium.options.android.common.context.show_chromedriver_log_option import ShowChromedriverLogOption
from appium.options.android.common.context.webview_devtools_port_option import WebviewDevtoolsPortOption
from appium.options.android.common.localization.locale_script_option import LocaleScriptOption
from appium.options.android.common.locking.skip_unlock_option import SkipUnlockOption
from appium.options.android.common.locking.unlock_key_option import UnlockKeyOption
from appium.options.android.common.locking.unlock_strategy_option import UnlockStrategyOption
from appium.options.android.common.locking.unlock_success_timeout_option import UnlockSuccessTimeoutOption
from appium.options.android.common.locking.unlock_type_option import UnlockTypeOption
from appium.options.android.common.mjpeg.mjpeg_screenshot_url_option import MjpegScreenshotUrlOption
from appium.options.android.common.other.disable_suppress_accessibility_service_option import (
    DisableSuppressAccessibilityServiceOption,
)
from appium.options.android.common.other.user_profile_option import UserProfileOption
from appium.options.android.common.signing.key_alias_option import KeyAliasOption
from appium.options.android.common.signing.key_password_option import KeyPasswordOption
from appium.options.android.common.signing.keystore_password_option import KeystorePasswordOption
from appium.options.android.common.signing.keystore_path_option import KeystorePathOption
from appium.options.android.common.signing.no_sign_option import NoSignOption
from appium.options.android.common.signing.use_keystore_option import UseKeystoreOption
from appium.options.common.app_option import AppOption
from appium.options.common.auto_web_view_option import AutoWebViewOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.clear_system_files_option import ClearSystemFilesOption
from appium.options.common.device_name_option import DeviceNameOption
from appium.options.common.enable_performance_logging_option import EnablePerformanceLoggingOption
from appium.options.common.is_headless_option import IsHeadlessOption
from appium.options.common.language_option import LanguageOption
from appium.options.common.locale_option import LocaleOption
from appium.options.common.orientation_option import OrientationOption
from appium.options.common.other_apps_option import OtherAppsOption
from appium.options.common.platform_version_option import PlatformVersionOption
from appium.options.common.skip_log_capture_option import SkipLogCaptureOption
from appium.options.common.system_port_option import SystemPortOption
from appium.options.common.udid_option import UdidOption

from .disable_window_animation_option import DisableWindowAnimationOption
from .mjpeg_server_port_option import MjpegServerPortOption
from .skip_device_initialization_option import SkipDeviceInitializationOption
from .skip_server_installation_option import SkipServerInstallationOption
from .uiautomator2_server_install_timeout_option import Uiautomator2ServerInstallTimeoutOption
from .uiautomator2_server_launch_timeout_option import Uiautomator2ServerLaunchTimeoutOption
from .uiautomator2_server_read_timeout_option import Uiautomator2ServerReadTimeoutOption


class UiAutomator2Options(
    AppiumOptions,
    AppOption,
    ClearSystemFilesOption,
    OrientationOption,
    UdidOption,
    LanguageOption,
    LocaleOption,
    IsHeadlessOption,
    SkipLogCaptureOption,
    AutoWebViewOption,
    EnablePerformanceLoggingOption,
    OtherAppsOption,
    DeviceNameOption,
    SystemPortOption,
    SkipServerInstallationOption,
    Uiautomator2ServerInstallTimeoutOption,
    Uiautomator2ServerLaunchTimeoutOption,
    Uiautomator2ServerReadTimeoutOption,
    DisableWindowAnimationOption,
    SkipDeviceInitializationOption,
    AppPackageOption,
    AppActivityOption,
    PlatformVersionOption,
    AppWaitActivityOption,
    AppWaitPackageOption,
    AppWaitDurationOption,
    AndroidInstallTimeoutOption,
    AppWaitForLaunchOption,
    IntentCategoryOption,
    IntentActionOption,
    IntentFlagsOption,
    OptionalIntentArgumentsOption,
    AutoGrantPermissionsOption,
    UninstallOtherPackagesOption,
    AllowTestPackagesOption,
    RemoteAppsCacheLimitOption,
    EnforceAppInstallOption,
    LocaleScriptOption,
    AdbPortOption,
    RemoteAdbHostOption,
    AdbExecTimeoutOption,
    ClearDeviceLogsOnStartOption,
    SkipLogcatCaptureOption,
    BuildToolsVersionOption,
    SuppressKillServerOption,
    IgnoreHiddenApiPolicyErrorOption,
    MockLocationAppOption,
    LogcatFormatOption,
    LogcatFilterSpecsOption,
    AllowDelayAdbOption,
    AvdOption,
    AvdLaunchTimeoutOption,
    AvdReadyTimeoutOption,
    AvdArgsOption,
    AvdEnvOption,
    NetworkSpeedOption,
    GpsEnabledOption,
    UseKeystoreOption,
    KeystorePathOption,
    KeystorePasswordOption,
    KeyAliasOption,
    KeyPasswordOption,
    NoSignOption,
    SkipUnlockOption,
    UnlockKeyOption,
    UnlockStrategyOption,
    UnlockSuccessTimeoutOption,
    UnlockTypeOption,
    MjpegServerPortOption,
    MjpegScreenshotUrlOption,
    AutoWebviewTimeoutOption,
    ChromeLoggingPrefsOption,
    ChromeOptionsOption,
    ChromedriverArgsOption,
    ChromedriverChromeMappingFileOption,
    ChromedriverDisableBuildCheckOption,
    ChromedriverExecutableDirOption,
    ChromedriverExecutableOption,
    ChromedriverPortOption,
    ChromedriverPortsOption,
    ChromedriverUseSystemExecutableOption,
    EnsureWebviewsHavePagesOption,
    ExtractChromeAndroidPackageFromContextNameOption,
    NativeWebScreenshotOption,
    RecreateChromeDriverSessionsOption,
    ShowChromedriverLogOption,
    WebviewDevtoolsPortOption,
    DisableSuppressAccessibilityServiceOption,
    UserProfileOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'UIAutomator2',
            PLATFORM_NAME: 'Android',
        }
