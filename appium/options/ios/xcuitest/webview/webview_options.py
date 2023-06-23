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
from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar("C", bound="SupportsCapabilities")


class WebViewOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name == ('WEBKIT_RESPONSE_TIMEOUT', 'WEBVIEW_CONNECT_TIMEOUT'):
            value = getattr(obj, 'get_capabilities')(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, 'get_capabilities')(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == ('WEBKIT_RESPONSE_TIMEOUT', 'WEBVIEW_CONNECT_TIMEOUT'):
            return getattr(obj, 'set_capabilities')(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        return getattr(obj, 'set_capabilities')(self.name, value)


class AbsoluteWebLocationsOption(SupportsCapabilities):
    ABSOLUTE_WEB_LOCATIONS = 'absoluteWebLocations'
    absolute_web_locations = WebViewOptionsDescriptor("ABSOLUTE_WEB_LOCATIONS")
    """
    This capability will direct the Get Element Location command, when used
    within webviews, to return coordinates which are relative to the origin of
    the page, rather than relative to the current scroll offset. This capability
    has no effect outside of webviews. Defaults to  false.

    Usage
    -----
    - `self.absolute_web_locations`
    - `self.absolute_web_locations` = `value`
    """


class AdditionalWebviewBundleIdsOption(SupportsCapabilities):
    ADDITIONAL_WEBVIEW_BUNDLE_IDS = 'additionalWebviewBundleIds'
    additional_webview_bundle_ids = WebViewOptionsDescriptor("ADDITIONAL_WEBVIEW_BUNDLE_IDS")
    """
    Array of possible bundle identifiers for webviews. This is sometimes
    necessary if the Web Inspector is found to be returning a modified
    bundle identifier for the app. Defaults to [].

    Usage
    -----
    - `self.additional_webview_bundle_ids`
    - `self.additional_webview_bundle_ids` = `value`
    """


class EnableAsyncExecuteFromHttpsOption(SupportsCapabilities):
    ENABLE_ASYNC_EXECUTE_FROM_HTTPS = 'enableAsyncExecuteFromHttps'
    enable_async_execute_from_https = WebViewOptionsDescriptor("ENABLE_ASYNC_EXECUTE_FROM_HTTPS")
    """
    Capability to allow simulators to execute asynchronous JavaScript
    on pages using HTTPS. Defaults to false.

    Usage
    -----
    - `self.enable_async_execute_from_https`
    - `self.enable_async_execute_from_https` = `value`
    """


class FullContextListOption(SupportsCapabilities):
    FULL_CONTEXT_LIST = 'fullContextList'
    full_context_list = WebViewOptionsDescriptor("FULL_CONTEXT_LIST")
    """
    Sets to return the detailed information on contexts for the get available
    context command. If this capability is enabled, then each item in the returned
    contexts list would additionally include WebView title, full URL and the bundle
    identifier. Defaults to false.

    Usage
    -----
    - `self.full_context_list`
    - `self.full_context_list` = `value`
    """


class IncludeSafariInWebviewsOption(SupportsCapabilities):
    INCLUDE_SAFARI_IN_WEBVIEWS = 'includeSafariInWebviews'
    include_safari_in_webviews = WebViewOptionsDescriptor("INCLUDE_SAFARI_IN_WEBVIEWS")
    """
    Add Safari web contexts to the list of contexts available during a
    native/webview app test. This is useful if the test opens Safari and
    needs to be able to interact with it. Defaults to false.

    Usage
    ----
    - `self.include_safari_in_webviews`
    - `self.include_safari_in_webviews` = `value`
    """


class NativeWebTapOption(SupportsCapabilities):
    NATIVE_WEB_TAP = 'nativeWebTap'
    native_web_tap = WebViewOptionsDescriptor("NATIVE_WEB_TAP")
    """
    Enable native, non-javascript-based taps being in web context mode. Defaults
    to false. Warning: sometimes the preciseness of native taps could be broken,
    because there is no reliable way to map web element coordinates to native ones.

    - `self.native_web_tap`
    - `self.native_web_tap` = `value`
    """


class SafariGarbageCollectOption(SupportsCapabilities):
    SAFARI_GARBAGE_COLLECT = 'safariGarbageCollect'
    safari_garbage_collect = WebViewOptionsDescriptor("SAFARI_GARBAGE_COLLECT")
    """
    Turns on/off Web Inspector garbage collection when executing scripts on Safari.
    Turning on may improve performance. Defaults to `False`.

    Usage
    -----
    - `self.safari_garbage_collect`
    - `self.safari_garbage_collect` = `value`
    """


class SafariIgnoreFraudWarningOption(SupportsCapabilities):
    SAFARI_IGNORE_FRAUD_WARNING = 'safariIgnoreFraudWarning'
    safari_ignore_fraud_warning = WebViewOptionsDescriptor("SAFARI_IGNORE_FRAUD_WARNING")
    """
    Prevent Safari from showing a fraudulent website warning.
    Default keeps current sim setting..

    Usage
    -----
    - `self.safari_ignore_fraud_warning`
    - `self.safari_ignore_fraud_warning` = `value`
    """


class SafariIgnoreWebHostnamesOption(SupportsCapabilities):
    SAFARI_IGNORE_WEB_HOSTNAMES = 'safariIgnoreWebHostnames'
    safari_ignore_web_hostnames = WebViewOptionsDescriptor("SAFARI_IGNORE_WEB_HOSTNAMES")
    """
    Provide a list of hostnames (comma-separated) that the Safari automation
    tools should ignore. This is to provide a workaround to prevent a webkit
    bug where the web context is unintentionally changed to a 3rd party website
    and the test gets stuck. The common culprits are search engines (yahoo, bing,
    google) and about:blank.

    Usage
    -----
    - `self.safari_ignore_web_hostnames`
    - `self.safari_ignore_web_hostnames` = `value`
    """


class SafariInitialUrlOption(SupportsCapabilities):
    SAFARI_INITIAL_URL = 'safariInitialUrl'
    safari_initial_url = WebViewOptionsDescriptor("SAFARI_INITIAL_URL")
    """
    Gets and Sets initial safari url, default is a local welcome page.

    Usage
    -----
    - `self.safari_initial_url`
    - `self.safari_initial_url` = `value`
    """


class SafariLogAllCommunicationHexDumpOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP = 'safariLogAllCommunicationHexDump'
    safari_log_all_communication_hex_dump = WebViewOptionsDescriptor("SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP")
    """
    Log all communication sent to and received from the Web Inspector, as raw
    hex dump and printable characters. This logging is done before any data
    manipulation, and so can elucidate some communication issues. Like
    appium:safariLogAllCommunication, this can produce a lot of data in some cases,
    so it is recommended to be used only when necessary. Defaults to false.

    Usage
    -----
    - `self.safari_log_all_communication_hex_dump`
    - `self.safari_log_all_communication_hex_dump` = `value`
    """


class SafariLogAllCommunicationOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION = 'safariLogAllCommunication'
    safari_log_all_communication = WebViewOptionsDescriptor("SAFARI_LOG_ALL_COMMUNICATION")
    """
    Log all plists sent to and received from the Web Inspector, as plain text.
    For some operations this can be a lot of data, so it is recommended to
    be used only when necessary. Defaults to false.

    - `self.safari_log_all_communication`
    - `self.safari_log_all_communication` = `value`
    """


class SafariOpenLinksInBackgroundOption(SupportsCapabilities):
    SAFARI_OPEN_LINKS_IN_BACKGROUND = 'safariOpenLinksInBackground'
    safari_open_links_in_background = WebViewOptionsDescriptor("SAFARI_OPEN_LINKS_IN_BACKGROUND")
    """
    Whether Safari should allow links to open in new windows.
    Default keeps current sim setting.

    Usage
    -----
    - `self.safari_open_links_in_background`
    - `self.safari_open_links_in_background` = `value`
    """


class SafariSocketChunkSizeOption(SupportsCapabilities):
    SAFARI_SOCKET_CHUNK_SIZE = 'safariSocketChunkSize'
    safari_socket_chunk_size = WebViewOptionsDescriptor("SAFARI_SOCKET_CHUNK_SIZE")
    """
    The size, in bytes, of the data to be sent to the Web Inspector on
    iOS 11+ real devices. Some devices hang when sending large amounts of
    data to the Web Inspector, and breaking them into smaller parts can be
    helpful in those cases. Defaults to 16384 (also the maximum possible).

    Usage
    -----
    - `self.safari_socket_chunk_size`
    - `self.safari_socket_chunk_size` = `value`
    """

class SafariWebInspectorMaxFrameLengthOption(SupportsCapabilities):
    SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH = 'safariWebInspectorMaxFrameLength'
    safari_web_inspector_max_frame_length = WebViewOptionsDescriptor("SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH")
    """
    The maximum size in bytes of a single data frame for the Web Inspector.
    Too high values could introduce slowness and/or memory leaks.
    Too low values could introduce possible buffer overflow exceptions.
    Defaults to 20MiB (20*1024*1024).

    Usage
    -----
    - `self.safari_web_inspector_max_frame_length`
    - `self.safari_web_inspector_max_frame_length` = `value`
    """

class WebkitResponseTimeoutOption(SupportsCapabilities):
    WEBKIT_RESPONSE_TIMEOUT = 'webkitResponseTimeout'
    webkit_response_timeout = WebViewOptionsDescriptor("WEBKIT_RESPONSE_TIMEOUT")
    """
    Time to wait for a response from WebKit in a Safari session.
    (Real device only) Set the time to wait for a respons

    Usage
    -----
    - `self.webkit_response_timeout`
    - `self.webkit_response_timeout` = `value`
    """


class WebviewConnectRetriesOption(SupportsCapabilities):
    WEBVIEW_CONNECT_RETRIES = 'webviewConnectRetries'
    webview_connect_retries = WebViewOptionsDescriptor("WEBVIEW_CONNECT_RETRIES")
    """
    Number of times to send connection message to remote debugger,
    to get a webview. Default: 8.

    Usage
    -----
    - `self.webview_connect_retries`
    - `self.webview_connect_retries` = `value`
    """


class WebviewConnectTimeoutOption(SupportsCapabilities):
    WEBVIEW_CONNECT_TIMEOUT = 'webviewConnectTimeout'
    webview_connect_timeout = WebViewOptionsDescriptor("WEBVIEW_CONNECT_TIMEOUT")
    """
    The time to wait for the initial presence of webviews in
    MobileSafari or hybrid apps. Defaults to 0ms.

    Usage
    -----
    - `self.webview_connect_timeout`
    - `self.webview_connect_timeout` = `value`
    """