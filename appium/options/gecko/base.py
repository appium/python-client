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
from appium.options.common.base import AppiumOptions
from appium.options.common.system_port_option import SystemPortOption

from .android_storage_option import AndroidStorageOption
from .firefox_options_option import FirefoxOptionsOption
from .marionette_port_option import MarionettePortOption
from .verbosity_option import VerbosityOption


class GeckoOptions(
    AppiumOptions,
    AndroidStorageOption,
    FirefoxOptionsOption,
    MarionettePortOption,
    SystemPortOption,
    VerbosityOption,
):
    @SystemPortOption.system_port.setter  # type: ignore
    def system_port(self, value: int) -> None:
        """
        The number of the port for the driver to listen on. Must be unique
        for each session. If not provided then the driver will try to detect
        it automatically.
        """
        SystemPortOption.system_port.fset(self, value)  # type: ignore

    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'Gecko',
        }
