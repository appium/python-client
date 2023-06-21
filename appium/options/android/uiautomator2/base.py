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

from appium.options.android.common.adb.adb_options import AdbExecTimeoutOption
from appium.options.android.common.adb.adb_options import AdbPortOption
from appium.options.android.common.adb.adb_options import AllowDelayAdbOption
from appium.options.android.common.adb.adb_options import BuildToolsVersionOption
from appium.options.android.common.adb.adb_options import ClearDeviceLogsOnStartOption
from appium.options.android.common.adb.adb_options import IgnoreHiddenApiPolicyErrorOption
from appium.options.android.common.adb.adb_options import LogcatFilterSpecsOption
from appium.options.android.common.adb.adb_options import LogcatFormatOption
from appium.options.android.common.adb.adb_options import MockLocationAppOption
from appium.options.android.common.adb.adb_options import RemoteAdbHostOption
from appium.options.android.common.adb.adb_options import SkipLogcatCaptureOption
from appium.options.android.common.adb.adb_options import SuppressKillServerOption
from appium.options.android.common.app.app_options import AllowTestPackagesOption
from appium.options.android.common.app.app_options import AndroidInstallTimeoutOption
from appium.options.android.common.app.app_options import AppActivityOption
from appium.options.android.common.app.app_options import AppPackageOption
from appium.options.android.common.app.app_options import AppWaitActivityOption
from appium.options.android.common.app.app_options import AppWaitDurationOption
from appium.options.android.common.app.app_options import AppWaitForLaunchOption
from appium.options.android.common.app.app_options import AppWaitPackageOption
from appium.options.android.common.app.app_options import AutoGrantPermissionsOption
from appium.options.android.common.app.app_options import EnforceAppInstallOption
from appium.options.android.common.app.app_options import IntentActionOption
from appium.options.android.common.app.app_options import IntentCategoryOption
from appium.options.android.common.app.app_options import IntentFlagsOption
from appium.options.android.common.app.app_options import OptionalIntentArgumentsOption
from appium.options.android.common.app.app_options import RemoteAppsCacheLimitOption
from appium.options.android.common.app.app_options import UninstallOtherPackagesOption
from appium.options.android.common.avd.avd_options import AvdArgsOption
from appium.options.android.common.avd.avd_options import AvdEnvOption
from appium.options.android.common.avd.avd_options import AvdLaunchTimeoutOption
from appium.options.android.common.avd.avd_options import AvdOption
from appium.options.android.common.avd.avd_options import AvdReadyTimeoutOption
from appium.options.android.common.avd.avd_options import GpsEnabledOption
from appium.options.android.common.avd.avd_options import NetworkSpeedOption
from appium.options.android.common.context.context_options import AutoWebviewTimeoutOption
from appium.options.android.common.context.context_options import ChromeLoggingPrefsOption
from appium.options.android.common.context.context_options import ChromeOptionsOption
from appium.options.android.common.context.context_options import ChromedriverArgsOption
from appium.options.android.common.context.context_options import ChromedriverChromeMappingFileOption
from appium.options.android.common.context.context_options import ChromedriverDisableBuildCheckOption
from appium.options.android.common.context.context_options import ChromedriverExecutableDirOption
from appium.options.android.common.context.context_options import ChromedriverExecutableOption
from appium.options.android.common.context.context_options import ChromedriverPortOption
from appium.options.android.common.context.context_options import ChromedriverPortsOption
from appium.options.android.common.context.context_options import ChromedriverUseSystemExecutableOption
from appium.options.android.common.context.context_options import EnsureWebviewsHavePagesOption
from appium.options.android.common.context.context_options import ExtractChromeAndroidPackageFromContextNameOption
from appium.options.android.common.context.context_options import NativeWebScreenshotOption
from appium.options.android.common.context.context_options import RecreateChromeDriverSessionsOption
from appium.options.android.common.context.context_options import ShowChromedriverLogOption
from appium.options.android.common.context.context_options import WebviewDevtoolsPortOption
from appium.options.android.common.localization.locale_script_option import LocaleScriptOption
from appium.options.android.common.locking.locking_options import SkipUnlockOption
from appium.options.android.common.locking.locking_options import UnlockKeyOption
from appium.options.android.common.locking.locking_options import UnlockStrategyOption
from appium.options.android.common.locking.locking_options import UnlockSuccessTimeoutOption
from appium.options.android.common.locking.locking_options import UnlockTypeOption
from appium.options.android.common.mjpeg.mjpeg_screenshot_url_option import MjpegScreenshotUrlOption
from appium.options.android.common.other.disable_suppress_accessibility_service_option import (
    DisableSuppressAccessibilityServiceOption,
)
from appium.options.android.common.other.user_profile_option import UserProfileOption
from appium.options.android.common.signing.signing_options import KeyAliasOption
from appium.options.android.common.signing.signing_options import KeyPasswordOption
from appium.options.android.common.signing.signing_options import KeystorePasswordOption
from appium.options.android.common.signing.signing_options import KeystorePathOption
from appium.options.android.common.signing.signing_options import NoSignOption
from appium.options.android.common.signing.signing_options import UseKeystoreOption
from appium.options.common.common_options import AppOption
from appium.options.common.common_options import AutoWebViewOption
from appium.options.common.common_options import AutomationNameOption
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.common_options import ClearSystemFilesOption
from appium.options.common.common_options import DeviceNameOption
from appium.options.common.common_options import EnablePerformanceLoggingOption
from appium.options.common.common_options import IsHeadlessOption
from appium.options.common.common_options import LanguageOption
from appium.options.common.common_options import LocaleOption
from appium.options.common.common_options import OrientationOption
from appium.options.common.common_options import OtherAppsOption
from appium.options.common.common_options import SkipLogCaptureOption
from appium.options.common.common_options import SystemPortOption
from appium.options.common.common_options import UdidOption

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
            AutomationNameOption.AUTOMATION_NAME: 'UIAutomator2',
            PLATFORM_NAME: 'Android',
        }
