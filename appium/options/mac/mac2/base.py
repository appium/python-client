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

from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.postrun_option import PostrunOption
from appium.options.common.prerun_option import PrerunOption

from .arguments_option import ArgumentsOption
from .bootstrap_root_option import BootstrapRootOption
from .bundle_id_option import BundleIdOption
from .environment_option import EnvironmentOption
from .server_startup_timeout_option import ServerStartupTimeoutOption
from .show_server_logs_option import ShowServerLogsOption
from .skip_app_kill_option import SkipAppKillOption
from .system_host_option import SystemHostOption
from .system_port_option import SystemPortOption
from .web_driver_agent_mac_url_option import WebDriverAgentMacUrlOption


class Mac2Options(
    AppiumOptions,
    PrerunOption,
    PostrunOption,
    ArgumentsOption,
    BootstrapRootOption,
    BundleIdOption,
    EnvironmentOption,
    ServerStartupTimeoutOption,
    ShowServerLogsOption,
    SkipAppKillOption,
    SystemHostOption,
    SystemPortOption,
    WebDriverAgentMacUrlOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'Mac2',
            PLATFORM_NAME: 'Mac',
        }
