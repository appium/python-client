from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities


class MacOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if self.name == "SERVER_STARTUP_TIMEOUT":
            value_ms = getattr(obj, "get_capabilities")(self.name)
            return None if value_ms is None else timedelta(milliseconds=value_ms)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        if self.name == "SERVER_STARTUP_TIMEOUT":
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)


class ArgumentsOption(SupportsCapabilities):
    ARGUMENTS = 'arguments'
    arguments = MacOptionsDescriptor("ARGUMENTS")


class BootstrapRootOption(SupportsCapabilities):
    BOOTSTRAP_ROOT = 'bootstrapRoot'
    bootstrap_root = MacOptionsDescriptor("BOOTSTRAP_ROOT")


class EnvironmentOption(SupportsCapabilities):
    ENVIRONMENT = 'environment'
    environment = MacOptionsDescriptor("ENVIRONMENT")


class ServerStartupTimeoutOption(SupportsCapabilities):
    SERVER_STARTUP_TIMEOUT = 'serverStartupTimeout'
    server_startup_timeout = MacOptionsDescriptor("SERVER_STARTUP_TIMEOUT")


class ShowServerLogsOption(SupportsCapabilities):
    SHOW_SERVER_LOGS = 'showServerLogs'
    show_server_logs = MacOptionsDescriptor("SHOW_SERVER_LOGS")


class WebDriverAgentMacUrlOption(SupportsCapabilities):
    WEB_DRIVER_ARGENT_MAC_URL = 'webDriverAgentMacUrl'
    web_driver_agent_mac_url = MacOptionsDescriptor("WEB_DRIVER_ARGENT_MAC_URL")