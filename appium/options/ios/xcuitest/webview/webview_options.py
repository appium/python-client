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
from typing import List, Optional, Union

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.transformers import transform_duration_get, transform_duration_set


class AbsoluteWebLocationsOption(SupportsCapabilities):
    ABSOLUTE_WEB_LOCATIONS = "absoluteWebLocations"
    absolute_web_locations = OptionsDescriptor[Optional[bool], bool](ABSOLUTE_WEB_LOCATIONS)
    """
    This capability will direct the Get Element Location command, when used
    within webviews, to return coordinates which are relative to the origin of
    the page, rather than relative to the current scroll offset. This capability
    has no effect outside of webviews. Defaults to  false.

    Usage
    -----
    - Get
        - `self.absolute_web_locations`
    - Set
        - `self.absolute_web_locations` = `value`
    
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


class AdditionalWebviewBundleIdsOption(SupportsCapabilities):
    ADDITIONAL_WEBVIEW_BUNDLE_IDS = "additionalWebviewBundleIds"
    additional_webview_bundle_ids = OptionsDescriptor[Optional[List[str]], List[str]](ADDITIONAL_WEBVIEW_BUNDLE_IDS)
    """
    Array of possible bundle identifiers for webviews. This is sometimes
    necessary if the Web Inspector is found to be returning a modified
    bundle identifier for the app. Defaults to [].

    Usage
    -----
    - Get
        - `self.additional_webview_bundle_ids`
    - Set
        - `self.additional_webview_bundle_ids` = `value`
    
    Parameters
    ----------
    `value`: `List[str]`

    Returns
    -------
    - Get
        - `Optional[List[str]]`
    - Set
        - `None`
    """


class EnableAsyncExecuteFromHttpsOption(SupportsCapabilities):
    ENABLE_ASYNC_EXECUTE_FROM_HTTPS = "enableAsyncExecuteFromHttps"
    enable_async_execute_from_https = OptionsDescriptor[Optional[bool], bool](ENABLE_ASYNC_EXECUTE_FROM_HTTPS)
    """
    Capability to allow simulators to execute asynchronous JavaScript
    on pages using HTTPS. Defaults to false.

    Usage
    -----
    - Get
        - `self.enable_async_execute_from_https`
    - Set
        - `self.enable_async_execute_from_https` = `value`
    
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


class FullContextListOption(SupportsCapabilities):
    FULL_CONTEXT_LIST = "fullContextList"
    full_context_list = OptionsDescriptor[Optional[bool], bool](FULL_CONTEXT_LIST)
    """
    Sets to return the detailed information on contexts for the get available
    context command. If this capability is enabled, then each item in the returned
    contexts list would additionally include WebView title, full URL and the bundle
    identifier. Defaults to false.

    Usage
    -----
    - Get
        - `self.full_context_list`
    - Set
        - `self.full_context_list` = `value`
    
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


class IncludeSafariInWebviewsOption(SupportsCapabilities):
    INCLUDE_SAFARI_IN_WEBVIEWS = "includeSafariInWebviews"
    include_safari_in_webviews = OptionsDescriptor[Optional[bool], bool](INCLUDE_SAFARI_IN_WEBVIEWS)
    """
    Add Safari web contexts to the list of contexts available during a
    native/webview app test. This is useful if the test opens Safari and
    needs to be able to interact with it. Defaults to false.

    Usage
    -----
    - Get
        - `self.include_safari_in_webviews`
    - Set
        - `self.include_safari_in_webviews` = `value`
    
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


class NativeWebTapOption(SupportsCapabilities):
    NATIVE_WEB_TAP = "nativeWebTap"
    native_web_tap = OptionsDescriptor[Optional[bool], bool](NATIVE_WEB_TAP)
    """
    Enable native, non-javascript-based taps being in web context mode. Defaults
    to false. Warning: sometimes the preciseness of native taps could be broken,
    because there is no reliable way to map web element coordinates to native ones.

    Usage
    -----
    - Get
        - `self.native_web_tap`
    - Set
        - `self.native_web_tap` = `value`
    
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


class SafariGarbageCollectOption(SupportsCapabilities):
    SAFARI_GARBAGE_COLLECT = "safariGarbageCollect"
    safari_garbage_collect = OptionsDescriptor[Optional[bool], bool](SAFARI_GARBAGE_COLLECT)
    """
    Turns on/off Web Inspector garbage collection when executing scripts on Safari.
    Turning on may improve performance. Defaults to `False`.

    Usage
    -----
    - Get
        - `self.safari_garbage_collect`
    - Set
        - `self.safari_garbage_collect` = `value`
    
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


class SafariIgnoreFraudWarningOption(SupportsCapabilities):
    SAFARI_IGNORE_FRAUD_WARNING = "safariIgnoreFraudWarning"
    safari_ignore_fraud_warning = OptionsDescriptor[Optional[bool], bool](SAFARI_IGNORE_FRAUD_WARNING)
    """
    Prevent Safari from showing a fraudulent website warning.
    Default keeps current sim setting..

    Usage
    -----
    - Get
        - `self.safari_ignore_fraud_warning`
    - Set
        - `self.safari_ignore_fraud_warning` = `value`
    
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


class SafariIgnoreWebHostnamesOption(SupportsCapabilities):
    SAFARI_IGNORE_WEB_HOSTNAMES = "safariIgnoreWebHostnames"
    safari_ignore_web_hostnames = OptionsDescriptor[Optional[str], str](SAFARI_IGNORE_WEB_HOSTNAMES)
    """
    Provide a list of hostnames (comma-separated) that the Safari automation
    tools should ignore. This is to provide a workaround to prevent a webkit
    bug where the web context is unintentionally changed to a 3rd party website
    and the test gets stuck. The common culprits are search engines (yahoo, bing,
    google) and about:blank.

    Usage
    -----
    - Get
        - `self.safari_ignore_web_hostnames`
    - Set
        - `self.safari_ignore_web_hostnames` = `value`
    
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


class SafariInitialUrlOption(SupportsCapabilities):
    SAFARI_INITIAL_URL = "safariInitialUrl"
    safari_initial_url = OptionsDescriptor[Optional[str], str](SAFARI_INITIAL_URL)
    """
    Gets and Sets initial safari url, default is a local welcome page.

    Usage
    -----
    - Get
        - `self.safari_initial_url`
    - Set
        - `self.safari_initial_url` = `value`
    
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


class SafariLogAllCommunicationHexDumpOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP = "safariLogAllCommunicationHexDump"
    safari_log_all_communication_hex_dump = OptionsDescriptor[Optional[bool], bool]
    (SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP)
    """
    Log all communication sent to and received from the Web Inspector, as raw
    hex dump and printable characters. This logging is done before any data
    manipulation, and so can elucidate some communication issues. Like
    appium:safariLogAllCommunication, this can produce a lot of data in some cases,
    so it is recommended to be used only when necessary. Defaults to false.

    Usage
    -----
    - Get
        - `self.safari_log_all_communication_hex_dump`
    - Set
        - `self.safari_log_all_communication_hex_dump` = `value`
    
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


class SafariLogAllCommunicationOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION = "safariLogAllCommunication"
    safari_log_all_communication = OptionsDescriptor[Optional[bool], bool]
    (SAFARI_LOG_ALL_COMMUNICATION)
    """
    Log all plists sent to and received from the Web Inspector, as plain text.
    For some operations this can be a lot of data, so it is recommended to
    be used only when necessary. Defaults to false.

    Usage
    -----
    - Get
        - `self.safari_log_all_communication`
    - Set
        - `self.safari_log_all_communication` = `value`
    
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


class SafariOpenLinksInBackgroundOption(SupportsCapabilities):
    SAFARI_OPEN_LINKS_IN_BACKGROUND = "safariOpenLinksInBackground"
    safari_open_links_in_background = OptionsDescriptor[Optional[bool], bool]
    (SAFARI_OPEN_LINKS_IN_BACKGROUND)
    """
    Whether Safari should allow links to open in new windows.
    Default keeps current sim setting.

    Usage
    -----
    - Get
        - `self.safari_open_links_in_background`
    - Set
        - `self.safari_open_links_in_background` = `value`
    
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


class SafariSocketChunkSizeOption(SupportsCapabilities):
    SAFARI_SOCKET_CHUNK_SIZE = "safariSocketChunkSize"
    safari_socket_chunk_size = OptionsDescriptor[Optional[int], int]
    (SAFARI_SOCKET_CHUNK_SIZE)
    """
    The size, in bytes, of the data to be sent to the Web Inspector on
    iOS 11+ real devices. Some devices hang when sending large amounts of
    data to the Web Inspector, and breaking them into smaller parts can be
    helpful in those cases. Defaults to 16384 (also the maximum possible).

    Usage
    -----
    - Get
        - `self.safari_socket_chunk_size`
    - Set
        - `self.safari_socket_chunk_size` = `value`
    
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


class SafariWebInspectorMaxFrameLengthOption(SupportsCapabilities):
    SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH = "safariWebInspectorMaxFrameLength"
    safari_web_inspector_max_frame_length = OptionsDescriptor[Optional[int], int]
    (SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH)
    """
    The maximum size in bytes of a single data frame for the Web Inspector.
    Too high values could introduce slowness and/or memory leaks.
    Too low values could introduce possible buffer overflow exceptions.
    Defaults to 20MiB (20*1024*1024).

    Usage
    -----
    - Get
        - `self.safari_web_inspector_max_frame_length`
    - Set
        - `self.safari_web_inspector_max_frame_length` = `value`
    
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


class WebkitResponseTimeoutOption(SupportsCapabilities):
    WEBKIT_RESPONSE_TIMEOUT = "webkitResponseTimeout"
    webkit_response_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (WEBKIT_RESPONSE_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    Time to wait for a response from WebKit in a Safari session.
    (Real device only) Set the time to wait for a respons

    Usage
    -----
    - Get
        - `self.webkit_response_timeout`
    - Set
        - `self.webkit_response_timeout` = `value`
    
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


class WebviewConnectRetriesOption(SupportsCapabilities):
    WEBVIEW_CONNECT_RETRIES = "webviewConnectRetries"
    webview_connect_retries = OptionsDescriptor[Optional[int], int](WEBVIEW_CONNECT_RETRIES)
    """
    Number of times to send connection message to remote debugger,
    to get a webview. Default: 8.

    Usage
    -----
    - Get
        - `self.webview_connect_retries`
    - Set
        - `self.webview_connect_retries` = `value`
    
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


class WebviewConnectTimeoutOption(SupportsCapabilities):
    WEBVIEW_CONNECT_TIMEOUT = "webviewConnectTimeout"
    webview_connect_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (WEBVIEW_CONNECT_TIMEOUT, transform_duration_get, transform_duration_set)
    """
    The time to wait for the initial presence of webviews in
    MobileSafari or hybrid apps. Defaults to 0ms.

    Usage
    -----
    - Get
        - `self.webview_connect_timeout`
    - Set
        - `self.webview_connect_timeout` = `value`
    
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
