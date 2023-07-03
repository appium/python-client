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

from appium.options.android.common.adb.adb_options import (
    AdbExecTimeoutOption,
    AdbPortOption,
    AllowDelayAdbOption,
    BuildToolsVersionOption,
    ClearDeviceLogsOnStartOption,
    IgnoreHiddenApiPolicyErrorOption,
    LogcatFilterSpecsOption,
    LogcatFormatOption,
    MockLocationAppOption,
    RemoteAdbHostOption,
    SkipLogcatCaptureOption,
    SuppressKillServerOption,
)
from appium.options.android.common.app.app_options import (
    AllowTestPackagesOption,
    AndroidInstallTimeoutOption,
    AppActivityOption,
    AppPackageOption,
    AppWaitActivityOption,
    AppWaitDurationOption,
    AppWaitForLaunchOption,
    AppWaitPackageOption,
    AutoGrantPermissionsOption,
    EnforceAppInstallOption,
    IntentActionOption,
    IntentCategoryOption,
    IntentFlagsOption,
    OptionalIntentArgumentsOption,
    RemoteAppsCacheLimitOption,
    UninstallOtherPackagesOption,
)
from appium.options.android.common.avd.avd_options import (
    AvdArgsOption,
    AvdEnvOption,
    AvdLaunchTimeoutOption,
    AvdOption,
    AvdReadyTimeoutOption,
    GpsEnabledOption,
    NetworkSpeedOption,
)
from appium.options.android.common.context.context_options import (
    AutoWebviewTimeoutOption,
    ChromedriverArgsOption,
    ChromedriverChromeMappingFileOption,
    ChromedriverDisableBuildCheckOption,
    ChromedriverExecutableDirOption,
    ChromedriverExecutableOption,
    ChromedriverPortOption,
    ChromedriverPortsOption,
    ChromedriverUseSystemExecutableOption,
    ChromeLoggingPrefsOption,
    ChromeOptionsOption,
    EnsureWebviewsHavePagesOption,
    ExtractChromeAndroidPackageFromContextNameOption,
    NativeWebScreenshotOption,
    RecreateChromeDriverSessionsOption,
    ShowChromedriverLogOption,
    WebviewDevtoolsPortOption,
)
from appium.options.android.common.localization.locale_script_option import LocaleScriptOption
from appium.options.android.common.locking.locking_options import (
    SkipUnlockOption,
    UnlockKeyOption,
    UnlockStrategyOption,
    UnlockSuccessTimeoutOption,
    UnlockTypeOption,
)
from appium.options.android.common.mjpeg.mjpeg_screenshot_url_option import MjpegScreenshotUrlOption
from appium.options.android.common.other.disable_suppress_accessibility_service_option import (
    DisableSuppressAccessibilityServiceOption,
)
from appium.options.android.common.other.user_profile_option import UserProfileOption
from appium.options.android.common.signing.signing_options import (
    KeyAliasOption,
    KeyPasswordOption,
    KeystorePasswordOption,
    KeystorePathOption,
    NoSignOption,
    UseKeystoreOption,
)
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.common_options import (
    AppOption,
    AutomationNameOption,
    AutoWebViewOption,
    ClearSystemFilesOption,
    DeviceNameOption,
    EnablePerformanceLoggingOption,
    IsHeadlessOption,
    LanguageOption,
    LocaleOption,
    OrientationOption,
    OtherAppsOption,
    SkipLogCaptureOption,
    SystemPortOption,
    UdidOption,
)

from .espresso_options import (
    ActivityOptionsOption,
    AppLocaleOption,
    EspressoBuildConfigOption,
    EspressoServerLaunchTimeoutOption,
    ForceEspressoRebuildOption,
    IntentOptionsOption,
    ShowGradleLogOption,
)


class EspressoOptions(
    AppiumOptions,
    AppOption,
    OrientationOption,
    UdidOption,
    LanguageOption,
    LocaleOption,
    IsHeadlessOption,
    SkipLogCaptureOption,
    AutoWebViewOption,
    DeviceNameOption,
    ClearSystemFilesOption,
    EnablePerformanceLoggingOption,
    OtherAppsOption,
    SystemPortOption,
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
    BuildToolsVersionOption,
    SkipLogcatCaptureOption,
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
    EspressoBuildConfigOption,
    EspressoServerLaunchTimeoutOption,
    ForceEspressoRebuildOption,
    ShowGradleLogOption,
    IntentOptionsOption,
    ActivityOptionsOption,
    AppLocaleOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AutomationNameOption.AUTOMATION_NAME: "Espresso",
            PLATFORM_NAME: "Android",
        }
