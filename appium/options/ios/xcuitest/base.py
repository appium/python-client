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

from appium.options.common.common_options import AppOption
from appium.options.common.common_options import AutoWebViewOption
from appium.options.common.common_options import AutomationNameOption
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.common_options import BundleIdOption
from appium.options.common.common_options import ClearSystemFilesOption
from appium.options.common.common_options import DeviceNameOption
from appium.options.common.common_options import EnablePerformanceLoggingOption
from appium.options.common.common_options import IsHeadlessOption
from appium.options.common.common_options import LanguageOption
from appium.options.common.common_options import LocaleOption
from appium.options.common.common_options import OrientationOption
from appium.options.common.common_options import OtherAppsOption
from appium.options.common.common_options import SkipLogCaptureOption
from appium.options.common.common_options import UdidOption

from .app.app_options import AppInstallStrategyOption
from .app.app_options import AppPushTimeoutOption
from .app.app_options import LocalizableStringsDirOption
from .general.include_device_caps_to_session_info_option import IncludeDeviceCapsToSessionInfoOption
from .general.reset_location_service_option import ResetLocationServiceOption
from .other.other_options import CommandTimeoutsOption
from .other.other_options import LaunchWithIdbOption
from .other.other_options import ShowIosLogOption
from .other.other_options import UseJsonSourceOption
from .simulator.simulator_options import CalendarAccessAuthorizedOption
from .simulator.simulator_options import CalendarFormatOption
from .simulator.simulator_options import ConnectHardwareKeyboardOption
from .simulator.simulator_options import CustomSslCertOption
from .simulator.simulator_options import EnforceFreshSimulatorCreationOption
from .simulator.simulator_options import ForceSimulatorSoftwareKeyboardPresenceOption
from .simulator.simulator_options import IosSimulatorLogsPredicateOption
from .simulator.simulator_options import KeepKeyChainsOption
from .simulator.simulator_options import KeychainsExcludePatternsOption
from .simulator.simulator_options import PermissionsOption
from .simulator.simulator_options import ReduceMotionOption
from .simulator.simulator_options import ResetOnSessionStartOnlyOption
from .simulator.simulator_options import ScaleFactorOption
from .simulator.simulator_options import ShutdownOtherSimulatorsOption
from .simulator.simulator_options import SimulatorDevicesSetPathOption
from .simulator.simulator_options import SimulatorPasteboardAutomaticSyncOption
from .simulator.simulator_options import SimulatorStartupTimeoutOption
from .simulator.simulator_options import SimulatorTracePointerOption
from .simulator.simulator_options import SimulatorWindowCenterOption
from .wda.wda_options import AllowProvisioningDeviceRegistrationOption
from .wda.wda_options import AutoAcceptAlertsOption
from .wda.wda_options import AutoDismissAlertsOption
from .wda.wda_options import DerivedDataPathOption
from .wda.wda_options import DisableAutomaticScreenshotsOption
from .wda.wda_options import ForceAppLaunchOption
from .wda.wda_options import KeychainPasswordOption
from .wda.wda_options import KeychainPathOption
from .wda.wda_options import MaxTypingFrequencyOption
from .wda.wda_options import MjpegServerPortOption
from .wda.wda_options import ProcessArgumentsOption
from .wda.wda_options import ResultBundlePathOption
from .wda.wda_options import ScreenshotQualityOption
from .wda.wda_options import ShouldTerminateAppOption
from .wda.wda_options import ShouldUseSingletonTestManagerOption
from .wda.wda_options import ShowXcodeLogOption
from .wda.wda_options import SimpleIsVisibleCheckOption
from .wda.wda_options import UpdatedWdaBundleIdOption
from .wda.wda_options import UseNativeCachingStrategyOption
from .wda.wda_options import UseNewWdaOption
from .wda.wda_options import UsePrebuiltWdaOption
from .wda.wda_options import UseSimpleBuildTestOption
from .wda.wda_options import UseXctestrunFileOption
from .wda.wda_options import WaitForIdleTimeoutOption
from .wda.wda_options import WaitForQuiescenceOption
from .wda.wda_options import WdaBaseUrlOption
from .wda.wda_options import WdaConnectionTimeoutOption
from .wda.wda_options import WdaEventloopIdleDelayOption
from .wda.wda_options import WdaLaunchTimeoutOption
from .wda.wda_options import WdaLocalPortOption
from .wda.wda_options import WdaStartupRetriesOption
from .wda.wda_options import WdaStartupRetryIntervalOption
from .wda.wda_options import WebDriverAgentUrlOption
from .wda.wda_options import XcodeOrgIdOption
from .wda.wda_options import XcodeSigningIdOption
from .webview.webview_options import AbsoluteWebLocationsOption
from .webview.webview_options import AdditionalWebviewBundleIdsOption
from .webview.webview_options import EnableAsyncExecuteFromHttpsOption
from .webview.webview_options import FullContextListOption
from .webview.webview_options import IncludeSafariInWebviewsOption
from .webview.webview_options import NativeWebTapOption
from .webview.webview_options import SafariGarbageCollectOption
from .webview.webview_options import SafariIgnoreFraudWarningOption
from .webview.webview_options import SafariIgnoreWebHostnamesOption
from .webview.webview_options import SafariInitialUrlOption
from .webview.webview_options import SafariLogAllCommunicationHexDumpOption
from .webview.webview_options import SafariLogAllCommunicationOption
from .webview.webview_options import SafariOpenLinksInBackgroundOption
from .webview.webview_options import SafariSocketChunkSizeOption
from .webview.webview_options import SafariWebInspectorMaxFrameLengthOption
from .webview.webview_options import WebkitResponseTimeoutOption
from .webview.webview_options import WebviewConnectRetriesOption
from .webview.webview_options import WebviewConnectTimeoutOption


class XCUITestOptions(
    AppiumOptions,
    AppOption,
    BundleIdOption,
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
    IncludeDeviceCapsToSessionInfoOption,
    ResetLocationServiceOption,
    AppInstallStrategyOption,
    AppPushTimeoutOption,
    LocalizableStringsDirOption,
    CommandTimeoutsOption,
    LaunchWithIdbOption,
    ShowIosLogOption,
    UseJsonSourceOption,
    CalendarAccessAuthorizedOption,
    CalendarFormatOption,
    ConnectHardwareKeyboardOption,
    CustomSslCertOption,
    EnforceFreshSimulatorCreationOption,
    ForceSimulatorSoftwareKeyboardPresenceOption,
    IosSimulatorLogsPredicateOption,
    KeepKeyChainsOption,
    KeychainsExcludePatternsOption,
    PermissionsOption,
    ReduceMotionOption,
    ResetOnSessionStartOnlyOption,
    ScaleFactorOption,
    ShutdownOtherSimulatorsOption,
    SimulatorDevicesSetPathOption,
    SimulatorPasteboardAutomaticSyncOption,
    SimulatorStartupTimeoutOption,
    SimulatorTracePointerOption,
    SimulatorWindowCenterOption,
    AllowProvisioningDeviceRegistrationOption,
    AutoAcceptAlertsOption,
    AutoDismissAlertsOption,
    DerivedDataPathOption,
    DisableAutomaticScreenshotsOption,
    ForceAppLaunchOption,
    KeychainPasswordOption,
    KeychainPathOption,
    MaxTypingFrequencyOption,
    MjpegServerPortOption,
    ProcessArgumentsOption,
    ResultBundlePathOption,
    ScreenshotQualityOption,
    ShouldTerminateAppOption,
    ShouldUseSingletonTestManagerOption,
    ShowXcodeLogOption,
    SimpleIsVisibleCheckOption,
    UpdatedWdaBundleIdOption,
    UseNativeCachingStrategyOption,
    UseNewWdaOption,
    UsePrebuiltWdaOption,
    UseSimpleBuildTestOption,
    UseXctestrunFileOption,
    WaitForIdleTimeoutOption,
    WaitForQuiescenceOption,
    WdaBaseUrlOption,
    WdaConnectionTimeoutOption,
    WdaEventloopIdleDelayOption,
    WdaLaunchTimeoutOption,
    WdaLocalPortOption,
    WdaStartupRetriesOption,
    WdaStartupRetryIntervalOption,
    WebDriverAgentUrlOption,
    XcodeOrgIdOption,
    XcodeSigningIdOption,
    AbsoluteWebLocationsOption,
    AdditionalWebviewBundleIdsOption,
    EnableAsyncExecuteFromHttpsOption,
    FullContextListOption,
    IncludeSafariInWebviewsOption,
    NativeWebTapOption,
    SafariGarbageCollectOption,
    SafariIgnoreFraudWarningOption,
    SafariIgnoreWebHostnamesOption,
    SafariInitialUrlOption,
    SafariLogAllCommunicationHexDumpOption,
    SafariLogAllCommunicationOption,
    SafariOpenLinksInBackgroundOption,
    SafariSocketChunkSizeOption,
    SafariWebInspectorMaxFrameLengthOption,
    WebkitResponseTimeoutOption,
    WebviewConnectRetriesOption,
    WebviewConnectTimeoutOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AutomationNameOption.AUTOMATION_NAME: 'XCUITest',
            PLATFORM_NAME: 'iOS',
        }
