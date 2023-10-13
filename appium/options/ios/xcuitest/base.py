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

from appium.options.common.app_option import AppOption
from appium.options.common.auto_web_view_option import AutoWebViewOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.bundle_id_option import BundleIdOption
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
from appium.options.common.udid_option import UdidOption

from .app.app_install_strategy_option import AppInstallStrategyOption
from .app.app_push_timeout_option import AppPushTimeoutOption
from .app.localizable_strings_dir_option import LocalizableStringsDirOption
from .general.include_device_caps_to_session_info_option import IncludeDeviceCapsToSessionInfoOption
from .general.reset_location_service_option import ResetLocationServiceOption
from .other.command_timeouts_option import CommandTimeoutsOption
from .other.launch_with_idb_option import LaunchWithIdbOption
from .other.show_ios_log_option import ShowIosLogOption
from .other.use_json_source_option import UseJsonSourceOption
from .simulator.calendar_access_authorized_option import CalendarAccessAuthorizedOption
from .simulator.calendar_format_option import CalendarFormatOption
from .simulator.connect_hardware_keyboard_option import ConnectHardwareKeyboardOption
from .simulator.custom_ssl_cert_option import CustomSslCertOption
from .simulator.enforce_fresh_simulator_creation_option import EnforceFreshSimulatorCreationOption
from .simulator.force_simulator_software_keyboard_presence_option import ForceSimulatorSoftwareKeyboardPresenceOption
from .simulator.ios_simulator_logs_predicate_option import IosSimulatorLogsPredicateOption
from .simulator.keep_key_chains_option import KeepKeyChainsOption
from .simulator.keychains_exclude_patterns_option import KeychainsExcludePatternsOption
from .simulator.permissions_option import PermissionsOption
from .simulator.reduce_motion_option import ReduceMotionOption
from .simulator.reset_on_session_start_only_option import ResetOnSessionStartOnlyOption
from .simulator.scale_factor_option import ScaleFactorOption
from .simulator.shutdown_other_simulators_option import ShutdownOtherSimulatorsOption
from .simulator.simulator_devices_set_path_option import SimulatorDevicesSetPathOption
from .simulator.simulator_pasteboard_automatic_sync_option import SimulatorPasteboardAutomaticSyncOption
from .simulator.simulator_startup_timeout_option import SimulatorStartupTimeoutOption
from .simulator.simulator_trace_pointer_option import SimulatorTracePointerOption
from .simulator.simulator_window_center_option import SimulatorWindowCenterOption
from .wda.allow_provisioning_device_regitration_option import AllowProvisioningDeviceRegistrationOption
from .wda.auto_accept_alerts_option import AutoAcceptAlertsOption
from .wda.auto_disimiss_alerts_option import AutoDismissAlertsOption
from .wda.derived_data_path_option import DerivedDataPathOption
from .wda.disable_automatic_screenshots_option import DisableAutomaticScreenshotsOption
from .wda.force_app_launch_option import ForceAppLaunchOption
from .wda.keychain_password_option import KeychainPasswordOption
from .wda.keychain_path_option import KeychainPathOption
from .wda.max_typing_frequency_option import MaxTypingFrequencyOption
from .wda.mjpeg_server_port_option import MjpegServerPortOption
from .wda.process_arguments_option import ProcessArgumentsOption
from .wda.result_bundle_path_option import ResultBundlePathOption
from .wda.screenshot_quality_option import ScreenshotQualityOption
from .wda.should_terminate_app_option import ShouldTerminateAppOption
from .wda.should_use_singleton_test_manager_option import ShouldUseSingletonTestManagerOption
from .wda.show_xcode_log_option import ShowXcodeLogOption
from .wda.simple_is_visible_check_option import SimpleIsVisibleCheckOption
from .wda.updated_wda_bundle_id_option import UpdatedWdaBundleIdOption
from .wda.use_native_caching_strategy_option import UseNativeCachingStrategyOption
from .wda.use_new_wda_option import UseNewWdaOption
from .wda.use_prebuilt_wda_option import UsePrebuiltWdaOption
from .wda.use_simple_build_test_option import UseSimpleBuildTestOption
from .wda.use_xctestrun_file_option import UseXctestrunFileOption
from .wda.wait_for_idle_timeout_option import WaitForIdleTimeoutOption
from .wda.wait_for_quiescence_option import WaitForQuiescenceOption
from .wda.wda_base_url_option import WdaBaseUrlOption
from .wda.wda_connection_timeout_option import WdaConnectionTimeoutOption
from .wda.wda_eventloop_idle_delay_option import WdaEventloopIdleDelayOption
from .wda.wda_launch_timeout_option import WdaLaunchTimeoutOption
from .wda.wda_local_port_option import WdaLocalPortOption
from .wda.wda_startup_retries_option import WdaStartupRetriesOption
from .wda.wda_startup_retry_interval_option import WdaStartupRetryIntervalOption
from .wda.web_driver_agent_url_option import WebDriverAgentUrlOption
from .wda.xcode_org_id_option import XcodeOrgIdOption
from .wda.xcode_signing_id_option import XcodeSigningIdOption
from .webview.absolute_web_locations_option import AbsoluteWebLocationsOption
from .webview.additional_webview_bundle_ids_option import AdditionalWebviewBundleIdsOption
from .webview.enable_async_execute_from_https_option import EnableAsyncExecuteFromHttpsOption
from .webview.full_context_list_option import FullContextListOption
from .webview.include_safari_in_webviews_option import IncludeSafariInWebviewsOption
from .webview.native_web_tap_option import NativeWebTapOption
from .webview.safari_garbage_collect_option import SafariGarbageCollectOption
from .webview.safari_ignore_fraud_warning_option import SafariIgnoreFraudWarningOption
from .webview.safari_ignore_web_hostnames_option import SafariIgnoreWebHostnamesOption
from .webview.safari_initial_url_option import SafariInitialUrlOption
from .webview.safari_log_all_communication_hex_dump_option import SafariLogAllCommunicationHexDumpOption
from .webview.safari_log_all_communication_option import SafariLogAllCommunicationOption
from .webview.safari_open_links_in_background_option import SafariOpenLinksInBackgroundOption
from .webview.safari_socket_chunk_size_option import SafariSocketChunkSizeOption
from .webview.safari_web_inspector_max_frame_length_option import SafariWebInspectorMaxFrameLengthOption
from .webview.webkit_response_timeout_option import WebkitResponseTimeoutOption
from .webview.webview_connect_retries_option import WebviewConnectRetriesOption
from .webview.webview_connect_timeout_option import WebviewConnectTimeoutOption


class XCUITestOptions(
    AppiumOptions,
    AppOption,
    BundleIdOption,
    PlatformVersionOption,
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
            AUTOMATION_NAME: 'XCUITest',
            PLATFORM_NAME: 'iOS',
        }
