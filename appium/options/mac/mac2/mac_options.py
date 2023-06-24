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

C = TypeVar('C', bound='SupportsCapabilities')


class MacOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: Any) -> Any:
        if self.name == 'SERVER_STARTUP_TIMEOUT':
            value_ms = getattr(obj, 'get_capability')(self.name)
            return None if value_ms is None else timedelta(milliseconds=value_ms)
        return getattr(obj, 'get_capability')(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name == 'SERVER_STARTUP_TIMEOUT':
            return getattr(obj, 'set_capability')(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        return getattr(obj, 'set_capability')(self.name, value)


class ArgumentsOption(SupportsCapabilities):
    ARGUMENTS = 'arguments'
    arguments = MacOptionsDescriptor('ARGUMENTS')


class BootstrapRootOption(SupportsCapabilities):
    BOOTSTRAP_ROOT = 'bootstrapRoot'
    bootstrap_root = MacOptionsDescriptor('BOOTSTRAP_ROOT')


class EnvironmentOption(SupportsCapabilities):
    ENVIRONMENT = 'environment'
    environment = MacOptionsDescriptor('ENVIRONMENT')


class ServerStartupTimeoutOption(SupportsCapabilities):
    SERVER_STARTUP_TIMEOUT = 'serverStartupTimeout'
    server_startup_timeout = MacOptionsDescriptor('SERVER_STARTUP_TIMEOUT')


class ShowServerLogsOption(SupportsCapabilities):
    SHOW_SERVER_LOGS = 'showServerLogs'
    show_server_logs = MacOptionsDescriptor('SHOW_SERVER_LOGS')


class WebDriverAgentMacUrlOption(SupportsCapabilities):
    WEB_DRIVER_ARGENT_MAC_URL = 'webDriverAgentMacUrl'
    web_driver_agent_mac_url = MacOptionsDescriptor('WEB_DRIVER_ARGENT_MAC_URL')


class SkipAppKillOption(SupportsCapabilities):
    SKIP_APP_KILL = 'skipAppKill'
    skip_app_kill = MacOptionsDescriptor('SKIP_APP_KILL')