from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities


class WebViewOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if self.name == ("WEBKIT_RESPONSE_TIMEOUT", "WEBVIEW_CONNECT_TIMEOUT"):
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        if self.name == ("WEBKIT_RESPONSE_TIMEOUT", "WEBVIEW_CONNECT_TIMEOUT"):
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        getattr(obj, "set_capabilities")(self.name, value)


class AbsoluteWebLocationsOption(SupportsCapabilities):
    ABSOLUTE_WEB_LOCATIONS = 'absoluteWebLocations'
    absolute_web_locations = WebViewOptionsDescriptor("ABSOLUTE_WEB_LOCATIONS")


class AdditionalWebviewBundleIdsOption(SupportsCapabilities):
    ADDITIONAL_WEBVIEW_BUNDLE_IDS = 'additionalWebviewBundleIds'
    additional_webview_bundle_ids = WebViewOptionsDescriptor("ADDITIONAL_WEBVIEW_BUNDLE_IDS")


class EnableAsyncExecuteFromHttpsOption(SupportsCapabilities):
    ENABLE_ASYNC_EXECUTE_FROM_HTTPS = 'enableAsyncExecuteFromHttps'
    enable_async_execute_from_https = WebViewOptionsDescriptor("ENABLE_ASYNC_EXECUTE_FROM_HTTPS")


class FullContextListOption(SupportsCapabilities):
    FULL_CONTEXT_LIST = 'fullContextList'
    full_context_list = WebViewOptionsDescriptor("FULL_CONTEXT_LIST")


class IncludeSafariInWebviewsOption(SupportsCapabilities):
    INCLUDE_SAFARI_IN_WEBVIEWS = 'includeSafariInWebviews'
    include_safari_in_webviews = WebViewOptionsDescriptor("INCLUDE_SAFARI_IN_WEBVIEWS")


class NativeWebTapOption(SupportsCapabilities):
    NATIVE_WEB_TAP = 'nativeWebTap'
    native_web_tap = WebViewOptionsDescriptor("NATIVE_WEB_TAP")


class SafariGarbageCollectOption(SupportsCapabilities):
    SAFARI_GARBAGE_COLLECT = 'safariGarbageCollect'
    safari_garbage_collect = WebViewOptionsDescriptor("SAFARI_GARBAGE_COLLECT")


class SafariIgnoreFraudWarningOption(SupportsCapabilities):
    SAFARI_IGNORE_FRAUD_WARNING = 'safariIgnoreFraudWarning'
    safari_ignore_fraud_warning = WebViewOptionsDescriptor("SAFARI_IGNORE_FRAUD_WARNING")


class SafariIgnoreWebHostnamesOption(SupportsCapabilities):
    SAFARI_IGNORE_WEB_HOSTNAMES = 'safariIgnoreWebHostnames'
    safari_ignore_web_hostnames = WebViewOptionsDescriptor("SAFARI_IGNORE_WEB_HOSTNAMES")


class SafariInitialUrlOption(SupportsCapabilities):
    SAFARI_INITIAL_URL = 'safariInitialUrl'
    safari_initial_url = WebViewOptionsDescriptor("SAFARI_INITIAL_URL")


class SafariLogAllCommunicationHexDumpOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP = 'safariLogAllCommunicationHexDump'
    safari_log_all_communication_hex_dump = WebViewOptionsDescriptor("SAFARI_LOG_ALL_COMMUNICATION_HEX_DUMP")


class SafariLogAllCommunicationOption(SupportsCapabilities):
    SAFARI_LOG_ALL_COMMUNICATION = 'safariLogAllCommunication'
    safari_log_all_communication = WebViewOptionsDescriptor("SAFARI_LOG_ALL_COMMUNICATION")


class SafariOpenLinksInBackgroundOption(SupportsCapabilities):
    SAFARI_OPEN_LINKS_IN_BACKGROUND = 'safariOpenLinksInBackground'
    safari_open_links_in_background = WebViewOptionsDescriptor("SAFARI_OPEN_LINKS_IN_BACKGROUND")


class SafariSocketChunkSizeOption(SupportsCapabilities):
    SAFARI_SOCKET_CHUNK_SIZE = 'safariSocketChunkSize'
    safari_socket_chunk_size = WebViewOptionsDescriptor("SAFARI_SOCKET_CHUNK_SIZE")

class SafariWebInspectorMaxFrameLengthOption(SupportsCapabilities):
    SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH = 'safariWebInspectorMaxFrameLength'
    safari_web_inspector_max_frame_length = WebViewOptionsDescriptor("SAFARI_WEB_INSPECTOR_MAX_FRAME_LENGTH")

class WebkitResponseTimeoutOption(SupportsCapabilities):
    WEBKIT_RESPONSE_TIMEOUT = 'webkitResponseTimeout'
    webkit_response_timeout = WebViewOptionsDescriptor("WEBKIT_RESPONSE_TIMEOUT")


class WebviewConnectRetriesOption(SupportsCapabilities):
    WEBVIEW_CONNECT_RETRIES = 'webviewConnectRetries'
    webview_connect_retries = WebViewOptionsDescriptor("WEBVIEW_CONNECT_RETRIES")


class WebviewConnectTimeoutOption(SupportsCapabilities):
    WEBVIEW_CONNECT_TIMEOUT = 'webviewConnectTimeout'
    webview_connect_timeout = WebViewOptionsDescriptor("WEBVIEW_CONNECT_TIMEOUT")