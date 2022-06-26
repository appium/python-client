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
from appium.options.common.skip_log_capture_option import SkipLogCaptureOption
from appium.options.common.system_port_option import SystemPortOption
from appium.options.common.udid_option import UdidOption

from .disable_window_animation_option import DisableWindowAnimationOption
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
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'UIAutomator2',
            PLATFORM_NAME: 'Android',
        }
